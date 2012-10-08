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
VERSION='1.0'
MAINTAINER='Greg Sutcliffe <greg.sutcliffe@gmail.com>'

PBUILDER="$1"
BUILD_DIR="$2"
TARGET="${BUILD_DIR}/${PACKAGE_NAME}"
DEB_STORE="/tmp/debs"

REPO='git://github.com/theforeman/smart-proxy.git'
BRANCH='9ea6076283d744ba55163ad45e3bacd96a1add72'

# TODO: For reprepro
# REPO_DIR='/home/greg/build-area/foreman-repo'
# DEB_REPO='stable'

DATE=$(date -R)
UNIXTIME=$(date +%s)
RELEASE="${VERSION}"
GIT='/usr/bin/git'

# Copy in packaging to the build dir
mkdir "${BUILD_DIR}/debian"
cp -r ./* "${BUILD_DIR}/debian/"

# Clone source code
cd "${BUILD_DIR}"
$GIT clone "${REPO}" "${TARGET}"
cd "${TARGET}"
$GIT checkout "${BRANCH}"
$GIT submodule init
$GIT submodule update
mv "${BUILD_DIR}/debian" "${TARGET}/"

# Cleanup source
LAST_COMMIT=$($GIT rev-list HEAD|/usr/bin/head -n 1)
rm -rf $(/usr/bin/find "${TARGET}" -name '.git*')

# Execute build using the pbuilder image in $1
pdebuild-$PBUILDER

# Copy packages
rm -rf   "${DEB_STORE}/$PBUILDER/stable/"
mkdir -p "${DEB_STORE}/$PBUILDER/stable/"
cp ../*changes "${DEB_STORE}/$PBUILDER/stable/"
cp ../*deb     "${DEB_STORE}/$PBUILDER/stable/"
