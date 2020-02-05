Name:           dynamips
Version:        0.2.21
Release:        2%{?dist}
Summary:        Cisco Router Emulator

# There is a GPL license file in COPYING but most files
# are missing a proper license header and some are pre-compiled
License:        Proprietary
URL:            https://github.com/GNS3/dynamips
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  elfutils-libelf-devel
BuildRequires:  libpcap-devel
BuildRequires:  libuuid-devel

%description
Dynamips is an IOS emulator with hypervisor, allowing users
to run several IOS images (in particular 3600 and 7200 series) as fully
functional routers


%prep
%autosetup -p1


%build
mkdir build
cd build
%{cmake} \
  ..

# Theses options don't build yet
#  -DBUILD_UDP_SEND:BOOL=True \
#  -DBUILD_UDP_RECV:BOOL=True \

%make_build


%install
cd build
%make_install

# Don't install pre-installed docs
rm -rf %{buildroot}%{_docdir}/dynamips


%files
%doc README.hypervisor ChangeLog MAINTAINERS
%doc RELEASE-NOTES TODO
# Don't distribute the COPYING until license is clarified
#license COPYING
%{_bindir}/%{name}
%{_bindir}/nvram_export
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/nvram_export.1.gz
%{_mandir}/man7/hypervisor_mode.7.gz


%changelog
* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.2.21-1
- Update dynamips

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.2.18-1
- Update to 0.2.18

* Tue Jan 13 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.2.14-1
- Update to 0.2.14
- Cleanup spec file

* Tue Apr 27 2010 Lucian Langa <cooly@gnome.eu.org> - 0.2.8-0.1.RC2
- update patch0
- update to upstream pre-release version

* Tue Mar 31 2009 Lucian Langa <cooly@gnome.eu.org> - 0.2.7-5
- misc cleanups

* Sat Aug 18 2007 Nigel Jones <dev@nigelj.com> 0.2.7-4
- Opps, silly mistakes/tiny touchups

* Sat Aug 18 2007 Nigel Jones <dev@nigelj.com> 0.2.7-3
- Fix License tag,
- Include Documentation (opps)
- Remove 'Cisco' from description

* Fri Jun 29 2007 Nigel Jones <dev@nigelj.com> 0.2.7-2
- Small touchups

* Fri Jun 29 2007 Nigel Jones <dev@nigelj.com> 0.2.7-1
- Initial RPM
