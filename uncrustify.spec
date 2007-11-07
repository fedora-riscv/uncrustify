Name:		uncrustify
Version:	0.40
Release: 2%{?dist}
Summary:	Reformat Source

Group:		Development/Tools
License:	GPL
URL:		http://uncrustify.sourceforge.net/
Source0:	http://umn.dl.sourceforge.net/sourceforge/uncrustify/uncrustify-%{version}.tgz
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
* Tue Nov  6 2007 Neal Becker <ndbecker2@gmail.com> - 0.40-2
- Increase release tag to satisfy cvs
- Bump tag

* Tue Nov  6 2007 Neal Becker <ndbecker2@gmail.com> - 0.40-1
- Update to 0.40

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.35-2
- Rebuild for selinux ppc32 issue.

* Fri Jul 20 2007 Neal Becker <ndbecker2@gmail.com> - 0.35-1
- 0.35

* Tue Jun 12 2007 Neal Becker <ndbecker2@gmail.com> - 0.34-1
- bump to 0.34

