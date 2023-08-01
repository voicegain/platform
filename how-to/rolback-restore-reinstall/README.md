# Rollback

Rollback is easy and can be done from the Cloud Web Console. Simply choose one of the prior versions, verify that it is compatible with your configurartion, and click Rebuild (scroll down to the Rebuild button).


![Rollback to previous version](./EDGE-Rollback.png)


# Restore from Backup
Here is how you restore the backups for Mongo and Minio.

We assume that they are stored in `/backup/mongo/{epoch time}` and `/backup/minio` folders respectively.

Minio has a single backup folder with subfolders for the buckets, while Mongo has a separate each time a backup is taken.

Before restoring backups make sure there is no user/api traffic to the Edge system.

The following commands should be copied and pasted into a terminal and output checked to ensure intended results (make sure you set the correct value of this source folder `/backup/mongo/{epoch time}`):

```
# 1. Make sure the terminal session can find the `mc` command:
export PATH=$PATH:$HOME/minio-binaries/
which mc

# 2. Assing the currently running minio service to the $minio variable:
minio=$(kubectl get ep | awk '/9000/ {print $2}')
echo $minio

# 3. Configure `mc`:
mc alias set -q --insecure minio https://${minio} accesskey secretkey                                               
mc ls --insecure minio

# 4. Restore minio. !!!Run without `--dry-run` argument after checking output!!! :
mc mirror --insecure /backup/minio/ minio/ --dry-run

# 5. Assing Mongo Backup Dir !!! MANUALLY ASSIGN: 
MONGO_BACKUP=/backup/mongo/<EPOCH TIME>

# 6. Assigning most recent mongo names directory in /nfs volumes as target of Mongo restore:
mongo=$(\ls -lart /nfs | awk '/default-ascalon-base-mongodb/ {print $NF}'| tail -n1)
echo $mongo

# 7. Restore mongo. Run without --dry-run after checking:
sudo rsync -avP /backup/mongo/{epoch time} /nfs/${mongo}/ --dry-run
```

Once the script completes you will need to Rebuild the Edge cluster from the Cloud Web Console.

# Reinstall and Restore from backup

First we need to either:
* Create a new Edge Cluster - see [Deploy Voicegain on hardware or a VM](../edge-on-hardware/Edge_Deploy.md)
  * We assume that you will have the needed Mongo and Minio backups stored somewhere safe  
* Reset an existing Edge Cluster - here are the steps:
  *   Do a kubeadm reset `sudo kubeadm reset`
  *   Delete old /nfs/default-* directories if you do not care about any of the old data
  *   From the bottom of the Edge Cluster status page get the EZInit script by clicking the Regenerate EZInit button. Note that you will need only the highlighted part of the command line script. ![Regenerate EZInit](./Regenerate-EZInit.png)
  *   After you download the script we need to make a change to it `sed -i.bak ':a;N;$!ba;s/clusterExist/#clusterExist/2' voicegain-init.sh`
  *   Then stop the heart beat that pings the Cloud `sudo rm -rfv /opt/voicegain/bin/tunnel_heartbeat`
  *   And finally run the EZInit script `sudo --preserve-env=HOME bash voicegain-init.sh`
  *   Once the scipt is complete we will deploy the correct version release and configuration via the Cloud Web Console
 
After these steps, we have a vanilla Edge Cluster with the correct configuration but no old user data.
We can restore that data following the steps from **Restore from Backup** section. Remember to run the Rebuild at the end.


