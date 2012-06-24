Summary:     dump/restore backup system
Summary(de): Dump/Restore-Backup-System 
Summary(fr): syst�me de sauvegarde dump/restore
Summary(pl): System kopii bezpiecze�stwa dump/restore
Summary(tr): dump/restore yedekleme sistemi
Name:        dump
Version:     0.3
Release:     14
Copyright:   UCB
Group:       Utilities/System
Source:      ftp://tsx-11.mit.edu:/pub/linux/packages/ext2fs/%{name}-%{version}.tar.gz
Patch:       dump-config.patch
Patch1:      dump-0.3-types.patch
Patch2:      dump-0.3-glibc.patch
Patch3:      dump-0.3-sparc.patch
Patch4:      dump-0.3-kernel.patch
Requires:    rmt
BuildRoot:   /tmp/%{name}-%{version}-root

%description
dump and restore can be used to backup extended 2 (ext2) partitions in
a variety of ways.

%description -l de
Sie k�nnen mit dump und restore verschiedene Verfahren zum Sichern 
von extended 2 (ext2)-Partitionen ausf�hren.

%description -l fr
dupm et restore servent � sauvegarder des partitions ext2 de plusieurs
fa�ons possibles

%description -l pl
Programy dump i restore s�u�� do tworzenia i odtwarzanie kopii
bezpiecze�stwa partycji z systemem plk�w ext2.

%description -l tr
dump, ext2 b�l�mlerini birka� de�i�ik �ekilde yedeklemek i�in kullan�l�r.
restore ise dump ile al�nan yedekleri geri y�kleyen programd�r.

%package -n rmt
Summary:     Remote (network) tape device access
Summary(de): Entfernter Zugriff (Netzwerk) auf Magnetbandger�te
Summary(fr): Acc�s distant (r�seau) � un p�riph�rique bande
Summary(pl): Zdalny dost�p do nap�d�w ta�m magnetycznych
Summary(tr): Uzak teyp s�r�c�lerine eri�im arac�
Group:       Utilities/System

%description -n rmt
rmt provides remote access to tape devices for programs like dump,
restore, and tar.

%description -l de -n rmt
rmt stellt Remote-Access zu Bandger�ten f�r Programme wie Dump, Restore 
und tar bereit. 

%description -l fr -n rmt
rmt offre un acc�s distant aux p�riph�riques bandes pour des programmes comme
dump, restore et tar.

%description -l pl -n rmt
Program rmt umo�liwia zdalny dost�p do nap�d�w ta�m magnetycznych
dla program�w takich jak dump, restore czy tar

%description -l tr -n rmt
rmt program�, dump, restore ve tar gibi programlar i�in teyp ayg�tlar�na
uzaktan eri�im sa�lar.

%prep
%setup -q
%patch0 -p0 -b .config 
%patch1 -p1 -b .types
%patch2 -p1 -b .glibc
#%patch3 -p1 -b .sparc
%patch4 -p1 -b .kernel

%build
make OPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,sbin,usr/man/man8}

MYNAME=`id -u`
MYGRP=`id -g`
make BINDIR=$RPM_BUILD_ROOT/sbin MANDIR=$RPM_BUILD_ROOT%{_mandir}/man8 \
BINOWN=$MYNAME BINGRP=$MYGRP MANOWN=$MYNAME MANGRP=$MYGRP install

> $RPM_BUILD_ROOT/etc/dumpdates

ln -sf dump $RPM_BUILD_ROOT/sbin/rdump
ln -sf restore $RPM_BUILD_ROOT/sbin/rrestore

echo ".so dump.8" > $RPM_BUILD_ROOT%{_mandir}/man8/rdump.8
echo ".so restore.8" > $RPM_BUILD_ROOT%{_mandir}/man8/rrestore.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root, 0755)
%doc COPYRIGHT KNOWNBUGS THANKS CHANGES dump-0.3.announce
%attr(0664,root, disk)	%verify(not md5 mtime size) %config(noreplace) /etc/dumpdates
%attr(6755,root,root) /sbin/dump
%attr(0755,root,root) /sbin/rdump
%attr(6755,root,root) /sbin/restore
%attr(0755,root,root) /sbin/rrestore
%attr(0755,root,  man) %{_mandir}/man8/dump.8
%attr(0755,root,  man) %{_mandir}/man8/rdump.8
%attr(0755,root,  man) %{_mandir}/man8/restore.8
%attr(0755,root,  man) %{_mandir}/man8/rrestore.8

%files -n rmt
%attr(0755,root,root) /sbin/rmt
%attr(0755,root,  man) %{_mandir}/man8/rmt.8 

%changelog
* Tue Sep 15 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3-14]
- added %verify rules to /etc/dumdates and added noreplace %config
  paramerer,
- rdump(8) and rrestore(8) man pagea are now maked as nroff include to
  dump(8) and restore(8) instead making sym link to dump.8 and restore.8
  (this allow compress man pages in future).

* Sat Sep 12 1998 Konrad St�pie� <konrad@interdata.com.pl>
- added ability to build from non-root,
- added %attr macros,
- added pl translation,
- removed link to rmt in /etc.

* Tue Jul 14 1998 Jeff Johnson <jbj@redhat.com>
- add build root.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for resolving linux/types.h and sys/types.h conflicts

* Wed Dec 31 1997 Erik Troan <ewt@redhat.com>
- added prototype of llseek() so dump would work on large partitions

* Thu Oct 30 1997 Donnie Barnes <djb@redhat.com>
- made all symlinks relative instead of absolute

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- Moved rmt to its own package.

* Tue Feb 11 1997 Michael Fulbright <msf@redhat.com>
- Added endian cleanups for SPARC

* Fri Feb 07 1997 Michael K. Johnson <johnsonm@redhat.com> 
- Made /etc/dumpdates writeable by group disk.
