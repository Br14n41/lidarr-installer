# This Python script will install Lidarr on an Ubuntu server.
# Version: 1.0
# Author: Br14n41 
# Date: 2024-05-14

import os


# We will check if the script is being run as root or with sudo privileges.
if os.geteuid() != 0:
    print('This script must be run with sudo privileges. Exiting.')
    exit()

# First, we need to install the required packages. We will use the apt package manager to install the required packages.
packages = ['curl', 'mediainfo', 'sqlite3', 'libchromaprint-tools']

for package in packages:
    os.system(f'sudo apt install {package} -y')

# Next, we need to download the Lidarr installation script from the official website using the wget command.
# The link in the script downloads Lidarr for AMD64 using arch=x64. If you're unsure of your architecture, you can determine it with the command: dpkg --print-architecture
# For ARM, armf, and armh architectures, change arch=x64 to: arch=arm
# For ARM64 architecture, change arch=x64 to: arch=arm64
os.system('wget --content-disposition \'http://lidarr.servarr.com/v1/update/master/updatefile?os=linux&runtime=netcore&arch=x64\' -O Lidarr.tar.gz')

# We will extract the downloaded tarball using the tar command.
os.system('tar -xvzf Lidarr.tar.gz')

# We will move the extracted files to the /opt directory.
os.system('sudo mv Lidarr /opt')

# Ensure ownership of the Lidarr directory is set to the user running the service.
os.system('sudo chown -R $USER /opt/Lidarr')

# We will create a systemd service file for Lidarr to manage the service.
service_file = '''
[Unit]
Description=Lidarr Daemon
After=network.target

[Service]
User=$USER
Group=$USER
Type=simple

ExecStart=/opt/Lidarr/Lidarr -nobrowser -data=/var/lib/lidarr/
TimeoutStopSec=20
KillMode=process
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
'''

# Use echo and sudo to write the service file
os.system(f'echo "{service_file}" | sudo tee /etc/systemd/system/lidarr.service > /dev/null')

# We will create the data directory for Lidarr and set the appropriate permissions.
os.system('sudo mkdir /var/lib/lidarr')
os.system('sudo chown -R $USER /var/lib/lidarr')

# We will reload the systemd manager configuration to apply the changes.
os.system('sudo systemctl -q daemon-reload')

# We will start the Lidarr service and enable it to start on boot.
os.system('sudo systemctl start lidarr')
os.system('sudo systemctl enable lidarr')

# We will open the required ports in the firewall to allow access to Lidarr.
os.system('sudo ufw allow 8686/tcp')

# Remove the downloaded tarball.
os.system('rm Lidarr.tar.gz')

print('Lidarr has been successfully installed on your Ubuntu server.')