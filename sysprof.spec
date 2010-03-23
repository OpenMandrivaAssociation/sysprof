%define	name	sysprof
%define	version	1.1.4
%define	release	%mkrel 1

Summary:	System-wide Linux Profiler
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.gz
Patch1:		sysprof-fix-str-fmt.patch
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
%patch1 -p1

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
