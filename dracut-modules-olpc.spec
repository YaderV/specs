Name:		dracut-modules-olpc
Version:	0.6.0
Release:	1%{?dist}
Summary:	OLPC modules for dracut initramfs

Group:		System Environment/Base
License:	GPLv2
URL:		http://wiki.laptop.org/go/Dracut-modules-olpc
Source0:	http://dev.laptop.org/pub/source/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	Pyrex, zlib-devel, python-devel, netpbm-progs
Requires:		dracut, bitfrost, mtd-utils-ubi, wireless-tools, busybox

%description
Dracut initramfs modules to implement OLPC-specific features, including
antitheft, switching between OS updates, and the OLPC boot animation.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_datadir}/dracut/modules.d/*
%{_libdir}/dracut-modules-olpc
%config(noreplace) /etc/dracut-olpc-*.conf


%changelog
* Mon Oct 10 2011 Daniel Drake <dsd@laptop.org> - 0.6.0
- New F15+ compatible version
- Don't activate modules unless requested in configuration (#707423)

* Thu Oct  6 2011 Daniel Drake <dsd@laptop.org> - 0.5.18-1
- XO-1.75 activation GUI fix

* Thu Sep 15 2011 Daniel Drake <dsd@laptop.org> - 0.5.17-1
- UBIFS and JFFS2 fixes for XO-1

* Sun Aug 28 2011 Daniel Drake <dsd@laptop.org> - 0.5.16-1
- XO-1.75 support

* Wed Jul 06 2011 Daniel Drake <dsd@laptop.org> - 0.5.15-1
- Fix connecting to some APs for activation, thanks to Aleksey Lim

* Sat Jun 25 2011 Daniel Drake <dsd@laptop.org> - 0.5.14-1
- Fix mounting root filesystems after activation

* Sun Jun 19 2011 Daniel Drake <dsd@laptop.org> - 0.5.13-1
- Activation fixes

* Fri Jun 17 2011 Daniel Drake <dsd@laptop.org> - 0.5.12-1
- Include kernel modules in activation initramfs

* Wed Jun  1 2011 Daniel Drake <dsd@laptop.org> - 0.5.11-1
- Fix creation of /versions/running link

* Mon May 30 2011 Daniel Drake <dsd@laptop.org> - 0.5.10-1
- Fix purging of unpartitioned boot configs

* Tue May 17 2011 Daniel Drake <dsd@laptop.org> - 0.5.9-1
- Start boot animation while purging old versions

* Tue Feb 22 2011 Daniel Drake <dsd@laptop.org> - 0.5.8-1
- Install build configuration files in /etc

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 13 2010 Daniel Drake <dsd@laptop.org> - 0.5.7-1
- Fix booting from UBIFS partitions

* Wed Nov 10 2010 Daniel Drake <dsd@laptop.org> - 0.5.6-1
- Fix booting of new update. Disable fstab verification.

* Tue Nov  9 2010 Daniel Drake <dsd@laptop.org> - 0.5.5-1
- New version purges old updates during boot

* Sun Nov  7 2010 Daniel Drake <dsd@laptop.org> - 0.5.4-1
- Add olpc-busybox module to make smaller initramfs

* Wed Sep 29 2010 jkeating - 0.5.3-2
- Rebuilt for gcc bug 634757

* Sat Sep 11 2010 Daniel Drake <dsd@laptop.org> - 0.5.3-1
- Fix detection of boot filesystem

* Sat Sep 11 2010 Daniel Drake <dsd@laptop.org> - 0.5.2-2
- Add missing dep on wireless-tools

* Thu Sep  2 2010 Daniel Drake <dsd@laptop.org> - 0.5.2-1
- Add ubifs boot support

* Tue Aug 31 2010 Daniel Drake <dsd@laptop.org> - 0.5.1-1
- Generate activation initramfs separately

* Tue Aug 24 2010 Daniel Drake <dsd@laptop.org> - 0.5.0-1
- New version for F14 support

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed May 26 2010 Daniel Drake <dsd@laptop.org> - 0.3.4-1
- Fix activation problem introduced by greplease change

* Thu May 20 2010 Daniel Drake <dsd@laptop.org> - 0.3.3-1
- Fix booting on secure XO1, and parsing of large activation files

* Mon Dec 14 2009 Daniel Drake <dsd@laptop.org> - 0.3.2-1
- New version to fix activation code

* Mon Dec 7 2009 Daniel Drake <dsd@laptop.org> - 0.3.1-1
- New version to fix booting alternate image

* Tue Nov 24 2009 Daniel Drake <dsd@laptop.org> - 0.3.0-1
- New version

* Wed Nov 18 2009 Daniel Drake <dsd@laptop.org> - 0.2.8-1
- New version

* Tue Nov 17 2009 Daniel Drake <dsd@laptop.org> - 0.2.7-1
- New version

* Mon Nov 16 2009 Daniel Drake <dsd@laptop.org> - 0.2.6-1
- New version

* Fri Nov 13 2009 Daniel Drake <dsd@laptop.org> - 0.2.5-1
- New version

* Thu Nov 12 2009 Daniel Drake <dsd@laptop.org> - 0.2.4-1
- New version

* Mon Nov  9 2009 Daniel Drake <dsd@laptop.org> - 0.2.3-1
- New version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Daniel Drake <dsd@laptop.org> - 0.2.1-1
- Initial import

