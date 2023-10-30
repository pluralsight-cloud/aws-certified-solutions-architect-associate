#!/bin/bash

# Allowing YUM updates and installations from cloud_user
echo '%password%' | passwd cloud_user --stdin
yum update -y
yum install -y httpd

# Starting and eanbling HTTPD service
systemctl start httpd.service
systemctl enable httpd.service

# Adding HTTPD group and adding cloud_user
groupadd www
usermod -a -G www cloud_user

# Creating simple index.html file for HTTPD base page
echo '<html><h1>Hello Gurus!</h1><h3>I live in this Availability Zone: ' > /var/www/html/index.html
curl http://169.254.169.254/latest/meta-data/placement/availability-zone >> /var/www/html/index.html
echo '</h3> <h3>I go by this Instance Id: ' >> /var/www/html/index.html
curl http://169.254.169.254/latest/meta-data/instance-id >> /var/www/html/index.html
echo '</h3></html> ' >> /var/www/html/index.html

# Restarting HTTPD service to enforce new index.html just to be safe.
systemctl restart httpd.service