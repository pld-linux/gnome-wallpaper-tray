Summary:	GNOME wallpaper changer lived in notification area
Name:		gnome-wallpaper-tray
Version:	0.4.4
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://earthworm.no-ip.com/wp_tray/wp_tray-%{version}.tar.gz
# Source0-md5:	7b81a5c10be1763e549a0a46bed9a746
URL:		http://earthworm.no-ip.com/wp_tray/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	gtk+2-devel >= 2.2.4
BuildRequires:	libglade2-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

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
%{_desktopdir}/*.desktop
%{_datadir}/wp_tray
%attr(755,root,root) %{_bindir}/wp_tray
