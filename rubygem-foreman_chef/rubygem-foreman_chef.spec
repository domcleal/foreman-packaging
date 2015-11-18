# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_chef

%global foreman_dir /usr/share/foreman
%global foreman_bundlerd_dir %{foreman_dir}/bundler.d

Summary:    Plugin for Chef integration with Foreman
Name:       %{?scl_prefix}rubygem-%{gem_name}
Version:    0.2.0
Release:    2%{?foremandist}%{?dist}
Group:      Applications/System
License:    GPLv3
URL:        http://github.com/theforeman/foreman_chef
Source0:    http://rubygems.org/downloads/%{gem_name}-%{version}.gem

Requires:   foreman >= 1.9.0

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.6.9
Requires: %{?scl_prefix}rubygem(foreman-tasks) < 0.8.0

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems

BuildArch: noarch

Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-chef
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Foreman extensions that are required for better Chef integration.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0} --no-rdoc --no-ri
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{foreman_bundlerd_dir}
cat <<GEMFILE > %{buildroot}%{foreman_bundlerd_dir}/%{gem_name}.rb
gem '%{gem_name}'
GEMFILE

%posttrans
# We need to run the db:migrate after the install transaction
/usr/sbin/foreman-rake db:migrate  >/dev/null 2>&1 || :
/usr/sbin/foreman-rake db:seed  >/dev/null 2>&1 || :
(/sbin/service foreman status && /sbin/service foreman restart) >/dev/null 2>&1
exit 0

%files
%dir %{gem_instdir}
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_instdir}/lib
%{gem_instdir}/config
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_dir}/%{gem_name}.rb
%doc %{gem_instdir}/LICENSE

%exclude %{gem_instdir}/test

%files doc
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-2
- Add foremandist for branched builds (dcleal@redhat.com)

* Tue Oct 06 2015 Dominic Cleal <dcleal@redhat.com> 0.2.0-1
- Update foreman_chef to 0.2.0 (mhulan@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.7-2
- Converted to tfm SCL (dcleal@redhat.com)

* Mon Aug 17 2015 Dominic Cleal <dcleal@redhat.com> 0.1.7-1
- Update foreman_chef to 0.1.7 (mhulan@redhat.com)

* Wed Jul 15 2015 Marek Hulan <mhulan@redhat.com> 0.1.6-1
- Update foreman_chef to 0.1.6 (mhulan@redhat.com)

* Wed Jul 08 2015 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update foreman_chef to 0.1.5 (mhulan@redhat.com)

* Mon Jun 22 2015 Marek Hulan <mhulan@redhat.com> 0.1.4-1
- Update foreman_chef to 0.1.4 (mhulan@redhat.com)

* Mon Mar 23 2015 Dominic Cleal <dcleal@redhat.com> 0.1.3-2
- Add db:migrate/seed postinstall steps (dcleal@redhat.com)

* Sun Mar 22 2015 Marek Hulan <mhulan@redhat.com> 0.1.3-1
- Update foreman_chef to 0.1.3 (mhulan@redhat.com)

* Tue Feb 24 2015 Marek Hulan <mhulan@redhat.com> 0.1.2-1
- Update foreman_chef to 0.1.2 (mhulan@redhat.com)

* Thu Jan 29 2015 Marek Hulan <mhulan@redhat.com> 0.1.1-1
- Update foreman_chef to 0.1.1 (mhulan@redhat.com)
- Fix RPM deps to match gemspec (dcleal@redhat.com)

* Wed Jan 14 2015 Marek Hulan <mhulan@redhat.com> 0.1.0-1
- Update foreman_chef to 0.1.0 (mhulan@redhat.com)

* Wed Jan 22 2014 Marek Hulan <mhulan@redhat.com> 0.0.4-1
- Update foreman_chef (mhulan@redhat.com)

* Mon Jan 20 2014 Marek Hulan <mhulan@redhat.com> 0.0.3-1
- new package built with tito
