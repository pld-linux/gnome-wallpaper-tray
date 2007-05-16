# TODO: change name for spec to gnome-applet-wallpaper-tray.spec
%define		realname	wp_tray
Summary:	GNOME wallpaper changer lived in notification area
Summary(pl.UTF-8):	Zmieniacz tapety GNOME obecny w obszarze powiadomień
Name:		gnome-wallpaper-tray
Version:	0.5.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://planetearthworm.com/projects/wp_tray/files/%{realname}-%{version}.tar.gz
# Source0-md5:	27b878b8d3864787388b49e934c1ee60
URL:		http://planetearthworm.com/projects/wp_tray/		
BuildRequires:	automake
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
BuildRequires:	gconfmm-devel >= 2.14
BuildRequires:	gnome-panel-devel >= 2.14
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	gtkmm-devel >= 2.10
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libglademm-devel >= 2.6
BuildRequires:	libgnomecanvasmm-devel >= 2.6
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libgnomeuimm-devel >= 2.6
BuildRequires:	libnotify-devel
BuildRequires:	libxml++-devel >= 2.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wallpaper Tray is a wallpaper utility that sits in your GNOME Panel
Notification Area. It gives you a random wallpaper from your chosen
directory at logon, on a timer, and allows you to select a new
wallpaper at random from its menu.

%description -l pl.UTF-8
Wallpaper Tray to narzędzie do tapet rezydujące w obszarze powiadomień
Panelu GNOME. Daje losową tapetę z podanego katalogu po zalogowaniu,
lub po upływie jakiegoś czasu oraz pozwala na losowy wybór nowej
tapety z menu.

%prep
%setup -q -n %{realname}-%{version}

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-boostfilesystem=/usr/%{_lib}/libboost_filesystem.so \
	--with-boostregex=/usr/%{_lib}/libboost_regex.so \
	--with-gconf-schema-file-dir=%{_sysconfdir}/schemas

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
        GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{_realname}.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall %{_realname}.schemas

%postun
%scrollkeeper_update_postun

%files
%defattr(644,root,root,755)
%doc NEWS README ChangeLog
%{_sysconfdir}/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%attr(755,root,root) /usr/%{_lib}/%{realname}
#%attr(755,root,root) %{_bindir}/%{realname}
%{_pixmapsdir}/*.png
%{_datadir}/%{realname}
