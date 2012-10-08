#!/bin/bash

# Script to be cloned from git to build foreman-proxy (stable)
# Assumes this repo/dir has been checked out already. Operates
# from ./ and copies to $source/debian

# Stop on errors
set -e

PACKAGE_NAME='foreman-proxy'
VERSION='1.0'
MAINTAINER='Greg Sutcliffe <greg.sutcliffe@gmail.com>'

BUILD_DIR=`mktemp -d`
TARGET="${BUILD_DIR}/${PACKAGE_NAME}"

REPO='git://github.com/theforeman/smart-proxy.git'
BRANCH='9ea6076283d744ba55163ad45e3bacd96a1add72'

REPO_DIR='/home/greg/build-area/foreman-repo'
DEB_REPO='stable'

function prepare_build() {
}

DATE=$(date -R)
UNIXTIME=$(date +%s)
RELEASE="${VERSION}"
GIT='/usr/bin/git'

cd "${BUILD_DIR}"

# Clone source code
$GIT clone "${REPO}" "${TARGET}"
cd "${TARGET}"
$GIT checkout "${BRANCH}"
$GIT submodule init
$GIT submodule update

# Copy in packaging
mkdir 'debian'
cd -
cp -r ./ "${BUILD_DIR}/debian/"
cd "${BUILD_DIR}"

# Cleanup source
LAST_COMMIT=$($GIT rev-list HEAD|/usr/bin/head -n 1)
rm -rf $(/usr/bin/find "${TARGET}" -name '.git*')

# call build
# copy packages
