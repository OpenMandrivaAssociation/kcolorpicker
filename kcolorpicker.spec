%define	oname		kColorPicker

%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		kcolorpicker
Version:	0.1.1
Release:	1
Summary:	Qt based Color Picker with popup menu
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kColorPicker
Source:		https://github.com/ksnip/kColorPicker/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)

%description
QToolButton with color popup menu with lets you select a color. The
popup featues a color dialog button which can be used to add custom
colors to the popup menu.

#------------------------------------------------

%package -n	%{libname}
Summary:	Qt based Color Picker with popup menu
Group:		System/Libraries

%description -n %{libname}
QToolButton with color popup menu with lets you select a color. The
popup featues a color dialog button which can be used to add custom
colors to the popup menu.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%cmake_qt5 \
	-DBUILD_EXAMPLE=ON
%cmake_build

%install
%cmake_install

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/lib%{oname}.so.%{version}

%files -n %{develname}
%doc README.md
%{_includedir}/%{oname}/
%{_libdir}/lib%{oname}.so
%{_libdir}/cmake/%{oname}/
