Summary:	IMAP Filter
Summary(pl.UTF-8):	Filtr dla protokołu IMAP
Name:		imapfilter
Version:	2.6.11
Release:	2
License:	MIT/X Consortium
Group:		Applications/Mail
Source0:	https://github.com/lefcha/imapfilter/archive/v%{version}.tar.gz
# Source0-md5:	ce2b896b350e4dfa1d6376dfb6072687
URL:		https://github.com/lefcha/imapfilter
BuildRequires:	lua51-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
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
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `pkg-config --cflags lua51` -DCONFIG_SHAREDIR='\"%{_datadir}/%{name}\"' " \
	LDFLAGS="%{rpmldflags}" \
	LIBS="-lm -lssl -lcrypto `pkg-config --libs lua51` -lpcre"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	SHAREDIR=%{_datadir}/%{name} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man?/*
