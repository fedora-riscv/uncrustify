Name:		uncrustify
Version:	0.30
Release:	1%{?dist}
Summary:	Reformat Source

Group:		Development/Tools
License:	GPL
URL:		http://uncrustify.sourceforge.net/
Source0:	http://umn.dl.sourceforge.net/sourceforge/uncrustify/uncrustify-0.30.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc autoconf gcc-c++ libstdc++
Requires:	libstdc++

%description
Source Code Beautifier for C, C++, C#, D, Java, and Pawn

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README NEWS BUGS
%{_bindir}/uncrustify
%{_datadir}/uncrustify



%changelog
