Summary:	IMAP Filter
Summary(pl.UTF-8):	Filtr dla protokołu IMAP
Name:		imapfilter
Version:	1.2.1
Release:	0.1
License:	MIT/X Consortium
Group:		Applications/Mail
Source0:	http://imapfilter.hellug.gr/source/%{name}-%{version}.tar.gz
# Source0-md5:	25673a7e93eb256b3b434ab7560dba76
URL:		http://imapfilter.hellug.gr/
BuildRequires:	lua50-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
imapfilter is a mail filtering utility. It connects to remote mail
servers using the Internet Message Access Protocol (IMAP), sends
searching queries to the server and processes mailboxes based on the
results. It can be used to delete, copy, move, flag, etc. messages
residing in mailboxes at the same or different mail servers. The 4rev1
and 4 versions of the IMAP protocol are supported.

%description -l pl.UTF-8
imapfilter jest narzędziem do filtrowania poczty. Łączy się ze zdalnym
serwerem korzystając z protokołu IMAP, wysyła zapytania na serwer i
przetwarza skrzynki w zależności od rezultatów. Może być
wykorzystywany do usuwania, kopiowania, przenoszenia, zmiany flag i
tym podobnych operacji na skrzynkach na tym samym lub innych
serwerach. Obsługuje zarówno wersję 4 jak i 4rev1 protokołu IMAP.

%prep
%setup -q

%build
%{__make} \
	MYCFLAGS="%{rpmcflags}" \
	INCDIRS="-I/usr/include/lua50" \
	LIBS="-lm -llua50 -llualib50 -lssl -lcrypto" \
	BINDIR=%{_bindir} \
	SHAREDIR=%{_datadir}/%{name} \
	MANDIR=%{_mandir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS sample.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
