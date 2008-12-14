%define	module	Catalyst-Model-DBI
%define name	perl-%{module}
%define	modprefix Catalyst

%define version 0.20

%define	rel	1
%define release %mkrel 3

Summary:	Catalyst DBI Model Class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl(DBI)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This is the DBI model class for Catalyst. It is nothing more than a
simple wrapper for DBI.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/%{modprefix}
%{_mandir}/*/*

%clean
rm -rf %{buildroot}


