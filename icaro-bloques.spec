%global github valentinbasel
%global commit 061483c

Name:           icaro-bloques
Version:        1
Release:        1%{?dist}
Summary:        A front-end for Icaro, a robotic educational project

License:        GPLv3
URL:            http://roboticaro.org/
Source0:        https://github.com/valentinbasel/icaro-bloques/tarball/master/%{github}-%{name}-%{commit}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
Requires:       pygame, pywebkitgtk, pygtksourceview, sdcc, gputils

%description
Icaro-bloques is a front-end for the Icaro Project, an educational robotic
software aimed to develop robotic and programming fundamentals.

%prep
%setup -q -n %{github}-%{name}-%{commit}

%build
# Nothing to build


%install
rm -rf %{buildroot}
#este proceso podrá variar, por el momento solo
#pruebas de instalar librerías
mkdir -p %{buildroot}%{_datadir}/sdcc/include/pic16
cp -a sdcc-include/*.h %{buildroot}%{_datadir}/sdcc/include/pic16
mkdir -p %{buildroot}%{_datadir}/sdcc/lib/pic16
cp -a sdcc-include/libdev18f4550.lib %{buildroot}%{_datadir}/sdcc/include/pic16
#copia de directorios
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a {funcion,lib,lkr,obj,source,tmp,tortucaro,include,componente,imagenes} %{buildroot}%{_datadir}/%{name}/
#copia de archivos
install {*.py,*.xml,*.dat,version} %{buildroot}%{_datadir}/%{name}/

%files
%doc README INSTALL COPYING AUTHORS documentos/publican/manual_np05/tmp/es-ES/pdf/Manual-0.1-manual_np05-es-ES.pdf
%{_datadir}/%{name}/
%{_datadir}/sdcc/include/pic16/
%{_datadir}/sdcc/lib/pic16/


%changelog
* Thu Sep 28 2012 Yader Velasquez <yaderv@fedoraproject.org> - 1-1
- Primer borrador de spec
