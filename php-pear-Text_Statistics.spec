%define		_class		Text
%define		_subclass	Statistics
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - compute readability indexes for documents
Summary(pl.UTF-8):	%{_pearname} - obliczanie wskaźników czytelnictwa dokumentów
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	53557e3e52d9d725162a6f8d77a7c94d
URL:		http://pear.php.net/package/Text_Statistics/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Text_Statistics-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Statistics allows for computation of readability indexes for text
documents.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa Text_Statistics pozwala na obliczanie wskaźników czytelnictwa
dla dokumentów tekstowych.

Ta klasa ma w PEAR status: %{_status}.

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
