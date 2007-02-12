Summary:	Asterisk Fax
Summary(pl.UTF-8):	Fax dla Asteriska
Name:		astfax
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.inter7.com/astfax/%{name}-%{version}.tar.gz
# Source0-md5:	66e4ef4efc42b3b136bfa81b77552bf5
URL:		http://www.inter7.com/index.php?page=astfax
BuildRequires:	eps-devel >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AstFax provides an outgoing email to fax gateway for the Asterisk PBX
package. Incoming fax to email can also be configured so your Asterisk
server can act as both an outgoing and incoming fax server.

%description -l pl.UTF-8
AstFax udostępnia bramkę z wychodzącej poczty na fax dla pakietu
Asterisk PBX. Można także skonfigurować bramkę z przychodzących faksów
na pocztę, więc serwer Asterisk może działać jako serwer faksów
wychodzących i przychodzących.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ast_fax $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ast_fax.call ChangeLog README testfax.*
%attr(755,root,root) %{_bindir}/*
