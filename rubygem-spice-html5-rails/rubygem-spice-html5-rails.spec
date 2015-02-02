%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from spice-html5-rails-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name spice-html5-rails
%global rubyabi 1.9.1

Summary: Spice client using HTML5 (WebSockets, Canvas)
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.1.5
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://www.spice-space.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
%if 0%{?fedora} > 18
Requires: %{?scl_prefix_ruby}ruby(release)
%else
Requires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygem(railties) >= 3.1.0
%if 0%{?fedora} > 18
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(abi) = %{rubyabi}
%endif
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Obsoletes: ruby193-rubygem-%{gem_name}

%description
Spice HTML5 client packed for Rails application


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/vendor
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/COPYING.LESSER
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/README.md

%files doc
%doc %{gem_docdir}

%changelog
* Thu Dec 18 2014 Dominic Cleal <dcleal@redhat.com> 0.1.5-1
- Update spice-html5-rails to 0.1.5 (dcleal@redhat.com)

* Tue Feb 11 2014 Dominic Cleal <dcleal@redhat.com> 0.1.4-1
- Update to v0.1.4 (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.1-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.0.1-5
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.1-3
- new package built with tito

* Wed Apr 03 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.1-2
- new package built with tito

* Wed Apr 03 2013 msuchy@redhat.com - 0.0.1-1
- Initial package
