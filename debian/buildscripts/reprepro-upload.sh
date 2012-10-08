#!/bin/bash

# Script to sign and upload finished debs to reprepro
# Assumes root perms (use sudo) and that the deb/changes files are in .

export GNUPGHOME=/root/test-reprepro/.gnupg
dpkg-sig -k E775FF07 --sign builder *changes

reprepro -b /root/test-reprepro -C $reponame includedeb $osnameversion *deb
