Name:		agave
Summary:	A GNOME tool to choose colors
Version:	0.4.7
Release:	6
Group:		Graphics
License:	GPL
URL:		http://home.gna.org/colorscheme/
Source0:	http://download.gna.org/colorscheme/releases/%{name}-%{version}.tar.bz2
Patch0:		agave-0.4.7-mdv-fix-str-fmt.patch
Patch1:		agave-0.4.7-fix-build.patch
BuildRequires:	docbook-dtd45-xml
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)
BuildRequires:	rarian
BuildRequires:	xsltproc
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gconfmm-2.6)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libgnomeui-2.0)

%description
A GNOME tool to choose colors.

%prep
%setup -q
%patch0 -p1 -b .strfmt
%patch1 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
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
%{_iconsdir}/hicolor/*/apps/agave.png
%{_iconsdir}/hicolor/scalable/apps/agave.svg

