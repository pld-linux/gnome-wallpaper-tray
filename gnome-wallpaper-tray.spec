Summary:	GNOME wallpaper changer lived in notification area
Summary(pl):	Zmieniacz tapety GNOME obecny w obszarze powiadomieñ
Name:		gnome-wallpaper-tray
Version:	0.4.6
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://earthworm.no-ip.com/wp_tray/wp_tray-%{version}.tar.gz
# Source0-md5:	455bb350252564139f04ca2de9af22a8
URL:		http://earthworm.no-ip.com/wp_tray/
BuildRequires:	gtk+2-devel >= 2.2.4
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.4.0
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

%build
%configure
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
