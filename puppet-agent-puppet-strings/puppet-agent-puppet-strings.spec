%define gem_name puppet-strings
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: Puppet documentation via YARD
Name: puppet-agent-%{gem_name}
Version: 0.4.0
Release: 1%{?dist}
Group: Development/Languages
License: ASL-2.0
URL: https://github.com/puppetlabs/puppetlabs-strings
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet-agent
Requires: puppet-agent-yard >= 0.8
Requires: puppet-agent-yard < 1
BuildArch: noarch

%description
A Puppet Face and plugin built on the YARD Documentation Tool and the
Puppet 4 Parser.

It is uses YARD and the Puppet Parser to generate HTML documentation
about Puppet code and Puppet extensions written in Ruby.

%prep
%setup -q -c -T
cp -a %{SOURCE0} ./

%build

%install
mkdir -p %{buildroot}%{gem_cache_dir}
cp -a ./%{gem_name}-%{version}.gem %{buildroot}%{gem_cache_dir}

%files
%{gem_cache_dir}/%{gem_name}-%{version}.gem

%post
/opt/puppetlabs/puppet/bin/gem install %{gem_cache_dir}/%{gem_name}-%{version}.gem >/dev/null

%preun
/opt/puppetlabs/puppet/bin/gem uninstall -x -v %{version} %{gem_name} >/dev/null

%changelog
