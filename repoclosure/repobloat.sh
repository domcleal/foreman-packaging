#!/bin/bash

set -e

if [ $# -lt 2 ]; then
  echo "Usage: $0 <yum.conf> <url>"
  exit 1
fi

yumorig=$1
url=$2
shift; shift

TEMPDIR=$(mktemp -d)
trap "rm -rf $TEMPDIR" EXIT

# repo names must be unique, or yum will get confused between different OSes and URLs
reponame=undertest-$(basename $yumorig .conf)-$(echo $url | cksum | sed 's/ /-/g')

yumconf=$TEMPDIR/yum.conf
cat $yumorig > $yumconf
cat >> $yumconf << EOF

[$reponame]
name=$reponame
gpgcheck=0
baseurl=$url

EOF

for p in $(repoquery -c $yumconf --repoid=$reponame -a --qf="%{name}\n"); do
  if ! repoquery -c $yumconf --repoid=$reponame --whatrequires $p | grep -q ^ ; then
    echo $p
  fi
done
