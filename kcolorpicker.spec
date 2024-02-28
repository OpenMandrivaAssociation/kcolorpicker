Name:		kcolorpicker
Version:	0.3.0
Release:	1
Summary:	Qt based Color Picker with popup menu
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://github.com/ksnip/kColorPicker
Source:		https://github.com/ksnip/kColorPicker/archive/v%{version}/kColorPicker-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)

%description
QToolButton with color popup menu with lets you select a color. The
popup featues a color dialog button which can be used to add custom
colors to the popup menu.

%prep
%autosetup -p1 -n kColorPicker-%{version}
%cmake \
	-DBUILD_EXAMPLE=ON \
	-DBUILD_WITH_QT6=OFF \
	-G Ninja

cd ..
export CMAKE_BUILD_DIR=build-qt6
%cmake \
	-DBUILD_EXAMPLE=ON \
	-DBUILD_WITH_QT6=ON \
	-G Ninja

%build
%ninja_build -C build
%ninja_build -C build-qt6

%install
%ninja_install -C build
%ninja_install -C build-qt6

%libpackages
