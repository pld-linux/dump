Summary:	Programs for backing up and restoring filesystems
Summary(de):	Dump/Restore-Backup-System
Summary(es):	Sistema de copia de seguridad dump/restore
Summary(fr):	syst�me de sauvegarde dump/restore
Summary(pl):	Programy do wykonywania kopii bezpiecze�stwa plik�w
Summary(pt_BR):	Sistema de backup dump/restore
Summary(ru):	��������� ��� ���������� ����������� � �������������� �������� ������
Summary(tr):	dump/restore yedekleme sistemi
Summary(uk):	�������� ��� ���������� ��Ц������ �� צ��������� �������� ������
Name:		dump
Version:	0.4b40
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/dump/%{name}-%{version}.tar.gz
# Source0-md5:	cc8c5f0dc6ac489a495404bce656309f
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-llh.patch
URL:		http://dump.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	openssl-devel >= 0.9.7a
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
Sie k�nnen mit dump und restore verschiedene Verfahren zum Sichern von
extended 2 (ext2)-Partitionen ausf�hren.

%description -l es
Dump y restore pueden ser usados para hacer copias de seguridad en
particiones ext2 de varias maneras diferentes.

%description -l fr
dupm et restore servent � sauvegarder des partitions ext2 de plusieurs
fa�ons possibles

%description -l pl
Pakiet dump zawiera programy dump i restore. Dump sprawdza pliki w
systemie plikowym i okre�la kt�re powinny by� zesk�adowane w kopii
bezpiecze�stwa a nast�pnie kopiuje te pliki na dysk, ta�m�
magnetyczn� lub inny no�nik. Polecenie restore wykonuje odwrotn�
operacj� i s�u�y do odtwarzania plik�w z kopii bezpiecze�stwa. Program
restore umo�liwia odtwarzanie ca�ego archiwum, a tak�e wybranych
plik�w i katalog�w.

%description -l pt_BR
o dump e o restore podem ser usados para fazer backup em parti��es
ext2 de v�rias maneiras diferentes.

%description -l ru
����� dump �������� dump � restore. Dump ������������� ����� �
�������� �������, ���������� ����� �� ��� ��������� � ���������
����������� � �������� ��� ����� �� ��������� ����, ����� ��� ������
��������. ������� restore ��������� �������� ������� - ��� �����
������������ ��� �������� ������� �� ��������� �����. �����������
��������������� ��������� ����� ����� ������������� �� ������ �����.
����� �� ������ ��� ��������� ��������� ����� ����� ���� �������������
��������� ����� � ������� ���������.

%description -l tr
dump, ext2 b�l�mlerini birka� de�i�ik �ekilde yedeklemek i�in
kullan�l�r. restore ise dump ile al�nan yedekleri geri y�kleyen
programd�r.

%description -l uk
����� dump ͦ����� dump �� restore. Dump ��������� ����� � �����צ�
�����ͦ, ��Ҧ�դ �˦ � ��� Ц�������� ���������� ��Ц������ �� ��Ц��
æ ����� �� ���������� ����, ��Ҧ��� ��� ����� ��Ӧ�. ������� restore
�����դ �������� ����æ� - ���� ���� צ������� ��� ������� ������� �
�������ϧ ��Ц�. ������Φ ������������Φ ������Φ ��Ц� ������
����������� �� ����� ��Ц�. ����� � ����ϧ ��� �������ϧ �������ϧ
��Ц� ������ ���� צ������Φ ����ͦ ����� �� ������ ������Ǧ�.

%package -n rmt
Summary:	Provides certain programs with access to remote tape devices
Summary(de):	Entfernter Zugriff (Netzwerk) auf Magnetbandger�te
Summary(es):	Acceso a dispositivo de cinta remoto (en red)
Summary(fr):	Acc�s distant (r�seau) � un p�riph�rique bande
Summary(pl):	Program do zdalnego dost�pu do nap�d�w ta�m magnetycznych
Summary(pt_BR):	Acesso a dispositivo de fita remoto (em rede)
Summary(ru):	��������� ��� ������� � ��������� ��������� �����������
Summary(tr):	Uzak teyp s�r�c�lerine eri�im arac�
Summary(uk):	�������� ��� ������� �� צ�������� ��Ҧ������ ������ϧ�
Group:		Applications/System

%description -n rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup) and tar (an archiving program).

%description -n rmt -l de
rmt stellt Remote-Access zu Bandger�ten f�r Programme wie Dump,
Restore und tar bereit.

%description -n rmt -l es
rmt provee acceso remoto a dispositivos de cinta para programas como
dump, restore y tar.

%description -n rmt -l fr
rmt offre un acc�s distant aux p�riph�riques bandes pour des
programmes comme dump, restore et tar.

%description -n rmt -l pl
Program rmt umo�liwia zdalny dost�p do nap�d�w ta�m magnetycznych dla
program�w takich jak dump, restore czy tar.

%description -n rmt -l pt_BR
rmt prov� acesso remoto a dispositivos de fita para programas como
dump, restore e tar.

%description -n rmt -l ru
������� rmt ������������� ��������� ������ � ��������� �����������
��������� ����������, �������� dump, restore, tar.

%description -n rmt -l tr
rmt program�, dump, restore ve tar gibi programlar i�in teyp
ayg�tlar�na uzaktan eri�im sa�lar.

%description -n rmt -l uk
���̦�� rmt ����� צ�������� ������ �� ��Ҧ������ ������ϧ� ������
���������, ��������� dump, restore, tar.

%package -n ermt
Summary:	Encrypting version of rmt
Summary(pl):	Wersja rmt z szyfrowaniem
Group:		Applications/System
Requires:	openssl >= 0.9.7a

%description -n ermt
ermt is an encrypting version of rmt.

%description -n ermt -l pl
ermt to wersja programu rmt z szyfrowaniem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
MYNAME=`id -ru` \
MYGRP=`id -rg`; \
%configure \
	--enable-ermt \
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
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_mandir}/man8,/usr/sbin}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install rmt/ermt $RPM_BUILD_ROOT/usr/sbin

> $RPM_BUILD_ROOT%{_sysconfdir}/dumpdates

ln -sf %{_sbindir}/rmt $RPM_BUILD_ROOT%{_sysconfdir}/rmt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT KNOWNBUGS README THANKS TODO CHANGES
%attr(664,root,disk) %verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/dumpdates
%attr(755,root,root) %{_sbindir}/*dump
%attr(755,root,root) %{_sbindir}/*restore
%{_mandir}/man8/*dump.8*
%{_mandir}/man8/*restore.8*

%files -n rmt
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rmt
%attr(755,root,root) %{_sysconfdir}/rmt
%{_mandir}/man8/rmt.8*

%files -n ermt
%defattr(644,root,root,755)
%attr(755,root,root) /usr/sbin/ermt
