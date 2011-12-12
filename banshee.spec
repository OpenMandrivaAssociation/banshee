%define name banshee
%define version 2.3.2
%define release %mkrel 1

%define build_appledevice 1
%define build_njb 0
%define build_mtp 1
%define build_karma 1
%define build_boo 1
#gw does not build with clutter 1.1.12:
#https://bugzilla.gnome.org/show_bug.cgi?id=611153
%define build_clutter 0
%define build_webkit 1

%if %mdvver == 201000
%define build_clutter 1
%endif

%if %mdvver < 201010
%define build_webkit 0
%endif

%if %mdvver < 201000
%define build_karma 0
%define build_clutter 0
%endif

%{?_without_njb: %{expand: %%global build_njb 0}}
%{?_with_njb: %{expand: %%global build_njb 1}}
%{?_without_mtp: %{expand: %%global build_mtp 0}}
%{?_with_mtp: %{expand: %%global build_mtp 1}}
%{?_without_karma: %{expand: %%global build_karma 0}}
%{?_with_karma: %{expand: %%global build_karma 1}}
%{?_without_boo: %{expand: %%global build_boo 0}}
%{?_with_boo: %{expand: %%global build_boo 1}}
%{?_without_clutter: %{expand: %%global build_clutter 0}}
%{?_with_clutter: %{expand: %%global build_clutter 1}}

Summary: Music player with mobile player support
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
#(nl) KDE Solid integration : from mdv svn  soft/mandriva-kde-translation/trunk/solid/
Source1: banshee-play-audiocd.desktop
#gw fix for API change in libgpod 0.8.2:
Patch0: banshee-2.0.0-fix-apple-track-size.patch
License: MIT
Group: Sound
Url: http://banshee.fm
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires: mono-devel >= 2.4.3
Buildrequires: dbus-sharp-glib-devel >= 0.5
%if %mdvver >= 201100
Buildrequires: mono-zeroconf-devel
Buildrequires: mono-addins-devel >= 0.6.2
Buildrequires: taglib-sharp-devel >= 2.0.3.7
Buildrequires: notify-sharp-devel
%else
Buildrequires: mono-zeroconf
Buildrequires: mono-addins
Buildrequires: taglib-sharp >= 2.0.3.7
Buildrequires: notify-sharp
%endif
Buildrequires: gnome-sharp2-devel
Buildrequires: webkit-sharp-devel
Buildrequires: gudev-sharp-devel
Buildrequires: gkeyfile-sharp-devel >= 0.1-1mdv
%if %build_webkit
Buildrequires: webkitgtk-devel >= 1.2.2
%endif
Buildrequires: libgoogle-data-mono-devel
Buildrequires: sqlite3-devel
Buildrequires: libgstreamer-plugins-base-devel >= 0.10.26
Buildrequires: libxrandr-devel libxxf86vm-devel
BuildRequires: gstreamer0.10-cdparanoia
BuildRequires: gstreamer0.10-gnomevfs
BuildRequires: gstreamer0.10-plugins-good
Buildrequires: gnome-desktop-devel
Buildrequires: libmtp-devel >= 0.2.1
%if %build_clutter
Buildrequires: clutter-devel >= 1.0
%endif
BuildRequires: gio-sharp-devel >= 2.22.3
BuildRequires: gtk-sharp-beans-devel
#gw not yet packaged:
#BuildRequires: clutter-sharp
%if %build_boo
Buildrequires: boo
%endif
BuildRequires: mono-tools >= 1.1.9
Buildrequires: librsvg
Buildrequires: desktop-file-utils
Buildrequires: gnome-common intltool
Buildrequires: gnome-doc-utils
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires: gstreamer0.10-plugins-base
Requires: gstreamer0.10-plugins-ugly
Requires: gstreamer0.10-cdparanoia
Requires: gstreamer0.10-gnomevfs
Provides: banshee-gstreamer banshee-official-plugins banshee-1
Obsoletes: banshee-gstreamer banshee-official-plugins banshee-1
Suggests: gstreamer0.10-xing
Suggests: gstreamer0.10-lame
Suggests: gstreamer0.10-faac
Suggests: gstreamer0.10-faad
#gw for bpm detection:
Suggests: gstreamer0.10-soundtouch
Suggests: brasero

%description
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

%if %build_appledevice
%package ipod
Group: Sound
Summary: Ipod support for Banshee
Requires: %name = %version
%if %build_appledevice
Buildrequires: libgpod-devel >= 0.7.95
%endif

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
Buildrequires: libmtp-devel >= 0.2.1

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
Provides: banshee-1-doc
Obsoletes: banshee-1-doc

%description doc
This package contains the API documentation for the %name in
Monodoc format.

%package devel
Group: Development/Other
Requires: %name = %version-%release
Summary: Development parts of %name

%description devel
This package contains the pkg-config files needed for building Banshee
extensions.

%prep
%setup -qn %name-%version
%apply_patches

%build
%configure2_5x  --with-vendor-build-id="%product_distribution %product_version"  \
 --enable-mtp \
%if !%build_appledevice
 --disable-appledevice \
%endif
%if %build_karma
 --enable-karma \
%endif
%if %build_clutter
 --enable-clutter \
%endif

make

%install
rm -rf %{buildroot} *.lang
%makeinstall_std MONO=true
%find_lang %name --all-name --with-gnome
ln -sf %_prefix/lib/gio-sharp/gio-sharp.dll* %buildroot%_libdir/%name/Backends/
%if %build_appledevice
ln -sf %_libdir/libgpod/libgpod-sharp.dll* %buildroot%_libdir/%name/Extensions/
%endif
%if %build_karma
ln -sf %_prefix/lib/karma-sharp/karma-sharp.dll %buildroot%_libdir/%name/Extensions/
%endif

