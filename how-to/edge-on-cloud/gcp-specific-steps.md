# <a id="top"></a>GCP Specific Steps for creating Kubernetes cluster suitable for Voicegain deployment
Required Steps, GCP Provided documentation, and recommended best practices

## <a id="toc"></a>Table of Contents
- [Step 0: Request GPUs from GCP](#step0)
- [Step 1: (Optional) Setup Google Storage Bucket](#step1)
- [Step 2: Create Cluster and Node Pools](#step2)
- [Step 3: Set up Cloud NAT](#step3)
- [Step 4: Reserve an Internal IP for Voicegain API](#step4)
- [Step 5: (Optional) Configure ip-masq-agent](#step5)
- [Step 6: Continue on Voicegain Web Console](#step6)




## <a id="step0"></a>Step 0: Request GPUs from GCP
In order to use GPUs you must request a Quota increase for them from GCP.

Be certain you are requesting them for the Region you wish to run your cluster in.  

GCP Link: [Working with quotas](https://cloud.google.com/docs/quota#managing_your_quota_console)

## <a id="step1"></a>Step 1: (Optional) Setup Google Storage Bucket

This is only needed if you want to use Google Storage for storing the submitted audio, otherwise the audio will be stored within the Kubernetes cluster to be created in [step 2](#step2). For more details see [How to configure a Google Storage bucket](./gcp-storage-bucket.md) .

## <a id="step2"></a>Step 2: Create Cluster and Node Pools

### Create Cluster and Default Node Pool

In this step, you will create a Regional Private Kubernetes Cluster on GCP, 
and create a default Node Pool of `n1-standard-8` instances.

#### Option A: Use the `default` network on the VPC and GCP suggested IP ranges 
(Preferred for Quick setup with default values)

You can run the following command to create a few components:
* a subnet in the default VPC
* a secondary ip range in subnet for Kubernetes pods
* a secondary ip range in subnet for Kubernetes services
* a regional private Kubernetes Cluster in the subnet
* a node pool of `n1-standard-8` instances
* one compute instance in each zone in the specified region

<pre>
gcloud container clusters create [CLUSTER_NAME] \
--create-subnetwork name=[SUBNET_NAME] --enable-ip-alias --enable-private-nodes \
--enable-master-authorized-networks --master-authorized-networks [VOICEGAIN_NAT_IP]/32,[LINUX_TERMINAL_IP]/32 --master-ipv4-cidr 172.19.0.0/28 --region [REGION] \
--num-nodes 1 --machine-type=n1-standard-8 --scopes=gke-default,datastore,storage-full \
--cluster-version "latest"
</pre>

<pre>
[CLUSTER_NAME]: Name of the NEW cluster
[SUBNET_NAME]: Name of the NEW subnet
[REGION]: GCP region to create cluster in
[VOICEGAIN_NAT_IP]: Voicegain IP allowed to connect GKE Master
[LINUX_TERMINAL_IP]: IP of linux terminal being used to run kubectl
</pre>


#### Option B: Use pre-created network and subnetwork on the VPC and custom IP ranges 
(Preferred for detail setup with custom values)

If you would like to create the cluster in the pre-created subnet, 
you can use this option. The following command will create a few components:
* a secondary ip range in subnet for Kubernetes pods
* a secondary ip range in subnet for Kubernetes services
* a regional private Kubernetes Cluster in the subnet you specified
* a node pool of `n1-standard-8` instances
* one compute instance in each zone in the specified region

<pre>
gcloud container clusters create [CLUSTER_NAME] \
--network [NETWORK_NAME] --subnetwork [SUBNET_NAME] --enable-ip-alias --enable-private-nodes \
--cluster-ipv4-cidr=[PODS_CIDR] --services-ipv4-cidr=[SERVICES_CIDR] \
--enable-master-authorized-networks --master-authorized-networks [VOICEGAIN_NAT_IP]/32,[LINUX_TERMINAL_IP]/32 --master-ipv4-cidr 172.19.0.0/28 --region [REGION] \
--num-nodes 1 --machine-type=n1-standard-8 --scopes=gke-default,datastore,storage-full \
--cluster-version "1.27.3-gke.100"
</pre>

<pre>
Needed Parameters:-
[CLUSTER_NAME]: Name of the NEW cluster
[NETWORK_NAME]: Name of the PRE-CREATED network
[SUBNET_NAME]: Name of the PRE-CREATED subnet
[REGION]: GCP region to create cluster in
[VOICEGAIN_NAT_IP]: Voicegain IP allowed to connect GKE Master
[LINUX_TERMINAL_IP]: IP of linux terminal being used to run kubectl

Optional Parameters:-
[PODS_CIDR]: IP Range for pods in kubernetes cluster
[SERVICES_CIDR]: IP Range for services in kubernetes cluster
</pre>

**>> Contact Voicegain (support@voicegain.ai) to get value for VOICEGAIN_NAT_IP <<**

**>> For LINUX_TERMINAL_IP value run "curl ifconfig.me" in Linux terminal <<**

**>> While choosing region check if all zones in region have support for T4 GPU nodes as they will be created in next steps <<**

GCP Link: [GPU regions and zones availability](https://cloud.google.com/compute/docs/gpus/gpu-regions-zones)

GCP Link: [gcloud container clusters create](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create)

### Create Other Node Pools

You will create two more node pools. 

Here is the command to create the first node pool. 
In this node pool, we use `n1-standard-16` instance with one T4 GPU.
<pre>
gcloud container node-pools create [GPU_NODE_POOL_NAME] --region [REGION] --cluster [CLUSTER_NAME] \
--disk-size=100GB --num-nodes=1 --machine-type=n1-standard-16 \
--accelerator type=nvidia-tesla-t4,count=1
</pre>

<pre>
[GPU_NODE_POOL_NAME]: Name of the NEW GPU node pool
[REGION]: GCP region the cluster is in
[CLUSTER_NAME]: Name of the cluster you created
</pre>

In the second node pool, we use `n1-standard-16` instance. 
This node pool is reserved for further use, so we set `--num-nodes` to `0`.

<pre>
gcloud container node-pools create [NON_GPU_NODE_POOL_NAME] --region [REGION] --cluster [CLUSTER_NAME] \
--disk-size=100GB --num-nodes=0 --machine-type=n1-standard-16
</pre>

<pre>
[NON_GPU_NODE_POOL_NAME]: Name of the NEW non-GPU node pool
[REGION]: GCP region the cluster is in
[CLUSTER_NAME]: Name of the cluster you created
</pre>

GCP Link: [gcloud container node-pools create](https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create)


## <a id="step3"></a>Step 3: Set up Cloud NAT

Because we are using **Private** Kubernetes cluster, each node in the cluster does not have a public IP to 
get access to Internet. In this step, we will set up Cloud NAT on GCP to solve this issue. 

### Create Router

Use this command to create a Router in the network and the region that the Kubernetes cluster is in.
<pre>
gcloud compute routers create [ROUTER_NAME] --network [NETWORK_NAME] --region [REGION]
</pre>

<pre>
[ROUTER_NAME]: Name of the NEW router
[NETWORK_NAME]: Name of the network
                Either 'default' or the name of the pre-created network
[REGION]: GCP region the cluster is in
</pre>

### Create NAT Router config

Now you will create a NAT configuration in the Router you created.

<pre>
gcloud compute routers nats create [NAT_ROUTER_CONFIG_NAME] --router-region [REGION] \
--router [ROUTER_NAME] \
--nat-custom-subnet-ip-ranges=[SUBNET_NAME] \
--auto-allocate-nat-external-ips 
</pre>

<pre>
[NAT_ROUTER_CONFIG_NAME]: Name of the NEW NAT router configuration
[REGION]: GCP region the cluster is in
[ROUTER_NAME]: Name of the router you created
[SUBNET_NAME]: Name of the subnet
               It's the [SUBNET_NAME] you used in step 2.
</pre>

GCP Link: [Set up Cloud NAT with GKE](https://cloud.google.com/nat/docs/gke-example)

## <a id="step4"></a>Step 4: Reserve an Internal IP for Voicegain API

Now you will reserve an Internal IP address in your subnet. 
This IP address will be used as the Voicegain API endpoint.

<pre>
gcloud compute addresses create [VOICEGAIN_API_IP_NAME] --subnet [SUBNET_NAME] --region [REGION]
</pre>

<pre>
[VOICEGAIN_API_IP_NAME]: Name of the NEW IP address
[SUBNET_NAME]: Name of the subnet
               It's the [SUBNET_NAME] you used in step 2.
[REGION]: GCP region the cluster is in
</pre>

**>> Contact Voicegain (support@voicegain.ai) and provide your reserved IP address <<**

You can message the output of the following command to Voicegain.
<pre>
gcloud compute addresses describe [VOICEGAIN_API_IP_NAME] --region [REGION]
</pre>

All done here!

## <a id="step5"></a>Step 5: (Optional) Configure ip-masq-agent

This step is only needed if the new cluster has to interact with sources/destinations located on [RFC 1918](https://tools.ietf.org/html/rfc1918)  IP ranges, e.g. 10.0.0.0/8. If that is the case, then the GKE Default SNAT will not work as desired and we need to configure **ip-masq-agent**.

Steps to configure ip-masq-agent are:

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


## <a id="step6"></a>Step 6: Continue on Voicegain Web Console 

[Continue with universal deployment guide Step 2](./universal-deployment-guide.md#Step2)

---
Goto: [top of document](#top)
