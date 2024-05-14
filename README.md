# Lidarr Installer

This project contains a script for installing and setting up Lidarr on a Linux system.

## Prerequisites

- Python 3.x
- The script will install the prerequisite packages: curl mediainfo sqlite3 libchromaprint-tools

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Br14n41/lidarr-installer.git
```
2. Run the script with sudo privileges:
```bash
sudo python3 lidarr.py
```

## Usage

The script will install Lidarr and set up a systemd service for it. The service will start Lidarr at boot and restart it if it fails.

Once installed, find your server at:
```bash
localhost:8686/
```
