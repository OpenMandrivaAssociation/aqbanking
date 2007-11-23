%define name aqbanking
%define version 2.3.3
%define release %mkrel 1
%define major 16
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define fname %name-%{version}
%define gwenmajor 38
%define aqhbcimajor 10
%define aqhbcilibname %mklibname aqhbci %aqhbcimajor
%define qtmajor 4
%define qtlibname %mklibname qbanking %qtmajor
%define gtkmajor 2
%define gtklibname %mklibname g2banking %gtkmajor
%define develnamegtk %mklibname -d g2banking
%define kdemajor 1
%define kdelibname %mklibname kbanking %kdemajor
%define develnamekde %mklibname -d kbanking
%define gkmajor 4
%define gklibname %mklibname geldkarte %gkmajor
%define develnamegk %mklibname -d geldkarte
%define ofxmajor 3
%define ofxlibname %mklibname aqofxconnect %ofxmajor
%define nonemajor 0
%define nonelibname %mklibname aqnone %nonemajor
%define dtausmajor 3
%define dtauslibname %mklibname aqdtaus %dtausmajor

Name: %{name}
Summary: A library for online banking functions and financial data import/export
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/aqbanking/%fname.tar.gz
Group: System/Libraries
License: GPL
URL: http://sourceforge.net/projects/aqbanking
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: libgwenhywfar-devel >= 2.3.0
BuildRequires: libchipcard3-devel
BuildRequires: libofx-devel >= 0.8.0
BuildRequires: libktoblzcheck-devel
BuildRequires: gtk+2-devel
BuildRequires: libglade2.0-devel
BuildRequires: kdelibs-devel


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


%package -n %gtklibname
Summary: Aqbanking tools for Gnome2/Gtk2
Group: System/Libraries

%description -n %gtklibname
Necessary for gtk2-based banking applications, e.g. Grisbi (but
not gnucash).

%package -n %develnamegtk
Summary: Aqbanking tools for Gnome2/Gtk2
Group: Development/C
Requires: %gtklibname = %version
Provides: libg2banking-devel = %version-%release
Obsoletes: %mklibname -d g2banking 2

%description -n %develnamegtk
Necessary for gtk2-based banking applications, e.g. Grisbi (but
not gnucash).

%package -n %gklibname
Summary: Aqbanking tools for Geldkarte
Group: System/Libraries

%description -n %gklibname
Necessary for accessing the German Geldkarte system.

%package -n %develnamegk
Summary: Aqbanking tools for Gnome2/Gtk2
Group: Development/C
Requires: %gklibname = %version
Provides: libgeldkarte-devel = %version-%release
Obsoletes: %mklibname -d geldkarte 4

%description -n %develnamegk
Necessary for accessing the German Geldkarte system.

%package geldkarte
Summary: Aqbanking tools for Geldkarte
Group: System/Libraries
%description geldkarte
Necessary for accessing the German Geldkarte system.

%package geldkarte-qt3
Summary: Aqbanking tools for Geldkarte
Group: System/Libraries
Requires: %name-geldkarte = %version
%description geldkarte-qt3
Necessary for accessing the German Geldkarte system.

%package ofx
Summary: Aqbanking tools for OFX
Group: System/Libraries
%description ofx
Necessary for OFX direct connect access.

%package -n %kdelibname
Summary: Aqbanking tools for KDE3
Group: System/Libraries

%description -n %kdelibname
Necessary for KDE-based banking applications, e.g. KMyMoney.

%package -n %develnamekde
Summary: Aqbanking tools for KDE3
Group: Development/C++
Requires: %kdelibname = %version
Provides: libkbanking-devel = %version-%release
Obsoletes: %mklibname -d kbanking 1

%description -n %develnamekde
Necessary for KDE-based banking applications, e.g. KMyMoney.

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
Requires: %ofxlibname = %version
Requires: %qtlibname = %version
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


%package -n %nonelibname
Summary: Aqbanking dummy backend library
Group: System/Libraries

%description -n %nonelibname
Necessary for viewing offline accounts.


%package -n %dtauslibname
Summary: Aqbanking DTAUS backend library
Group: System/Libraries

%description -n %dtauslibname
Necessary for viewing DTAUS (German financial format) accounts.

%prep
%setup -q -n %fname

%build
%configure2_5x

#parallel compilation must be disabled
#otherwise build will be linked with system libraries
#not the package one
make

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

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%post -n %aqhbcilibname -p /sbin/ldconfig
%postun -n %aqhbcilibname -p /sbin/ldconfig
%post -n %qtlibname -p /sbin/ldconfig
%postun -n %qtlibname -p /sbin/ldconfig
%post -n %gtklibname -p /sbin/ldconfig
%postun -n %gtklibname -p /sbin/ldconfig
%post -n %kdelibname -p /sbin/ldconfig
%postun -n %kdelibname -p /sbin/ldconfig
%post -n %gklibname -p /sbin/ldconfig
%postun -n %gklibname -p /sbin/ldconfig
%post -n %ofxlibname -p /sbin/ldconfig
%postun -n %ofxlibname -p /sbin/ldconfig
%post -n %nonelibname -p /sbin/ldconfig
%postun -n %nonelibname -p /sbin/ldconfig
%post -n %dtauslibname -p /sbin/ldconfig
%postun -n %dtauslibname -p /sbin/ldconfig


