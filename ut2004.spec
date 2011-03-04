Summary:	Editor's Choice Edition plus Mega Pack for the critically-acclaimed first-person shooter
Name:		ut2004
Version:	3369.3
Release:	0.2
License:	ut2003
Group:		Applications/Games
Source0:	http://www.3dgamers.com/dl/games/unrealtourn2k4/ut2004-lnxpatch3369-2.tar.bz2
# Source0-md5:	0fa447e05fe5a38e0e32adf171be405e
Source1:	http://mirrors.kernel.org/gentoo/distfiles/ut2004-v3369-3-linux-dedicated.7z
# Source1-md5:	8f797af8dc3142f61e1c3c3885e6dc40
Source2:	README.PLD
URL:		http://www.unrealtournament2004.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRequires: p7zip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# ut2004-bin sym versions are rather odd
%define		_noautoprov		ut2004-bin
%define		_enable_debug_packages	0

%define		gamelibdir		%{_libdir}/games/%{name}
%define		gamedatadir		%{_datadir}/games/%{name}

%description
Unreal Tournament - futuristic FPS game.

%description -l pl.UTF-8
Unreal Tournament - futurystyczna gra FPS.

%prep
%setup -qc
# p7zip has no options be quiet
7z x %{SOURCE1} -bd >/dev/null
cp -p %{SOURCE2} .

cd UT2004-Patch/System
# These files are owned by ut2004-bonuspack-mega
rm -f Manifest.in{i,t} Packages.md5

rm -f ucc-bin*
%ifarch %{x8664}
mv -f ut2004-bin-linux-amd64 ut2004-bin
%else
rm -f ut2004-bin-linux-amd64
%endif
cd -

%ifarch %{x8664}
mv -f ut2004-ucc-bin-09192008/ucc-bin-linux-amd64 UT2004-Patch/System/ucc-bin
%else
mv -f ut2004-ucc-bin-09192008/ucc-bin UT2004-Patch/System
%endif
chmod a+rx UT2004-Patch/System/ut2004-bin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{gamedatadir},%{gamelibdir}} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir},%{_bindir}}

cp -a UT2004-Patch/* $RPM_BUILD_ROOT%{gamelibdir}

ln -s %{_libdir}/libopenal.so $RPM_BUILD_ROOT%{gamelibdir}/System/openal.so
ln -s %{_libdir}/libSDL-1.2.so.0 $RPM_BUILD_ROOT%{gamelibdir}/System/libSDL-1.2.so.0

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f $RPM_BUILD_ROOT%{gamelibdir}/System/cdkey ]; then
%banner %{name} <<EOF
You need to put cd key to file:
  %{gamelibdir}/System/cdkey

CD key format is: XXXXX-XXXXX-XXXXX-XXXXX (all uppercase)
EOF
fi

%files
%defattr(644,root,root,755)
%doc README.PLD
%dir %{gamelibdir}
%{gamelibdir}/Animations
%{gamelibdir}/Help
%{gamelibdir}/Textures
%dir %{gamelibdir}/System
%attr(755,root,root) %{gamelibdir}/System/libSDL-1.2.so.0
%attr(755,root,root) %{gamelibdir}/System/openal.so
%attr(755,root,root) %{gamelibdir}/System/ucc-bin
%attr(755,root,root) %{gamelibdir}/System/ut2004-bin
%{gamelibdir}/Speech/*.xml
%{gamelibdir}/System/*.ini
%{gamelibdir}/System/*.u
%{gamelibdir}/System/*.ucl

# %lang?
%{gamelibdir}/System/*.det
%{gamelibdir}/System/*.kot
%{gamelibdir}/System/*.est
%{gamelibdir}/System/*.frt
%{gamelibdir}/System/*.int
%{gamelibdir}/System/*.itt
# web subpackage?
%{gamelibdir}/Web
