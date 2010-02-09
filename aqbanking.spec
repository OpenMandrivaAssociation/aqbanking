%define name aqbanking
%define version 4.2.4
%define release %mkrel 2
%define major 29
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define fname %name-%{version}
%define gwenmajor 47
%define aqhbcimajor 17
%define aqhbcilibname %mklibname aqhbci %aqhbcimajor
%define qtmajor 8
%define qtlibname %mklibname qbanking %qtmajor
%define ofxmajor 5
%define ofxlibname %mklibname aqofxconnect %ofxmajor

Name: %{name}
Summary: A library for online banking functions and financial data import/export
Version: %{version}
Release: %{release}
Source: http://files.hboeck.de/aq/%fname.tar.gz
Group: System/Libraries
License: GPLv2+
URL: http://www.aquamaniac.de/sites/aqbanking/index.php
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libgwenhywfar-devel >= 3.10
BuildRequires: libchipcard-devel
BuildRequires: libofx-devel >= 0.8.2
BuildRequires: libktoblzcheck-devel
BuildRequires: gmp-devel
BuildRequires: qt4-devel
BuildConflicts: qt3-devel

%description 
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package qt3
Summary: QT3-based front-ends for Aqbanking
Group: System/Libraries
Obsoletes: aqhbci-qt-tools
Provides: aqhbci-qt-tools
Provides: aqbanking-ofx-qt3
Obsoletes: aqbanking-ofx-qt3
%description qt3 
Necessary for all banking applications.

%package -n %{qtlibname}
Summary: Library for QT3 front-end for Aqbanding
Group: System/Libraries

%description -n %{qtlibname}
Library for the Aqbanking QT3 integration.

%package -n %{ofxlibname}
Summary: Library for OFX access for Aqbanding
Group: System/Libraries

%description -n %{ofxlibname}
Library for the Aqbanking OFX access.

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
Requires: aqhbci >= %version

%description -n %{aqhbcilibname}
This is the backend for the Aqbanking library which 
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. 


%package -n %libname
Summary: A library for online banking functions and financial data import/export
Group: System/Libraries
Requires: %name >= %version

%description -n %libname
The intention of AqBanking is to provide a middle layer between the
program and the various Online Banking libraries (e.g. AqHBCI). The
first backend which is already supported is AqHBCI, a library which
implements a client for the German HBCI (Home Banking Computer
Interface) protocol. Additionally, Aqbanking provides various plugins
to simplify import and export of financial data. Currently there are
import plugins for the following formats: DTAUS (German financial
format), SWIFT (MT940 and MT942).

%package -n %develname
Summary: Aqbanking development kit
Group: Development/C++
Requires: %{libname} = %{version}
Requires: %aqhbcilibname = %version
Requires: %qtlibname = %version
Requires: %ofxlibname = %version
Provides: lib%name-devel = %{version}-%{release}
Requires: OpenSP-devel
Provides: aqhbci-devel = %version-%release
Provides: libaqhbci-devel = %version-%release
Obsoletes: %mklibname -d %name 16
Obsoletes: %mklibname -d aqhbci 10
Obsoletes: %mklibname -d qbanking 4
Obsoletes: %mklibname -d aqofxconnect 3

%description -n %develname
This package contains aqbanking-config and header files for writing and
compiling programs using Aqbanking.



%prep
%setup -q -n %fname

%build
#gw don't know where this is supposed to come from:
export target_cpu=%_arch
export qt3_libs="$(pkg-config QtCore QtGui Qt3Support --libs)"
export qt3_includes="$(pkg-config QtCore QtGui Qt3Support --cflags)"
export PATH=%_libdir/qt4/bin:$PATH
%configure2_5x --with-frontends="qbanking"
#parallel compilation must be disabled
#otherwise build will be linked with system libraries
#not the package one
make qt4-port

%install
rm -rf $RPM_BUILD_ROOT %name.lang installed-docs

