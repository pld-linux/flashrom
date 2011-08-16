Summary:	Tool Flashing your BIOS from the Unix/Linux command line
Summary(pl.UTF-8):	Narzędzie do aktualizacji BIOS z lini poleceń Unix/Linux
Name:		flashrom
Version:	0.9.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://download.flashrom.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	d739a91aece12cc1e622038bb199541c
URL:		http://www.coreboot.org/Flashrom
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
flashrom is a utility for identifying, reading, writing, verifying and
erasing flash chips. It's often used to flash BIOS / EFI / coreboot /
firmware images.
    - Supports more than 160 flash chips, 75 chipsets, 100 mainboards, and
      10 PCI devices which can be used as external programmers.
    - Supports parallel, LPC, FWH and SPI flash interfaces and various
      chip packages (DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32, TSOP40 and
      more)
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
    - Portability. Supports Linux, FreeBSD, DragonFly BSD, Solaris, Mac OS
      X, and other Unix-like OSes.

%description -l pl.UTF-8
flashrom to narzędzie do identyfikacji, odczytu, zapisu, weryfikacji i
kasowania układów flash. Jest często używany do programowania BIOS /
EFI / coreboot / firmware z pliku.
    - Obsługuje ponad 160 chipów flash, 75 chipsetów, 100 płyt głównych i
      10 urządzeń PCI, które mogą być wykorzystane jako zewnętrzne
      programatory.
    - Wspiera układy flash równoległe, LPC, SPI i FWH o różnych
      obudowach/wyprowadzeniach (DIP32, PLCC32, DIP8, SO8/SOIC8, TSOP32,
      TSOP40 i inne)
    - Nie potrzeba fizycznego dostępu, wystarczy dostęp do konta root.
    - Nie potrzebuje bootowalnej dyskietki, rozruchowego dysku CD-ROM lub
      innych nośników.
    - Nie potrzebne są klawiatura czy monitor. Wystarczy przeprogramować
      zdalnie poprzez SSH.
    - Nie ma potrzeby ponownego uruchamiania komputera. Zaprogramuj swój
      chip w uruchomionym systemie, zweryfikuj, bądź szczęśliwy. Nowy
      firmware będzie dostępny przy następnym bootowaniu.
    - Crossflashing i hotflashing jest możliwe tak długo, jak układy flash
      są elektrycznie i logicznie kompatybilne (ten sam protokół). Świetna
      metoda do przywracania sprzętu z źle zaprogramowanym firmware/BIOS.
    - Możliwość tworzenia skryptów do wielokrotnego programowania.
      Programowanie identycznych maszyn w tym samym czasie z wiersza
      poleceń. Zaleca się sprawdzanie komunikatów programu flashrom i kodów
      błędów.
    - Szybkość. flashrom jest często znacznie szybszy niż większość
      sprzedawanych narzędzi do flashowania.
    - Wszechstronność. Wspiera Linux, FreeBSD, Dragonfly BSD, Solaris, Mac
      OS X i inne systemy operacyjne oparte na Unix.

%prep
%setup -q

%build
%{__make} \
	CC='%{__cc}' \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}
install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYING
%attr(755,root,root) %{_sbindir}/flashrom
%{_mandir}/man8/flashrom.8*
