%define major 34
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

%define gwenmajor 60
%define aqhbcimajor 20
%define aqhbcilibname %mklibname aqhbci %{aqhbcimajor}
%define ofxmajor 7
%define ofxlibname %mklibname aqofxconnect %{ofxmajor}
%define cppmajor 0
%define cpplibname %mklibname aqbankingpp %{cppmajor}

Name:		aqbanking
Summary:	A library for online banking functions and financial data import/export
Version:	5.0.25
Release:	1
Group:		System/Libraries
License:	GPLv2+
URL:		http://www.aquamaniac.de/sites/aqbanking/index.php
Source:		http://files.hboeck.de/aq/%{name}-%{version}.tar.gz
Patch0:		aqbanking-4.99.6-fix-link.patch
BuildRequires:	pkgconfig(gwenhywfar)
BuildRequires:	libchipcard-devel
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(ktoblzcheck)
BuildRequires:	gmp-devel

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

%package -n %{develname}
Summary:	Aqbanking development kit
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Requires:	%{aqhbcilibname} = %{version}-%{release}
Requires:	%{ofxlibname} = %{version}-%{release}
Requires:	%{cpplibname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	OpenSP-devel
Provides:	aqhbci-devel = %{version}-%{release}
Provides:	libaqhbci-devel = %{version}-%{release}

%description -n %{develname}
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

%files -n %{develname}
%{_bindir}/aqbanking-config
%{_includedir}/aqbanking5
%{_libdir}/libaqbankingpp.so
%{_libdir}/libaqbanking.so
%{_libdir}/libaqnone.so
%{_libdir}/libaqhbci.so
%{_libdir}/libaqofxconnect.so
%{_datadir}/aclocal/aqbanking.m4
%{_libdir}/pkgconfig/aqbanking.pc


%changelog
* Fri Jan 20 2012 Andrey Bondrov <abondrov@mandriva.org> 5.0.22-1mdv2012.0
+ Revision: 762897
- New version 5.0.22

* Mon Jan 09 2012 Andrey Bondrov <abondrov@mandriva.org> 5.0.21-1
+ Revision: 758746
- New version 5.0.21

* Tue Sep 27 2011 Andrey Bondrov <abondrov@mandriva.org> 5.0.16-1
+ Revision: 701428
- New version: 5.0.16

* Tue Jun 14 2011 Funda Wang <fwang@mandriva.org> 5.0.10-1
+ Revision: 685096
- new version 5.0.10

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 5.0.7-3
+ Revision: 681338
- finally correct libname

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 5.0.7-2
+ Revision: 681041
- fix wrong pkg name

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 5.0.7-1
+ Revision: 680643
- add cpp libname
- new version 5.0.7

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-3
+ Revision: 662787
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 5.0.4-2
+ Revision: 639960
- rebuild

* Wed Feb 23 2011 Funda Wang <fwang@mandriva.org> 5.0.4-1
+ Revision: 639433
- new version 5.0.4

* Wed Feb 09 2011 Funda Wang <fwang@mandriva.org> 5.0.2-1
+ Revision: 636963
- New version 5.0.2

* Tue Sep 21 2010 Funda Wang <fwang@mandriva.org> 5.0.1-1mdv2011.0
+ Revision: 580318
- new version 5.0.1

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 5.0.0-1mdv2011.0
+ Revision: 574524
- new version 5.0.0

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 4.99.25-1mdv2011.0
+ Revision: 574303
- new version 4.99.25

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 4.99.20-1mdv2011.0
+ Revision: 571761
- New version 4.99.20

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - remove qt build dep

* Wed Aug 04 2010 Funda Wang <fwang@mandriva.org> 4.99.14-1mdv2011.0
+ Revision: 565970
- New version 4.99.14

* Thu Jul 29 2010 Funda Wang <fwang@mandriva.org> 4.99.11-1mdv2011.0
+ Revision: 563064
- New version 4.99.11 towards 5.0

* Wed Apr 14 2010 Funda Wang <fwang@mandriva.org> 4.2.9-1mdv2010.1
+ Revision: 534693
- new version 4.2.9

* Wed Mar 31 2010 Funda Wang <fwang@mandriva.org> 4.2.7-1mdv2010.1
+ Revision: 530487
- New version 4.2.7

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 4.2.4-3mdv2010.1
+ Revision: 503969
- byebye qt3 build

* Tue Feb 09 2010 Funda Wang <fwang@mandriva.org> 4.2.4-2mdv2010.1
+ Revision: 502930
- rebuild for new gmp

* Sat Feb 06 2010 Frederik Himpe <fhimpe@mandriva.org> 4.2.4-1mdv2010.1
+ Revision: 501507
- Update to new version 4.2.4

* Sat Jan 09 2010 Funda Wang <fwang@mandriva.org> 4.2.3-1mdv2010.1
+ Revision: 488120
- new version 4.2.3

  + Frederik Himpe <fhimpe@mandriva.org>
    - Update to new version 4.2.2 (new libaqhbci major)

* Thu Sep 24 2009 GÃ¶tz Waschk <waschk@mandriva.org> 4.1.7-2mdv2010.0
+ Revision: 448329
- readd qbanking front-end, but link it with qt4

* Wed Sep 23 2009 Frederik Himpe <fhimpe@mandriva.org> 4.1.7-1mdv2010.0
+ Revision: 448015
- Update to new version 4.1.7

* Fri Sep 11 2009 Emmanuel Andry <eandry@mandriva.org> 4.1.4-1mdv2010.0
+ Revision: 438476
- New version 4.1.4
- bump minimal gwenhywfar version BR

* Sun Jun 21 2009 Funda Wang <fwang@mandriva.org> 4.1.0-1mdv2010.0
+ Revision: 387556
- New version 4.1.0

* Sat May 30 2009 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2010.0
+ Revision: 381421
- New version 4.0.0

* Wed May 27 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 3.8.2-2mdv2010.0
+ Revision: 380046
- Fix build and file list
- Remove qt3 lib requires
- Remove qt3 support  we will package q4banking soon

* Wed Mar 04 2009 GÃ¶tz Waschk <waschk@mandriva.org> 3.8.2-1mdv2009.1
+ Revision: 348260
- new version

* Thu Dec 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.8.1-1mdv2009.1
+ Revision: 309990
- new version
- fix source URL

* Sat Oct 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.8.0-1mdv2009.1
+ Revision: 294859
- new version
- new qtmajor

* Wed Aug 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.7.2-1mdv2009.0
+ Revision: 276482
- new version

* Wed Aug 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.7.1-1mdv2009.0
+ Revision: 274299
- new version
- bump deps
- update file list

* Fri Aug 01 2008 Funda Wang <fwang@mandriva.org> 3.6.2-1mdv2009.0
+ Revision: 259130
- New version 3.6.2

* Wed Jul 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.6.1-1mdv2009.0
+ Revision: 233051
- new version

* Sun Jul 06 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.6.0-1mdv2009.0
+ Revision: 232301
- new version
- update file list

* Sat Jun 14 2008 Funda Wang <fwang@mandriva.org> 3.5.1-1mdv2009.0
+ Revision: 219147
- comment out non-exists subpackages
- New version 3.5.1

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 3.5.0-1mdv2009.0
+ Revision: 216782
- New version 3.5.0
- fix url

* Wed May 28 2008 Funda Wang <fwang@mandriva.org> 3.4.2-1mdv2009.0
+ Revision: 212175
- New version 3.4.2

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version

* Wed Apr 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.4.0-1mdv2009.0
+ Revision: 196754
- new version

* Wed Apr 16 2008 GÃ¶tz Waschk <waschk@mandriva.org> 3.3.0-1mdv2009.0
+ Revision: 194654
- fix buildrequires
- new version
- remove obsolete subpackages
- new major versions
- bump deps

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 23 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.3.3-1mdv2008.1
+ Revision: 111476
- fix build on x86_64
- new version
- new devel name
- fix buildrequires
- merge some of the devel packages

* Tue May 29 2007 Frederic Crozat <fcrozat@mandriva.com> 2.2.9-1mdv2008.0
+ Revision: 32532
- Release 2.2.9


* Fri Jan 19 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.6-1mdv2007.0
+ Revision: 110815
- new version

* Fri Dec 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.4-1mdv2007.1
+ Revision: 102534
- new version
- fix buildrequires

* Fri Dec 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.3-1mdv2007.1
+ Revision: 89587
- Import aqbanking

* Fri Dec 01 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.2.3-1mdv2007.1
- New version 2.2.3

* Sun Aug 27 2006 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2007.0
- update file list
- New release 2.2.1

* Sat Jun 17 2006 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdv2007.0
- update file list
- bump major
- bump deps
- New release 2.1.0

* Thu Jun 08 2006 Götz Waschk <waschk@mandriva.org> 2.0.0-2mdv2007.0
- fix build

* Tue Apr 04 2006 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdk
- New release 2.0.0

* Tue Mar 28 2006 Götz Waschk <waschk@mandriva.org> 1.9.11-0.rc1.1mdk
- New release 1.9.11

* Fri Mar 24 2006 GÃ¶tz Waschk <waschk@mandriva.org> 1.9.10-1mdk
- New release 1.9.10

* Tue Mar 21 2006 Götz Waschk <waschk@mandriva.org> 1.9.9-1mdk
- bump deps
- New release 1.9.9

* Tue Mar 07 2006 Götz Waschk <waschk@mandriva.org> 1.9.8-1mdk
- add dtaus package
- update majors
- New release 1.9.8

* Mon Feb 20 2006 Götz Waschk <waschk@mandriva.org> 1.9.7-5mdk
- fix conflict

* Mon Feb 20 2006 Götz Waschk <waschk@mandriva.org> 1.9.7-4mdk
- obsolete aqbanking-ofx-qt3

* Mon Feb 20 2006 Götz Waschk <waschk@mandriva.org> 1.9.7-3mdk
- fix buildrequires

* Sun Feb 19 2006 Götz Waschk <waschk@mandriva.org> 1.9.7-2mdk
- add conflict

* Fri Feb 17 2006 Götz Waschk <waschk@mandriva.org> 1.9.7-1mdk
- update file list
- bump deps
- new major
- New release 1.9.7

* Wed Jan 18 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.8.0-4mdk
- rebuild for new gwenhywfar

* Mon Jan 09 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.8.0-3mdk
- Rebuild

* Tue Dec 06 2005 Götz Waschk <waschk@mandriva.org> 1.8.0-2mdk
- build with ktobblzcheck

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 1.8.0-1mdk
- merge with aqhbci
- update buildrequires
- New release 1.8.0

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-4mdk
- rebuilt against openssl-0.9.8a

* Sat Jul 30 2005 Frederic Crozat <fcrozat@mandriva.com> 1.2.0-3mdk
- Remove .so file from lib package

* Wed Jul 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.0-2mdk
- cosmetics

* Sat Jul 16 2005 Götz Waschk <waschk@mandriva.org> 1.2.0-1mdk
- New release 1.2.0

* Tue Jul 12 2005 Götz Waschk <waschk@mandriva.org> 1.1.0-1mdk
- update file list
- bump deps
- New release 1.1.0

* Wed Jun 15 2005 Götz Waschk <waschk@mandriva.org> 1.0.12-1mdk
- New release 1.0.12

* Sat Jun 04 2005 Götz Waschk <waschk@mandriva.org> 1.0.11-1mdk
- update file list
- New release 1.0.11

* Sat May 21 2005 Götz Waschk <waschk@mandriva.org> 1.0.10-1mdk
- New release 1.0.10

* Thu May 05 2005 Götz Waschk <waschk@mandriva.org> 1.0.9-2mdk
- fix devel deps

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 1.0.9-1mdk
- requires new gwenhywfar
- New release 1.0.9

* Thu Apr 07 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.7-1mdk 
- Release 1.0.7

* Mon Feb 21 2005 Götz Waschk <waschk@linux-mandrake.com> 1.0.5-1mdk
- 1.0.5beta

* Mon Feb 21 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.9.9-1mdk
- New release 0.9.9

* Tue Dec 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.8-2mdk 
- Fix .la files

* Mon Dec 13 2004 Götz Waschk <waschk@linux-mandrake.com> 0.9.8-1mdk
- initial package

