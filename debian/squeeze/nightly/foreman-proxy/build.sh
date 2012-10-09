#!/bin/bash

# Script to be cloned from git to build foreman-proxy (stable)
# Assumes this repo/dir has been checked out already. Operates
# from ./ and copies to $source/debian

# Expected input
# $1 - pbuilder base image, eg squeeze64
# $2 - precreated temp dir to use

# Stop on errors
set -e

PACKAGE_NAME='foreman-proxy'
VERSION='1.1'
MAINTAINER='Greg Sutcliffe <greg.sutcliffe@gmail.com>'

# Name of the pbuilder env to use
PBUILDER="$1"

# We use readlink to get an absolute path to the Jenkins
# checkout, but readlink expects the path to exist
mkdir -p "../$1"
BUILD_DIR=`readlink -f ../$1`
TARGET="${BUILD_DIR}/${PACKAGE_NAME}"
DEB_STORE='/tmp/debs'

REPO='git://github.com/theforeman/smart-proxy.git'
BRANCH='develop'

DATE=$(date -R)
UNIXTIME=$(date +%s)
RELEASE="${VERSION}"
GIT='/usr/bin/git'

# Copy in packaging to the build dir
mkdir -p  "${BUILD_DIR}/debian"
cp -r ./* "${BUILD_DIR}/debian/"

# Clone source code
cd "${BUILD_DIR}"
$GIT clone "${REPO}" "${TARGET}"
cd "${TARGET}"
$GIT checkout "${BRANCH}"
$GIT submodule init
$GIT submodule update
# Move packaging into source clone
mv "${BUILD_DIR}/debian" "${TARGET}/"

# Cleanup source
LAST_COMMIT=$($GIT rev-list HEAD|/usr/bin/head -n 1)
rm -rf $(/usr/bin/find "${TARGET}" -name '.git*')

# Add 'nightly' to changelog
mv debian/changelog debian/changelog.tmp

echo "$PACKAGE_NAME ($RELEASE) UNRELEASED; urgency=low

  * Automatically built package based on the state of
    $REPO at commit $LAST_COMMIT

 -- $MAINTAINER  $DATE
" > debian/changelog

cat debian/changelog.tmp >> debian/changelog
rm -f debian/changelog.tmp

# Execute build using the pbuilder image in $1
pdebuild-$PBUILDER

# Copy packages
rm -rf   "${DEB_STORE}/$PBUILDER/nightly/"
mkdir -p "${DEB_STORE}/$PBUILDER/nightly/"
cp ../*changes "${DEB_STORE}/$PBUILDER/nightly/"
cp ../*deb     "${DEB_STORE}/$PBUILDER/nightly/"
