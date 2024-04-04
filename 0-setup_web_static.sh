#!/usr/bin/env bash
#Set up web server for deployment of web-server

sudo apt-get update -y
sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo chown -R $USER:$USER /data/web_static/releases/test/
echo "<h1>Hey Server!</h1>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
SERVER_CONFIG="
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
}
"
echo "$SERVER_CONFIG" > /etc/nginx/sites-enabled/default
sudo service nginx restart
exit 0
