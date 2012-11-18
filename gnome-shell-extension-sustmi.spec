%global git 72282ce 
%global wiuuid windowoverlay-icons@sustmidown.centrum.cz
%global hpsuuid historymanager-prefix-search@sustmidown.centrum.cz
%global github gnome-shell-extensions-sustmi

Name:			gnome-shell-extension-sustmi
Version:		3.0
Release:		6.git%{git}%{?dist}
Summary:		Include two extensions, windowoverlay-icons and historymanager-prefix-search

Group:			User Interface/Desktops
License:		GPLv3+
URL:			https://github.com/sustmi/gnome-shell-extensions-sustmi
Source0:		https://github.com/sustmi/gnome-shell-extensions-sustmi/tarball/master/sustmi-%{github}-%{version}-4-g%{git}.tar.gz
BuildArch:		noarch

Requires:		gnome-shell

%description
This package provides two GNOME Shell extensions, windowoverlay-icons
and historymanager-prefix-search

%package		windowoverlay-icons
Summary:		Viewing the app icons over the window in the windows overview

%description	windowoverlay-icons
This extension allow to view the icons over the application in the 
windows overview. Useful to avoid confusion with the windows when
you have a lot of them open on the same desktop

%package		historymanager-prefix-search
Summary:		Use PageUp and PageDown to move in the log according the prefix

%description	historymanager-prefix-search
Use PageUp and PageDown to move in HistoryManager (eg. RunCommand, 
Looking Glass) according to prefix

%prep
%setup -q -n sustmi-%{github}-%{git}


%build
# Nothing to build


%install
# Install windowoverlay-icons
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{wiuuid}
install -Dp -m 0644 windowoverlay-icons/{extension.js,metadata.json,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{wiuuid}/

# Install historymanager-prefix-search
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{hpsuuid}
install -Dp -m 0644 historymanager-prefix-search/{extension.js,metadata.json,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{hpsuuid}/


%files			windowoverlay-icons
%doc README COPYING
%{_datadir}/gnome-shell/extensions/%{wiuuid}/

%files			historymanager-prefix-search
%doc README COPYING
%{_datadir}/gnome-shell/extensions/%{hpsuuid}/

%changelog

* Sun Jan 29 2012 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-6.git72282ce
- Description fixed

* Sat Jan 15 2012 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-5.git72282ce
- Buildroot cleaning and defattr macro removed

* Sat Jan 14 2012 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-4.git72282ce
- Create sub-package for historymanager-prefix-search

* Sun Dec 25 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-3.git72282ce
- Post relase git checkout 72282ce
- Include support for gnome 3.2

* Tue Dec 20 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-2
- Fix longitude line errors

* Sat Dec 17 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.3-1
- First pkg
