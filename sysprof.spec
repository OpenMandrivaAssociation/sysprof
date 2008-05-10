%define	name	sysprof
%define	version	1.0.10
%define	release	%mkrel 1

Summary:	System-wide Linux Profiler
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source:		%{name}-%{version}.tar.gz
URL:		http://www.daimi.au.dk/~sandmann/sysprof/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires(post):	dkms
Requires(preun):	dkms
BuildRequires:	autoconf2.5
BuildRequires:	libglade2.0-devel
BuildRequires:	binutils-devel
BuildRequires:	ImageMagick
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
sed -i 's/include.*\.\.\/config\.h.*$/define PACKAGE_VERSION \"%{version}\"/' module/sysprof-module.c

%build
aclocal
autoconf
automake
%configure2_5x --disable-kernel-module
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Menu
######



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
cp sysprof-icon.png $RPM_BUILD_ROOT%{_liconsdir}/sysprof.png
convert sysprof-icon.png -geometry 32x32 $RPM_BUILD_ROOT%{_iconsdir}/sysprof.png
convert sysprof-icon.png -geometry 16x16 $RPM_BUILD_ROOT%{_miconsdir}/sysprof.png

# DKMS 
######

install -d -m 755 %{buildroot}%{_prefix}/src
cp -a module %{buildroot}%{_prefix}/src/%{name}-%{version}

cat > %{buildroot}%{_prefix}/src/%{name}-%{version}/dkms.conf <<EOF

PACKAGE_VERSION="%{version}"

# Items below here should not have to change with each driver version
PACKAGE_NAME="%{name}"
MAKE[0]="make -C \${kernel_source_dir} SUBDIRS=\${dkms_tree}/\${PACKAGE_NAME}/\${PACKAGE_VERSION}/build modules"
CLEAN="make clean"

BUILT_MODULE_NAME[0]="\$PACKAGE_NAME-module"
DEST_MODULE_LOCATION[0]="/kernel/3rdparty/\$PACKAGE_NAME/"

AUTOINSTALL=yes
REMAKE_INITRD=no

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
dkms add -m %{name} -v %{version} --rpm_safe_upgrade
dkms build -m %{name} -v %{version} --rpm_safe_upgrade
dkms install -m %{name} -v %{version} --rpm_safe_upgrade

%preun
dkms remove -m %{name} -v %{version} --rpm_safe_upgrade --all ||:

%postun
%update_menus

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README TODO
%{_bindir}/*
%{_prefix}/src/%{name}-%{version}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_liconsdir}/*
%{_iconsdir}/*.png
%{_miconsdir}/*
%{_datadir}/applications/mandriva-%{name}.desktop
