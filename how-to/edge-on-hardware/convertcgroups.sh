#!/bin/bash

set -e

# Preliminary check for cgroup drivers
echo "Checking current cgroup driver settings..."
CRICTL_INFO=$(sudo crictl -r unix:///run/containerd/containerd.sock info | grep -i "cgroup driver" || echo "No cgroup driver info found")
KUBELET_CONFIG=$(sudo grep -i "cgroupDriver" /var/lib/kubelet/config.yaml || echo "No cgroupDriver info found")

# Print cgroup driver status
echo "Containerd cgroup driver settings:"
if echo "$CRICTL_INFO" | grep -q "systemd"; then
  echo "Containerd is using systemd as the cgroup driver."
elif echo "$CRICTL_INFO" | grep -q "cgroupfs"; then
  echo "Containerd is using cgroupfs as the cgroup driver."
else
  echo "Containerd cgroup driver is not explicitly set or not found."
fi

echo
echo "Kubelet cgroup driver settings:"
if echo "$KUBELET_CONFIG" | grep -q "systemd"; then
  echo "Kubelet is using systemd as the cgroup driver."
elif echo "$KUBELET_CONFIG" | grep -q "cgroupfs"; then
  echo "Kubelet is using cgroupfs as the cgroup driver."
else
  echo "Kubelet cgroup driver is not explicitly set or not found."
fi

# If both are already using cgroupfs, exit
if echo "$CRICTL_INFO" | grep -q "cgroupfs" && echo "$KUBELET_CONFIG" | grep -q "cgroupfs"; then
  echo "Both containerd and kubelet are already using cgroupfs as the cgroup driver."
  exit 0
fi

# Prompt to continue
read -p "Do you want to continue with the modifications to use cgroupfs as the cgroup driver? (yes/no): " choice
if [[ "$choice" != "yes" ]]; then
  echo "Aborting the script as per user request."
  exit 0
fi

# Stop kubelet and backup config
sudo systemctl stop kubelet
sudo cp /var/lib/kubelet/config.yaml /var/lib/kubelet/config.yaml.bak

# Change cgroup driver to cgroupfs
sudo sed -i 's|cgroupDriver: systemd|cgroupDriver: cgroupfs|g' /var/lib/kubelet/config.yaml

# Install NVIDIA container toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sudo sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt update
sudo apt-get install -y nvidia-container-toolkit

# Configure containerd
CONTAINERDCONF="/etc/containerd/config.toml"
sudo cp ${CONTAINERDCONF}{,.bak}
sudo containerd config default | sudo tee ${CONTAINERDCONF} > /dev/null
sudo nvidia-ctk runtime configure --runtime=containerd --config=${CONTAINERDCONF}
sudo sed -i 's|default_runtime_name = "runc"|default_runtime_name = "nvidia"|g' ${CONTAINERDCONF}

# Restart containerd and kubelet
sudo systemctl stop containerd kubelet
sleep 15
sudo systemctl restart containerd kubelet

# Inform the user to check containerd status
echo "Check containerd status and will need to delete the rex-0 pod so it will be recreated"
sleep 15

# Delete terminating pods forcefully
kubectl get po | awk '/Terminating/ {print $1}' | \
while read po; do
  echo "If pods not terminating run: kubectl delete po ${po} --grace-period=0 --force"
done

echo "Checking node description for available GPUs..."
kubectl describe node $(kubectl get nodes -o name) | grep -i "nvidia.com/gpu"

