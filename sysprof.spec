%define	name	sysprof
%define	version	1.1.6
%define	release	%mkrel 2

Summary:	System-wide Linux Profiler
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.daimi.au.dk/~sandmann/sysprof/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	autoconf2.5
BuildRequires:	libglade2.0-devel
BuildRequires:	binutils-devel
BuildRequires:	imagemagick
ExclusiveArch:	%{ix86} x86_64

%description
Sysprof is a sampling profiler that uses a kernel module to generate
stacktraces which are then interpreted by the userspace program
"sysprof".

Sysprof handles shared libraries and applications do not need to be
recompiled. In fact they don't even have to be restarted.

Just insert the kernel module and start sysprof.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Sysprof
Comment=System-wide Linux Profiler
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Development;Profiling;X-MandrivaLinux-MoreApplications-Development-Tools;
EOF

mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_iconsdir},%{_miconsdir}}
cp sysprof-icon-48.png $RPM_BUILD_ROOT%{_liconsdir}/sysprof.png
cp sysprof-icon-16.png $RPM_BUILD_ROOT%{_miconsdir}/sysprof.png
cp sysprof-icon-32.png $RPM_BUILD_ROOT%{_iconsdir}/sysprof.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
/etc/udev/rules.d/60-sysprof.rules
%{_liconsdir}/*
%{_iconsdir}/*.png
%{_miconsdir}/*
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-2mdv2011.0
+ Revision: 615081
- the mass rebuild of 2010.1 packages

* Thu May 06 2010 Frederic Crozat <fcrozat@mandriva.com> 1.1.6-1mdv2010.1
+ Revision: 542993
- Release 1.1.6

* Tue Mar 23 2010 Pascal Terjan <pterjan@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 526876
- Switch to 1.1 branch

* Wed Nov 25 2009 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 1.0.12-2mdv2010.1
+ Revision: 469874
- fix static linking against against libbfd (P2)

* Wed May 13 2009 Pascal Terjan <pterjan@mandriva.org> 1.0.12-1mdv2010.0
+ Revision: 375265
- Update to 1.0.12

* Fri Mar 06 2009 Pascal Terjan <pterjan@mandriva.org> 1.0.10-7mdv2009.1
+ Revision: 349951
- Rebuild for new binutils

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1.0.10-6mdv2009.1
+ Revision: 318882
- fix strfmt

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Sep 30 2008 Pascal Terjan <pterjan@mandriva.org> 1.0.10-6mdv2009.0
+ Revision: 290107
- Fix the previous patch

* Thu Sep 25 2008 Pascal Terjan <pterjan@mandriva.org> 1.0.10-5mdv2009.0
+ Revision: 288216
- Add recent patches from svn to build against recent kernels

* Tue Aug 19 2008 Funda Wang <fwang@mandriva.org> 1.0.10-4mdv2009.0
+ Revision: 273972
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.0.10-3mdv2009.0
+ Revision: 269401
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Pascal Terjan <pterjan@mandriva.org>
    - rebuild for new libbfd

* Sat May 10 2008 Pascal Terjan <pterjan@mandriva.org> 1.0.10-1mdv2009.0
+ Revision: 205435
- update to new version 1.0.10

* Tue Feb 26 2008 Pascal Terjan <pterjan@mandriva.org> 1.0.9-3mdv2008.1
+ Revision: 175473
- Rebuild for new libbfd

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild for new libbfd
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Oct 27 2007 Pascal Terjan <pterjan@mandriva.org> 1.0.9-1mdv2008.1
+ Revision: 102680
- 1.0.9

* Fri Jun 08 2007 Pascal Terjan <pterjan@mandriva.org> 1.0.8-3mdv2008.0
+ Revision: 37221
- rebuild for new libbfd


* Tue Jan 16 2007 Pascal Terjan <pterjan@mandriva.org> 1.0.8-2mdv2007.0
+ Revision: 109494
- Rebuild for new binutils

* Sun Dec 31 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.8-1mdv2007.1
+ Revision: 102961
- 1.0.8
- Import sysprof

* Fri Aug 25 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.3-1mdv2007.0
- New release 1.0.3
- XDG menu

* Sat Apr 01 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.2-2mdk
- Rebuild for new binutils

* Mon Feb 27 2006 Pascal Terjan <pterjan@mandriva.org> 1.0.2-1mdk
- New release 1.0.2

* Mon Dec 19 2005 Pascal Terjan <pterjan@mandriva.org> 1.0.1-1mdk
- 1.0.1
- drop P0 (merged upstream)
- only works on x86

* Wed Oct 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-2mdk
- Fix BuildRequires (add ImageMagick because of the use of convert)
- Split Requires(post,preun) into Requires(post) and Requires(preun)

* Tue Oct 11 2005 Pascal Terjan <pterjan@mandriva.org> 1.0-1mdk
- first Mandriva package

