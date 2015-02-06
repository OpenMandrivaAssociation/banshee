%define build_appledevice	1
%define build_njb		0
%define build_mtp		1
%define build_karma		1
%define build_boo		1
#gw does not build with clutter 1.1.12:
#https://bugzilla.gnome.org/show_bug.cgi?id=611153
%define build_clutter		0
%define build_webkit		1

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

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Music player with mobile player support
Name:		banshee
Version:	2.6.0
Release:	2
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
#(nl) KDE Solid integration : from mdv svn  soft/mandriva-kde-translation/trunk/solid/
Source1:	banshee-play-audiocd.desktop
License:	MIT
Group:		Sound
Url:		http://banshee.fm

BuildRequires:	intltool
BuildRequires:	pkgconfig(dbus-sharp-glib-1.0) >= 0.5
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gconf-sharp-2.0) >= 2.8
BuildRequires:	pkgconfig(gdata-sharp-youtube) >= 1.4
BuildRequires:	pkgconfig(gio-sharp-2.0) >= 2.22.3
BuildRequires:	pkgconfig(gkeyfile-sharp)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.26
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10) >= 0.10.26
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.8
BuildRequireS:	pkgconfig(gtk-sharp-beans-2.0)
BuildRequires:	pkgconfig(gudev-sharp-1.0)
BuildRequires:	pkgconfig(mono) >= 2.4.3
BuildRequires:	pkgconfig(mono-addins) >= 0.3.1
BuildRequires:	pkgconfig(mono-zeroconf)
BuildRequires:	pkgconfig(notify-sharp)
BuildRequires:	pkgconfig(sqlite3) >= 3.4
BuildRequires:	pkgconfig(taglib-sharp) >= 2.0.3.7
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xxf86vm)

%if %{build_mtp}
BuildRequires:	pkgconfig(libmtp)
%endif

%if %{build_appledevice}
Buildrequires:	pkgconfig(libgpod-sharp)
%endif

%if %{build_webkit}
Buildrequires:	pkgconfig(webkit-1.0) >= 1.2.2
%endif

%if %{build_clutter}
Buildrequires:	pkgconfig(clutter-1.0) >= 1.0.1
%endif

%if %{build_boo}
Buildrequires:	pkgconfig(boo) >= 0.8.1
%endif

%if %{build_karma}
Buildrequires:	pkgconfig(karma-sharp)
%endif

Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-ugly
Requires:	gstreamer0.10-cdparanoia
Requires:	gstreamer0.10-gnomevfs
Suggests:	gstreamer0.10-xing
Suggests:	gstreamer0.10-lame
Suggests:	gstreamer0.10-faac
Suggests:	gstreamer0.10-faad
#gw for bpm detection:
Suggests:	gstreamer0.10-soundtouch
Suggests:	brasero

%description
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

%if %{build_appledevice}
%package ipod
Group:		Sound
Summary:	Ipod support for Banshee
Requires:	%{name} = %{version}-%{release}

%description ipod
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for iPod support in Banshee.
%endif

%if %{build_njb}
%package njb
Group:		Sound
Summary:	Nomad jukebox support for Banshee
Requires:	%{name} = %{version}-%{release}
Buildrequires:	njb-sharp >= 0.3.0

%description njb
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for Nomad jukebox support in Banshee.
%endif

%if %{build_mtp}
%package mtp
Group:		Sound
Summary:	MTP audio player support for Banshee
Requires:	%{name} = %{version}-%{release}

%description mtp
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for MTP audio player support in Banshee.
%endif

%if %{build_karma}
%package karma
Group:		Sound
Summary:	Rio Karma audio player support for Banshee
Requires:	%{name} = %{version}

%description karma
With Banshee you can easily import, manage, and play selections from
your music collection. Banshee allows you to import CDs, sync your
music collection to an mobile device, play music directly from an
mobile player, create playlists with songs from your library, and
create audio and MP3 CDs from subsets of your library.

Install this package for Rio Karma audio player support in Banshee.
%endif

%package doc
Summary:	Development documentation for %{name}
Group:		Development/Other
Requires(post):		mono-tools >= 1.1.9
Requires(postun):	mono-tools >= 1.1.9
BuildArch:	noarch

%description doc
This package contains the API documentation for the %{name} in
Monodoc format.

%package devel
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Summary:	Development parts of %{name}

%description devel
This package contains the pkg-config files needed for building Banshee
extensions.

%prep
%setup -q

%build
%configure2_5x  \
	--with-vendor-build-id="%{_vendor} %{distro_release}"  \
%if %{build_mtp}
	--enable-mtp \
%endif
%if !%{build_appledevice}
	--disable-appledevice \
%endif
%if %{build_karma}
	--enable-karma \
%endif
%if %{build_clutter}
	--enable-clutter \
%endif
	--disable-static \
	--disable-scrollkeeper \
	--disable-schemas-install
%make

%install
%makeinstall_std MONO=true

%find_lang %{name} --with-gnome

%if %{build_appledevice}
ln -sf %{_libdir}/libgpod/libgpod-sharp.dll* %{buildroot}%{_libdir}/%{name}/Extensions/
%endif

%if %{build_karma}
ln -sf %{_prefix}/lib/karma-sharp/karma-sharp.dll %{buildroot}%{_libdir}/%{name}/Extensions/
%endif

# we don't want these
find %{buildroot} -name "*.la" -delete

