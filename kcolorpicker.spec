%define libname %mklibname kColorPicker
%define devname %mklibname -d kColorPicker

Name:		kcolorpicker
Version:	0.3.1
Release:	5
Summary:	Qt based Color Picker with popup menu
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kColorPicker
Source:		https://github.com/ksnip/kColorPicker/archive/v%{version}/kColorPicker-%{version}.tar.gz

BuildSystem:	 cmake
BuildOption:	 -DBUILD_EXAMPLE=ON -DBUILD_WITH_QT6=ON

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)

%description
QToolButton with color popup menu with lets you select a color. The
popup featues a color dialog button which can be used to add custom
colors to the popup menu.

%package -n %{libname}
Summary:	Library providing a widget for selecting a color
Group:		System/Libraries
%rename kcolorpicker

%description -n %{libname}
Library providing a widget for selecting a color

%package -n %{devname}
Summary:	Development package for %name
Requires: %{libname} = %{EVRD}
%rename kcolorpicker-devel

%description -n %{devname}
%summary

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/libkColorPicker.so*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/*
%{_libdir}/libkColorPicker.so*
