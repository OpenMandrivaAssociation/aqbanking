%define major 43
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

%define gwenmajor 60
%define aqhbcimajor 24
%define aqhbcilibname %mklibname aqhbci %{aqhbcimajor}
%define ofxmajor 7
%define ofxlibname %mklibname aqofxconnect %{ofxmajor}
%define cppmajor 0
%define cpplibname %mklibname aqbankingpp %{cppmajor}
%define ebicsmajor 0
%define ebicslibname %mklibname aqebics %ebicsmajor
%define paypalmajor 0
%define paypallibname %mklibname paypal %paypalmajor

Summary:	A library for online banking functions and financial data import/export
Name:		aqbanking
Version:	5.99.33beta
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.aquamaniac.de/sites/aqbanking/index.php
Source0:	https://www.aquamaniac.de/rdm/attachments/download/145/aqbanking-%{version}.tar.gz
BuildRequires:	pkgconfig(gwenhywfar)
BuildRequires:	libchipcard-devel
BuildRequires:	libtool-devel
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(ktoblzcheck)
BuildRequires:	gmp-devel
BuildRequires:	gwenhywfar-tools
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(xmlsec1-gnutls) >= 1.0.0
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(gnutls)

%description
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package -n %{cpplibname}
Summary:	CPP wrapper Aqbanding
Group:		System/Libraries

%description -n %{cpplibname}
This is the CPP wrapper for Aqbanding.

%package ofx
Summary: Aqbanking tools for OFX
Group: System/Libraries

%description ofx
Necessary for OFX direct connect access.

%package -n aqhbci
Summary:	The HBCI backend for the Aqbanking library
Group:		System/Libraries

%description -n aqhbci
This is the backend for the Aqbanking library which 
implements a client for the German HBCI (Home Banking Computer
Interface) protocol.

%package -n %{aqhbcilibname}
Summary:	Library for HBCI backend for Aqbanding
Group:		System/Libraries
Requires:	aqhbci >= %{version}

%description -n %{aqhbcilibname}
This is the backend for the Aqbanking library which 
implements a client for the German HBCI (Home Banking Computer
Interface) protocol.

%package -n aqebics
Summary: The EBICS backend for the Aqbanking library
Group: System/Libraries

%description -n aqebics
This is the backend for the Aqbanking library which
implements a client for the EBICS protocol.

%package -n aqpaypal
Summary: The Paypal backend for the Aqbanking library
Group: System/Libraries

%description -n aqpaypal
This is the backend for the Aqbanking library which
implements a client for Paypal

%package -n %{ebicslibname}
Summary: Library for AqEBICS backend for Aqbanding
Group: System/Libraries

%description -n %{ebicslibname}
This is the backend for the Aqbanking library which
implements a client for the EBICS protocol.

%package -n %{paypallibname}
Summary: Library for Paypal backend for Aqbanding
Group: System/Libraries

%description -n %{paypallibname}
This is the backend for the Aqbanking library which
implements a client for Paypal.

%package -n %{libname}
Summary:	A library for online banking functions and financial data import/export
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n %{libname}
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package -n %{devname}
Summary:	Aqbanking development kit
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{aqhbcilibname} < %{version}-%{release}
Obsoletes:	%{ofxlibname} < %{version}-%{release}
Obsoletes:	%{cpplibname} < %{version}-%{release}
Obsoletes:	%{ebicslibname} < %{version}-%{release}
Obsoletes:	%{paypallibname} < %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	opensp-devel
Provides:	aqhbci-devel = %{version}-%{release}
Provides:	libaqhbci-devel = %{version}-%{release}

%description -n %{devname}
This package contains aqbanking-config and header files for writing and
compiling programs using Aqbanking.

%prep
%setup -q
%apply_patches

autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*/*/*/*/*.a

%find_lang %{name}

%files -n aqhbci
%{_bindir}/aqhbci-tool4
%{_libdir}/%{name}/plugins/%{major}/providers/aqhbci*

%files -f %{name}.lang
%doc %{_docdir}/aqbanking
%{_bindir}/aqbanking-cli
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{major}/
%dir %{_libdir}/%{name}/plugins/%{major}/providers/
%dir %{_libdir}/%{name}/plugins/%{major}/imexporters/
%dir %{_libdir}/%{name}/plugins/%{major}/dbio/
%{_libdir}/%{name}/plugins/%{major}/bankinfo/
%{_libdir}/%{name}/plugins/%{major}/imexporters/camt*
%{_libdir}/%{name}/plugins/%{major}/imexporters/csv*
%{_libdir}/%{name}/plugins/%{major}/imexporters/ctxfile*
%{_libdir}/%{name}/plugins/%{major}/imexporters/eri*
%{_libdir}/%{name}/plugins/%{major}/imexporters/openhbci*
%{_libdir}/%{name}/plugins/%{major}/imexporters/q43.*
%{_libdir}/%{name}/plugins/%{major}/imexporters/sepa*
%{_libdir}/%{name}/plugins/%{major}/imexporters/swift*
%{_libdir}/%{name}/plugins/%{major}/imexporters/xml*
%{_libdir}/%{name}/plugins/%{major}/imexporters/yellownet*
%{_libdir}/%{name}/plugins/%{major}/providers/aqnone*
%{_libdir}/%{name}/plugins/%{major}/dbio/swift.so
%{_libdir}/%{name}/plugins/%{major}/dbio/swift.xml
%{_datadir}/%{name}

%files ofx
%{_libdir}/%{name}/plugins/%{major}/imexporters/ofx*
%{_libdir}/%{name}/plugins/%{major}/providers/aqofxconnect*

%files -n aqebics
%_bindir/aqebics-tool
%{_libdir}/%{name}/plugins/%major/providers/aqebics.*

%files -n aqpaypal
%_bindir/aqpaypal-tool

%files -n %{libname}
%{_libdir}/libaqbanking.so.%{major}*

%files -n %{devname}
%{_bindir}/aqbanking-config
%{_includedir}/aqbanking6
%{_libdir}/cmake/aqbanking-5.99
%{_libdir}/libaqbanking.so
%{_datadir}/aclocal/aqbanking.m4
%{_libdir}/pkgconfig/aqbanking.pc

