Summary:	QtEmu - a graphical interface for Qemu written in Qt4
Summary(pl.UTF-8):	QtEmu - interfejs graficzny dla Qemu napisany w Qt4
Name:		qtemu
Version:	1.0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qtemu/%{name}-%{version}.tar.bz2
# Source0-md5:	44560abe5b1df47f8ff6050d5864f453
Source1:	%{name}.desktop
Patch0:		%{name}-help.patch
URL:		http://qtemu.org/
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QtEmu - a graphical interface for Qemu written in Qt4

%description -l pl.UTF-8
QtEmu - interfejs graficzny dla Qemu napisany w Qt4

%prep
%setup -q -n %{name}
%patch0 -p1

%build
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}-%{version},%{_desktopdir},%{_iconsdir}}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/%{name}.png $RPM_BUILD_ROOT%{_iconsdir}
cp -Ra help $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/%{name}.png
