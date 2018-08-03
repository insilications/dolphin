#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dolphin
Version  : 18.07.90
Release  : 5
URL      : https://github.com/KDE/dolphin/archive/v18.07.90.tar.gz
Source0  : https://github.com/KDE/dolphin/archive/v18.07.90.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: dolphin-bin
Requires: dolphin-lib
Requires: dolphin-data
Requires: dolphin-license
BuildRequires : attica-dev
BuildRequires : baloo-dev
BuildRequires : baloo-widgets-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kactivities-dev
BuildRequires : kbookmarks-dev
BuildRequires : kcmutils-dev
BuildRequires : kcodecs-dev
BuildRequires : kcompletion-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdelibs4support-dev
BuildRequires : kfilemetadata-dev
BuildRequires : kiconthemes-dev
BuildRequires : kinit-dev
BuildRequires : kio-dev
BuildRequires : kitemviews-dev
BuildRequires : kjobwidgets-dev
BuildRequires : knewstuff-dev
BuildRequires : knotifications-dev
BuildRequires : kparts-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : phonon-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev

%description
See http://dolphin.kde.org for information about Dolphin.

%package bin
Summary: bin components for the dolphin package.
Group: Binaries
Requires: dolphin-data
Requires: dolphin-license

%description bin
bin components for the dolphin package.


%package data
Summary: data components for the dolphin package.
Group: Data

%description data
data components for the dolphin package.


%package dev
Summary: dev components for the dolphin package.
Group: Development
Requires: dolphin-lib
Requires: dolphin-bin
Requires: dolphin-data
Provides: dolphin-devel

%description dev
dev components for the dolphin package.


%package doc
Summary: doc components for the dolphin package.
Group: Documentation

%description doc
doc components for the dolphin package.


%package lib
Summary: lib components for the dolphin package.
Group: Libraries
Requires: dolphin-data
Requires: dolphin-license

%description lib
lib components for the dolphin package.


%package license
Summary: license components for the dolphin package.
Group: Default

%description license
license components for the dolphin package.


%prep
%setup -q -n dolphin-18.07.90

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533310222
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1533310222
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/dolphin
cp COPYING %{buildroot}/usr/share/doc/dolphin/COPYING
cp COPYING.DOC %{buildroot}/usr/share/doc/dolphin/COPYING.DOC
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dolphin
/usr/bin/servicemenudeinstallation
/usr/bin/servicemenuinstallation

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.dolphin.desktop
/usr/share/config.kcfg/dolphin_compactmodesettings.kcfg
/usr/share/config.kcfg/dolphin_detailsmodesettings.kcfg
/usr/share/config.kcfg/dolphin_directoryviewpropertysettings.kcfg
/usr/share/config.kcfg/dolphin_generalsettings.kcfg
/usr/share/config.kcfg/dolphin_iconsmodesettings.kcfg
/usr/share/config.kcfg/dolphin_versioncontrolsettings.kcfg
/usr/share/dbus-1/interfaces/org.freedesktop.FileManager1.xml
/usr/share/dbus-1/services/org.kde.dolphin.FileManager1.service
/usr/share/kservices5/dolphinpart.desktop
/usr/share/kservices5/kcmdolphingeneral.desktop
/usr/share/kservices5/kcmdolphinnavigation.desktop
/usr/share/kservices5/kcmdolphinservices.desktop
/usr/share/kservices5/kcmdolphinviewmodes.desktop
/usr/share/kservicetypes5/fileviewversioncontrolplugin.desktop
/usr/share/metainfo/org.kde.dolphin.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/Dolphin/KVersionControlPlugin
/usr/include/Dolphin/dolphinvcs_version.h
/usr/include/Dolphin/kversioncontrolplugin.h
/usr/lib64/cmake/DolphinVcs/DolphinVcsConfig.cmake
/usr/lib64/cmake/DolphinVcs/DolphinVcsConfigVersion.cmake
/usr/lib64/cmake/DolphinVcs/DolphinVcsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/DolphinVcs/DolphinVcsTargets.cmake
/usr/lib64/libdolphinvcs.so
/usr/lib64/libkdeinit5_dolphin.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/dolphin/default-ui.png
/usr/share/doc/HTML/en/dolphin/grouping-view.png
/usr/share/doc/HTML/en/dolphin/index.cache.bz2
/usr/share/doc/HTML/en/dolphin/index.docbook
/usr/share/doc/HTML/en/dolphin/locationbar-breadcrumb.png
/usr/share/doc/HTML/en/dolphin/locationbar-context-menu.png
/usr/share/doc/HTML/en/dolphin/locationbar-editable.png
/usr/share/doc/HTML/en/dolphin/locationbar-kioslaves-menu.png
/usr/share/doc/HTML/en/dolphin/locationbar-places-icon.png
/usr/share/doc/HTML/en/dolphin/nepomuk-search-more-options.png
/usr/share/doc/HTML/en/dolphin/nepomuk-search.png
/usr/share/doc/HTML/en/dolphin/preferences-general-behavior.png
/usr/share/doc/HTML/en/dolphin/preferences-navigation.png
/usr/share/doc/HTML/en/dolphin/preferences-services.png
/usr/share/doc/HTML/en/dolphin/preferences-startup.png
/usr/share/doc/HTML/en/dolphin/preferences-trash.png
/usr/share/doc/HTML/en/dolphin/preferences-viewmodes-icons.png
/usr/share/doc/HTML/en/dolphin/toolbar-navigation.png
/usr/share/doc/HTML/en/dolphin/toolbar-view-appearance.png
/usr/share/doc/HTML/en/dolphin/toolbar.png
/usr/share/doc/HTML/en/dolphin/viewproperties-dialog.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdolphinprivate.so.5
/usr/lib64/libdolphinprivate.so.5.0.0
/usr/lib64/libdolphinvcs.so.5
/usr/lib64/libdolphinvcs.so.5.0.0
/usr/lib64/qt5/plugins/dolphinpart.so
/usr/lib64/qt5/plugins/kcm_dolphingeneral.so
/usr/lib64/qt5/plugins/kcm_dolphinnavigation.so
/usr/lib64/qt5/plugins/kcm_dolphinservices.so
/usr/lib64/qt5/plugins/kcm_dolphinviewmodes.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/dolphin/COPYING
/usr/share/doc/dolphin/COPYING.DOC
