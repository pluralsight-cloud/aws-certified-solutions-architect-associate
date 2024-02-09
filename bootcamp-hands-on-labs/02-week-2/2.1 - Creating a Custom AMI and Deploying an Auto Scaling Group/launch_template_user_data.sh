#!/bin/bash

# updating yum packages
sudo yum update -y

# Creating simple index.html file for HTTPD base page
echo '<html><h1>Hello Gurus!</h1><h3>I live in this Availability Zone: ' > /var/www/html/index.html
curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> /var/www/html/index.html
echo '</h3> <h3>I go by this Instance Id: ' >> /var/www/html/index.html
curl http://169.254.169.254/latest/meta-data/instance-id >> /var/www/html/index.html
echo '</h3></html> ' >> /var/www/html/index.html

# Restarting HTTPD service to enforce new index.html just to be safe.
systemctl restart httpd.service