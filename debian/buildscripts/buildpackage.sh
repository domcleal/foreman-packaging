#!/bin/bash

# $1 is the target pbuilder tgz, eg. squeeze32
# $2 is the git directory to use from foreman-rpms, eg debian/squeeze/stable/foreman-proxy

# Check out packaging files and build script
DIR=`mktemp -d`
cd $DIR
git clone git://github.com/theforeman/foreman-rpms.git -b deb_by_dirs foreman-debs

# Run build script
cd foreman-debs/$2
./build.sh $1 $DIR

# Cleanup
rm -rf $DIR
