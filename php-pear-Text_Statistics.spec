%include	/usr/lib/rpm/macros.php
%define         _class          Text
%define         _subclass       Statistics
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Compute readability indexes for documents
Summary(pl):	%{_pearname} - obliczanie wska¼ników czytelnictwa dokumentów
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	4714f16104fe67ff728f581e6dfcd563
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Statistics allows for computation of readability indexes for text
documents.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa Text_Statistics pozwala na obliczanie wska¼ników czytelnictwa
dla dokumentów tekstowych.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
