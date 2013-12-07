%define major 34
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

%define gwenmajor 60
%define aqhbcimajor 20
%define aqhbcilibname %mklibname aqhbci %{aqhbcimajor}
%define ofxmajor 7
%define ofxlibname %mklibname aqofxconnect %{ofxmajor}
%define cppmajor 0
%define cpplibname %mklibname aqbankingpp %{cppmajor}

Summary:	A library for online banking functions and financial data import/export
Name:		aqbanking
Version:	5.0.25
Release:	6
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.aquamaniac.de/sites/aqbanking/index.php
Source:		http://files.hboeck.de/aq/%{name}-%{version}.tar.gz
Patch0:		aqbanking-4.99.6-fix-link.patch
BuildRequires:	pkgconfig(gwenhywfar)
BuildRequires:	libchipcard-devel
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(ktoblzcheck)
BuildRequires:	gmp-devel
BuildRequires:	gwenhywfar-tools

%description
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package -n %{ofxlibname}
Summary:	Library for OFX access for Aqbanding
Group:		System/Libraries

%description -n %{ofxlibname}
Library for the Aqbanking OFX access.

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
Requires:	%{aqhbcilibname} = %{version}-%{release}
Requires:	%{ofxlibname} = %{version}-%{release}
Requires:	%{cpplibname} = %{version}-%{release}
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
%patch0 -p0 -b .link

%build
%configure2_5x
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*/*/*/*/*.a

%find_lang %{name}

mv %{buildroot}%{_datadir}/doc/%{name} installed-docs
mv %{buildroot}%{_datadir}/doc/aqhbci/* installed-docs

%files -n aqhbci
%doc src/plugins/backends/aqhbci/tools/aqhbci-tool/README
%{_bindir}/aqhbci-tool4
%{_bindir}/hbcixml3
%{_libdir}/%{name}/plugins/%{major}/providers/aqhbci*

%files -n %{aqhbcilibname}
%{_libdir}/libaqhbci.so.%{aqhbcimajor}*

%files -f %{name}.lang
%doc installed-docs
%{_bindir}/aqbanking-cli
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%{major}/
%dir %{_libdir}/%{name}/plugins/%{major}/providers/
%dir %{_libdir}/%{name}/plugins/%{major}/imexporters/
%{_libdir}/%{name}/plugins/%{major}/bankinfo/
%{_libdir}/%{name}/plugins/%{major}/imexporters/csv*
%{_libdir}/%{name}/plugins/%{major}/imexporters/ctxfile*
%{_libdir}/%{name}/plugins/%{major}/imexporters/dtaus*
%{_libdir}/%{name}/plugins/%{major}/imexporters/eri*
%{_libdir}/%{name}/plugins/%{major}/imexporters/openhbci*
%{_libdir}/%{name}/plugins/%{major}/imexporters/q43.*
%{_libdir}/%{name}/plugins/%{major}/imexporters/sepa*
%{_libdir}/%{name}/plugins/%{major}/imexporters/swift*
%{_libdir}/%{name}/plugins/%{major}/imexporters/xmldb*
%{_libdir}/%{name}/plugins/%{major}/imexporters/yellownet*
%{_libdir}/%{name}/plugins/%{major}/providers/aqnone*
%{_libdir}/gwenhywfar/plugins/%{gwenmajor}/dbio/dtaus.so
%{_libdir}/gwenhywfar/plugins/%{gwenmajor}/dbio/dtaus.xml
%{_libdir}/gwenhywfar/plugins/%{gwenmajor}/dbio/swift.so
%{_libdir}/gwenhywfar/plugins/%{gwenmajor}/dbio/swift.xml
%{_datadir}/%{name}

%files ofx
%dir %{_libdir}/%{name}/plugins/%{major}/imexporters/ofx*
%{_libdir}/%{name}/plugins/%{major}/providers/aqofxconnect*

%files -n %{ofxlibname}
%{_libdir}/libaqofxconnect.so.%{ofxmajor}*

%files -n %{cpplibname}
%{_libdir}/libaqbankingpp.so.%{cppmajor}*

%files -n %{libname}
%{_libdir}/libaqbanking.so.%{major}*
%{_libdir}/libaqnone.so.%{major}*

%files -n %{devname}
%{_bindir}/aqbanking-config
%{_includedir}/aqbanking5
%{_libdir}/libaqbankingpp.so
%{_libdir}/libaqbanking.so
%{_libdir}/libaqnone.so
%{_libdir}/libaqhbci.so
%{_libdir}/libaqofxconnect.so
%{_datadir}/aclocal/aqbanking.m4
%{_libdir}/pkgconfig/aqbanking.pc

