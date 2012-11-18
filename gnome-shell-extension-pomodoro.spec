%global git 9cbaf93
%global uuid pomodoro@arun.codito.in 
%global github codito-gnome-shell-pomodoro

Name:           gnome-shell-extension-pomodoro
Version:        0.5
Release:        1%{?dist}
Summary:        A gnome-shell extension for the pomodoro technique

Group:          User Interface/Desktops
License:        GPLv3+
URL:            https://github.com/codito/gnome-shell-pomodoro
Source0:        https://github.com/codito/gnome-shell-pomodoro/tarball/%{version}/%{github}-%{version}-1-g%{git}.tar.gz
BuildArch:      noarch

Requires:       gnome-shell >= 3.2.0


%description
This extension helps you to work with the pomodoro technique here. It
provides a countdown timer in the gnome-shell and keeps track of completed
25 minute cycles.


%prep
%setup -q -n %{github}-%{git}


%build
# Nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 %{uuid}/{extension.js,metadata.json,bell.wav} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/


%files
%defattr(-,root,root,-)
%doc README.md COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog
* Thu Dec 08 2011 Yader Velasquez <yaderv@fedoraproject.org> - 0.5-1
- Version 0.5

* Fri Jun 03 2011 Fabian Affolter <fabian@bernewireless.net> - 0-0.2.git13030cd
- License is GPLv3+
- COPYING file added

* Thu Jun 02 2011 Fabian Affolter <fabian@bernewireless.net> - 0-0.1.git286a249
- Initial package for Fedora
