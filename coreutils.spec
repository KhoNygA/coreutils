
# _with_selinux - build with selinux support

# TODO:
# - see Source 8

Summary:	GNU Core-utils - basic command line utilities
Summary(pl):	GNU Core-utils - podstawowe narz�dzia dzia�aj�ce z linii polece�
Name:		coreutils
Version:	5.0
Release:	0.10
License:	GPL
Group:		Applications/System
# devel versions:
#Source0:	ftp://alpha.gnu.org/gnu/fetish/%{name}-%{version}.tar.bz2
# final versions:
Source0:	ftp://ftp.gnu.org/gnu/coreutils/%{name}-%{version}.tar.bz2
# Source0-md5: 94e5558ee2a65723d4840bfde2d323f0
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/fileutils-non-english-man-pages.tar.bz2
# Source1-md5: def2f215ac4832e3de0889f06d8543ca
Source2:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/sh-utils-non-english-man-pages.tar.bz2
# Source2-md5: 9c5fd04cad759fe8d2a70d755679cbc9
Source3:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/textutils-non-english-man-pages.tar.bz2
# Source3-md5: 4331303b69dd3b74b7c9be9fa3905557
Source4:	DIR_COLORS
Source5:	fileutils.sh
Source6:	fileutils.csh
Source7:	su.pamd
# to be put in Source1
Source8:	stat.1.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-pam.patch
Patch2:		%{name}-getgid.patch
Patch3:		%{name}-utmp.patch
Patch4:		%{name}-su-paths.patch
Patch5:		%{name}-uname-cpuinfo.patch
Patch6:		%{name}-date-man.patch
Patch7:		%{name}-mem.patch
Patch8:		%{name}-install-C.patch
Patch9:		%{name}-po.patch
Patch10:	%{name}-no-nb.patch
# based on http://acl.bestbits.at/current/diff/fileutils-4.1.8acl-0.8.25.diff.gz
Patch11:	%{name}-acl-0.8.25.patch
Patch12:	%{name}-selinux.patch
BuildRequires:	acl-devel
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake >= 1.7
BuildRequires:	gettext-devel >= 0.11.5
BuildRequires:	help2man
BuildRequires:	pam-devel
BuildRequires:	texinfo >= 4.2
%{?_with_selinux:BuildRequires:	selinux-libs-devel}
Provides:	fileutils
Provides:	sh-utils
Provides:	stat
Provides:	textutils
Obsoletes:	fileutils
Obsoletes:	sh-utils
Obsoletes:	stat
Obsoletes:	textutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are the GNU core utilities.  This package is the union of
the GNU fileutils, sh-utils, and textutils packages.

Most of these programs have significant advantages over their Unix
counterparts, such as greater speed, additional options, and fewer
arbitrary limits.

The programs that can be built with this package are:

  basename cat chgrp chmod chown chroot cksum comm cp csplit cut date dd
  df dir dircolors dirname du echo env expand expr factor false fmt fold
  ginstall head hostid id join link ln logname ls md5sum mkdir mkfifo
  mknod mv nice nl nohup od paste pathchk pinky pr printenv printf ptx
  pwd rm rmdir seq sha1sum shred sleep sort split stat stty su sum sync
  tac tail tee test touch tr true tsort tty uname unexpand uniq unlink
  users vdir wc who whoami yes

%description -l pl
Narz�dzia podstawowe (core utilities) GNU to po��czone paczki GNU
fileutils, sh-utils i textutils.

Wi�kszo�� z zawartych program�w jest znacznie ulepszona w por�wnaniu
z ich uniksowymi odpowiednikami, np. szybciej dzia�aj�, maj� dodatkowe
opcje i mniej ogranicze�.

Programy zawarte w tej paczce to:

  basename cat chgrp chmod chown chroot cksum comm cp csplit cut date dd
  df dir dircolors dirname du echo env expand expr factor false fmt fold
  ginstall head hostid id join link ln logname ls md5sum mkdir mkfifo
  mknod mv nice nl nohup od paste pathchk pinky pr printenv printf ptx
  pwd rm rmdir seq sha1sum shred sleep sort split stat stty su sum sync
  tac tail tee test touch tr true tsort tty uname unexpand uniq unlink
  users vdir wc who whoami yes

%prep
%setup -q -a1 -a3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%{?_with_selinux:%patch12 -p1}

perl -pi -e 's@GNU/Linux@PLD Linux@' m4/host-os.m4

# nb_NO is just an alias for no_NO in glibc
# no.po is outdated, nb.po is more fresh here
mv -f po/{nb,no}.po
rm -f po/{nb,no}.gmo

%build
# jm's inttypes.m4 and inttypes.m4 from gettext are really different files
mv -f m4/{inttypes.m4,jm-inttypes.m4}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-pam

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/bin,%{_bindir},%{_sbindir},/etc/pam.d,/etc/profile.d}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_bindir}/{uptime,hostname,groups,kill}
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{uptime,hostname,groups}.1*

ln -sf test $RPM_BUILD_ROOT%{_bindir}/[

mv -f $RPM_BUILD_ROOT%{_bindir}/{basename,cat,chgrp,chmod,chown,cp,date,dd,df,\
echo,false,id,link,ln,ls,mkdir,mknod,mv,nice,pwd,rm,rmdir,sleep,sort,stty,\
sync,touch,true,unlink,uname} $RPM_BUILD_ROOT/bin

mv -f $RPM_BUILD_ROOT%{_bindir}/chroot $RPM_BUILD_ROOT%{_sbindir}

# su is missed by "make install"
install src/su $RPM_BUILD_ROOT/bin

install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE5} %{SOURCE6} $RPM_BUILD_ROOT/etc/profile.d
install %{SOURCE7} $RPM_BUILD_ROOT/etc/pam.d/su

mv -f man/pt_BR/*.1 man/pt
for d in cs da de es fi fr hu id it ja ko nl pl pt ru ; do
	install -d $RPM_BUILD_ROOT%{_mandir}/$d/man1
	install man/$d/*.1 $RPM_BUILD_ROOT%{_mandir}/$d/man1
done
install %{SOURCE8} $RPM_BUILD_ROOT%{_mandir}/pl/man1/stat.1
bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man1/{groups,hostname,uptime}.1
for f in `find $RPM_BUILD_ROOT%{_mandir} -type f -name ginstall.1`; do
	mv -f $f `dirname $f`/install.1
done

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS THANKS-to-translators TODO
%attr(755,root,root) /bin/[!s]*
%attr(755,root,root) /bin/s[!u]*
%attr(4755,root,root) /bin/su
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/su
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/DIR_COLORS
%attr(755,root,root) /etc/profile.d/*
%{_mandir}/man1/*
%lang(cs) %{_mandir}/cs/man1/*
%lang(da) %{_mandir}/da/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(id) %{_mandir}/id/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(pt) %{_mandir}/pt/man1/*
%lang(ru) %{_mandir}/ru/man1/*
%{_infodir}/coreutils.info*
