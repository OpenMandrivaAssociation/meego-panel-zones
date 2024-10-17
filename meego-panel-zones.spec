Name: meego-panel-zones
Summary: Zones panel
Version: 0.2.1
Release: %mkrel 1
Group: System Environment/Desktop
License: LGPL 2.1
URL: https://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
Requires: mx
Requires: mutter-meego
BuildRequires: libclutter1.0-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgnome-menu-devel
BuildRequires: mx-devel
BuildRequires: meego-panel-devel
BuildRequires: libwnck-1-devel
BuildRequires: libGConf2-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
Obsoletes: moblin-panel-zones < 0.2.1

%description
Meego zones panel

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang meego-panel-zones

%files -f meego-panel-zones.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*
%{_datadir}/dbus-1/services/com.meego.UX.Shell.Panels.zones.service
%{_datadir}/meego-panel-zones/people.png
%{_datadir}/meego-panel-zones/style/app-background-panel-highlight.png
%{_datadir}/meego-panel-zones/style/app-background-panel.png
%{_datadir}/meego-panel-zones/style/background-gradient.png
%{_datadir}/meego-panel-zones/style/close-button-hover.png
%{_datadir}/meego-panel-zones/style/close-button.png
%{_datadir}/meego-panel-zones/style/content-panel-background-highlight-orange.png
%{_datadir}/meego-panel-zones/style/content-panel-background.png
%{_datadir}/meego-panel-zones/style/content-panel-header-grey.png
%{_datadir}/meego-panel-zones/style/content-panel-header-orange.png
%{_datadir}/meego-panel-zones/style/switcher.css
%{_datadir}/meego-panel-zones/style/workspace-title-new-symbol-active.png
%{_datadir}/mutter-meego/panels/meego-panel-zones.desktop

