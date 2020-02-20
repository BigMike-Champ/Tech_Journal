#secure-ssh.sh
#author mike
#creates a new ssh user using the $l parameter
#adds a public key from the local repo or curled from the remote repo
#removes roots ability to ssh in


newuser=$1
useradd -m -d /home/$newuser -s /bin/bash $newuser
mkdir /home/$newuser/.ssh
mkdir /home/$newuser/.ssh/authorized_keys
cp /home/michael/Tech-Journal/SYS265/linux/public-keys/id_rsa.pub /home/$newuser/.ssh/authorized_keys
sed -z 's/PermitRootLogin yes\|$/PermitRootLogin no/' /etc/ssh/sshd_config

