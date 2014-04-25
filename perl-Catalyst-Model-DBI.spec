%define	upstream_name	 Catalyst-Model-DBI
%define upstream_version 0.32

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Catalyst DBI Model Class

License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(DBIx::Connector)
BuildRequires:	perl(Catalyst) >= 5.0
BuildRequires:	perl(Class::C3)
BuildRequires:	perl(DBI)

BuildArch:	noarch

%description
This is the DBI model class for Catalyst. It is nothing more than a
simple wrapper for DBI.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Catalyst
%{_mandir}/*/*



