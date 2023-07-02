#
# Conditional build:
%bcond_without	apidocs	# API documentation
%bcond_without	ftdi	# FTDI chips
%bcond_without	jaylink	# J-Link chips

%ifarch %{ix86} %{x8664} x32
%define		with_port_io	1
%endif
#
Summary:	Tool Flashing your BIOS from the Unix/Linux command line
Summary(pl.UTF-8):	Narzędzie do aktualizacji BIOS-u z linii poleceń Uniksa/Linuksa
Name:		flashrom
Version:	1.3.0
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
# Source0-md5:	dd2727f8fa05a4517689ca4f9d87e600
Patch0:		x32.patch
URL:		https://www.flashrom.org/Flashrom
%{?with_apidocs:BuildRequires:	doxygen}
%{?with_ftdi:BuildRequires:	libftdi1-devel >= 1.0}
%{?with_jaylink:BuildRequires:	libjaylink-devel}
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pciutils-devel
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
ExclusiveArch:	%{ix86} %{x8664} x32 mips ppc ppc64 sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
flashrom is a utility for identifying, reading, writing, verifying and
erasing flash chips. It's often used to flash BIOS / EFI / coreboot /
firmware images.
 - Supports more than 470 flash chips, 291 chipsets, 500 mainboards,
   79 PCI devices, 17 USB devices and various parallel/serial port
   programmers.
 - Supports parallel, LPC, FWH and SPI flash interfaces and various
   chip packages (DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32, TSOP40,
  TSOP48, BGA and more)
 - No physical access needed, root access is sufficient.
 - No bootable floppy disk, bootable CD-ROM or other media needed.
 - No keyboard or monitor needed. Simply reflash remotely via SSH.
 - No instant reboot needed. Reflash your chip in a running system,
   verify it, be happy. The new firmware will be present next time you
   boot.
 - Crossflashing and hotflashing is possible as long as the flash chips
   are electrically and logically compatible (same protocol). Great for
   recovery.
 - Scriptability. Reflash a whole pool of identical machines at the
   same time from the command line. It is recommended to check flashrom
   output and error codes.
 - Speed. flashrom is often much faster than most vendor flash tools.
 - Portability. Supports DOS, Linux, FreeBSD (including
   Debian/kFreeBSD), NetBSD, OpenBSD, DragonFly BSD, Solaris, Mac OS
   X, and other Unix-like OSes, as well as GNU Hurd.

%description -l pl.UTF-8
flashrom to narzędzie do identyfikacji, odczytu, zapisu, weryfikacji i
kasowania układów flash. Jest często używany do programowania obrazów
BIOS-u / EFI / coreboot / firmware'u.
 - Obsługuje ponad 470 układów flash, 291 chipsetów, 500 płyt głównych,
   79 urządzeń PCI, 17 urządzeń USB i różne programatory podłączane
   przez port równoległy/szeregowy.
 - Wspiera układy flash równoległe, LPC, FWH i SPI o różnych
   obudowach/wyprowadzeniach (DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32,
   TSOP40, TSOP48, BGA i inne)
 - Nie wymaga fizycznego dostępu, wystarczy dostęp do konta roota.
 - Nie potrzebuje bootowalnej dyskietki, rozruchowego dysku CD-ROM lub
   innych nośników.
 - Nie jest wymagana klawiatura ani monitor. Wystarczy przeprogramować
   zdalnie poprzez SSH.
 - Nie ma potrzeby ponownego uruchamiania komputera. Wystarczy
   przeprogramować układ w uruchomionym systemie, zweryfikować i być
   szczęśliwym. Nowy firmware będzie dostępny po następnym
   uruchomieniu.
 - Crossflashing i hotflashing są możliwe na tyle, na ile układy flash
   są elektrycznie i logicznie kompatybilne (ten sam protokół). Jest to
   świetna metoda do przywracania sprzętu ze źle zaprogramowanym
   firmwarem/BIOS-em.
 - Pozwala na tworzenie skryptów do wielokrotnego programowania.
   Programowanie identycznych maszyn w tym samym czasie z wiersza
   poleceń. Zaleca się sprawdzanie komunikatów programu flashrom i
   kodów błędów.
 - Szybkość. flashrom jest często znacznie szybszy niż większość
   sprzedawanych narzędzi do flashowania.
 - Przenośność. Obsługuje systemy DOS, Linux, FreeBSD (w tym
   Debian/kFreeBSD), Dragonfly BSD, Solaris, Mac OS X oraz inne
   systemy operacyjne oparte na Uniksie, a także GNU Hurd.

%package -n libflashrom
Summary:	Flash ROM programming library
Summary(pl.UTF-8):	Biblioteka do programowania pamięci Flash ROM
Group:		Libraries

%description -n libflashrom
Flash ROM programming library.

%description -n libflashrom -l pl.UTF-8
Biblioteka do programowania pamięci Flash ROM.

%package -n libflashrom-devel
Summary:	Header files for libflashrom library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libflashrom
Group:		Development/Libraries
Requires:	libflashrom = %{version}-%{release}

%description -n libflashrom-devel
Header files for libflashrom library.

%description -n libflashrom-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libflashrom.

%package -n libflashrom-static
Summary:	Static libflashrom library
Summary(pl.UTF-8):	Statyczna biblioteka libflashrom
Group:		Development/Libraries
Requires:	libflashrom-devel = %{version}-%{release}

%description -n libflashrom-static
Static libflashrom library.

%description -n libflashrom-static -l pl.UTF-8
Statyczna biblioteka libflashrom.

%package -n libflashrom-apidocs
Summary:	API documentation for libflashrom library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libflashrom
Group:		Documentation
BuildArch:	noarch

%description -n libflashrom-apidocs
API documentation for libflashrom library.

%description -n libflashrom-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libflashrom.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1

%build
%meson build \
	-Dprogrammer=group_i2c,group_pci,group_serial,group_usb%{?with_ftdi:,group_ftdi}%{?with_jaylink:,group_jlink},internal,linux_mtd,linux_spi%{?with_port_io:,rayer_spi}

%ninja_build -C build

%if %{with apidocs}
doxygen
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man8

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libflashrom -p /sbin/ldconfig
%postun	-n libflashrom -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README Documentation/*.txt
%attr(755,root,root) %{_sbindir}/flashrom
%{_mandir}/man8/flashrom.8*

%files -n libflashrom
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflashrom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflashrom.so.1

%files -n libflashrom-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflashrom.so
%{_includedir}/libflashrom.h
%{_pkgconfigdir}/flashrom.pc

%files -n libflashrom-static
%defattr(644,root,root,755)
%{_libdir}/libflashrom.a

%if %{with apidocs}
%files -n libflashrom-apidocs
%defattr(644,root,root,755)
%doc libflashrom-doc/html/{search,*.css,*.html,*.js,*.png}
%endif
