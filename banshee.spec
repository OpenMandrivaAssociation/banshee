%define name banshee
%define version 0.12.1
%define release %mkrel 1

%define build_ipod 1
%define build_njb 1
%define build_mtp 1
%define build_karma 0

%{?_without_ipod: %{expand: %%global build_ipod 0}}
%{?_without_njb: %{expand: %%global build_njb 0}}
%{?_with_njb: %{expand: %%global build_njb 1}}
%{?_without_mtp: %{expand: %%global build_mtp 0}}
%{?_with_mtp: %{expand: %%global build_mtp 1}}
%{?_without_karma: %{expand: %%global build_karma 0}}
%{?_with_karma: %{expand: %%global build_karma 1}}

Summary: Music player with mobile player support
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://banshee-project.org/files/banshee/%{name}-%{version}.tar.bz2
#Source0: http://banshee-project.org/files/banshee/%{name}-%{cvs}.tar.bz2
# http://bugzilla.gnome.org/show_bug.cgi?id=350773
Patch: http://bobcopeland.com/karma/banshee/fix-transcode.patch
License: BSD
Group: Sound
Url: http://banshee-project.org/index.php/Main_Page
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: mono-devel mono-data-sqlite
Buildrequires: gnome-sharp2
Buildrequires: sqlite3-devel
BuildRequires: avahi-sharp
Buildrequires: libgstreamer-plugins-base-devel
BuildRequires: gstreamer0.10-cdparanoia
BuildRequires: gstreamer0.10-gnomevfs
BuildRequires: gstreamer0.10-plugins-good
Buildrequires: gnome-desktop-devel
Buildrequires: dbus-glib-devel
Buildrequires: libnautilus-burn-devel
Buildrequires: libmusicbrainz-devel
BuildRequires: mono-tools >= 1.1.9
Buildrequires: perl-XML-Parser
Buildrequires: librsvg
Buildrequires: desktop-file-utils

Buildrequires: gnome-common intltool
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: gstreamer0.10-plugins-base
Requires: gstreamer0.10-plugins-ugly
Requires: gstreamer0.10-cdparanoia
Requires: gstreamer0.10-gnomevfs
Requires: %mklibname musicbrainz 4
Provides: banshee-gstreamer banshee-official-plugins
Obsoletes: banshee-gstreamer banshee-official-plugins
#Suggests: gstreamer0.10-xing
#Suggests: gstreamer0.10-lame
#Suggests: gstreamer0.10-faac
#Suggests: gstreamer0.10-faad

%description
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

%if %build_ipod
%package ipod
Group: Sound
Summary: Ipod support for Banshee
Requires: %name = %version
Buildrequires: ipod-sharp >= 0.6.3

%description ipod
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for iPod support in Banshee.
%endif
%if %build_njb
%package njb
Group: Sound
Summary: Nomad jukebox support for Banshee
Requires: %name = %version
Buildrequires: njb-sharp >= 0.3.0

%description njb
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for Nomad jukebox support in Banshee.
%endif

%if %build_mtp
%package mtp
Group: Sound
Summary: MTP audio player support for Banshee
Requires: %name = %version
Requires: libgphoto2-sharp
Buildrequires: libgphoto2-sharp

%description mtp
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for MTP audio player support in Banshee.
%endif


%if %build_karma
%package karma
Group: Sound
Summary: Rio Karma audio player support for Banshee
Requires: %name = %version
Buildrequires: karma-sharp

%description karma
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for Rio Karma audio player support in Banshee.
%endif

%package doc
Summary: Development documentation for %name
Group: Development/Other
Requires(post): mono-tools >= 1.1.9
Requires(postun): mono-tools >= 1.1.9

%description doc
This package contains the API documentation for the %name in
Monodoc format.

%prep
%setup -q -n %name-%version
%if %build_karma
cd src/Core
%patch -p2
cd ../..
%endif
##setup -q -n %name
#./autogen.sh

%build
%configure2_5x  \
%if %build_mtp
 --enable-mtp \
%endif
%if %build_karma
 --enable-karma \
%endif
 --with-gstreamer-0-10 

