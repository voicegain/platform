# <a id="top"></a>Steps to configure ip-masq-agent

a) Obtain the current ip-masq-agent configmap (note that there may be none).

<pre>
kubectl get configmap ip-masq-agent -n kube-system -o yaml > ip-masq-agent-config.yaml
</pre>

b) Now edit it (or create a new one), e.g., here we removed (not included) 10.0.0.0/8:

<pre>
apiVersion: v1
kind: ConfigMap
metadata:
  name: ip-masq-agent
  namespace: kube-system
data:
  config: |
    nonMasqueradeCIDRs:
      - 172.16.0.0/12
      - 192.168.0.0/16      
      - 100.64.0.0/10
    masqLinkLocal: false
    resyncInterval: 60s
</pre>

c) Then apply it back to the cluster:
<pre>
kubectl apply -f ip-masq-agent-config.yaml
</pre>

d) After you create or edit your ip-masq-agent ConfigMap, deploy the ip-masq-agent DaemonSet.

You will want to copy and paste the entire code block below into the terminal of your linux system that has kubectl configured and connected to your new cluster:

<pre>
echo "
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ip-masq-agent
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: ip-masq-agent
  template:
    metadata:
      labels:
        k8s-app: ip-masq-agent
    spec:
      hostNetwork: true
      containers:
      - name: ip-masq-agent
        image: gke.gcr.io/ip-masq-agent:v2.9.3-v0.2.4-gke.5
        args:
            # The masq-chain must be IP-MASQ
            - --masq-chain=IP-MASQ
        securityContext:
          privileged: true
        volumeMounts:
          - name: config-volume
            mountPath: /etc/config
      volumes:
        - name: config-volume
          configMap:
            name: ip-masq-agent
            optional: true
            items:
              - key: config
                path: ip-masq-agent
      tolerations:
      - effect: NoSchedule
        operator: Exists
      - effect: NoExecute
        operator: Exists
      - key: "CriticalAddonsOnly"
        operator: "Exists"
" > vg_masqdaemonset.yaml
</pre>

<pre>
kubectl apply -f vg_masqdaemonset.yaml
</pre>

e) After applying the updated ConfigMap, you can check the status of the ip-masq-agent pods in the kube-system namespace to ensure they are running correctly:
<pre>
kubectl get pods -n kube-system -l k8s-app=ip-masq-agent
</pre>

f) If you notice any issues with the ip-masq-agent pods, you can check the logs for more information:
<pre>
kubectl logs -n kube-system -l k8s-app=ip-masq-agent
</pre>