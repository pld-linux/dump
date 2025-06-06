#
# Conditional build:
%bcond_with	kerberos	# Kerberos support (requires krcmd function)

Summary:	Programs for backing up and restoring filesystems
Summary(de.UTF-8):	Dump/Restore-Backup-System
Summary(es.UTF-8):	Sistema de copia de seguridad dump/restore
Summary(fr.UTF-8):	système de sauvegarde dump/restore
Summary(pl.UTF-8):	Programy do wykonywania kopii bezpieczeństwa plików
Summary(pt_BR.UTF-8):	Sistema de backup dump/restore
Summary(ru.UTF-8):	Программы для резервного копирования и восстановления файловых систем
Summary(tr.UTF-8):	dump/restore yedekleme sistemi
Summary(uk.UTF-8):	Програми для резервного копіювання та відновлення файлових систем
Name:		dump
Version:	0.4b51
Release:	1
License:	BSD
Group:		Applications/System
Source0:	https://downloads.sourceforge.net/dump/%{name}-%{version}.tar.gz
# Source0-md5:	9d1c8e4c6ffdf729e359737d2360040c
Patch0:		%{name}-ext2fs.patch
URL:		https://dump.sourceforge.net/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel >= 1.20.0
BuildRequires:	libblkid-devel
BuildRequires:	libcom_err-devel
BuildRequires:	libselinux-devel
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	lzo-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.7a
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	zlib-devel
Requires:	e2fsprogs-libs >= 1.20.0
Requires:	rmt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
The dump package contains both dump and restore. Dump examines files
in a filesystem, determines which ones need to be backed up, and
copies those files to a specified disk, tape or other storage medium.
The restore command performs the inverse function of dump; it can
restore a full backup of a filesystem. Subsequent incremental backups
can then be layered on top of the full backup. Single files and
directory subtrees may also be restored from full or partial backups.

%description -l de.UTF-8
Sie können mit dump und restore verschiedene Verfahren zum Sichern von
extended 2 (ext2)-Partitionen ausführen.

%description -l es.UTF-8
Dump y restore pueden ser usados para hacer copias de seguridad en
particiones ext2 de varias maneras diferentes.

%description -l fr.UTF-8
dupm et restore servent à sauvegarder des partitions ext2 de plusieurs
façons possibles

%description -l pl.UTF-8
Pakiet dump zawiera programy dump i restore. Dump sprawdza pliki w
systemie plikowym i określa które powinny być zeskładowane w kopii
bezpieczeństwa a następnie kopiuje te pliki na dysk, taśmę magnetyczną
lub inny nośnik. Polecenie restore wykonuje odwrotną operację i służy
do odtwarzania plików z kopii bezpieczeństwa. Program restore
umożliwia odtwarzanie całego archiwum, a także wybranych plików i
katalogów.

%description -l pt_BR.UTF-8
o dump e o restore podem ser usados para fazer backup em partições
ext2 de várias maneiras diferentes.

%description -l ru.UTF-8
Пакет dump содержит dump и restore. Dump просматривает файлы в
файловой системе, определяет какие из них нуждаются в резервном
копировании и копирует эти файлы на указанный диск, ленту или другой
носитель. Команда restore выполняет обратную функцию - она может
восстановить всю файловую систему из резервной копии. Последующие
инкрементальные резервные копии могут накладываться на полную копию.
Также из полной или частичной резервной копии могут быть восстановлены
отдельные файлы и деревья каталогов.

%description -l tr.UTF-8
dump, ext2 bölümlerini birkaç değişik şekilde yedeklemek için
kullanılır. restore ise dump ile alınan yedekleri geri yükleyen
programdır.

%description -l uk.UTF-8
Пакет dump містить dump та restore. Dump проглядає файли у файловій
системі, вирішує які з них підлягають резервному копіюванню та копіює
ці файли на визначений диск, стрічку або інший носій. Команда restore
виконує зворотню функцію - вона може відновити всю файлову систему з
резервної копії. Наступні інкрементальні резервні копії можуть
накладатися на повну копію. Також з повної або часткової резервної
копії можуть бути відновлені окремі файли та дерева каталогів.

%package -n rmt
Summary:	Provides certain programs with access to remote tape devices
Summary(de.UTF-8):	Entfernter Zugriff (Netzwerk) auf Magnetbandgeräte
Summary(es.UTF-8):	Acceso a dispositivo de cinta remoto (en red)
Summary(fr.UTF-8):	Accès distant (réseau) à un périphérique bande
Summary(pl.UTF-8):	Program do zdalnego dostępu do napędów taśm magnetycznych
Summary(pt_BR.UTF-8):	Acesso a dispositivo de fita remoto (em rede)
Summary(ru.UTF-8):	Программы для доступа к удаленным ленточным устройствам
Summary(tr.UTF-8):	Uzak teyp sürücülerine erişim aracı
Summary(uk.UTF-8):	Програми для доступу до віддалених стрічкових пристроїв
Group:		Applications/System

%description -n rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup) and tar (an archiving program).

%description -n rmt -l de.UTF-8
rmt stellt Remote-Access zu Bandgeräten für Programme wie Dump,
Restore und tar bereit.

%description -n rmt -l es.UTF-8
rmt provee acceso remoto a dispositivos de cinta para programas como
dump, restore y tar.

%description -n rmt -l fr.UTF-8
rmt offre un accès distant aux périphériques bandes pour des
programmes comme dump, restore et tar.

%description -n rmt -l pl.UTF-8
Program rmt umożliwia zdalny dostęp do napędów taśm magnetycznych dla
programów takich jak dump, restore czy tar.

%description -n rmt -l pt_BR.UTF-8
rmt provê acesso remoto a dispositivos de fita para programas como
dump, restore e tar.

%description -n rmt -l ru.UTF-8
Утилита rmt предоставляет удаленный доступ к ленточным устройствам
некоторым программам, например dump, restore, tar.

%description -n rmt -l tr.UTF-8
rmt programı, dump, restore ve tar gibi programlar için teyp
aygıtlarına uzaktan erişim sağlar.

%description -n rmt -l uk.UTF-8
Утиліта rmt надає віддалений доступ до стрічкових пристроїв деяким
програмам, наприклад dump, restore, tar.

%package -n ermt
Summary:	Encrypting version of rmt
Summary(pl.UTF-8):	Wersja rmt z szyfrowaniem
Group:		Applications/System
Requires:	openssl >= 0.9.7a

%description -n ermt
ermt is an encrypting version of rmt.

%description -n ermt -l pl.UTF-8
ermt to wersja programu rmt z szyfrowaniem.

%prep
%setup -q
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ermt \
	%{?with_kerberos:--enable-kerberos} \
	--enable-rmt \
	--enable-readline \
	--enable-selinux \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

> $RPM_BUILD_ROOT%{_sysconfdir}/dumpdates

ln -sfr $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}/rmt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KNOWNBUGS MAINTAINERS NEWS README TODO
%attr(664,root,disk) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/dumpdates
%attr(755,root,root) %{_sbindir}/dump
%attr(755,root,root) %{_sbindir}/rdump
%attr(755,root,root) %{_sbindir}/restore
%attr(755,root,root) %{_sbindir}/rrestore
%{_mandir}/man8/dump.8*
%{_mandir}/man8/rdump.8*
%{_mandir}/man8/restore.8*
%{_mandir}/man8/rrestore.8*

%files -n rmt
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rmt
%attr(755,root,root) %{_sysconfdir}/rmt
%{_mandir}/man8/rmt.8*

%files -n ermt
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ermt
