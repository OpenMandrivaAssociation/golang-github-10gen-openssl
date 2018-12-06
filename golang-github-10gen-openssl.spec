# Run tests in check section
# Deactivating test: tests randomly fail in Koji
%bcond_with check

# https://github.com/10gen/openssl
%global goipath         github.com/10gen/openssl
%global commit          58f60a8e59ba35b53e6821bda7003c4ea626dbf9

%gometa

Name:           %{goname}
Version:        0
Release:        0.18%{?dist}
Summary:        OpenSSL bindings for Go
# Detected licences
# - *No copyright* Apache License (v2.0) at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/spacemonkeygo/spacelog)
BuildRequires: openssl-devel

%description
%{summary}.


%package devel
Summary:       %{summary}
BuildArch:     noarch
Requires: openssl-devel

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS


%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.18.20181111git58f60a8
- Bump to commit 58f60a8e59ba35b53e6821bda7003c4ea626dbf9
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.17.gitcbe9e82
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Marek Skalický <mskalick@redhat.com> - 0-0.16.gitcbe9e82
- Update to latest upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git4c6dbaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git4c6dbaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.git4c6dbaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Marek Skalický <mskalick@redhat.com> - 0-0.12.git4c6dbaf
- Use compat openssl 1.0
- Exclude ppc64 architecture (missing cgo)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git4c6dbaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 08 2016 jchaloup <jchaloup@redhat.com> - 0-0.10.git4c6dbaf
- Enable devel and unit-test for epel7
  related: #1247160

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.git4c6dbaf
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.git4c6dbaf
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git4c6dbaf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git4c6dbaf
- Put back path to header files
  related: #1247160

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.git4c6dbaf
- Update to spec-2.0
  related: #1247160

* Mon Jul 27 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git4c6dbaf
- Rebuild all Fedora branches to test modified spec file
  related: #1247160

* Mon Jul 27 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git4c6dbaf
- Update of spec file to spec-2.0
  resolves: #1247160

* Thu Jun 18 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git4c6dbaf
- Add missing openssl
  related: #1232234

* Mon Jun 15 2015 Marek Skalicky <mskalick@redhat.com> - 0-0.1.git4c6dbaf
- First package for Fedora
  resolves: #1232234
