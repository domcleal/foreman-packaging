%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name table_print

Summary: TablePrint turns objects into nicely formatted columns for easy reading
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.5.1
Release: 4%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/arches/table_print
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
TablePrint turns objects into nicely formatted columns for easy reading.
Works great in rails console, works on pure ruby objects, auto-detects
columns, lets you traverse ActiveRecord associations. Simple, powerful.

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
%{?scl:scl enable %{scl} - << \EOF}
gem install --local --install-dir .%{gem_dir} \
            --force %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%{gem_spec}
%{gem_instdir}/features
%{gem_instdir}/spec
%{gem_instdir}/Rakefile
%{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/LICENSE.txt

%changelog
* Tue Aug 25 2015 Dominic Cleal <dcleal@redhat.com> 1.5.1-4
- Converted to tfm SCL (dcleal@redhat.com)

* Tue Jul 28 2015 Dominic Cleal <dcleal@redhat.com> 1.5.1-3
- Convert table_print to SCL (dcleal@redhat.com)

* Thu May 29 2014 Dominic Cleal <dcleal@redhat.com> 1.5.1-2
- Modernise and update for EL7 (dcleal@redhat.com)

* Fri Mar 21 2014 Martin Bačovský <mbacovsk@redhat.com> 1.5.1-1
- Bump to 1.5.1 (mbacovsk@redhat.com)

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-3
- Fix up the spec's description and summary to remove rpmlint warnings
  (shk@redhat.com)

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-2
- new package built with tito

* Tue Aug 27 2013 Sam Kottler <shk@redhat.com> 1.1.5-1
- Initial package creation
