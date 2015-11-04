%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from jquery-rails-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-rails

Summary: Use jQuery with Rails 3
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 2.0.3
Release: 1%{?dist}
Group: Development/Languages
# jquery-rails itself is MIT, bundled JavaScripts are the rest
License: MIT and (MIT or GPLv2) and (MIT or BSD or GPLv2) and BSD
URL: http://rubygems.org/gems/jquery-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ror}rubygem(railties) >= 3.1.0
Requires: %{?scl_prefix_ror}rubygem(railties) < 5.0
Requires: %{?scl_prefix_ruby}rubygem(thor) => 0.14
Requires: %{?scl_prefix_ruby}rubygem(thor) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 3
application.


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
%doc %{gem_instdir}/LICENSE
# bunch of bundled JS files here
%{gem_instdir}/vendor
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile.lock
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md

%changelog
* Thu Jul 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-2
- Imported from Fedora again.
- Specfile cleanup

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-1
- Initial package
