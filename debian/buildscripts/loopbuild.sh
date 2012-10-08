#!/bin/bash

# Sample script to loop over a set of package builds

# Debian 6
./buildpackage.sh squeeze64 debian/debian6/stable/foreman-proxy
./buildpackage.sh squeeze32 debian/debian6/stable/foreman-proxy

./buildpackage.sh squeeze64 debian/debian6/nightly/foreman-proxy
./buildpackage.sh squeeze32 debian/debian6/nightly/foreman-proxy

# Ubuntu 12.04 LTS
./buildpackage.sh precise64 debian/ubuntu1204/stable/foreman-proxy
./buildpackage.sh precise32 debian/ubuntu1204/stable/foreman-proxy

./buildpackage.sh precise64 debian/ubuntu1204/nightly/foreman-proxy
./buildpackage.sh precise32 debian/ubuntu1204/nightly/foreman-proxy
