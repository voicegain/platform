# <a id="top"></a>GCP Specific Steps for creating Kubernetes cluster suitable for Voicegain deployment
Required Steps, GCP Provided documentation, and recommended best practices

## <a id="toc"></a>Table of Contents
- [Step 1: Request GPUs from GCP](#step1)
- [Step 2: Create Cluster and Node Pools](#step2)
- [Step 3: Set up Cloud NAT](#step3)
- [Step 4: Reserve an Internal IP for Voicegain API](#step4)
- [Step 5: Continue on Voicegain Web Console](#step5)

## <a id="step1"></a>Step 1: Request GPUs from GCP
In order to use GPUs you must request a Quota increase for them from GCP.

Be certain you are requesting them for the Region you wish to run your cluster in.  

GCP Link: [Working with quotas](https://cloud.google.com/docs/quota#managing_your_quota_console)

## <a id="step2"></a>Step 2: Create Cluster and Node Pools

### Create Cluster and Default Node Pool

In this step, you will create a Regional Private Kubernetes Cluster on GCP, 
and create a default Node Pool of `n1-standard-8` instances.

#### Option A: Use the `default` network on the VPC

You can run the following command to create a few components:
* a subnet in the default VPC
* a regional private Kubernetes Cluster in the subnet
* a node pool of `n1-standard-8` instances
* one compute instance in each zone in the specified region

<pre>
gcloud container clusters create [CLUSTER_NAME] \
--create-subnetwork name=[SUBNET_NAME] --enable-ip-alias --enable-private-nodes \
--no-enable-master-authorized-networks --master-ipv4-cidr 172.19.0.0/28 --region [REGION] \
--num-nodes 1 --machine-type=n1-standard-8 --scopes=gke-default,datastore,storage-full \
--cluster-version "1.22.15-gke.1000"
</pre>

<pre>
[CLUSTER_NAME]: Name of the NEW cluster
[SUBNET_NAME]: Name of the NEW subnet
[REGION]: GCP region to create cluster in
</pre>

#### Option B: Use pre-created network and subnetwork on the VPC

If you would like to create the cluster in the pre-created subnet, 
you can use this option. The following command will create a few components:
* a regional private Kubernetes Cluster in the subnet you specified
* a node pool of `n1-standard-8` instances
* one compute instance in each zone in the specified region

<pre>
gcloud container clusters create [CLUSTER_NAME] \
--network [NETWORK_NAME] --subnetwork [SUBNET_NAME] --enable-ip-alias --enable-private-nodes \
--no-enable-master-authorized-networks --master-ipv4-cidr 172.19.0.0/28 --region [REGION] \
--num-nodes 1 --machine-type=n1-standard-8 --scopes=gke-default,datastore,storage-full \
--cluster-version "1.22.15-gke.1000"
</pre>

<pre>
[CLUSTER_NAME]: Name of the NEW cluster
[NETWORK_NAME]: Name of the PRE-CREATED network
[SUBNET_NAME]: Name of the PRE-CREATED subnet
[REGION]: GCP region to create cluster in
</pre>

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
gcloud compute addresses describe [VOICEGAIN_API_IP_NAME]
</pre>

All done here!

## <a id="step5"></a>Step 5: Continue on Voicegain Web Console 

[Continue with universal deployment guide Step 2](./universal-deployment-guide.md#Step2)

---
Goto: [top of document](#top)