make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std MONO=true
mkdir -p %buildroot%_prefix/lib/monodoc/
mv %buildroot%buildroot/%_prefix/lib/monodoc/* %buildroot%_prefix/lib/monodoc/
install -D -m 644 docs/MonodocNodeConfig.exe %buildroot%_libdir/banshee-doc/MonodocNodeConfig.exe
%find_lang %name

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name} 
?package(%{name}): command="%{_bindir}/%name" icon="music-player-banshee.png" longtitle="Music Management Application" title="Banshee" needs="x11" section="Multimedia/Sound" startup_notify="true" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#icons
mkdir -p %buildroot{%_liconsdir,%_miconsdir}
rsvg -w 48 -h 48 data/images/music-player-banshee.svg %buildroot%_miconsdir/music-player-banshee.png
rsvg -w 32 -h 32 data/images/music-player-banshee.svg %buildroot%_iconsdir/music-player-banshee.png
rsvg -w 16 -h 16 data/images/music-player-banshee.svg %buildroot%_liconsdir/music-player-banshee.png

rm -f %buildroot%_libdir/%name/*.a
cd %buildroot%_libdir/%name/Banshee.Dap/
%if %build_ipod
ln -sf %_prefix/lib/ipod-sharp/{ipod-sharp.dll*,ipod-sharp-ui.dll*} .
%endif
%if %build_njb
ln -sf %_libdir/njb-sharp/*njb* .
%endif
%if %build_mtp
ln -sf %_prefix/lib/libgphoto2-sharp/* .
%endif
%if %build_karma
ln -sf %_libdir/karma-sharp/* .
%endif


find %buildroot -name \*.config -type f|xargs chmod 644

%post
%{update_menus}
%define schemas %{name}-core %{name}-interface %{name}-plugin-audioscrobbler %{name}-plugin-daap %{name}-plugin-metadatasearcher %{name}-plugin-minimode %{name}-plugin-mmkeys %{name}-plugin-notificationarea %{name}-plugin-podcast %{name}-plugin-radio %{name}-plugin-recommendation
%post_install_gconf_schemas %schemas
%update_scrollkeeper
%update_icon_cache hicolor
%update_desktop_database

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%{clean_menus}
%clean_icon_cache hicolor
%clean_desktop_database

%post doc
%_bindir/mono %_libdir/banshee-doc/MonodocNodeConfig.exe --insert "Banshee Libraries" classlib-banshee %_prefix/lib/monodoc/sources/../monodoc.xml
%_bindir/monodoc --make-index > /dev/null

%preun doc
if [ "$1" = "0" ]; then %_bindir/mono %_libdir/banshee-doc/MonodocNodeConfig.exe --remove classlib-banshee %_prefix/lib/monodoc/sources/../monodoc.xml; fi

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README ChangeLog AUTHORS
%_sysconfdir/gconf/schemas/%{name}-core.schemas
%_sysconfdir/gconf/schemas/%{name}-interface.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-audioscrobbler.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-daap.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-metadatasearcher.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-minimode.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-mmkeys.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-notificationarea.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-podcast.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-radio.schemas
%_sysconfdir/gconf/schemas/%{name}-plugin-recommendation.schemas
%_bindir/%name
%dir %_libdir/%name/
%dir %_libdir/%name/Banshee.MediaEngine/
%dir %_libdir/%name/Banshee.Dap/
%dir %_libdir/%name/Banshee.Plugins
%_libdir/%name/Banshee.MediaEngine/Banshee.MediaEngine.GStreamer*
%_libdir/%name/Banshee.Dap/Banshee.Dap.MassStorage.dll*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.Audioscrobbler.dll*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.MetadataSearch*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.Daap*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.MiniMode*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.MMKeys*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.NotificationAreaIcon*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.Podcast*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.Radio*
%_libdir/%name/Banshee.Plugins/Banshee.Plugins.Recommendation*
%_libdir/%name/*.exe*
%_libdir/%name/*.dll*
%_libdir/%name/*.so
%attr(644,root,root) %_libdir/%name/*.la
%_libdir/pkgconfig/%name.pc
%_datadir/%name/
%_datadir/dbus-1/services/*
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/music-player-%name.*
%_menudir/%name
%_liconsdir/*.png
%_iconsdir/*.png
%_miconsdir/*.png


%if %build_ipod
%files ipod
%defattr(-,root,root)
%_libdir/%name/Banshee.Dap/Banshee.Dap.Ipod.dll*
%_libdir/%name/Banshee.Dap/ipod-sharp*
%endif

%if %build_njb
%files njb
%defattr(-,root,root)
%_libdir/%name/Banshee.Dap/*jb*
%endif

%if %build_mtp
%files mtp
%defattr(-,root,root)
%_libdir/%name/Banshee.Dap/Banshee.Dap.Mtp*
%_libdir/%name/Banshee.Dap/libgphoto2-sharp*
%endif

%if %build_karma
%files karma
%defattr(-,root,root)
%_libdir/%name/Banshee.Dap/Banshee.Dap.Karma*
%_libdir/%name/Banshee.Dap/karma-sharp*
%endif

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/banshee-docs*
%_libdir/banshee-doc/


