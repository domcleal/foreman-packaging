%define rbname rkerberos
%define version 0.1.0
%define release 1

Summary: A Ruby interface for the the Kerberos library
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Artistic 2.0
URL: http://github.com/djberg96/rkerberos
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
Patch0: rubygem-rkerberos-0001-Add-credential-cache.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby 
Requires: rubygems >= 1.8.10

BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildRequires: ruby-devel
BuildRequires: krb5-devel
BuildRequires: rubygem-rake-compiler 

Provides: rubygem(%{rbname}) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
The rkerberos library is an interface for the Kerberos 5 network
authentication protocol. It wraps the Kerberos C API.

%prep
%setup -q -T -c

%build
%{__rm} -rf %{buildroot}
mkdir -p ./%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}' --with-%{rbname}-include=/usr/include/et"
gem install --local --install-dir ./%{gemdir} -V --force %{SOURCE0}

# Apply patch and rebuild
patch -p1 -d ./%{gemdir}/gems/%{rbname}-%{version} -i %{PATCH0}
pushd ./%{gemdir}/gems/%{rbname}-%{version}
rake clean compile
popd

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -a ./%{gemdir}/* %{buildroot}%{gemdir}
# .so is copied into lib/
rm -rf %{buildroot}/%{gemdir}/gems/%{rbname}-%{version}/{ext,tmp}
# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gemdir}/specifications/%{rbname}-%{version}.gemspec

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/%{rbname}-%{version}/Rakefile
%doc %{gemdir}/gems/%{rbname}-%{version}/README
%doc %{gemdir}/gems/%{rbname}-%{version}/CHANGES
%doc %{gemdir}/gems/%{rbname}-%{version}/MANIFEST
%{gemdir}/gems/%{rbname}-%{version}/test
%{gemdir}/gems/%{rbname}-%{version}/lib/rkerberos.so
%{gemdir}/gems/%{rbname}-%{version}/rkerberos.gemspec
%doc %{gemdir}/doc/%{rbname}-%{version}
%{gemdir}/cache/%{rbname}-%{version}.gem
%{gemdir}/specifications/%{rbname}-%{version}.gemspec

%changelog
* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- Initial 0.1.0 release
- Add patch 103cea7d (Add credential cache argument to get_init_creds_keytab)
