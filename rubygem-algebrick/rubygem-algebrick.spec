%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name algebrick

Summary: Algebraic types and pattern matching
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.4.0
Release: 2%{?dist}
Group: Development/Languages
License: GPLv3
URL: http://github.com/pitr-ch/algebrick
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygem(activesupport)
%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = 1.9.1
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: rubygem(%{gem_name}) = %{version}

Obsoletes: ruby193-rubygem-%{gem_name}

%description
It's a gem providing algebraic types and pattern matching seamlessly
integrates with standard features Ruby.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/VERSION
%{gem_instdir}/lib
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/README_FULL.md

%changelog
* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-2
- Fix scl build (inecas@redhat.com)

* Mon Jan 20 2014 Ivan Nečas <inecas@redhat.com> 0.4.0-1
- new package built with tito

