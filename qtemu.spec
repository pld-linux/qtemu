# TODO
# - optflags
# - use cmake based build and install translations
Summary:	QtEmu - a graphical interface for Qemu written in Qt4
Summary(pl.UTF-8):	QtEmu - interfejs graficzny dla Qemu napisany w Qt4
Name:		qtemu
Version:	1.0.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtemu/%{name}-%{version}.tar.bz2
# Source0-md5:	3b93e209dc62e52a1d94c8eb24d0b149
Source1:	%{name}.desktop
Patch0:		%{name}-help.patch
URL:		http://qtemu.org/
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtEmu - a graphical interface for Qemu written in Qt4.

%description -l pl.UTF-8
QtEmu - interfejs graficzny dla Qemu napisany w Qt4.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version},%{_desktopdir},%{_pixmapsdir}}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p images/crystal/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a help $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
