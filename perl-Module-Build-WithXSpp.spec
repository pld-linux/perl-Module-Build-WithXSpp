#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Module
%define		pnam	Build-WithXSpp
%include	/usr/lib/rpm/macros.perl
Summary:	Module::Build::WithXSpp - XS++ enhanced flavour of Module::Build
Name:		perl-Module-Build-WithXSpp
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f3d6ad08127f62eed9baef131870f450
URL:		http://search.cpan.org/dist/Module-Build-WithXSpp/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(ExtUtils::CppGuess) >= 0.04
BuildRequires:	perl(ExtUtils::XSpp) >= 0.11
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This subclass of Module::Build adds some tools and
processes to make it easier to use for wrapping C++
using XS++ (ExtUtils::XSpp).

There are a few minor differences from using Module::Build
for an ordinary XS module and a few conventions that you
should be aware of as an XS++ module author. They are documented
in the /"FEATURES AND CONVENTIONS" section below. But if you
can't be bothered to read all that, you may choose skip it and
blindly follow the advice in /"JUMP START FOR THE IMPATIENT".

An example of a full distribution based on this build tool
can be found in the ExtUtils::XSpp distribution under
examples/XSpp-Example. Using that example as the basis
for your Module::Build::WithXSpp-based distribution
is probably a good idea.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/Build/*.pm
#%{perl_vendorlib}/Module/Build/WithXSpp
%{_mandir}/man3/*
