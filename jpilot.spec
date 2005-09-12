%define version 0.99.8-pre7-beta

Summary:   palm pilot desktop for Linux
Name:      jpilot
Version:   %{version}
Release:   1
License:   GPL
Group:     Applications/Productivity
Source:    http://jpilot.org/jpilot-%{version}.tar.gz
URL:       http://jpilot.org
Packager:  Paul Gear <paul@gear.dyndns.org>
Prefix:    /usr
DocDir:    %{prefix}/share/doc
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires:  pilot-link > 0.11.2

%description
J-Pilot is a desktop organizer application for the palm pilot that runs
under Linux and Unix using X-Windows and GTK+.  It is similar in
functionality to the one that 3Com distributes and has many features
not found in the 3Com desktop.

%define _prefix %{prefix}
%define _mandir %{prefix}/share/man
%define _infodir %{prefix}/share/info
%define _datadir %{prefix}/share

%prep

%setup -q

%build
if [ ! -f ./configure ]; then
  ./autogen.sh --prefix=%{prefix} --mandir=%{_mandir}
else
  %configure --prefix=%{prefix} --mandir=%{_mandir}
fi
#gzip -9f docs/*.1
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install docs/jpilot*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -d $RPM_BUILD_ROOT%{_datadir}/jpilot/
install jpilotrc.* $RPM_BUILD_ROOT%{_datadir}/jpilot/
install empty/*.pdb $RPM_BUILD_ROOT%{_datadir}/jpilot/
strip jpilot
install -d $RPM_BUILD_ROOT%{_bindir}
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/pixmaps
install -m644 icons/*.xpm $RPM_BUILD_ROOT%{prefix}/share/pixmaps

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%docdir /usr/doc
%doc BUGS ChangeLog COPYING AUTHORS INSTALL README TODO UPGRADING
%doc icons/README
%doc icons/jpilot-icon1.xpm icons/jpilot-icon2.xpm
%doc icons/jpilot-icon3.xpm icons/jpilot-icon4.xpm
%doc docs/plugin.html docs/manual.html
%doc docs/jpilot-address.png
%doc docs/jpilot-datebook.png
%doc docs/jpilot-expense.png
%doc docs/jpilot-install.png
%doc docs/jpilot-memo.png
%doc docs/jpilot-prefs.png
%doc docs/jpilot-print.png
%doc docs/jpilot-search.png
%doc docs/jpilot-todo.png
%doc docs/jpilot-toplogo.jpg
%{_bindir}/jpilot
%{_bindir}/jpilot-dump
%{_bindir}/jpilot-dial
%{_bindir}/jpilot-sync
%{_datadir}/jpilot/jpilotrc.blue
%{_datadir}/jpilot/jpilotrc.default
%{_datadir}/jpilot/jpilotrc.green
%{_datadir}/jpilot/jpilotrc.purple
%{_datadir}/jpilot/jpilotrc.steel
%{_datadir}/jpilot/DatebookDB.pdb
%{_datadir}/jpilot/AddressDB.pdb
%{_datadir}/jpilot/ToDoDB.pdb
%{_datadir}/jpilot/MemoDB.pdb
%{_datadir}/jpilot/Memo32DB.pdb
%{_datadir}/jpilot/ExpenseDB.pdb
%{_libdir}/jpilot/plugins/libexpense.so
%{_libdir}/jpilot/plugins/libexpense.so.0
%{_libdir}/jpilot/plugins/libexpense.so.0.0.0
%{_libdir}/jpilot/plugins/libexpense.la
%{_libdir}/jpilot/plugins/libsynctime.so
%{_libdir}/jpilot/plugins/libsynctime.so.0
%{_libdir}/jpilot/plugins/libsynctime.so.0.0.0
%{_libdir}/jpilot/plugins/libsynctime.la
%{_libdir}/jpilot/plugins/libkeyring.so
%{_libdir}/jpilot/plugins/libkeyring.so.0
%{_libdir}/jpilot/plugins/libkeyring.so.0.0.0
%{_libdir}/jpilot/plugins/libkeyring.la
%{_datadir}/locale/*/LC_MESSAGES/jpilot.mo
%{_mandir}/man1/jpilot.1.gz
%{_mandir}/man1/jpilot-dial.1.gz
%{_mandir}/man1/jpilot-sync.1.gz
%{_mandir}/man1/jpilot-dump.1.gz
%{_mandir}/man1/jpilot-upgrade-99.1.gz
%{prefix}/share/pixmaps/*
%{_datadir}/gnome/apps/Applications/jpilot.desktop

%changelog
* Sat Feb 22 2003 Judd Montgomery <judd@jpilot.org>
- fixed jpilotrc.* and empty/* files not being included
* Sat Feb 22 2003 Vladimir Bormotov <bor@insight.donbass.com>
- call autogen.sh if no configure found
- installation improvements
- Oct 8, 2002 <judd@jpilot.org>
  updated for automake build
* Tue Jun  5 2001 Christian W. Zuckschwerdt <zany@triq.net>
- moved jpilot.spec to jpilot.spec.in and autoconf'ed it.
- fixed this spec file so we don't need superuser privileges.
- changed the hardcoded path into rpm macros
* Wed Nov 22 2000 Matthew Vanecek <linux4us@home.com>
- deleted the calls to 'install' in the % install section since
  this is already done in the Makefile.
- Deleted the %attr tags from the %files list and made the default
  attribute to -,root,root.
- changed the /usr/ to % {prefix}/
- Added the % post section
- Added the % clean section
- Changed the description