%makeinstall_std
rm -f %buildroot%_libdir/*/*/*/*/*.a
perl -pi -e "s°-L$RPM_BUILD_DIR/%fname/src/libs/aqbanking°°" %buildroot%_libdir/*.la
perl -pi -e "s°-L$RPM_BUILD_DIR/%fname/src/plugins/backends/aqhbci/plugin°°" %buildroot%_libdir/*.la 
find %buildroot%_libdir/*/ -name \*.la|xargs rm -f
chmod 644 %buildroot%_libdir/*.la

%find_lang %name
mv %buildroot%_datadir/doc/%name installed-docs
mv %buildroot%_datadir/doc/aqhbci/* installed-docs

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files -n aqhbci
%defattr(-,root,root)
%doc src/plugins/backends/aqhbci/tools/aqhbci-tool/README
%_bindir/aqhbci-tool4
%{_bindir}/hbcixml3
%_libdir/%name/plugins/%major/providers/aqhbci*

%files -n %aqhbcilibname
%defattr(-,root,root)
%_libdir/libaqhbci.so.%{aqhbcimajor}*

%files -n %qtlibname
%defattr(-,root,root)
%{_libdir}/libqbanking.so.%{qtmajor}*

%files qt3
%defattr(-,root,root)
%_libdir/%name/plugins/%major/wizards/qt3-wizard
%_libdir/%name/plugins/%major/wizards/qt3_wizard.xml
%_libdir/%name/plugins/%major/debugger/aqhbci/
%_bindir/qb-help%{qtmajor}
%_libdir/%name/plugins/%major/frontends/qbanking/

%files -f %name.lang
%defattr(-,root,root)
%doc installed-docs
%{_bindir}/aqbanking-cli
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%major/
%dir %{_libdir}/%{name}/plugins/%major/providers/
#%dir %{_libdir}/%{name}/plugins/%major/wizards/
%dir %{_libdir}/%{name}/plugins/%major/imexporters/
%{_libdir}/%{name}/plugins/%major/bankinfo/
%{_libdir}/%{name}/plugins/%major/imexporters/csv*
%{_libdir}/%{name}/plugins/%major/imexporters/ctxfile*
%{_libdir}/%{name}/plugins/%major/imexporters/dtaus*
%{_libdir}/%{name}/plugins/%major/imexporters/eri*
%{_libdir}/%{name}/plugins/%major/imexporters/openhbci*
%{_libdir}/%{name}/plugins/%major/imexporters/sepa*
%{_libdir}/%{name}/plugins/%major/imexporters/swift*
%{_libdir}/%{name}/plugins/%major/imexporters/xmldb*
%{_libdir}/%{name}/plugins/%major/imexporters/yellownet*
%{_libdir}/%{name}/plugins/%major/providers/aqnone*
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/dtaus.so
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/dtaus.xml
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/swift.so
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/swift.xml

%{_datadir}/%{name}

%files ofx
%defattr(-,root,root)
%dir %{_libdir}/%{name}/plugins/%major/imexporters/ofx*
%{_libdir}/%{name}/plugins/%major/providers/aqofxconnect*

%files -n %ofxlibname
%defattr(-,root,root)
%_libdir/libaqofxconnect.so.%{ofxmajor}*

%files -n %libname
%defattr(-,root,root)
%{_libdir}/libaqbanking.so.%{major}*
%_libdir/libaqnone.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_bindir}/aqbanking-config
%{_includedir}/aqbanking
%{_includedir}/aqhbci/
%{_includedir}/aqofxconnect/
%{_includedir}/qbanking
%{_libdir}/libaqbanking.la
%{_libdir}/libaqnone.la
%{_libdir}/libaqbanking.so
%{_libdir}/libaqnone.so
%{_libdir}/libaqhbci.la
%_libdir/libaqhbci.so
%_libdir/libaqofxconnect.so
%_libdir/libaqofxconnect.la
%_libdir/libqbanking.la
%_libdir/libqbanking.so
%{_datadir}/aclocal/aqbanking.m4
%_libdir/pkgconfig/aqbanking.pc
