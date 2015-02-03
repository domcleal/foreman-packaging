%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%{!?scl_v8:%global scl_v8 v8314}
%{!?scl_prefix_v8:%global scl_prefix_v8 %{scl_v8}-}

%global gem_name sprockets

Summary:  Rack-based asset packaging system
Name:     %{?scl_prefix}rubygem-%{gem_name}
Version:  2.8.2
Release:  2%{?dist}
Group:    Development/Languages
License:  MIT
URL:      http://getsprockets.org/
Source0:  http://rubygems.org/gems/%{gem_name}-%{version}.gem
# to get tests:
# git clone https://github.com/sstephenson/sprockets.git && cd sprockets/
# git checkout v2.8.2 && tar czf sprockets-tests-2.8.2.tgz test/
Source1:  sprockets-%{version}-tests.tgz

Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}rubygem(hike) => 1.2
Requires: %{?scl_prefix_ruby}rubygem(hike) < 2
Requires: %{?scl_prefix}rubygem(multi_json) => 1.0
Requires: %{?scl_prefix}rubygem(multi_json) < 2
Requires: %{?scl_prefix_ruby}rubygem(rack) => 1.0
Requires: %{?scl_prefix_ruby}rubygem(rack) < 2
Requires: %{?scl_prefix_ruby}rubygem(tilt) => 1.1
Requires: %{?scl_prefix_ruby}rubygem(tilt) < 2
Conflicts: %{?scl_prefix_ruby}rubygem(tilt) = 1.3.0
%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
Requires: %{?scl_prefix_ruby}ruby(abi)
%else
Requires: %{?scl_prefix_ruby}ruby(release)
%endif

BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(coffee-script)
# these two gems aren't in Fedora yet and are only soft dependencies
# BuildRequires: %{?scl_prefix}rubygem(eco)
# BuildRequires: %{?scl_prefix}rubygem(ejs)
BuildRequires: %{?scl_prefix_ruby}rubygem(execjs)
BuildRequires: %{?scl_prefix_ruby}rubygem(hike) => 1.2
BuildRequires: %{?scl_prefix_ruby}rubygem(hike) < 2
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildRequires: %{?scl_prefix_ruby}rubygem(uglifier)
BuildRequires: %{?scl_prefix}rubygem(multi_json)
BuildRequires: %{?scl_prefix_ruby}rubygem(json)
BuildRequires: %{?scl_prefix_ruby}rubygem(rack) => 1.0
BuildRequires: %{?scl_prefix_ruby}rubygem(rack) < 2
BuildRequires: %{?scl_prefix_ruby}rubygem(rack-test)
BuildRequires: %{?scl_prefix_ruby}rubygem(rake)
BuildRequires: %{?scl_prefix}rubygem(sass)
BuildRequires: %{?scl_prefix_ruby}rubygem(therubyracer)
BuildRequires: %{?scl_prefix_ruby}rubygem(tilt) => 1.1
BuildRequires: %{?scl_prefix_ruby}rubygem(tilt) < 2
BuildConflicts: %{?scl_prefix_ruby}rubygem(tilt) = 1.3.0
%if "%{?scl_ruby}" == "ruby193" || (0%{?el6} && 0%{!?scl:1})
BuildRequires: %{?scl_prefix_ruby}ruby(abi)
%else
BuildRequires: %{?scl_prefix_ruby}ruby(release)
%endif
%if "%{?scl_v8}" != ""
BuildRequires: %{?scl_v8}
BuildRequires: %{?scl_v8}-scldevel
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

Obsoletes: ruby193-rubygem-%{gem_name}

%description
Sprockets is a Rack-based asset packaging system that concatenates and serves
JavaScript, CoffeeScript, CSS, LESS, Sass, and SCSS.

%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} "}
gem install --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}
%{?scl:"}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
tar xzf %{SOURCE1}
# 4 errors due to missing Gems "eco" and "ejs"
%{?scl:scl enable %{scl} %{?scl_v8} - << \EOF}
testrb -Ilib test | grep '447 tests, 1158 assertions, 0 failures, 4 errors, 0 skips'
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%{_bindir}/sprockets
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%doc %{gem_docdir}

%changelog
* Fri Oct 10 2014 Dominic Cleal <dcleal@redhat.com> 2.8.2-2
- Rebuild under SCL for Foreman (ehelms@redhat.com)

* Tue Dec 11 2012 Josef Stribny <jstribny@redhat.com> - 2.8.2-1
- Upgraded to version 2.8.2
- Added rubygem-uglifier build dependency

* Wed Jul 18 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-1
- Initial package
