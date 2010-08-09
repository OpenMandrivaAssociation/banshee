%define name banshee
%define version 1.7.3
%define release %mkrel 1
%define oname banshee-1

%define build_ipod 1
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

%if %mdvver < 201100
%define build_webkit 0
%endif

%if %mdvver < 201000
%define build_karma 0
%define build_clutter 0
%endif

%{?_without_ipod: %{expand: %%global build_ipod 0}}
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
Source0: http://banshee.fm/files/banshee/stable/%version/%{oname}-%{version}.tar.bz2
#(nl) KDE Solid integration : from mdv svn  soft/mandriva-kde-translation/trunk/solid/
Source1: banshee-play-audiocd.desktop
Patch0: banshee-fix-configure.patch
Patch1: banshee-1-1.7.3-fix-makefile.patch
License: MIT
Group: Sound
Url: http://banshee.fm
BuildRoot: %{_tmppath}/%{oname}-%{version}-%{release}-buildroot
Buildrequires: mono-devel
Buildrequires: mono-zeroconf-devel
Buildrequires: mono-addins
Buildrequires: gnome-sharp2-devel
Buildrequires: webkit-sharp-devel
%if %build_webkit
Buildrequires: webkitgtk-devel >= 1.2.2
%endif
Buildrequires: libgoogle-data-mono-devel
Buildrequires: sqlite3-devel
Buildrequires: libgstreamer-plugins-base-devel
Buildrequires: libxrandr-devel libxxf86vm-devel
BuildRequires: gstreamer0.10-cdparanoia
BuildRequires: gstreamer0.10-gnomevfs
BuildRequires: gstreamer0.10-plugins-good
Buildrequires: gnome-desktop-devel
Buildrequires: ndesk-dbus-glib-devel
Buildrequires: taglib-sharp-devel >= 2.0.3.7
Buildrequires: notify-sharp
Buildrequires: libmtp-devel >= 0.2.1
%if %build_clutter
Buildrequires: clutter-devel >= 1.0
%endif
BuildRequires: gio-sharp-devel
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
Suggests: brasero

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
Buildrequires: ipod-sharp-devel >= 0.8.5
Requires: ipod-sharp >= 0.8.5

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
%setup -q -n %oname-%version
%apply_patches
aclocal -I build/m4 -I build/m4/shave -I build/m4/banshee -I build/m4/shamrock
autoconf
automake

%build
%configure2_5x  --with-vendor-build-id="Mandriva Linux %mandriva_release"  \
 --enable-mtp \
%if %build_karma
 --enable-karma \
%endif
%if %build_clutter
 --enable-clutter \
%endif

make

%install
rm -rf $RPM_BUILD_ROOT *.lang
%makeinstall_std MONO=true
%find_lang %oname
%find_lang %name  --with-gnome
cat %name.lang >> %oname.lang
ln -sf %_prefix/lib/ipod-sharp/{ipod-sharp-ui*,ipod-sharp.dll*} %buildroot%_libdir/%oname/Extensions/
%if %build_karma
ln -sf %_prefix/lib/karma-sharp/karma-sharp.dll %buildroot%_libdir/%oname/Extensions/
%endif

