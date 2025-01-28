# <a id="top"></a>Azure Specific Steps for creating Kubernetes cluster suitable for Voicegain deployment
Required Steps, Azure Provided documentation, and recommended best practices

## <a id="toc"></a>Table of Contents
- [Step 0: Azure GPU Quotas](#step0)
- [Step 1: Create Azure Resource Group](#step1)
- [Step 2: (Optional) Setup Azure Storage Account](#step2) #ToDo
- [Step 3: Create Cluster and Node Pools](#step3)
- [Step 4: Reserve an Public IP for Voicegain API](#step4)
- [Step 6: Continue on Voicegain Web Console](#step5)


## <a id="step0"></a>Step 0: Request GPUs from AZURE
In order to use GPUs you must request a Quota increase for them from Azure.

Be certain you are requesting them for the Region you wish to run your cluster in.  

AZURE Link: [GPU Quota Usage](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu#deployment-considerations)

## <a id="step1"></a>Step 1: Create Azure Resource group

<pre>
az group create --name [RESOURCE_GROUP_NAME] --location [REGION]
</pre>

<pre>
[RESOURCE_GROUP_NAME]: Azure Resource Group Name of AKS Cluster
[REGION]: AZURE region to create cluster in
</pre>

## <a id="step2"></a>Step 2: (Optional) Setup Azure Storage Account (Documentation Incomplete)

This is only needed if you want to use Azure Blob Storage inside Azure Storage account for storing the submitted audio, otherwise the audio will be stored within the Kubernetes cluster to be created in [step 3](#step2). For more details see [How to configure a Azure Blob Storage in Azure Storage Account](./azure-storage-account.md) .

## <a id="step3"></a>Step 3: Create Cluster and Node Pools

### Create Cluster and Default Node Pool

In this step, you will create a Regional Public Kubernetes Cluster on AZURE, 
and create a default Node Pool of `Standard_D8_v3` instances.

#### Option A: Create Virtual Network and use AZURE suggested IP ranges 
(Preferred for Quick setup with default values)

You can run the following command to create a few components:
* a Virtual Network
* a subnet in the Virtual Network
* a regional public Kubernetes Cluster in the subnet
* a resource group to store AKS resources
* a node pool of `Standard_D8_v3` instances
* one compute instance in each zone in the specified region

<pre>
az aks create --name [CLUSTER_NAME]  --resource-group [AZURE_RESOURCE_GROUP_NAME] --location [REGION] --network-plugin azure --api-server-authorized-ip-ranges [VOICEGAIN_NAT_IP],[LINUX_TERMINAL_IP]  --enable-managed-identity --node-count 1 --node-vm-size Standard_D8_v3 --nodepool-name [DEFAULT_NODE_POOL_NAME] --tier [TIER]
</pre>

<pre>
Needed Parameters:-
[CLUSTER_NAME]: Name of the NEW cluster
[RESOURCE_GROUP_NAME]: Azure Resource Group Name of AKS Cluster

Optional Parameters:-
[REGION]: AZURE region to create cluster in
[VOICEGAIN_NAT_IP]: Voicegain IP allowed to connect Kubernetes Master
[LINUX_TERMINAL_IP]: IP of linux terminal being used to run kubectl
[DEFAULT_NODE_POOL_NAME]: Name of default nodepool attached to Cluster
[TIER]: free or standard
</pre>


#### Option B: Use pre-created Virtual Network and subnetwork using custom IP ranges 
(Preferred for detail setup with custom values)

If you would like to create the cluster in the pre-created subnet, 
you can use this option. The following command will create a few components:
* a regional public Kubernetes Cluster
* a resource group to store AKS resources
* a node pool of `Standard_D8_v3` instances
* one compute instance in each zone in the specified region

<pre>
az aks create --name [CLUSTER_NAME]  --resource-group [AZURE_RESOURCE_GROUP_NAME] --location [REGION] --network-plugin azure --api-server-authorized-ip-ranges [VOICEGAIN_NAT_IP],[LINUX_TERMINAL_IP]  --enable-managed-identity --node-count 1 --node-vm-size Standard_D8_v3 --nodepool-name [DEFAULT_NODE_POOL_NAME] --tier [TIER] --pod-subnet-id [POD_SUBNET_RESOURCE_ID] --vnet-subnet-id [NODES_SUBNET_RESOURCE_ID] --service-cidr [K8S_SERVICES_VIP_CIDR] --dns-service-ip [K8S_SERVICES_VIP_DNS]
</pre>

<pre>
Needed Parameters:-
[CLUSTER_NAME]: Name of the NEW cluster
[RESOURCE_GROUP_NAME]: Azure Resource Group Name of AKS Cluster

Optional Parameters:-
[REGION]: AZURE region to create cluster in
[VOICEGAIN_NAT_IP]: Voicegain IP allowed to connect Kubernetes Master
[LINUX_TERMINAL_IP]: IP of linux terminal being used to run kubectl
[DEFAULT_NODE_POOL_NAME]: Name of default nodepool attached to Cluster
[TIER]: free or standard
[POD_SUBNET_RESOURCE_ID]: Subnet Resource id where pods will be deployed
[NODES_SUBNET_RESOURCE_ID]: Subnet Resource id where nodes will be deployed
[K8S_SERVICES_VIP_CIDR]: CIDR for virtual IP to be used by K8S service (should not overlap with any subnet in same or peered VPC) (default - 10.0.0.0/16)
[K8S_SERVICES_VIP_DNS]: The address should be the .10 address of your service IP address range (default 10.0.0.10)
</pre>

**>> Contact Voicegain (support@voicegain.ai) to get value for VOICEGAIN_NAT_IP <<**

**>> For LINUX_TERMINAL_IP value run "curl ifconfig.me" in Linux terminal <<**

AZURE Link: [az aks create](https://learn.microsoft.com/en-us/cli/azure/aks?view=azure-cli-latest#az-aks-create())

### (Optional) Add new IP to existing authorised list for Kubernetes Master Control Plane

1) Open Azure Portal
2) Navigate to Kubernetes Services
3) Select Kubernetes cluster
4) Select Networking tab from left menu
5) Add new IP in Security IP Ranges comma seperated
6) Click Apply

### Create Other Node Pools

You will create two more node pools. 

Here is the command to create the first node pool. 
In this node pool, we use `Standard_NC16as_T4_v3` instance with one T4 GPU.
<pre>
az extension add --name aks-preview
az extension update --name aks-preview
az feature register --namespace "Microsoft.ContainerService" --name "GPUDedicatedVHDPreview"
az feature show --namespace "Microsoft.ContainerService" --name "GPUDedicatedVHDPreview"
az provider register --namespace Microsoft.ContainerService

az aks nodepool add --resource-group [RESOURCE_GROUP_NAME] --cluster-name [CLUSTER_NAME] --name [GPU_NODE_POOL_NAME] --node-count 1 --node-vm-size Standard_NC16as_T4_v3 --node-osdisk-size 100 --aks-custom-headers UseGPUDedicatedVHD=true
</pre>

<pre>
[GPU_NODE_POOL_NAME]: Name of the NEW GPU node pool
[RESOURCE_GROUP_NAME]: Azure Resource Group Name of AKS Cluster
[CLUSTER_NAME]: Name of the cluster you created
</pre>

AZURE Link: [GPU sizes](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu)

AZURE Link: [GPU AKS Cluster Guide](https://learn.microsoft.com/en-us/azure/aks/gpu-cluster)


In the second node pool, we use `Standard_D16_v3` instance. 
This node pool is reserved for further use, so we set `--num-nodes` to `0`.

<pre>
az aks nodepool add --resource-group [RESOURCE_GROUP_NAME] --cluster-name [CLUSTER_NAME] --name [NON_GPU_NODE_POOL_NAME] --node-count 0 --node-vm-size Standard_D16_v3 --node-osdisk-size 100
</pre>

<pre>
[NON_GPU_NODE_POOL_NAME]: Name of the NEW non-GPU node pool
[RESOURCE_GROUP_NAME]: Azure Resource Group Name of AKS Cluster
[CLUSTER_NAME]: Name of the cluster you created
</pre>

AZURE Link: [az aks nodepool add](https://learn.microsoft.com/en-us/cli/azure/aks/nodepool?view=azure-cli-latest)

## <a id="step4"></a>Step 4: Reserve an Public IP for Voicegain API

Now you will reserve an Public IP address. 
This IP address will be used as the Voicegain API endpoint.

<pre>
az network public-ip create --resource-group myNetworkResourceGroup --name [VOICEGAIN_API_IP_NAME] --sku Standard --allocation-method static
</pre>

<pre>
[VOICEGAIN_API_IP_NAME]: Name of the NEW IP address
[AKS_RESOURCE_GROUP_NAME]: Resource group created by AKS. Format for it is MC_resourcegroupname_clustername_location
</pre>

**>> Contact Voicegain (support@voicegain.ai) and provide your reserved IP address <<**

You can message the output of the following command to Voicegain.
<pre>
az network public-ip show --name [VOICEGAIN_API_IP_NAME] --resource-group [AKS_RESOURCE_GROUP_NAME]
</pre>

All done here!

## <a id="step5"></a>Step 5: Continue on Voicegain Web Console 

[Continue with universal deployment guide Step 2](./universal-deployment-guide.md#Step2)

---
Goto: [top of document](#top)
