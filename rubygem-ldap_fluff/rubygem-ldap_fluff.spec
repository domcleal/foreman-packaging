%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ldap_fluff

Summary: LDAP integration for Active Directory, FreeIPA and POSIX
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.3.3
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: https://github.com/theforeman/ldap_fluff
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}rubygem(activesupport)
Requires: %{?scl_prefix}rubygem(net-ldap) >= 0.3.1
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Obsoletes: ruby193-rubygem-%{gem_name}

%if 0%{?fedora} > 18
Requires:       %{?scl_prefix_ruby}ruby(release)
%else
Requires:       %{?scl_prefix_ruby}ruby(abi) = 1.9.1
%endif

%description
Provides multiple implementations of LDAP queries for various backends.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}
%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}
#rake ldap_fluff:gem

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/{.yardoc,etc}

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/test

%changelog
* Mon Nov 10 2014 Dominic Cleal <dcleal@redhat.com> 0.3.3-1
- update ldap_fluff to 0.3.3 (dcleal@redhat.com)

* Wed Oct 15 2014 Dominic Cleal <dcleal@redhat.com> 0.3.2-1
- update ldap_fluff to 0.3.2 (dcleal@redhat.com)

* Wed Aug 27 2014 Dominic Cleal <dcleal@redhat.com> 0.3.1-1
- update ldap_fluff to 0.3.1 (dcleal@redhat.com)

* Fri Aug 01 2014 Dominic Cleal <dcleal@redhat.com> 0.3.0-1
- update ldap_fluff to 0.3.0 (dcleal@redhat.com)

* Thu May 29 2014 Petr Chalupa <pchalupa@redhat.com> 0.2.5-1
- update ldap_fluff to 0.2.5 (pchalupa@redhat.com)

* Tue May 27 2014 Petr Chalupa <pchalupa@redhat.com> 0.2.4-1
- update ldap_fluff to 0.2.4 (pchalupa@redhat.com)

* Mon May 19 2014 Petr Chalupa <pchalupa@redhat.com> 0.2.3-1
- update ldap_fluff to 0.2.3 (pchalupa@redhat.com)

* Tue Aug 27 2013 Partha Aji <paji@redhat.com> 0.2.2-2
- Updated to use ruby release for f19 (paji@redhat.com)

* Thu May 30 2013 Marek Hulan <mhulan@redhat.com> 0.2.2-1
- Gem ldap_fluff upgraded to 0.2.2 (mhulan@redhat.com)

* Thu May 30 2013 Marek Hulan <mhulan@redhat.com> 0.2.1-2
- ldap_fluff does not create /etc/ldap_fluff.yml anymore (mhulan@redhat.com)

* Thu May 30 2013 Marek Hulan <mhulan@redhat.com> 0.2.1-1
- Ldap_fluff update to 0.2.1 (mhulan@redhat.com)

* Thu May 16 2013 Brad Buckingham <bbuckingham@redhat.com> 0.1.7-2
- ldap_fluff - bumping version (bbuckingham@redhat.com)

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-3
- correct build directory in SC env

* Wed Feb 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-2
- new package built with tito

* Thu Nov 01 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.3-1
- update to ldap_fluff-0.1.3.gem and polish the spec (msuchy@redhat.com)

* Mon Jul 16 2012 Miroslav Suchý <msuchy@redhat.com> 0.1.1-2
- cleanup spec file (msuchy@redhat.com)

* Tue Jul 10 2012 Jordan OMara <jomara@redhat.com> 0.1.1-1
- new package built with tito

* Fri Jul 06 2012 Jordan OMara <jomara@redhat.com> 0.1.1-1
- A few minor IPA bugs (jomara@redhat.com)
- Adding .rvmrc; unit tests only support 1.9.3 (jomara@redhat.com)

* Fri Jul 06 2012 Jordan OMara <jomara@redhat.com> 0.1.0-1
- Adding the rest of free ipa support - testing, configuration
  (jomara@redhat.com)
- Adding FreeIPA support (jomara@redhat.com)
- Fix for empty set return for missing ldap user (jomara@redhat.com)
- Removing files that shouldnt have been committed (jomara@redhat.com)

* Fri Jun 29 2012 Jordan OMara <jomara@redhat.com> 0.0.6-1
- Adding some heavy recursive tests (jomara@redhat.com)
- Updating README to fix formatting (jsomara@gmail.com)
- Adding anon_queries to AD config; Fixing AD recursive group walk
  (jomara@redhat.com)
- Fixing a posix merge_filter bug. NEEDS SOME TESTS (jomara@redhat.com)
- Fixing a few minor bugs (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.5-1
- Forgot to remove obsolete files from lib (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.4-1
- rdoc/task -> rake/rdoctask for older rpm support (jomara@redhat.com)
- Updating readme (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.3-1
- Automatic commit of package [rubygem-ldap_fluff] release [0.0.2-1].
  (jomara@redhat.com)

* Tue Jun 26 2012 Jordan OMara <jomara@redhat.com> 0.0.2-1
- new package built with tito
