Summary:	gurgitate mail filtering and mail delivery agent
Summary(pl):	gurgitate - narzêdzie do filtrowania i dostarczania poczty
Name:		gurgitate-mail
Version:	1.6.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.dagbrown.com/software/gurgitate-mail/%{name}-%{version}.tar.gz
# Source0-md5:	9a35334c512f9111d9d95e6e549e283c
URL:		http://www.dagbrown.com/software/gurgitate-mail/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"gurgitate-mail" is a program which reads your mail and filters it
according to the .gurgitate-rules.rb file in your home directory. The
configuration file uses Ruby syntax and is thus quite flexible.

%description -l pl
gurgitate-mail to program odczytuj±cy pocztê i filtruj±cy j± zgodnie z
plikiem .gurgitate-rules.rb w katalogu domowym. Plik konfiguracyjny
u¿ywa sk³adni Ruby'ego, przez co jest do¶æ elastyczny.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_rubylibdir},%{_mandir}/man1}

echo "#!/usr/bin/ruby" > $RPM_BUILD_ROOT%{_bindir}/gurgitate-mail
cat gurgitate-mail >> $RPM_BUILD_ROOT%{_bindir}/gurgitate-mail
chmod +x $RPM_BUILD_ROOT%{_bindir}/gurgitate-mail
cp -a gurgitate-mail.rb $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a gurgitate $RPM_BUILD_ROOT%{ruby_rubylibdir}
install gurgitate-mail.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{ruby_rubylibdir}/*
%{_mandir}/man1/*
