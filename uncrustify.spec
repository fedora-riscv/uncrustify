Name:		uncrustify
Version:	0.50
Release: 	3%{?dist}
Summary:	Reformat Source

Group:		Development/Tools
License:	GPLv2
URL:		http://uncrustify.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/uncrustify/uncrustify-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc autoconf gcc-c++ libstdc++

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
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m644 man/uncrustify.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README NEWS BUGS
%doc documentation
%{_bindir}/uncrustify
%{_datadir}/uncrustify
%{_mandir}/man1/uncrustify.1*


%changelog
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov  3 2008 Neal Becker <ndbecker2@gmail.com> - 0.50-2
- Documentation fixes

* Mon Nov  3 2008 Neal Becker <ndbecker2@gmail.com> - 0.50-1
- Update to 0.50

* Sun Jun 15 2008 Neal Becker <ndbecker2@gmail.com> - 0.47-1
- Update to 0.47

* Thu Apr 24 2008 Neal Becker <ndbecker2@gmail.com> - 0.46-1
- Update to 0.46

* Sun Mar  9 2008 Neal Becker <ndbecker2@gmail.com> - 0.45-1
- Update to 0.45

* Wed Feb 13 2008 Neal Becker <ndbecker2@gmail.com> - 0.44-1
- Update to 0.44

* Tue Jan 29 2008 Neal Becker <ndbecker2@gmail.com> - 0.43-2
- Remove explicit dep libstdc++

* Tue Jan 29 2008 Neal Becker <ndbecker2@gmail.com> - 0.43-1
- Update to 0.43

* Sun Nov 18 2007 Neal Becker <ndbecker2@gmail.com> - 0.41-1
- Update to 0.41

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