rm -f %buildroot%_libdir/%name/*.a %buildroot%_libdir/%name/Backends/*.a

#gw fix paths in pkgconfig files
perl -pi -e "s^/lib$^/%_lib^" %buildroot%_libdir/pkgconfig/*.pc

#(nl) KDE Solid integration
mkdir -p %buildroot/%_datadir/apps/solid/actions/
install -D -m 644 %{SOURCE1} %{buildroot}%_datadir/apps/solid/actions/

#gw: generated at installation time
rm -rf %buildroot%_datadir/{applications/mimeinfo.cache,\
mime/{XMLnamespaces,a*,g*,icons,m*,subclasses,t*}}

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS README AUTHORS
# ChangeLog
%_bindir/bamz
%_bindir/%name
%_bindir/muinshee
%dir %_libdir/%name/
%dir %_libdir/%name/Backends
%_libdir/%name/Backends/Banshee.GStreamer.*
%_libdir/%name/Backends/Banshee.Gio.*
%_libdir/%name/Backends/Banshee.Gnome.*
%_libdir/%name/Backends/Banshee.NowPlaying.X11.*
%_libdir/%name/Backends/Banshee.Unix.*
%_libdir/%name/Backends/gio-sharp.dll*
%_libdir/%name/Backends/libbnpx11.la
%_libdir/%name/Backends/libbnpx11.so
%dir %_libdir/%name/Extensions
%_libdir/%name/Extensions/Banshee.Audiobook.dll*
%if %build_boo
%_libdir/%name/Extensions/Banshee.BooScript.dll*
%endif
%_libdir/%name/Extensions/Banshee.AmazonMp3.exe*
%_libdir/%name/Extensions/Banshee.Bpm.dll*
%_libdir/%name/Extensions/Banshee.CoverArt.dll*
%_libdir/%name/Extensions/Banshee.Daap.dll*
%_libdir/%name/Extensions/Banshee.Dap.MassStorage.dll*
%_libdir/%name/Extensions/Banshee.Dap.dll*
%_libdir/%name/Extensions/Banshee.Emusic.dll*
%_libdir/%name/Extensions/Banshee.Emusic.Store.dll*
%_libdir/%name/Extensions/Banshee.FileSystemQueue.dll*
%_libdir/%name/Extensions/Banshee.Fixup.dll*
%_libdir/%name/Extensions/Banshee.InternetArchive.dll*
%_libdir/%name/Extensions/Banshee.InternetRadio.dll*
%_libdir/%name/Extensions/Banshee.Lastfm.dll*
%_libdir/%name/Extensions/Banshee.LastfmStreaming.dll*
%_libdir/%name/Extensions/Banshee.LibraryWatcher.dll*
%_libdir/%name/Extensions/Banshee.MiniMode.dll*
%_libdir/%name/Extensions/Banshee.Mpris.dll*
%_libdir/%name/Extensions/Banshee.MultimediaKeys.dll*
%_libdir/%name/Extensions/Banshee.NotificationArea.dll*
%_libdir/%name/Extensions/Banshee.NowPlaying.dll*
%_libdir/%name/Extensions/Banshee.OpticalDisc.dll*
%_libdir/%name/Extensions/Banshee.PlayerMigration.dll*
%_libdir/%name/Extensions/Banshee.PlayQueue.dll*
%_libdir/%name/Extensions/Banshee.Podcasting.dll*
%_libdir/%name/Extensions/Banshee.YouTube.dll*
%if %build_webkit
%_libdir/%name/Extensions/Banshee.AmazonMp3.Store.dll*
%_libdir/%name/Extensions/Banshee.MiroGuide.dll*
%_libdir/%name/Extensions/Banshee.Wikipedia.dll*
%endif
%_libdir/%name/*.exe*
%_libdir/%name/Banshee*.dll*
%_libdir/%name/Hyena*.dll*
%_libdir/%name/Lastfm*.dll*
%_libdir/%name/Migo.dll*
%_libdir/%name/Mono*.dll*
%_libdir/%name/MusicBrainz.dll*
%_libdir/%name/*.so
%_libdir/%name/Banshee.Services.addins
%attr(644,root,root) %_libdir/%name/*.la
%_datadir/%name/
%_datadir/dbus-1/services/*
%_datadir/applications/%{name}.desktop
%_datadir/applications/%{name}-audiocd.desktop
%_datadir/applications/%{name}-media-player.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/apps/solid/actions/banshee-play-audiocd.desktop
%_datadir/mime/packages/banshee-amz.xml
%_datadir/mime/packages/banshee-emx.xml

%files devel
%defattr(-,root,root)
%_libdir/pkgconfig/%{name}*.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/banshee-docs*
%_prefix/lib/monodoc/sources/hyena-docs*

%if %build_appledevice
%files ipod
%defattr(-,root,root)
%_libdir/%name/Extensions/Banshee.Dap.AppleDevice.dll*
%_libdir/%name/Extensions/libgpod-sharp.dll*
%endif

%if %build_njb
%files njb
%defattr(-,root,root)
%_libdir/%name/Extensions/Banshee.Dap/*jb*
%endif

%if %build_mtp
%files mtp
%defattr(-,root,root)
%_libdir/%name/Mtp.dll*
%_libdir/%name/Extensions/Banshee.Dap.Mtp.dll*
%endif

%if %build_karma
%files karma
%defattr(-,root,root)
%_libdir/%name/Extensions/Banshee.Dap.Karma.dll*
%_libdir/%name/Extensions/karma-sharp.dll
%_libdir/%name/Extensions/karma-sharp.dll.config
%endif

