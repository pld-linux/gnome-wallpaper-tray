Summary:	GNOME wallpaper changer lived in notification area
Summary(pl):	Zmieniacz tapety GNOME obecny w obszarze powiadomieñ
Name:		gnome-wallpaper-tray
Version:	0.5.3
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://planetearthworm.com/projects/wp_tray/files/wp_tray-%{version}.tar.gz
# Source0-md5:	27b878b8d3864787388b49e934c1ee60
Patch0:		%{name}-desktop.patch
URL:		http://planetearthworm.com/projects/wp_tray/		
BuildRequires:	automake
BuildRequires:	boost-filesystem-devel
BuildRequires:	boost-regex-devel
BuildRequires:	gconfmm-devel >= 2.6
BuildRequires:	gnome-panel-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.6.3
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libglademm-devel >= 2.4
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

%description -l pl
Wallpaper Tray to narzêdzie do tapet rezyduj±ce w obszarze powiadomieñ
Panelu GNOME. Daje losow± tapetê z podanego katalogu po zalogowaniu,
lub po up³ywie jakiego¶ czasu oraz pozwala na losowy wybór nowej
tapety z menu.

%prep
%setup -q -n wp_tray-%{version}
#%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-boostfilesystem=/usr/%{_lib}/libboost_filesystem.so \
	--with-boostregex=/usr/%{_lib}/libboost_regex.so 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	gnomemenudir=%{_desktopdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/wp_tray
%{_datadir}/wp_tray
%{_desktopdir}/*.desktop
