%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Statistics
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - compute readability indexes for documents
Summary(pl):	%{_pearname} - obliczanie wska¼ników czytelnictwa dokumentów
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	4714f16104fe67ff728f581e6dfcd563
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Text_Statistics/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Statistics allows for computation of readability indexes for text
documents.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa Text_Statistics pozwala na obliczanie wska¼ników czytelnictwa
dla dokumentów tekstowych.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
