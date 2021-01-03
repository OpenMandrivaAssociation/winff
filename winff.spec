%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A graphical interface for the video converter ffmpeg
Name:		winff
Version:	1.5.5
Release:	1
License:	GPLv3
Group:		Video
Url:		https://github.com/WinFF/winff/
Source0:	http://winff.googlecode.com/files/%{name}-%{version}-source.tar.gz
Patch1:		enable-build-with-lazarus-1.8.patch
BuildRequires:	lazarus
BuildRequires:	dos2unix
BuildRequires:	pkgconfig(x11)
Requires:	ffmpeg
Requires:	xterm

%description
WinFF is a GUI for the command line video converter, FFMPEG. It will 
convert most any video file that FFmpeg will convert. WinFF does 
multiple files in multiple formats at one time. You can for example 
convert mpeg's, flv's, and mov's, all into avi's all at once.

%prep
%setup -q -n %{name}
%autopatch -p1
# Fix EOL (Version 1.2.0)
dos2unix *.txt

%build
lazbuild --ws=qt5 -B winff.lpr

%install
%__mkdir_p %{buildroot}{%{_bindir},%{_datadir}/%{name}/languages}

# Install winff binary
%__install %{name} %{buildroot}%{_bindir}

# Install languages
%__install languages/*.po %{buildroot}%{_datadir}/%{name}/languages

# Install presets
%__install presets.xml %{buildroot}%{_datadir}/%{name}

%__mkdir_p %{buildroot}{%{_datadir}/pixmaps,%{_datadir}/applications,%{_mandir}/man1}

# Install man page
%__install %{name}.1 %{buildroot}%{_mandir}/man1

# Install icons
%__install winff-icons/48x48/%{name}.png %{buildroot}%{_datadir}/pixmaps
for i in 16 24 32 48; do
	%__mkdir_p %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
	%__install winff-icons/"$i"x"$i"/*.png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
done

# Desktop file
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=WinFF
GenericName=WinFF
Comment=A GUI for FFMPEG
Exec=%{name}
Icon=%{name}
Categories=AudioVideo;Video;
EOF

%files
%doc *.txt docs/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/*
%{_mandir}/man1/*


%changelog
* Thu Feb 09 2012 Andrey Bondrov <abondrov@mandriva.org> 1.4.1-1mdv2011.0
+ Revision: 772352
- Add patch0 to remove hardcoded build target
- New version 1.4.1

* Thu Dec 22 2011 Guilherme Moro <guilherme@mandriva.com> 1.4.0-0
+ Revision: 744444
- disable debug packages
- enable generating dwarf
- updated to version 1.4.0

* Tue Nov 01 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.3.2-1
+ Revision: 709261
- version bump

* Tue Nov 01 2011 Александр Казанцев <kazancas@mandriva.org> 1.3.1-3
+ Revision: 708679
+ rebuild (emptylog)

* Sat Sep 11 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3.1-1mdv2011.0
+ Revision: 577154
- update to 1.3.1

* Fri Aug 06 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3.0-1mdv2011.0
+ Revision: 566545
- update to 1.3.0

* Thu Feb 04 2010 Jérôme Brenier <incubusss@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 500607
- new version 1.2.0
- drop no more needed permissions fix

* Thu Dec 03 2009 Jérôme Brenier <incubusss@mandriva.org> 1.1.1-1mdv2010.1
+ Revision: 472887
--pcp option no more needed for lazbuild
- add Requires: xterm
- initial import
- Created package structure for winff.

