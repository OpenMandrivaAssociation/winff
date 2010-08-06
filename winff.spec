Summary:	A graphical interface for the video converter ffmpeg
Name:		winff
Version:	1.3.0
Release:	%mkrel 1
License:	GPLv3
Group:		Video
Url:		http://winff.org
Source0:	http://winff.googlecode.com/files/%{name}-%{version}-source.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	lazarus
BuildRequires:	dos2unix
Requires:	ffmpeg
Requires:	xterm

%description
WinFF is a GUI for the command line video converter, FFMPEG. It will 
convert most any video file that FFmpeg will convert. WinFF does 
multiple files in multiple formats at one time. You can for example 
convert mpeg's, flv's, and mov's, all into avi's all at once.

%prep
%setup -q -n %{name}

# Fix EOL (Version 1.2.0)
dos2unix -U *.txt

%build
lazbuild --widgetset=gtk2 -B winff.lpr

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}{%{_bindir},%{_datadir}/%{name}/languages}

# Install winff binary
install %{name} %{buildroot}%{_bindir}

# Install languages
install languages/*.po %{buildroot}%{_datadir}/%{name}/languages

# Install presets
install presets.xml %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}{%{_datadir}/pixmaps,%{_datadir}/applications,%{_mandir}/man1}

# Install man page
install %{name}.1 %{buildroot}%{_mandir}/man1

# Install icons
install winff-icons/48x48/%{name}.png %{buildroot}%{_datadir}/pixmaps
for i in 16 24 32 48; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
	install winff-icons/"$i"x"$i"/*.png %{buildroot}%{_datadir}/icons/hicolor/"$i"x"$i"/apps
done

# Desktop file
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=WinFF
GenericName=WinFF
Comment=A GUI for FFMPEG
Exec=%{name}
Icon=%{name}
Categories=AudioVideo;Video;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc *.txt docs/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png
%{_iconsdir}/*
%{_mandir}/man1/*