# gw fix paths in pkgconfig files
perl -pi -e "s^/lib$^/%{_lib}^" %{buildroot}%{_libdir}/pkgconfig/*.pc

#(nl) KDE Solid integration
mkdir -p %{buildroot}/%{_datadir}/apps/solid/actions/
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/apps/solid/actions/

%post doc
%{_bindir}/monodoc --make-index > /dev/null

%postun doc
if [ "$1" = "0" -a -x %{_bindir}/monodoc ]; then %{_bindir}/monodoc --make-index > /dev/null
fi

%files -f %{name}.lang
%doc NEWS README AUTHORS
%{_bindir}/bamz
%{_bindir}/%{name}
%{_bindir}/muinshee
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/Backends
%{_libdir}/%{name}/Backends/Banshee.GStreamer.*
%{_libdir}/%{name}/Backends/Banshee.Gio.*
%{_libdir}/%{name}/Backends/Banshee.Gnome.*
%{_libdir}/%{name}/Backends/Banshee.NowPlaying.X11.*
%{_libdir}/%{name}/Backends/Banshee.Unix.*
%{_libdir}/%{name}/Backends/gio-sharp.dll*
%{_libdir}/%{name}/Backends/libbnpx11.so
%dir %{_libdir}/%{name}/Extensions
%{_libdir}/%{name}/Extensions/Banshee.Audiobook.dll*

%if %build_boo
%{_libdir}/%{name}/Extensions/Banshee.BooScript.dll*
%endif

%{_libdir}/%{name}/Extensions/Banshee.AmazonMp3.exe*
%{_libdir}/%{name}/Extensions/Banshee.Bpm.dll*
%{_libdir}/%{name}/Extensions/Banshee.CoverArt.dll*
%{_libdir}/%{name}/Extensions/Banshee.Daap.dll*
%{_libdir}/%{name}/Extensions/Banshee.Dap.MassStorage.dll*
%{_libdir}/%{name}/Extensions/Banshee.Dap.dll*
%{_libdir}/%{name}/Extensions/Banshee.Emusic.dll*
%{_libdir}/%{name}/Extensions/Banshee.Emusic.Store*
%{_libdir}/%{name}/Extensions/Banshee.FileSystemQueue.dll*
%{_libdir}/%{name}/Extensions/Banshee.Fixup.dll*
%{_libdir}/%{name}/Extensions/Banshee.InternetArchive.dll*
%{_libdir}/%{name}/Extensions/Banshee.InternetRadio.dll*
%{_libdir}/%{name}/Extensions/Banshee.Lastfm.dll*
%{_libdir}/%{name}/Extensions/Banshee.LastfmStreaming.dll*
%{_libdir}/%{name}/Extensions/Banshee.LibraryWatcher.dll*
%{_libdir}/%{name}/Extensions/Banshee.MiniMode.dll*
%{_libdir}/%{name}/Extensions/Banshee.Mpris.dll*
%{_libdir}/%{name}/Extensions/Banshee.MultimediaKeys.dll*
%{_libdir}/%{name}/Extensions/Banshee.NotificationArea.dll*
%{_libdir}/%{name}/Extensions/Banshee.NowPlaying.dll*
%{_libdir}/%{name}/Extensions/Banshee.OpticalDisc.dll*
%{_libdir}/%{name}/Extensions/Banshee.PlayerMigration.dll*
%{_libdir}/%{name}/Extensions/Banshee.PlayQueue.dll*
%{_libdir}/%{name}/Extensions/Banshee.Podcasting.dll*
%{_libdir}/%{name}/Extensions/Banshee.YouTube.dll*

%if %build_webkit
%{_libdir}/%{name}/Extensions/Banshee.AmazonMp3.Store.dll*
%{_libdir}/%{name}/Extensions/Banshee.MiroGuide.dll*
%{_libdir}/%{name}/Extensions/Banshee.Wikipedia.dll*
%endif

%{_libdir}/%{name}/*.exe*
%{_libdir}/%{name}/Banshee*.dll*
%{_libdir}/%{name}/Hyena*.dll*
%{_libdir}/%{name}/Lastfm*.dll*
%{_libdir}/%{name}/Migo.dll*
%{_libdir}/%{name}/Mono*.dll*
%{_libdir}/%{name}/MusicBrainz.dll*
%{_libdir}/%{name}/*.so
%{_libdir}/%{name}/Banshee.Services.addins
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-audiocd.desktop
%{_datadir}/applications/%{name}-media-player.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/apps/solid/actions/banshee-play-audiocd.desktop
%{_datadir}/mime/packages/banshee-amz.xml
%{_datadir}/mime/packages/banshee-emx.xml

%files devel
%{_libdir}/pkgconfig/%{name}*.pc

%files doc
%{_prefix}/lib/monodoc/sources/banshee-docs*
%{_prefix}/lib/monodoc/sources/hyena-docs*

%if %{build_appledevice}
%files ipod
%{_libdir}/%{name}/Extensions/Banshee.Dap.AppleDevice.dll*
%{_libdir}/%{name}/Extensions/libgpod-sharp.dll*
%endif

%if %{build_njb}
%files njb
%{_libdir}/%{name}/Extensions/Banshee.Dap/*jb*
%endif

%if %{build_mtp}
%files mtp
%{_libdir}/%{name}/Mtp.dll*
%{_libdir}/%{name}/Extensions/Banshee.Dap.Mtp.dll*
%endif

%if %{build_karma}
%files karma
%{_libdir}/%{name}/Extensions/Banshee.Dap.Karma.dll*
%{_libdir}/%{name}/Extensions/karma-sharp.dll*
%endif
