# Rollback

Rollback is easy and can be done from the Cloud Web Console. Simply choose one of the prior versions, verify that it is compatible with your configurartion, and click Rebuild (scroll down to the Rebuild button).


![Rollback to previous version](./EDGE-Rollback.png)


# Restore from Backup
Here is how you restore the backups for Mongo and Minio.

We assume that they are stored in `/backup/mongo/{epoch time}` and `/backup/minio` folders respectively.

Minio has a single backup folder with subfolders for the buckets, while Mongo has a separate each time a backup is taken.

Before restoring backups make sure there is no user/api traffic to the Edge system.

Here is a script that will restore the backups (make sure you set the correct value of this source folder `/backup/mongo/{epoch time}`):

```
export PATH=$PATH:$HOME/minio-binaries/
which mc

minio=$(kubectl get ep | awk '/9000/ {print $2}')
echo $minio
mc alias set -q --insecure minio https://${minio} accesskey secretkey                                               
mc ls --insecure minio

# Restore minio. Run without --dry-run after checking:
mc mirror --insecure /backup/minio/ minio/ --dry-run

mongo=$(\ls -lart /nfs | awk '/default-ascalon-base-mongodb/ {print $NF}'| tail -n1)
# Restore mongo. Run without --dry-run after checking:
sudo rsync -avP /backup/mongo/{epoch time} /nfs/${mongo}/ --dry-run
```

Once the script completes you will need to Rebuild the Edge cluster from the Cloud Web Console.

# Reinstall and Restore from backup

First we need to either:
* Create a new Edge Cluster - see [Deploy Voicegain on hardware or a VM](../edge-on-hardware/Edge_Deploy.md)
  * We assume that you will have the needed Mongo and Minio backuos stored somewhere safe  
* Reset an existing Edge Cluster - here are the steps:
  *   Do a kubeadm reser `sudo kubeadm reset`
  *   Delete old /nfs/default-* directories if you do not care about any of the old data
  *   From the bottom of the Edge Cluster status page get the EZInit script by clicking the Regenerate EZInit button. Note that you will need only the highlighted part of the command line script.
  *   


