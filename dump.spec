Summary:	Programs for backing up and restoring filesystems
Summary(de):	Dump/Restore-Backup-System
Summary(es):	Sistema de copia de seguridad dump/restore
Summary(fr):	système de sauvegarde dump/restore
Summary(pl):	Programy do wykonywania kopii bezpieczeñstwa plików
Summary(pt_BR):	Sistema de backup dump/restore
Summary(ru):	ðÒÏÇÒÁÍÍÙ ÄÌÑ ÒÅÚÅÒ×ÎÏÇÏ ËÏÐÉÒÏ×ÁÎÉÑ É ×ÏÓÓÔÁÎÏ×ÌÅÎÉÑ ÆÁÊÌÏ×ÙÈ ÓÉÓÔÅÍ
Summary(tr):	dump/restore yedekleme sistemi
Summary(uk):	ðÒÏÇÒÁÍÉ ÄÌÑ ÒÅÚÅÒ×ÎÏÇÏ ËÏÐ¦À×ÁÎÎÑ ÔÁ ×¦ÄÎÏ×ÌÅÎÎÑ ÆÁÊÌÏ×ÉÈ ÓÉÓÔÅÍ
Name:		dump
Version:	0.4b34
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/dump/%{name}-%{version}.tar.gz
# Source0-md5:	b78f91cede9c2b383c46905c688845c6
Patch0:		%{name}-sparc.patch
Patch1:		%{name}-autoconf.patch
Patch2:		%{name}-use_ncurses.patch
URL:		http://dump.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	e2fsprogs-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
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

%description -l de
Sie können mit dump und restore verschiedene Verfahren zum Sichern von
extended 2 (ext2)-Partitionen ausführen.

%description -l es
Dump y restore pueden ser usados para hacer copias de seguridad en
particiones ext2 de varias maneras diferentes.

%description -l fr
dupm et restore servent à sauvegarder des partitions ext2 de plusieurs
façons possibles

%description -l pl
Pakiet dump zawiera programy dump i restore. Dump sprawdza pliki w
systemie plikowym i okre¶la które powinny byæ zesk³adowane w kopii
bezpieczeñstwa an nastêpnie kopiuje te pliki na dysk, ta¶mê
magnetyczna lub inny nosnik. Polecenie restore wykonujê odwrotna
operacjê i s³u¿y do odtwarzania plików z kopii bezpieczeñstwa. Program
restore umo¿liwia odtwarzanie ca³ego archiwum, a tak¿e wybranych
plików i katalogów.

%description -l pt_BR
o dump e o restore podem ser usados para fazer backup em partições
ext2 de várias maneiras diferentes.

%description -l ru
ðÁËÅÔ dump ÓÏÄÅÒÖÉÔ dump É restore. Dump ÐÒÏÓÍÁÔÒÉ×ÁÅÔ ÆÁÊÌÙ ×
ÆÁÊÌÏ×ÏÊ ÓÉÓÔÅÍÅ, ÏÐÒÅÄÅÌÑÅÔ ËÁËÉÅ ÉÚ ÎÉÈ ÎÕÖÄÁÀÔÓÑ × ÒÅÚÅÒ×ÎÏÍ
ËÏÐÉÒÏ×ÁÎÉÉ É ËÏÐÉÒÕÅÔ ÜÔÉ ÆÁÊÌÙ ÎÁ ÕËÁÚÁÎÎÙÊ ÄÉÓË, ÌÅÎÔÕ ÉÌÉ ÄÒÕÇÏÊ
ÎÏÓÉÔÅÌØ. ëÏÍÁÎÄÁ restore ×ÙÐÏÌÎÑÅÔ ÏÂÒÁÔÎÕÀ ÆÕÎËÃÉÀ - ÏÎÁ ÍÏÖÅÔ
×ÏÓÓÔÁÎÏ×ÉÔØ ×ÓÀ ÆÁÊÌÏ×ÕÀ ÓÉÓÔÅÍÕ ÉÚ ÒÅÚÅÒ×ÎÏÊ ËÏÐÉÉ. ðÏÓÌÅÄÕÀÝÉÅ
ÉÎËÒÅÍÅÎÔÁÌØÎÙÅ ÒÅÚÅÒ×ÎÙÅ ËÏÐÉÉ ÍÏÇÕÔ ÎÁËÌÁÄÙ×ÁÔØÓÑ ÎÁ ÐÏÌÎÕÀ ËÏÐÉÀ.
ôÁËÖÅ ÉÚ ÐÏÌÎÏÊ ÉÌÉ ÞÁÓÔÉÞÎÏÊ ÒÅÚÅÒ×ÎÏÊ ËÏÐÉÉ ÍÏÇÕÔ ÂÙÔØ ×ÏÓÓÔÁÎÏ×ÌÅÎÙ
ÏÔÄÅÌØÎÙÅ ÆÁÊÌÙ É ÄÅÒÅ×ØÑ ËÁÔÁÌÏÇÏ×.

%description -l tr
dump, ext2 bölümlerini birkaç deðiþik þekilde yedeklemek için
kullanýlýr. restore ise dump ile alýnan yedekleri geri yükleyen
programdýr.

