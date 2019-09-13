#
# Conditional build:
%bcond_without	ftdi	# FTDI chips
%bcond_without	jaylink	# J-Link chips
#
Summary:	Tool Flashing your BIOS from the Unix/Linux command line
Summary(pl.UTF-8):	Narzędzie do aktualizacji BIOS-u z linii poleceń Uniksa/Linuksa
Name:		flashrom
Version:	1.1
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://download.flashrom.org/releases/%{name}-v%{version}.tar.bz2
# Source0-md5:	91bab6c072e38a493bb4eb673e4fe0d6
URL:		https://www.flashrom.org/Flashrom
%{?with_ftdi:BuildRequires:	libftdi1-devel >= 1.0}
%{?with_jaylink:BuildRequires:	libjaylink-devel}
# libusb 0.1 still needed for PICKIT2_SPI dongle
BuildRequires:	libusb-compat-devel >= 0.1
BuildRequires:	libusb-devel >= 1.0
BuildRequires:	pciutils-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
ExclusiveArch:	%{ix86} %{x8664} x32 mips ppc ppc64 sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

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

%prep
%setup -q -n %{name}-v%{version}

%build
%{__make} \
	CC='%{__cc}' \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	%{!?with_ftdi:CONFIG_FT2232_SPI=no} \
	%{?with_jaylink:CONFIG_JLINK_SPI=yes}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/flashrom
%{_mandir}/man8/flashrom.8*
