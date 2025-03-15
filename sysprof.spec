# Fix me! https://gitlab.gnome.org/GNOME/sysprof/-/issues/99
%global optflags %{optflags} -Wno-format-nonliteral

%global api		6
%global major		6
%define libname		%mklibname sysprof %major
%define libnameui	%mklibname sysprof-ui %major
%define devname		%mklibname sysprof -d

%define url_ver	%(echo %{version}|cut -d. -f1,2)

# sysprof builds a static library and doesn't make a difference between CFLAGS
# for that and shared libraries -- resulting in clang LTO files being in the
# *.a library, resulting in build failures for anything that tries to link to
# the library using a different compiler
%global _disable_lto 1

Name:		sysprof
Version:	48.rc
Release:	1
Summary:	A system-wide Linux profiler
Group:		Development/Tools

License:	GPLv3+
URL:		https://www.sysprof.com
Source0:	https://download.gnome.org/sources/sysprof/%{url_ver}/sysprof-%{version}.tar.xz
Patch0:		disable-werror-on-wshadow.patch

BuildRequires:	binutils-devel
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	itstool
BuildRequires:	polkit-1-devel
BuildRequires:	pkgconfig(systemd)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	libxml2-utils
BuildRequires:	meson

Requires:	hicolor-icon-theme
Requires:	%{name}-cli%{?_isa} = %{version}-%{release}

%description
Sysprof is a sampling CPU profiler for Linux that collects accurate,
high-precision data and provides efficient access to the sampled
calltrees.


%package        cli
Summary:	Sysprof command line utility
Group:		Development/Tools

%description    cli
The %{name}-cli package contains the sysprof-cli command line utility.


%package     -n %libname
Summary:	Sysprof library
Group:		System/Libraries
Obsoletes:	%libnameui < %{EVRD}

%description -n %libname
The libsysprof package contains the Sysprof library.

#package     -n %libnameui
#Summary:	Sysprof UI library
#Group:		System/Libraries

#description -n %libnameui
#The libsysprof-ui package contains the Sysprof UI library.

%package        agent
Summary:        Sysprof agent utility

%description    agent
The %{name}-agent package contains the sysprof-agent program. It provides a P2P
D-Bus API to the process which can control subprocesses. It's used by IDE
tooling to have more control across container boundaries.


%package        -n %devname
Summary:	Development files for %{name}
Group:		Development/Tools
Requires:	%{libname} = %{version}-%{release}
#Requires:	%{libnameui} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-ui-devel = %{version}-%{release}

%description    -n %devname
The %{devname} package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
%meson
%build
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

#check
#appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
#desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
#meson_test || :

%files
%license COPYING
%doc NEWS README.md AUTHORS
%{_bindir}/sysprof
%{_datadir}/applications/org.gnome.Sysprof.desktop
#{_datadir}/glib-2.0/schemas/org.gnome.sysprof3.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.gnome.Sysprof.appdata.xml
%{_datadir}/mime/packages/sysprof-mime.xml

%files cli -f %{name}.lang
%license COPYING
%{_bindir}/sysprof-cli
%{_libexecdir}/sysprofd
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof.Agent.xml
#{_datadir}/dbus-1/interfaces/org.gnome.Sysprof2.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Profiler.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Sysprof3.Service.xml
#{_datadir}/dbus-1/system.d/org.gnome.Sysprof2.conf
%{_datadir}/dbus-1/system.d/org.gnome.Sysprof3.conf
#{_datadir}/dbus-1/system-services/org.gnome.Sysprof2.service
%{_datadir}/dbus-1/system-services/org.gnome.Sysprof3.service
%{_datadir}/polkit-1/actions/org.gnome.sysprof3.policy
#{_unitdir}/sysprof2.service
%{_unitdir}/sysprof3.service

%files -n %libname
%license COPYING
%{_libdir}/libsysprof-%{major}.so
%{_libdir}/libsysprof-%{major}.so.6*
%{_libdir}/libsysprof-memory-%{major}.so
%{_libdir}/libsysprof-speedtrack-%{major}.so
%{_libdir}/libsysprof-tracer-%{major}.so

#files -n %libnameui
#license COPYING
#{_libdir}/libsysprof-ui-%{api}.so

%files agent
%license COPYING
%{_bindir}/sysprof-agent

%files -n %devname
%{_includedir}/sysprof-%{major}/
%{_libdir}/pkgconfig/sysprof-%{major}.pc
%{_libdir}/pkgconfig/sysprof-capture-4.pc
%{_libdir}/libsysprof-capture-4.a
