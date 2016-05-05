%define gem_name yard
%define gem_cache_dir %{_datadir}/foreman-installer/gems

Summary: Documentation generation tool for Ruby
Name: puppet-agent-%{gem_name}
Version: 0.8.7.6
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://yardoc.org/
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: puppet-agent
BuildArch: noarch

%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

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
