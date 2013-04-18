%define rbname djberg96-krb5-auth
%define version 0.9.0
%define release 1

Summary: A Ruby interface for the the Kerberos library
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}%{dist}
Group: Development/Ruby
License: Distributable
URL: http://github.com/djberg96/krb5-auth
Source0: http://rubygems.org/downloads/%{rbname}-%{version}.gem
Patch0: rubygem-djberg96-krb5-auth-0001-Add-credential-cache.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: ruby 
Requires: rubygems >= 1.8.10

BuildRequires: ruby 
BuildRequires: rubygems >= 1.8.10
BuildRequires: ruby-devel
BuildRequires: krb5-devel
BuildRequires: rubygem-rake-compiler 

Provides: rubygem(djberg96-krb5-auth) = %{version}

%define gemdir /usr/lib/ruby/gems/1.8
%define gembuilddir %{buildroot}%{gemdir}

%description
The krb5-auth library is an interface for the Kerberos 5 network
authentication protocol. It wraps the Kerberos C API.

This particular version was created by Daniel Berger as a fork of
the krb5-auth project.

%prep
%setup -q -T -c

%build
%{__rm} -rf %{buildroot}
mkdir -p ./%{gemdir}
export CONFIGURE_ARGS="--with-cflags='%{optflags}' --with-krb5_auth-include=/usr/include/et"
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
%{gemdir}/gems/%{rbname}-%{version}/lib/krb5_auth.so
%{gemdir}/gems/%{rbname}-%{version}/krb5-auth.gemspec
%doc %{gemdir}/gems/%{rbname}-%{version}/samples/sample_config_display.rb
%doc %{gemdir}/doc/djberg96-krb5-auth-0.9.0
%{gemdir}/cache/djberg96-krb5-auth-0.9.0.gem
%{gemdir}/specifications/djberg96-krb5-auth-0.9.0.gemspec

%changelog
* Thu Apr 18 2013 Dominic Cleal <dcleal@redhat.com> 0.9.0-1
- Initial 0.9.0 release
- Add patch 103cea7d (Add credential cache argument to get_init_creds_keytab)
