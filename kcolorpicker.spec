Name:		%{_lib}kColorPicker
Version:	0.3.1
Release:	1
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

%rename %name-Qt6

%description
QToolButton with color popup menu with lets you select a color. The
popup featues a color dialog button which can be used to add custom
colors to the popup menu.

%package devel

Summary:	Development package for %name
Requires: %name = %version

%description devel
%summary

%files
%doc README.md
%license LICENSE
%{_libdir}/*

%files devel
%{_includedir}/*
%{_prefix}/lib/debug/*
%{_libdir}/cmake/*

