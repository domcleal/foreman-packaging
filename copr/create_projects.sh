#!/bin/bash
#
# Creates a set of Copr projects

if [ $# -lt 1 -o $# -gt 2 ]; then
  echo "$0 VERSION [OS]"
  echo "  creates projects in Copr for a given version and optionally, version"
  echo "    example: $0 nightly"
  echo "    example: $0 nightly rhel7"
  exit 1
fi

VERSION=$1
ONLYOS=$2

NONSCL_SYSTEMS="fedora21"
SCL_SYSTEMS="rhel6 rhel7"

create() {
  REPOS_EXTRA=''
  local OPTIND OS PRODUCT REPOS REPOS_EXTRA SCL
  while getopts "o:p:s:r:" opt; do
    case $opt in
      o) OS=$OPTARG ;;
      p) PRODUCT=$OPTARG ;;
      r) REPOS_EXTRA="$REPOS_EXTRA $OPTARG" ;;
      s) SCL=$OPTARG ;;
    esac
  done

  if [ -n "$ONLYOS" -a "$OS" != "$ONLYOS" ]; then
    return
  fi

  CHROOT=$(echo $OS | sed 's/\([0-9]\+\)/-\1-x86_64/; s/rhel/epel/')

  if [[ $OS =~ ^rhel ]]; then
    REPOS='http://mirror.centos.org/centos/$releasever/sclo/$basearch/rh/ http://mirror.centos.org/centos/$releasever/sclo/$basearch/scl/'
  fi

  copr create \
    --chroot $CHROOT \
    --repo "$REPOS $REPOS_EXTRA" \
    --description "Foreman $VERSION build repository" \
    --instructions "Not for direct use, see http://theforeman.org and http://yum.theforeman.org for official repos." \
    "@theforeman/$PRODUCT-$VERSION-$SCL-$OS"

  # create the same, but with -test extension and inheriting from the main repo for scratch builds
  copr create \
    --chroot $CHROOT \
    --repo "$REPOS $REPOS_EXTRA copr://@theforeman/$PRODUCT-$VERSION-$SCL-$OS" \
    --description "Foreman $VERSION scratch/test build repository" \
    --instructions "Not for direct use, see http://theforeman.org and http://yum.theforeman.org for official repos." \
    "@theforeman/$PRODUCT-$VERSION-$SCL-$OS-test"
  copr modify \
    --disable_createrepo true \
    "@theforeman/$PRODUCT-$VERSION-$SCL-$OS-test"

  if [ $SCL = scl ]; then
    echo "*** Visit https://copr.fedorainfracloud.org/coprs/@theforeman/$PRODUCT-$VERSION-$SCL-$OS/edit_chroot/$CHROOT/ and edit package list"
  fi
}

### Foreman
# create non-SCL projects for all OSes
for SYSTEM in $NONSCL_SYSTEMS $SCL_SYSTEMS; do
  create -p foreman -s nonscl -o $SYSTEM
done

# create SCL projects for SCL OSes, includes:
#   - non-SCL project
for SYSTEM in $SCL_SYSTEMS; do
  create -p foreman -s scl -o $SYSTEM \
    -r "copr://@theforeman/foreman-$VERSION-nonscl-$SYSTEM"
done

### Plugins
# create non-SCL plugin projects for SCL OSes, includes:
#   - SCL core project (to get foreman macros defined)
for SYSTEM in $SCL_SYSTEMS; do
  create -p foreman-plugins -s nonscl -o $SYSTEM \
    -r "copr://@theforeman/foreman-$VERSION-scl-$SYSTEM"
done

# create non-SCL plugin projects for non-SCL OSes, includes:
#   - non-SCL core project (to get foreman macros defined)
for SYSTEM in $NONSCL_SYSTEMS; do
  create -p foreman-plugins -s nonscl -o $SYSTEM \
    -r "copr://@theforeman/foreman-$VERSION-nonscl-$SYSTEM"
done

# create SCL plugin projects for SCL OSes, includes:
#   - SCL core project (to get foreman macros defined)
#   - non-SCL plugin project
for SYSTEM in $SCL_SYSTEMS; do
  create -p foreman-plugins -s scl -o $SYSTEM \
    -r "copr://@theforeman/foreman-plugins-$VERSION-nonscl-$SYSTEM" \
    -r "copr://@theforeman/foreman-$VERSION-scl-$SYSTEM"
done
