%global git 8b12e08
%global uuid calc@patapon.info
%global github eonpatapon

Name:		gnome-shell-extension-calc
Version:	0
Release:	0.4.git%{git}%{?dist}
Summary:	A simple calculator in the search overview

Group:		User Interface/Desktops
License:	GPLv2+
URL:		https://github.com/eonpatapon/gnome-shell-extension-calc
Source0:	https://github.com/eonpatapon/gnome-shell-extension-calc/tarball/master/%{github}-%{name}-%{git}.tar.gz
BuildArch:	noarch

Requires:	gnome-shell >= 3.2.1

%description
Gnome shell extension that allows to make simple math operations in 
the search overview

%prep
%setup -q -n %{github}-%{name}-%{git}


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%files
%doc README.md COPYING screenshot.png
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Sat May 12 2012 Yader Velasquez <yaderv@fedoraproject.org> - 0-0.4.git8b12e08
- support for gnome "3.4"

* Sun Jan 15 2012 Yader Velasquez <yaderv@fedoraproject.org> - 0-0.3.git2fca097
- buildroot cleaning and defattr macro removed

* Thu Jan 05 2012 Yader Velasquez <yaderv@fedoraproject.org> - 0-0.2.git2fca097
- new source url
- license changed to GPLv2+
- clean section removed

* Mon Dec 26 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0-0.1.gitc92bb40
- first package
