%define upstream_name    Class-DBI-Pg
Name:       perl-%{upstream_name}
Version:    0.09
Release:    6

Summary:    Class::DBI extension for Postgres
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Class-DBI-Pg
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Class::DBI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Class::DBI::Pg automate the setup of Class::DBI columns and primary key for
Postgres.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 680792
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 403009
- rebuild using %0.09 Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.09-3mdv2009.0
+ Revision: 241180
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.0
+ Revision: 81240
- import perl-Class-DBI-Pg


* Thu Sep 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.0
- first mdv release
