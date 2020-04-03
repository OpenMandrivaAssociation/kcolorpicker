%define major		%{version}
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		kcolorpicker
Version:	0.1.1
Release:	%mkrel 1
Summary:	Qt based Color Picker with popup menu
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kColorPicker
Source:		https://github.com/ksnip/kColorPicker/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc-c++
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
%autosetup -p1 -n kColorPicker-%{version}

%build
%cmake_qt5 \
	-DBUILD_EXAMPLE=ON
%cmake_build

%install
%cmake_install

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libkColorPicker.so.%{major}

%files -n %{develname}
%doc README.md
%{_includedir}/kColorPicker/
%{_libdir}/libkColorPicker.so
%{_libdir}/cmake/kColorPicker/
