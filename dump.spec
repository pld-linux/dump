Summary:	dump/restore backup system
Summary(de):	Dump/Restore-Backup-System 
Summary(fr):	système de sauvegarde dump/restore
Summary(pl):	System kopii bezpieczeñstwa dump/restore
Summary(tr):	dump/restore yedekleme sistemi
Name:		dump
Version:	0.4b4
Release:	1
Copyright:	UCB
Group:		Utilities/System
Source:		ftp://tsx-11.mit.edu:/pub/linux/packages/ext2fs/%{name}-%{version}.tar.gz
Patch0:		dump-glibc.patch
Patch1:		dump-sparc.patch
Patch2:		dump-kernel.patch
Requires:	rmt
BuildRoot:	/tmp/%{name}-%{version}-root

%description
dump and restore can be used to backup extended 2 (ext2) partitions in
a variety of ways.

%description -l de
Sie können mit dump und restore verschiedene Verfahren zum Sichern 
von extended 2 (ext2)-Partitionen ausführen.

%description -l fr
dupm et restore servent à sauvegarder des partitions ext2 de plusieurs
façons possibles

%description -l pl
Programy dump i restore s³u¿± do tworzenia i odtwarzanie kopii
bezpieczeñstwa partycji z systemem plków ext2.

%description -l tr
dump, ext2 bölümlerini birkaç deðiþik þekilde yedeklemek için kullanýlýr.
restore ise dump ile alýnan yedekleri geri yükleyen programdýr.

%package -n rmt
Summary:	Remote (network) tape device access
Summary(de):	Entfernter Zugriff (Netzwerk) auf Magnetbandgeräte
Summary(fr):	Accès distant (réseau) à un périphérique bande
Summary(pl):	Zdalny dostêp do napêdów ta¶m magnetycznych
Summary(tr):	Uzak teyp sürücülerine eriþim aracý
Group:		Utilities/System

%description -n rmt
rmt provides remote access to tape devices for programs like dump,
restore, and tar.

%description -l de -n rmt
rmt stellt Remote-Access zu Bandgeräten für Programme wie Dump, Restore 
und tar bereit. 

%description -l fr -n rmt
rmt offre un accès distant aux périphériques bandes pour des programmes comme
dump, restore et tar.

%description -l pl -n rmt
Program rmt umo¿liwia zdalny dostêp do napêdów ta¶m magnetycznych
dla programów takich jak dump, restore czy tar

%description -l tr -n rmt
rmt programý, dump, restore ve tar gibi programlar için teyp aygýtlarýna
uzaktan eriþim saðlar.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1

%build
MYNAME=`id -ru` \
MYGRP=`id -rg` \
%configure \
	--enable-rmt \
	--with-ccopts="$RPM_OPT_FLAGS" \
	--with-ldopts="-s" \
	--with-binowner=$MYNAME \
	--with-bingrp=$MYGRP \
	--with-binmode=6755 \
	--with-manowner=$MYNAME \
	--with-mangrp=$MYGRP \
	--with-manmode=644
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,sbin,%{_mandir}/man8}

make BINDIR=$RPM_BUILD_ROOT/sbin MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8 install

> $RPM_BUILD_ROOT/etc/dumpdates

ln -sf dump $RPM_BUILD_ROOT/sbin/rdump
ln -sf restore $RPM_BUILD_ROOT/sbin/rrestore

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/{rdump,rrestore}.8

echo ".so dump.8" > $RPM_BUILD_ROOT%{_mandir}/man8/rdump.8
echo ".so restore.8" > $RPM_BUILD_ROOT%{_mandir}/man8/rrestore.8

gzip -9nf COPYRIGHT KNOWNBUGS THANKS CHANGES dump-0.3.announce \
	$RPM_BUILD_ROOT%{_mandir}/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYRIGHT,KNOWNBUGS,THANKS,CHANGES,dump-0.3.announce}.gz
%attr(664,root, disk) %verify(not md5 mtime size) %config(noreplace) /etc/dumpdates
%attr(6755,root,root) /sbin/dump
%attr(755,root,root) /sbin/rdump
%attr(6755,root,root) /sbin/restore
%attr(755,root,root) /sbin/rrestore
%{_mandir}/man8/dump.8.gz
%{_mandir}/man8/rdump.8.gz
%{_mandir}/man8/restore.8.gz
%{_mandir}/man8/rrestore.8.gz

%files -n rmt
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/rmt
%{_mandir}/man8/rmt.8.gz