%description -l uk
ðÁËÅÔ dump Í¦ÓÔÉÔØ dump ÔÁ restore. Dump ÐÒÏÇÌÑÄÁ¤ ÆÁÊÌÉ Õ ÆÁÊÌÏ×¦Ê
ÓÉÓÔÅÍ¦, ×ÉÒ¦ÛÕ¤ ÑË¦ Ú ÎÉÈ Ð¦ÄÌÑÇÁÀÔØ ÒÅÚÅÒ×ÎÏÍÕ ËÏÐ¦À×ÁÎÎÀ ÔÁ ËÏÐ¦À¤
Ã¦ ÆÁÊÌÉ ÎÁ ×ÉÚÎÁÞÅÎÉÊ ÄÉÓË, ÓÔÒ¦ÞËÕ ÁÂÏ ¦ÎÛÉÊ ÎÏÓ¦Ê. ëÏÍÁÎÄÁ restore
×ÉËÏÎÕ¤ Ú×ÏÒÏÔÎÀ ÆÕÎËÃ¦À - ×ÏÎÁ ÍÏÖÅ ×¦ÄÎÏ×ÉÔÉ ×ÓÀ ÆÁÊÌÏ×Õ ÓÉÓÔÅÍÕ Ú
ÒÅÚÅÒ×ÎÏ§ ËÏÐ¦§. îÁÓÔÕÐÎ¦ ¦ÎËÒÅÍÅÎÔÁÌØÎ¦ ÒÅÚÅÒ×Î¦ ËÏÐ¦§ ÍÏÖÕÔØ
ÎÁËÌÁÄÁÔÉÓÑ ÎÁ ÐÏ×ÎÕ ËÏÐ¦À. ôÁËÏÖ Ú ÐÏ×ÎÏ§ ÁÂÏ ÞÁÓÔËÏ×Ï§ ÒÅÚÅÒ×ÎÏ§
ËÏÐ¦§ ÍÏÖÕÔØ ÂÕÔÉ ×¦ÄÎÏ×ÌÅÎ¦ ÏËÒÅÍ¦ ÆÁÊÌÉ ÔÁ ÄÅÒÅ×Á ËÁÔÁÌÏÇ¦×.

%package -n rmt
Summary:	Provides certain programs with access to remote tape devices
Summary(de):	Entfernter Zugriff (Netzwerk) auf Magnetbandgeräte
Summary(es):	Acceso a dispositivo de cinta remoto (en red)
Summary(fr):	Accès distant (réseau) à un périphérique bande
Summary(pl):	Program do zdalnego dostêpu do napêdów ta¶m magnetycznych
Summary(pt_BR):	Acesso a dispositivo de fita remoto (em rede)
Summary(ru):	ðÒÏÇÒÁÍÍÙ ÄÌÑ ÄÏÓÔÕÐÁ Ë ÕÄÁÌÅÎÎÙÍ ÌÅÎÔÏÞÎÙÍ ÕÓÔÒÏÊÓÔ×ÁÍ
Summary(tr):	Uzak teyp sürücülerine eriþim aracý
Summary(uk):	ðÒÏÇÒÁÍÉ ÄÌÑ ÄÏÓÔÕÐÕ ÄÏ ×¦ÄÄÁÌÅÎÉÈ ÓÔÒ¦ÞËÏ×ÉÈ ÐÒÉÓÔÒÏ§×
Group:		Applications/System

%description -n rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup) and tar (an archiving program).

%description -n rmt -l de
rmt stellt Remote-Access zu Bandgeräten für Programme wie Dump,
Restore und tar bereit.

%description -n rmt -l es
rmt provee acceso remoto a dispositivos de cinta para programas como
dump, restore y tar.

%description -n rmt -l fr
rmt offre un accès distant aux périphériques bandes pour des
programmes comme dump, restore et tar.

%description -n rmt -l pl
Program rmt umo¿liwia zdalny dostêp do napêdów ta¶m magnetycznych dla
programów takich jak dump, restore czy tar.

%description -n rmt -l pt_BR
rmt provê acesso remoto a dispositivos de fita para programas como
dump, restore e tar.

%description -n rmt -l ru
õÔÉÌÉÔÁ rmt ÐÒÅÄÏÓÔÁ×ÌÑÅÔ ÕÄÁÌÅÎÎÙÊ ÄÏÓÔÕÐ Ë ÌÅÎÔÏÞÎÙÍ ÕÓÔÒÏÊÓÔ×ÁÍ
ÎÅËÏÔÏÒÙÍ ÐÒÏÇÒÁÍÍÁÍ, ÎÁÐÒÉÍÅÒ dump, restore, tar.

%description -n rmt -l tr
rmt programý, dump, restore ve tar gibi programlar için teyp
aygýtlarýna uzaktan eriþim saðlar.

%description -n rmt -l uk
õÔÉÌ¦ÔÁ rmt ÎÁÄÁ¤ ×¦ÄÄÁÌÅÎÉÊ ÄÏÓÔÕÐ ÄÏ ÓÔÒ¦ÞËÏ×ÉÈ ÐÒÉÓÔÒÏ§× ÄÅÑËÉÍ
ÐÒÏÇÒÁÍÁÍ, ÎÁÐÒÉËÌÁÄ dump, restore, tar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
MYNAME=`id -ru` \
MYGRP=`id -rg`; \
%configure \
	--enable-rmt \
	--enable-readline \
	--with-ccopts="%{rpmcflags}" \
	--with-ldopts="%{rpmldflags}" \
	--with-binowner=$MYNAME \
	--with-bingrp=$MYGRP \
	--with-binmode=755 \
	--with-manowner=$MYNAME \
	--with-mangrp=$MYGRP \
	--with-manmode=644
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,sbin,%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

> $RPM_BUILD_ROOT%{_sysconfdir}/dumpdates

ln -sf ..%{_sbindir}/rmt $RPM_BUILD_ROOT%{_sysconfdir}/rmt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT KNOWNBUGS README THANKS TODO CHANGES
%attr(664,root, disk) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/dumpdates
%attr(755,root,root) %{_sbindir}/*dump
%attr(755,root,root) %{_sbindir}/*restore
%{_mandir}/man8/*dump.8*
%{_mandir}/man8/*restore.8*

%files -n rmt
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rmt
%attr(755,root,root) %{_sysconfdir}/rmt
%{_mandir}/man8/rmt.8*
