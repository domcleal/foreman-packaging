%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name deface

Summary: Deface is a library that allows you to customize views in Rails
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.0.2
Release: 1%{?dist}
Group: Development/Libraries
License: MIT
URL: https://github.com/DefaceCommunity/deface
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
Requires: %{?scl_prefix}rubygem(colorize) >= 0.5.8
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.6.0
Requires: %{?scl_prefix}rubygem(nokogiri) < 1.7.0
Requires: %{?scl_prefix_ror}rubygem(polyglot)
Requires: %{?scl_prefix_ror}rubygem(rails) >= 3.1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}rubygems
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%{?scl:Obsoletes: ruby193-rubygem-%{gem_name}}

%description
Deface is a library that allows you to customize ERB, Haml and Slim
views in a Rails application without editing the underlying view.

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

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/init.rb
%{gem_instdir}/tasks
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/gemfiles
%exclude %{gem_instdir}/spec

%files doc
%doc %{gem_instdir}/MIT-LICENSE
%doc %{gem_instdir}/CHANGELOG.markdown
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Mon Nov 16 2015 Dominic Cleal <dcleal@redhat.com> 1.0.2-1
- Update deface to 1.0.2 (dcleal@redhat.com)

* Thu Aug 27 2015 Dominic Cleal <dcleal@redhat.com> 1.0.1-1
- Update deface to 1.0.1 (dcleal@redhat.com)

* Wed Aug 26 2015 Dominic Cleal <dcleal@redhat.com> 0.7.2-7
- Converted to tfm SCL (dcleal@redhat.com)

* Wed Aug 14 2013 Lukas Zapletal <lzap+git@redhat.com> 0.7.2-6
- rebuild


* Fri May 31 2013 Miroslav Suchý <msuchy@redhat.com> 0.7.2-5
- change ruby(abi) to ruby(release) for F19+ (msuchy@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-3
- new package built with tito

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-2
- rubygem-deface - convert to scl (inecas@redhat.com)

* Thu Mar 28 2013 Ivan Necas <inecas@redhat.com> 0.7.2-1
- new package built with tito
