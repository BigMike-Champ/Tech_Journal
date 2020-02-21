#secure-ssh.sh
#author mike
#creates a new ssh user using the $l parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in


newuser=$1
useradd -m -d /home/$newuser -s /bin/bash $newuser
sudo mkdir /home/$newuser/.ssh
sudo cp /home/michaelu/Tech_Journal/linux/public-keys/id_rsa.pub /home/$newuser/.ssh/authorized_keys
sudo chmod 700 /home/$newuser/.ssh
sudo chmod 600 /home/$newuser/.ssh/authorized_keys
sudo chown -R $newuser:$newuser /home/$newuser/.ssh


