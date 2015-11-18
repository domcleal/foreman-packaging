%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name dynflow

Summary: DYNamic workFLOW engine
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.8.7
Release: 1%{?foremandist}%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/Dynflow/dynflow
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?el6} && 0%{!?scl:1}
Requires: %{?scl_prefix_ruby}ruby(abi)
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix}rubygem(algebrick) >= 0.7.0
Requires: %{?scl_prefix}rubygem(algebrick) < 0.8.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby) >= 0.9.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby) < 0.10.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby-edge) >= 0.1.0
Requires: %{?scl_prefix}rubygem(concurrent-ruby-edge) < 0.2.0
Requires: %{?scl_prefix}rubygem(multi_json)
Requires: %{?scl_prefix}rubygem(apipie-params)
Requires: %{?scl_prefix}rubygem-sequel
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Ruby workflow/orchestration engine

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-ri --no-rdoc
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/web
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/test
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/examples

%changelog
* Mon Oct 12 2015 Dominic Cleal <dcleal@redhat.com> 0.8.7-1
- Update dynflow to 0.8.7 (inecas@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.8.6-1
- Release dynflow 0.8.6 (stbenjam@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.8.5-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 20 2015 Dominic Cleal <dcleal@redhat.com> 0.8.5-2
- Package dynflow for non-SCL on el7 (stbenjam@redhat.com)

* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.8.5-1
- Release dynflow 0.8.5 (stbenjam@redhat.com)

* Mon Aug 03 2015 Ivan Nečas <inecas@redhat.com> 0.8.2-1
- Update dynflow to 0.8.2 (inecas@redhat.com)
- Automatic commit of package [rubygem-dynflow] minor release [0.8.1-1].
  (dcleal@redhat.com)
- Update dynflow to 0.8.1 (inecas@redhat.com)

* Thu Jul 02 2015 Dominic Cleal <dcleal@redhat.com> 0.8.1-1
- Update dynflow to 0.8.1 (inecas@redhat.com)

* Fri Jun 19 2015 Ivan Nečas <inecas@redhat.com> 0.7.9-1
- Update dynflow to 0.7.9 (inecas@redhat.com)

* Mon May 18 2015 Dominic Cleal <dcleal@redhat.com> 0.7.8-1
- Update dynflow to 0.7.8 (inecas@redhat.com)

* Tue Mar 17 2015 Dominic Cleal <dcleal@redhat.com> 0.7.7-1
- Update dynflow to 0.7.7 (inecas@redhat.com)

* Wed Jan 28 2015 Dominic Cleal <dcleal@redhat.com> 0.7.6-1
- Update to dynflow 0.7.6 (inecas@redhat.com)

* Fri Dec 05 2014 Dominic Cleal <dcleal@redhat.com> 0.7.5-1
- Update to dynflow 0.7.5 (brad@redhat.com)

* Tue Aug 12 2014 Ivan Nečas <inecas@redhat.com> 0.7.3-1
- Bump version (inecas@redhat.com)

* Mon Jul 14 2014 Ivan Nečas <inecas@redhat.com> 0.7.2-1
- Bump version (inecas@redhat.com)

* Fri Jun 13 2014 Ivan Nečas <inecas@redhat.com> 0.7.1-1
- Bump version (inecas@redhat.com)

* Tue Jun 10 2014 Ivan Nečas <inecas@redhat.com> 0.7.0-1
- Bump version (inecas@redhat.com)

* Mon Apr 07 2014 Ivan Nečas <inecas@redhat.com> 0.6.1-1
- Bump version (inecas@redhat.com)

* Tue Mar 25 2014 Ivan Nečas <inecas@redhat.com> 0.6.0-1
- Bump version (inecas@redhat.com)

* Tue Mar 18 2014 Ivan Nečas <inecas@redhat.com> 0.5.1-1
- Bump version (inecas@redhat.com)

* Tue Feb 25 2014 Ivan Nečas <inecas@redhat.com> 0.5.0-1
- Bump to version 0.5.0 (inecas@redhat.com)

* Wed Aug 28 2013 Partha Aji <paji@redhat.com> 0.1.0-2
- F19 Changes - made ruby abi conditional (paji@redhat.com)

* Tue May 07 2013 Ivan Necas <inecas@redhat.com> 0.1.0-1
- new package built with tito
