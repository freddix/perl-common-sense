%include	/usr/lib/rpm/macros.perl

%define		pdir	common
%define		pnam	sense

Summary:	Module implementing sane defaults in Perl scripts
Name:		perl-common-sense
Version:	3.73
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6da7455a43ab60ed21c2a5e3b3ddeda8
Patch0:		%{name}-bug87486.patch
URL:		http://search.cpan.org/dist/common-sense/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements some sane defaults for Perl programs, as
defined by two typical (or not so typical - use your common sense)
specimens of Perl coders.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}
# revert upstream change
# to be removed in 2073, after freddix will upgrade to perl 5.16
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%dir %{perl_vendorlib}/common
%{perl_vendorlib}/common/*.pm
%{_mandir}/man3/common::sense.3pm*

