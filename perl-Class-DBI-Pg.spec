%define module  Class-DBI-Pg
%define name    perl-%{module}
%define version 0.09
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Class::DBI extension for Postgres
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Class/%{module}-%{version}.tar.gz
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Class::DBI)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Class::DBI::Pg automate the setup of Class::DBI columns and primary key for
Postgres.

%prep
%setup -q -n %{module}-%{version} 

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

