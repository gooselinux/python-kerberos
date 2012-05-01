%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
Name:           python-kerberos
Version:        1.1
Release:        6.2%{?dist}
Summary:        A high-level wrapper for Kerberos (GSSAPI) operations

Group:          System Environment/Libraries
License:        ASL 2.0
URL:            http://trac.calendarserver.org/projects/calendarserver/browser/PyKerberos
# Pull from SVN
# svn export http://svn.calendarserver.org/repository/calendarserver/PyKerberos/tags/release/PyKerberos-1.1/ python-kerberos-1.1
# tar czf python-kerberos-%{version}.tar.gz python-kerberos-%{version}
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  python-devel
BuildRequires:  krb5-devel
BuildRequires:  python-setuptools

Patch0: PyKerberos-delegation.patch

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire
Kerberos.framework, and instead offer a limited set of functions that do what
is needed for client/serverKerberos authentication based on
<http://www.ietf.org/rfc/rfc4559.txt>.

Much of the C-code here is adapted from Apache's mod_auth_kerb-5.0rc7.


%prep
%setup -q

%patch0 -p1 -b .delegation

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README.txt LICENSE test.py
%{python_sitearch}/*


%changelog
* Wed Jan  5 2011 Rob Crittenden <rcritten@redhat.com> - 1.1-6.2
- Rebuilt for RHEL 6

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1-5.2
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Simo Sorce <ssorce@redhat.com> - 1.1-3.1
- Fix minor issue with delegation patch

* Fri Dec 12 2008 Simo Sorce <ssorce@redhat.com> - 1.1-3
- Add delegation patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-2
- Rebuild for Python 2.6

* Thu Nov 27 2008 Simo Sorce <ssorce@redhat.com> - 1.1-1
- New Upstream Release
- Remove patches as this version has them included already

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-6
- Autorebuild for GCC 4.3

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-5
- Package the egg-info too

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-4
- Switch from python_sitelib macro to python_sitearch
- Add python-setuptools to BuildRequires

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-3
- Use the setup.py install target in order to generate debuginfo.

* Thu Jan  3 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-2
- Add krb5-devel to BuildRequires

* Wed Jan  2 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-1
- Change name to python-kerberos from PyKerberos
- Change license from "Apache License" to ASL 2.0 per guidelines
- Upstream released 1.0 which is equivalent to version 1541. Reverting
  to that.

* Tue Aug 28 2007 Rob Crittenden <rcritten@redhat.com> - 0.1735-2
- Include GSS_C_DELEG_FLAG in gss_init_sec_context() so the command-line
  tools can do kerberos ticket forwarding.

* Tue Jul 31 2007 Rob Crittenden <rcritten@redhat.com> - 0.1735-1
- Initial rpm version
