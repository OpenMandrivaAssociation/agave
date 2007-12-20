
%define name    agave
%define version 0.4.3 
%define release %mkrel 1 

Name:           %{name} 
Summary:        A GNOME tool to choose colors
Version:        %{version} 
Release:        %{release} 
Source0:        http://download.gna.org/colorscheme/releases/%{name}-%{version}.tar.bz2 

BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  gtkmm2.4-devel
BuildRequires:  libglademm2.4-devel
BuildRequires:  gnomeui2-devel
BuildRequires:  gconfmm2.6-devel
BuildRequires:  boost-devel

URL:            http://home.gna.org/colorscheme/

Group:          Graphics
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPL 

%description
A GNOME tool to choose colors

%prep
%setup -q 

%build 
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%buildroot

%find_lang %name

%clean 
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(0755,root,root) 
%doc README NEWS COPYING AUTHORS 
%{_bindir}/agave
%{_sysconfdir}/gconf/schemas/agave.schemas
%dir %{_datadir}/agave
%dir %{_datadir}/agave/palettes
%{_datadir}/agave/palettes/*.gpl
%dir %{_datadir}/agave/pixmaps
%{_datadir}/agave/pixmaps/*.png
%dir %{_datadir}/agave/ui
%{_datadir}/agave/ui/agave.glade
%{_datadir}/agave/ui/*.ui
%{_datadir}/applications/agave.desktop
%dir %{_datadir}/gnome/help/agave
%dir %{_datadir}/gnome/help/agave/C
%{_datadir}/gnome/help/agave/C/*.xml
%dir %{_datadir}/gnome/help/agave/C/figures
%{_datadir}/gnome/help/agave/C/figures/*.png
%{_datadir}/icons/hicolor/48x48/apps/agave-icon.png
%{_datadir}/icons/hicolor/scalable/apps/agave-icon.svg
%dir %{_datadir}/omf/agave
%{_datadir}/omf/agave/agave-C.omf


