Name:		uncrustify
Version:	0.74.0
Release:	%autorelease
Summary:	Reformat Source

License:	GPLv2
URL:		http://uncrustify.sourceforge.net/
Source0:	https://prdownloads.sourceforge.net/uncrustify/uncrustify-%{version}.tar.gz
BuildRequires:	gcc gcc-c++ libstdc++ cmake

%description
Source Code Beautifier for C, C++, C#, D, Java, and Pawn

%prep
%autosetup -c

%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc AUTHORS
%doc NEWS
%doc README.md
%doc documentation
%{_bindir}/uncrustify
%dir %{_datadir}/doc/uncrustify
%{_datadir}/doc/uncrustify/*
%{_mandir}/man1/uncrustify.1*


%autochangelog
