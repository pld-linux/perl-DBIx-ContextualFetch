#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	ContextualFetch
Summary:	Add contextual fetches to DBI
Summary(pl):	Dodanie kontekstowych pobrañ do DBI
Name:		perl-DBIx-ContextualFetch
Version:	1.01
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d36c5244c73a973a945b9294b619fe49
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBD-SQLite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBIx::ContextualFetch module adds contextual fetches to DBI. DBI
itself doesn't take much advantage of Perl's context sensitivity.
DBIx::ContextualFetch redefines some of the various fetch methods to
fix this oversight. It also adds a few new methods for convenience
(though not necessarily efficiency).

%description -l pl
Modu³ DBIx::ContextualFetch dodaje kontekstowe pobrania do DBI. Samo
DBI nie robi wiêkszego u¿ytku z perlowej kontekstowo¶ci.
DBIx::ContextualFetch redefiniuje czê¶æ ró¿nych metod pobieraj±cych,
aby poprawiæ to przeoczenie. Dodaje tak¿e kilka nowych metod dla
wygody (ale niekoniecznie wydajno¶ci).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DBIx/ContextualFetch.pm
%{_mandir}/man3/*