rm -f %buildroot%_libdir/%oname/*.a %buildroot%_libdir/%oname/gstreamer-0.10/*.a %buildroot%_libdir/%oname/Backends/*.a

#gw fix paths in pkgconfig files
perl -pi -e "s^/lib$^/%_lib^" %buildroot%_libdir/pkgconfig/*.pc

#(nl) KDE Solid integration
mkdir -p %buildroot/%_datadir/apps/solid/actions/
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%_datadir/apps/solid/actions/

#gw: generated at installation time
rm -rf %buildroot%_datadir/{applications/mimeinfo.cache,\
mime/{XMLnamespaces,a*,g*,icons,m*,subclasses,t*}}

%post doc
%_bindir/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %_bindir/monodoc ]; then %_bindir/monodoc --make-index > /dev/null
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %oname.lang
%defattr(-,root,root)
%doc NEWS README ChangeLog AUTHORS
%_bindir/bamz
%_bindir/%oname
%_bindir/muinshee
%dir %_libdir/%oname/
%dir %_libdir/%oname/Backends
%_libdir/%oname/Backends/Banshee.GStreamer.*
%_libdir/%oname/Backends/Banshee.Gio.*
%_libdir/%oname/Backends/Banshee.Gnome.*
%_libdir/%oname/Backends/Banshee.Hal.*
%_libdir/%oname/Backends/Banshee.NowPlaying.X11.*
%_libdir/%oname/Backends/Banshee.Unix.*
%_libdir/%oname/Backends/libbnpx11.la
%_libdir/%oname/Backends/libbnpx11.so
%dir %_libdir/%oname/Extensions
%_libdir/%oname/Extensions/Banshee.Audiobook.dll*
%_libdir/%oname/Extensions/Banshee.AudioCd.dll*
%if %build_boo
%_libdir/%oname/Extensions/Banshee.BooScript.dll*
%endif
%_libdir/%oname/Extensions/Banshee.AmazonMp3.exe*
%_libdir/%oname/Extensions/Banshee.Bpm.dll*
%_libdir/%oname/Extensions/Banshee.CoverArt.dll*
%_libdir/%oname/Extensions/Banshee.Daap.dll*
%_libdir/%oname/Extensions/Banshee.Dap.MassStorage.dll*
%_libdir/%oname/Extensions/Banshee.Dap.dll*
%_libdir/%oname/Extensions/Banshee.Emusic.dll*
%_libdir/%oname/Extensions/Banshee.FileSystemQueue.dll*
%_libdir/%oname/Extensions/Banshee.Fixup.dll*
%_libdir/%oname/Extensions/Banshee.InternetArchive.dll*
%_libdir/%oname/Extensions/Banshee.InternetRadio.dll*
%_libdir/%oname/Extensions/Banshee.Lastfm.dll*
%_libdir/%oname/Extensions/Banshee.LastfmStreaming.dll*
%_libdir/%oname/Extensions/Banshee.LibraryWatcher.dll*
%_libdir/%oname/Extensions/Banshee.MiniMode.dll*
%_libdir/%oname/Extensions/Banshee.MultimediaKeys.dll*
%_libdir/%oname/Extensions/Banshee.NotificationArea.dll*
%_libdir/%oname/Extensions/Banshee.NowPlaying.dll*
%_libdir/%oname/Extensions/Banshee.PlayerMigration.dll*
%_libdir/%oname/Extensions/Banshee.PlayQueue.dll*
%_libdir/%oname/Extensions/Banshee.Podcasting.dll*
%_libdir/%oname/Extensions/Banshee.YouTube.dll*
%if %build_webkit
%_libdir/%oname/Extensions/Banshee.AmazonMp3.Store.dll*
%_libdir/%oname/Extensions/Banshee.MiroGuide.dll*
%_libdir/%oname/Extensions/Banshee.Wikipedia.dll*
%endif
%_libdir/%oname/*.exe*
%_libdir/%oname/Banshee*.dll*
%_libdir/%oname/Hyena*.dll*
%_libdir/%oname/Lastfm*.dll*
%_libdir/%oname/Migo.dll*
%_libdir/%oname/Mono*.dll*
%_libdir/%oname/MusicBrainz.dll*
%_libdir/%oname/*.so
%_libdir/%oname/gstreamer-0.10/
%_libdir/%oname/Banshee.Services.addins
%attr(644,root,root) %_libdir/%oname/*.la
%_datadir/%oname/
%_datadir/dbus-1/services/*
%_datadir/applications/%{oname}.desktop
%_datadir/applications/%{oname}-audiocd.desktop
%_datadir/applications/%{oname}-media-player.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/apps/solid/actions/banshee-play-audiocd.desktop
%_datadir/mime/packages/amazonmp3.xml

%files devel
%defattr(-,root,root)
%_libdir/pkgconfig/%{oname}*.pc

%files doc
%defattr(-,root,root)
%_prefix/lib/monodoc/sources/banshee-docs*
%_prefix/lib/monodoc/sources/hyena-docs*

%if %build_ipod
%files ipod
%defattr(-,root,root)
%_libdir/%oname/Extensions/Banshee.Dap.Ipod.dll*
%_libdir/%oname/Extensions/ipod-sharp*
%endif

%if %build_njb
%files njb
%defattr(-,root,root)
%_libdir/%oname/Extensions/Banshee.Dap/*jb*
%endif

%if %build_mtp
%files mtp
%defattr(-,root,root)
%_libdir/%oname/Mtp.dll*
%_libdir/%oname/Extensions/Banshee.Dap.Mtp.dll*
%endif

%if %build_karma
%files karma
%defattr(-,root,root)
%_libdir/%oname/Extensions/Banshee.Dap.Karma.dll*
%_libdir/%oname/Extensions/karma-sharp.dll
%endif

