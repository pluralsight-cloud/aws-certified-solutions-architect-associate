#!/bin/bash

echo {{ssm:/dev/squid_conf}} | base64 --decode > /tmp/squid_conf