# Create private k8s cluster on GCP

## Prerequisites

### Region
You will need to pick a region where all of this will be deployed.

### Quotas
https://console.cloud.google.com/iam-admin/quotas

To start with you will need to request the following quotas (later we will request more so that we can handle 1200 ports, we may potentially also switch from T4 to A2 wich are newer):
* GPU: 3 T4 GPUS (under Compute Engine API -> NVIDIA T4 GPUs)
* vCPU: 72 vCPUs (under Compute Engine API-> CPUs)

## Step 1. Creating a private cluster with no client access to the public endpoint
Here is the document describeing how to create private cluster:

https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#private_cp

Here is the document describing `gcloud container clusters create` command:

https://cloud.google.com/sdk/gcloud/reference/container/clusters/create

The steps:
1. We should create a **Standard Cluster**, not an **Autopilot cluster**
2. Cluster version: **1.22.15-gke.1000** (use --cluster-version parameter in the command)
3. We should set up a **regional** cluster (use --region parameter in the command)
4. When creating the cluster, a default 
[nodepool](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pools) will be created.
We will use these settings for the default node pool `--disk-size=100GB --machine-type=n1-standard-8 --num-nodes=1`

## Step 2. Set up Cloud NAT with GKE
https://cloud.google.com/nat/docs/gke-example

After this step, the nodes in the cluster should be able to reach internet using NAT IP.

## Step 3. Create node pools suitable for Voicegain deployment
A default node pool was created when creating the cluster. We need to create two more node pools.

Here is the document describing how to create a node pool:

https://cloud.google.com/kubernetes-engine/docs/how-to/node-pools

Here is the document describing `gcloud container node-pools create` command:

https://cloud.google.com/sdk/gcloud/reference/container/node-pools/create

Use these settings to create a node pool of 16 vCPUs and T4 GPU:

`--disk-size=100GB --machine-type=n1-standard-16 --num-nodes=1 --accelerator type=nvidia-tesla-t4,count=1`

Use these settings to create a node pool of 16 vCPUs 
(We can set num-nodes to 0 for now. We will use this node pool when we scale up):

`--disk-size=100GB --machine-type=n1-standard-16 --num-nodes=0`

## Step 4

Once Step 4 is complete please let us know and we will provide instructions how to connect your Kubernetes Cluster to your account on the Voicegain Console.

