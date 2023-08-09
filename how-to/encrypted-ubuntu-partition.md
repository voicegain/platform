Here's a consolidated guide that combines all the steps to create an encrypted partition that automounts only when you log in, without needing to enter the passphrase.

1. **Install the Required Software**:

   ```bash
   sudo apt-get update
   sudo apt-get install cryptsetup
   ```

2. **Prepare the Partition**:

   ```bash
   sudo umount /dev/sdXN
   ```

3. **Create the Encrypted Device**:

   ```bash
   sudo cryptsetup luksFormat /dev/sdXN
   ```

4. **Create a Key File**:

   ```bash
   sudo dd if=/dev/urandom of=/home/yourusername/.keyfile bs=1024 count=4
   sudo chmod 0400 /home/yourusername/.keyfile
   sudo chown yourusername:yourusername /home/yourusername/.keyfile
   ```

5. **Add the Key File to LUKS**:

   ```bash
   sudo cryptsetup luksAddKey /dev/sdXN /home/yourusername/.keyfile
   ```

6. **Create a Filesystem**:

   ```bash
   sudo mkfs.ext4 /dev/mapper/my_encrypted_partition
   ```

7. **Create a Mount Script**:

   ```bash
   nano /home/yourusername/mount_encrypted.sh
   ```

   Add the following:

   ```bash
   #!/bin/bash
   sudo cryptsetup luksOpen /dev/sdXN my_encrypted_partition --key-file /home/yourusername/.keyfile
   sudo mount /dev/mapper/my_encrypted_partition /mnt/my_encrypted_partition
   ```

   Save, exit, and make it executable:

   ```bash
   chmod +x /home/yourusername/mount_encrypted.sh
   ```

8. **Configure sudo**:

   ```bash
   sudo visudo
   ```

   Add the following lines:

   ```bash
   yourusername ALL=(ALL) NOPASSWD: /sbin/cryptsetup
   yourusername ALL=(ALL) NOPASSWD: /bin/mount
   ```

9. **Add the Script to Startup Applications**: Look for "Startup Applications" or a similar tool in your system settings, and add the script there.

10. **Reboot**: Reboot your system to test the setup.

Please replace `/dev/sdXN` with your partition's path and `yourusername` with your actual username. Always back up any important data on the partition before proceeding, as these steps will erase existing data on the partition. Make sure you understand each step as misconfiguration might lead to issues.
