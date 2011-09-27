%define name aqbanking
%define version 5.0.16
%define release %mkrel 1
%define major 33
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}
%define fname %{name}-%{version}
%define gwenmajor 60
%define aqhbcimajor 20
%define aqhbcilibname %mklibname aqhbci %{aqhbcimajor}
%define ofxmajor 7
%define ofxlibname %mklibname aqofxconnect %{ofxmajor}
%define cppmajor 0
%define cpplibname %mklibname aqbankingpp %{cppmajor}

Name: %{name}
Summary: A library for online banking functions and financial data import/export
Version: %{version}
Release: %{release}
Source: http://files.hboeck.de/aq/%fname.tar.gz
Patch0: aqbanking-4.99.6-fix-link.patch
Group: System/Libraries
License: GPLv2+
URL: http://www.aquamaniac.de/sites/aqbanking/index.php
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libgwenhywfar-devel >= 4.0.4
BuildRequires: libchipcard-devel
BuildRequires: libofx-devel >= 0.8.2
BuildRequires: libktoblzcheck-devel
BuildRequires: gmp-devel

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
Summary: Library for OFX access for Aqbanding
Group: System/Libraries

%description -n %{ofxlibname}
Library for the Aqbanking OFX access.

%package -n %{cpplibname}
Summary: CPP wrapper Aqbanding
Group: System/Libraries
Obsoletes: %{_lib}aqbankingppccppmajor < 5.0.7-2
Obsoletes: %{_lib}aqbankingpp%{ccppmajor} < 5.0.7-3

%description -n %{cpplibname}
This is the CPP wrapper for Aqbanding.

%package ofx
Summary: Aqbanking tools for OFX
Group: System/Libraries

%description ofx
Necessary for OFX direct connect access.

%package -n aqhbci
Summary: The HBCI backend for the Aqbanking library
Group: System/Libraries

%description -n aqhbci
This is the backend for the Aqbanking library which 
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. 

%package -n %{aqhbcilibname}
Summary: Library for HBCI backend for Aqbanding
Group: System/Libraries
Requires: aqhbci >= %{version}

%description -n %{aqhbcilibname}
This is the backend for the Aqbanking library which 
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. 

%package -n %{libname}
Summary: A library for online banking functions and financial data import/export
Group: System/Libraries
Requires: %{name} >= %{version}

%description -n %{libname}
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package -n %{develname}
Summary: Aqbanking development kit
Group: Development/C++
Requires: %{libname} = %{version}
Requires: %{aqhbcilibname} = %{version}
Requires: %{ofxlibname} = %{version}
Requires: %{cpplibname} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Requires: OpenSP-devel
Provides: aqhbci-devel = %{version}-%{release}
Provides: libaqhbci-devel = %{version}-%{release}
Obsoletes: %mklibname -d %{name} 16
Obsoletes: %mklibname -d aqhbci 10
Obsoletes: %mklibname -d qbanking 4
Obsoletes: %mklibname -d aqofxconnect 3

%description -n %{develname}
This package contains aqbanking-config and header files for writing and
compiling programs using Aqbanking.

%prep
%setup -q -n %{fname}
%patch0 -p0 -b .link

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %{name}.lang installed-docs

%makeinstall_std
rm -f %{buildroot}%{_libdir}/*/*/*/*/*.a
find %{buildroot}%{_libdir} -name \*.la|xargs rm -f

%find_lang %{name}
mv %{buildroot}%{_datadir}/doc/%{name} installed-docs
mv %{buildroot}%{_datadir}/doc/aqhbci/* installed-docs

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n aqhbci
%defattr(-,root,root)
%doc src/plugins/backends/aqhbci/tools/aqhbci-tool/README
%{_bindir}/aqhbci-tool4
%{_bindir}/hbcixml3
%{_libdir}/%{name}/plugins/%{major}/providers/aqhbci*

%files -n %{aqhbcilibname}
%defattr(-,root,root)
%{_libdir}/libaqhbci.so.%{aqhbcimajor}*

%files -f %{name}.lang
%defattr(-,root,root)
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
%defattr(-,root,root)
%dir %{_libdir}/%{name}/plugins/%{major}/imexporters/ofx*
%{_libdir}/%{name}/plugins/%{major}/providers/aqofxconnect*

%files -n %{ofxlibname}
%defattr(-,root,root)
%{_libdir}/libaqofxconnect.so.%{ofxmajor}*

%files -n %{cpplibname}
%defattr(-,root,root)
%{_libdir}/libaqbankingpp.so.%{cppmajor}*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libaqbanking.so.%{major}*
%{_libdir}/libaqnone.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/aqbanking-config
%{_includedir}/aqbanking5
%{_libdir}/libaqbankingpp.so
%{_libdir}/libaqbanking.so
%{_libdir}/libaqnone.so
%{_libdir}/libaqhbci.so
%{_libdir}/libaqofxconnect.so
%{_datadir}/aclocal/aqbanking.m4
%{_libdir}/pkgconfig/aqbanking.pc
