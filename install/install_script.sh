#!/bin/bash
echo "Starting DarkSecurity installation script..."

# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y bro elasticsearch kibana logstash apache2 python3-flask nmap

echo "Installation complete. Please configure your system accordingly."
