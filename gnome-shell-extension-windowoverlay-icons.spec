%global git 72282ce 
%global uuid windowoverlay-icons@sustmidown.centrum.cz
%global github gnome-shell-extensions-sustmi

Name:			gnome-shell-extension-windowoverlay-icons
Version:		3.0
Release:		3.git%{git}%{?dist}
Summary:		Viewing the app icons over the window in the windows overview

Group:			User Interface/Desktops
License:		GPLv3+
URL:			https://github.com/sustmi/gnome-shell-extensions-sustmi
Source0:		https://github.com/sustmi/gnome-shell-extensions-sustmi/tarball/master/sustmi-%{github}-%{version}-4-g%{git}.tar.gz
BuildArch:		noarch

Requires:		gnome-shell

%description
This extension allow to view the icons over the application in the 
windows overview. Useful to avoid confusion with the windows when
you have a lot of them open on the same desktop.

%prep
%setup -q -n sustmi-%{github}-%{git}


%build
# Nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 windowoverlay-icons/{extension.js,metadata.json,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Sun Dec 25 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-3.git72282ce
- Post relase git checkout 72282ce
- Include support for gnome 3.2

* Tue Dec 20 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-2
- Fix longitude line errors

* Sat Dec 17 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-1
- First pkg
