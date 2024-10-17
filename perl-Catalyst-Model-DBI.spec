%define	upstream_name	 Catalyst-Model-DBI
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Catalyst DBI Model Class
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.280.0-2mdv2011.0
+ Revision: 680720
- mass rebuild

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 497906
- update to 0.28

* Fri Jan 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.1
+ Revision: 494963
- adding missing buildrequires:
- update to 0.25

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2010.1
+ Revision: 460824
- update to 0.24

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 408939
- rebuild using %%perl_convert_version

* Sun Dec 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-3mdv2009.1
+ Revision: 314241
- update to new version 0.20

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.19-3mdv2009.0
+ Revision: 241154
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.0
+ Revision: 46970
- update to new version 0.19


* Sun Jan 28 2007 Buchan Milne <bgmilne@mandriva.org> 0.15-1mdv2007.0
+ Revision: 114646
- New version 0.15

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Catalyst-Model-DBI

* Tue Jun 27 2006 Scott Karns <scottk@mandriva.org> 0.14-1mdv2007.0
- Version 0.14

* Thu Jun 01 2006 Scott Karns <scottk@mandriva.org> 0.13-1mdv2007.0
- Version 0.13

* Wed May 31 2006 Scott Karns <scottk@mandriva.org> 0.12-1mdv2007.0
- Version 0.12

* Fri Mar 17 2006 Buchan Milne <bgmilne@mandriva.org> 0.11-1mdk
- First Mandriva package, from Scott Ryan