%files -n aqhbci
%defattr(-,root,root)
%doc src/plugins/backends/aqhbci/tools/aqhbci-tool/README
%_bindir/aqhbci-tool
%{_bindir}/hbcixml2
%_datadir/aqhbci/
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
%_bindir/qb-help
%_libdir/%name/plugins/%major/frontends/qbanking/

%files -f %name.lang
%defattr(-,root,root)
%doc installed-docs
%_bindir/%name-tool
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/plugins/%major/
%dir %{_libdir}/%{name}/plugins/%major/providers/
%dir %{_libdir}/%{name}/plugins/%major/wizards/
%dir %{_libdir}/%{name}/plugins/%major/imexporters/
%{_libdir}/%{name}/plugins/%major/bankinfo/
%{_libdir}/%{name}/plugins/%major/imexporters/csv*
%{_libdir}/%{name}/plugins/%major/imexporters/dbio*
%{_libdir}/%{name}/plugins/%major/imexporters/dtaus*
%{_libdir}/%{name}/plugins/%major/imexporters/eri*
%{_libdir}/%{name}/plugins/%major/imexporters/openhbci*
%{_libdir}/%{name}/plugins/%major/imexporters/qif*
%{_libdir}/%{name}/plugins/%major/imexporters/swift*
%{_libdir}/%{name}/plugins/%major/imexporters/xmldb*
%{_libdir}/%{name}/plugins/%major/imexporters/yellownet*
%{_libdir}/%{name}/plugins/%major/providers/aqdtaus*
%{_libdir}/%{name}/plugins/%major/providers/aqnone*
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/dtaus.so
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/dtaus.so.0
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/dtaus.so.0.0.0
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/dtaus.xml
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/swift.so
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/swift.so.0
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/swift.so.0.0.0
%{_libdir}/gwenhywfar/plugins/%gwenmajor/dbio/swift.xml
%{_libdir}/gwenhywfar/plugins/%gwenmajor/crypttoken/*

%{_datadir}/%{name}

%files ofx
%defattr(-,root,root)
%dir %{_libdir}/%{name}/plugins/%major/imexporters/ofx*
%{_libdir}/%{name}/plugins/%major/providers/aqofxconnect*

%files geldkarte
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/%major/providers/aqgeldkarte*

%files -n %gtklibname
%defattr(-,root,root)
%_libdir/libg2banking.so.%{gtkmajor}*

%files -n %develnamegtk
%defattr(-,root,root)
%_libdir/libg2banking.so
%_libdir/libg2banking.la
%{_bindir}/g2banking-config
%{_includedir}/g2banking
%{_datadir}/aclocal/g2banking.m4

%files -n %kdelibname
%defattr(-,root,root)
%_libdir/libkbanking.so.%{kdemajor}*

%files -n %develnamekde
%defattr(-,root,root)
%_libdir/libkbanking.so
%_libdir/libkbanking.la
%{_bindir}/kbanking-config
%{_includedir}/kbanking
%{_datadir}/aclocal/kbanking.m4

%files -n %gklibname
%defattr(-,root,root)
%_libdir/libaqgeldkarte.so.%{gkmajor}*

%files -n %develnamegk
%defattr(-,root,root)
%{_bindir}/aqgeldkarte-config
%{_includedir}/aqgeldkarte/
%{_libdir}/libaqgeldkarte.la
%{_libdir}/libaqgeldkarte.so
%{_datadir}/aclocal/aqgeldkarte.m4

%files -n %ofxlibname
%defattr(-,root,root)
%_libdir/libaqofxconnect.so.%{ofxmajor}*


%files -n %libname
%defattr(-,root,root)
%{_libdir}/libaqbanking.so.%{major}*
%_libdir/libcbanking.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_bindir}/aqbanking-config
%{_bindir}/aqdtaus-config
%{_bindir}/aqhbci-config
%{_bindir}/aqofxconnect-config
%{_bindir}/cbanking-config
%{_bindir}/qbanking-config
%{_includedir}/aqbanking
%{_includedir}/aqdtaus
%{_includedir}/aqhbci/
%{_includedir}/aqofxconnect/
%{_includedir}/cbanking/
%{_includedir}/qbanking
%{_libdir}/libaqdtaus.la
%{_libdir}/libcbanking.la
%{_libdir}/libaqbanking.la
%{_libdir}/libaqnone.la
%{_libdir}/libaqdtaus.so
%{_libdir}/libcbanking.so
%{_libdir}/libaqbanking.so
%{_libdir}/libaqnone.so
%{_libdir}/libqbanking.la
%{_libdir}/libqbanking.so
%{_libdir}/libaqhbci.la
%_libdir/libaqhbci.so
%_libdir/libaqofxconnect.so
%_libdir/libaqofxconnect.la
%{_libdir}/pkgconfig/aqbanking.pc
%{_datadir}/aclocal/aqbanking.m4
%{_datadir}/aclocal/aqdtaus.m4
%_datadir/aclocal/aqhbci.m4
%{_datadir}/aclocal/aqofxconnect.m4
%{_datadir}/aclocal/cbanking.m4
%{_datadir}/aclocal/qbanking.m4

%files -n %nonelibname
%defattr(-,root,root)
%_libdir/libaqnone.so.%{nonemajor}*

%files -n %dtauslibname
%defattr(-,root,root)
%_libdir/libaqdtaus.so.%{dtausmajor}*


