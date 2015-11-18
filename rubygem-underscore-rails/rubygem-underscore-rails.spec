%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name underscore-rails

Summary: underscore.js asset pipeline provider/wrapper
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 1.8.3
Release: 2%{?dist}
Group: Development/Ruby
License: MIT
URL: https://github.com/rweng/underscore-rails
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
underscore.js asset pipeline provider/wrapper.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}-doc}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%setup -q -c -T
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
%{gem_instdir}/vendor
%doc %{gem_instdir}/LICENSE.md
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/*.gemspec

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Gemfile
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/Readme.md

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.8.3-2
- Converted to tfm SCL (dcleal@redhat.com)

* Thu Aug 13 2015 Dominic Cleal <dcleal@redhat.com> 1.8.3-1
- new package built with tito
