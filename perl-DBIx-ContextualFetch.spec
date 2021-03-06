#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	DBIx
%define		pnam	ContextualFetch
Summary:	Add contextual fetches to DBI
Summary(pl.UTF-8):	Dodanie kontekstowych pobrań do DBI
Name:		perl-DBIx-ContextualFetch
Version:	1.03
Release:	2
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	20a78432ae26b266216b7b30ff7941c3
URL:		http://search.cpan.org/dist/DBIx-ContextualFetch/
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

%description -l pl.UTF-8
Moduł DBIx::ContextualFetch dodaje kontekstowe pobrania do DBI. Samo
DBI nie robi większego użytku z perlowej kontekstowości.
DBIx::ContextualFetch redefiniuje część różnych metod pobierających,
aby poprawić to przeoczenie. Dodaje także kilka nowych metod dla
wygody (ale niekoniecznie wydajności).

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
