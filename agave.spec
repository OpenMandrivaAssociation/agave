
%define name    agave
%define version 0.4.7
%define release %mkrel 1

Name:           %{name} 
Summary:        A GNOME tool to choose colors
Version:        %{version} 
Release:        %{release} 
Source0:        http://download.gna.org/colorscheme/releases/%{name}-%{version}.tar.bz2 
Patch0:		agave-0.4.7-mdv-fix-str-fmt.patch

BuildRequires:  pkgconfig
BuildRequires:  gnome-doc-utils
BuildRequires:  perl(XML::Parser)
BuildRequires:  gtkmm2.4-devel
BuildRequires:  libglademm2.4-devel
BuildRequires:  gnomeui2-devel
BuildRequires:  gconfmm2.6-devel
BuildRequires:  boost-devel
BuildRequires:	intltool

URL:            http://home.gna.org/colorscheme/

Group:          Graphics
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPL 

%description
A GNOME tool to choose colors

%prep
%setup -q 
%patch0 -p1 -b .strfmt

%build 
%configure 
%make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%find_lang %name

%clean 
rm -rf %{buildroot}

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
%dir %{_datadir}/gnome/help/agave/cs
%dir %{_datadir}/gnome/help/agave/de
%{_datadir}/gnome/help/agave/*/*.xml
%dir %{_datadir}/gnome/help/agave/C/figures
%dir %{_datadir}/gnome/help/agave/cs/figures
%dir %{_datadir}/gnome/help/agave/de/figures
%{_datadir}/gnome/help/agave/*/figures/*.png
%{_iconsdir}/hicolor/*/apps/agave.png
%{_iconsdir}/hicolor/scalable/apps/agave.svg
%dir %{_datadir}/omf/agave
%{_datadir}/omf/agave/agave*.omf


