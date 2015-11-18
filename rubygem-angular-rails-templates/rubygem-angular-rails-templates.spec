# Template for Rubygem's spec file
# It should work with f18, f19, rhel6 and rhel6 with SCL

%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name angular-rails-templates

Name:      %{?scl_prefix}rubygem-%{gem_name}
Version:   0.1.2
Release:   3%{?dist}
Epoch:     1
Summary:   Use your angular templates with rails' asset pipeline
Group:     Development/Languages
License:   MIT
URL:       https://github.com/pitr/angular-rails-templates
Source0:   http://rubygems.org/downloads/%{gem_name}-%{version}.gem

BuildArch: noarch
Provides:  %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

Requires:  %{?scl_prefix_ruby}ruby(rubygems)
Requires:  %{?scl_prefix_ruby}rubygem(railties) >= 3.1
Requires:  %{?scl_prefix}rubygem(sprockets)
Requires:  %{?scl_prefix_ruby}rubygem(tilt)
Requires:  %{?scl_prefix_ruby}ruby(release)

BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(release)

%description
Adds your HTML templates into Angular's $templateCache using Rails asset pipeline.
It removes the need for AJAX calls to retrieve the templates (or for you to manually set them into the DOM).

%package doc
BuildArch:  noarch
Requires:   %{name} = %{epoch}:%{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for %{name}

%description doc
This package contains documentation for %{pkg_name}

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
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}

%files
%dir %{gem_instdir}
%{gem_instdir}/vendor/assets/javascripts/angular-rails-templates.js.erb
%{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}
%{gem_libdir}

%files doc
%doc %{gem_instdir}/README.md

%changelog
* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-3
- Fix checks against scl name, optimise rhel/empty SCL conditional
  (dcleal@redhat.com)
- Converted to tfm SCL (dcleal@redhat.com)
- Fix typo in -doc requires on main package (dcleal@redhat.com)

* Thu Feb 12 2015 Dominic Cleal <dcleal@redhat.com> 0.1.2-2
- Fix dep to include epoch between -doc and main package (dcleal@redhat.com)

* Thu Feb 12 2015 Eric D. Helms <ericdhelms@gmail.com> 0.1.2-1
- Update rubygem-angular-rails-templates to 0.1.2 (ericdhelms@gmail.com)

* Mon Feb 09 2015 Eric D. Helms <ericdhelms@gmail.com> 0.1.3-1
- Update 'rubygem-angular-rails-templates' to 0.1.3 (ericdhelms@gmail.com)

* Thu Oct 02 2014 Dominic Cleal <dcleal@redhat.com> 0.0.4-7
- new package built with tito (ehelms@redhat.com)
