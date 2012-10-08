#!/bin/bash

# Sample script to loop over a set of package builds

# Debian 6
sudo ./buildpackage.sh squeeze64 debian/debian6/stable/foreman-proxy
sudo ./buildpackage.sh squeeze32 debian/debian6/stable/foreman-proxy

sudo ./buildpackage.sh squeeze64 debian/debian6/nightly/foreman-proxy
sudo ./buildpackage.sh squeeze32 debian/debian6/nightly/foreman-proxy

# Ubuntu 12.04 LTS
sudo ./buildpackage.sh precise64 debian/ubuntu1204/stable/foreman-proxy
sudo ./buildpackage.sh precise32 debian/ubuntu1204/stable/foreman-proxy

sudo ./buildpackage.sh precise64 debian/ubuntu1204/nightly/foreman-proxy
sudo ./buildpackage.sh precise32 debian/ubuntu1204/nightly/foreman-proxy
