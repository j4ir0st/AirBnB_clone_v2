#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
echo "Test fake HTML file" > /data/web_static/current/index.html
sudo sed -i "/server_name _;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo apt-get autoremove -y
sudo service nginx restart
