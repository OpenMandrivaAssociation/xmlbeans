%{?_javapackages_macros:%_javapackages_macros}
# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%bcond_with bootstrap
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           xmlbeans
Version:        2.6.0
Release:        6.1%{?dist}%{?with_bootstrap:.boot}
Summary:        XML-Java binding tool
URL:            http://xmlbeans.apache.org/
Source0:        http://www.apache.org/dist/xmlbeans/source/%{name}-%{version}-src.tgz
# Pom file is not available from maven repository for the
# currently released version
Source1:        %{version}/%{name}-%{version}.pom
Source2:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}-xpath/%{version}/%{name}-xpath-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}-xmlpublic/%{version}/%{name}-xmlpublic-%{version}.pom
Patch0:         xmlbeans-2.6.0-nodownload.patch
Patch1:         0001-Update-to-newer-saxon-API.patch
Patch2:         xmlbeans-2.6.0-iso-8859-1-encoding.patch
Patch3:         xmlbeans-2.6.0-jsr-bundle.patch
Patch4:         xmlbeans-scripts-classpath.patch
License:        ASL 2.0

%if %without bootstrap
BuildRequires:  xmlbeans
%endif
BuildRequires:  java-devel
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  ant >= 0:1.6, ant-junit, ant-contrib, junit
BuildRequires:  xml-commons-resolver >= 0:1.1
BuildRequires:  bea-stax-api
BuildRequires:  saxon >= 8
Requires:       jpackage-utils >= 0:1.6
Requires:       java

BuildArch:      noarch

%description
XMLBeans is a tool that allows you to access the full power 
of XML in a Java friendly way. It is an XML-Java binding tool. 
The idea is that you can take advantage the richness and 
features of XML and XML Schema and have these features mapped 
as naturally as possible to the equivalent Java language and 
typing constructs. XMLBeans uses XML Schema to compile Java 
interfaces and classes that you can then use to access and 
modify XML instance data. Using XMLBeans is similar to using 
any other Java interface/class, you will see things like 
getFoo or setFoo just as you would expect when working with 
Java. While a major use of XMLBeans is to access your XML 
instance data with strongly typed Java classes there are also 
API's that allow you access to the full XML infoset (XMLBeans 
keeps full XML Infoset fidelity) as well as to allow you to 
reflect into the XML schema itself through an XML Schema 
Object model.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.


%package manual
Summary:        Documents for %{name}

%description manual
%{summary}.


%package scripts
Summary:        Scripts for %{name}
Requires:       %{name} = %{version}-%{release}

%description scripts
%{summary}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .nodownload
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1


%build
# Piccolo and jam are rebuilt from source and bundled with xbean
# ant clean.jars leaves some dangling jars around, do not use it
find . \( -name '*.jar' -o -name '*.zip' \) \
        -not -name 'piccolo*.jar' -not -name 'jam*.jar' \
        %{?with_bootstrap:-not -name 'oldxbean.jar' } \
        -print -delete

# Replace bundled libraries
mkdir -p build/lib
ln -sf $(build-classpath xml-commons-resolver) build/lib/resolver.jar
ln -sf $(build-classpath xmlbeans/xbean) external/lib/oldxbean.jar
ln -sf $(build-classpath bea-stax-api) external/lib/jsr173_1.0_api.jar
ln -sf $(build-classpath saxon) external/lib/saxon9.jar
ln -sf $(build-classpath saxon) external/lib/saxon9-dom.jar

# Fix CRLF
sed 's/\r//' -i LICENSE.txt NOTICE.txt README.txt docs/stylesheet.css docs/xmlbeans.css docs/guide/tools.html

# Build
ant -Djavac.source=1.5 -Djavac.target=1.5 default docs

%install
# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 build/lib/xmlpublic.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlpublic.jar
install -p -m 0644 build/lib/xbean_xpath.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean_xpath.jar
install -p -m 0644 build/lib/xbean.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean.jar

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-xbean.pom
%add_maven_depmap JPP.%{name}-xbean.pom %{name}/xbean.jar
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-xbean_xpath.pom
%add_maven_depmap JPP.%{name}-xbean_xpath.pom %{name}/xbean_xpath.jar
install -pm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-xmlpublic.pom
%add_maven_depmap JPP.%{name}-xmlpublic.pom %{name}/xmlpublic.jar

# bin
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/dumpxsb   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/inst2xsd  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/scomp     $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/sdownload $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/sfactor   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/svalidate $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/validate  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xpretty   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xsd2inst  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xsdtree   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xstc      $RPM_BUILD_ROOT%{_bindir}


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/reference/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf build/docs/reference

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_pkgdocdir}
cp -pr build/docs/* LICENSE.txt NOTICE.txt README.txt $RPM_BUILD_ROOT%{_pkgdocdir}

%files -f .mfiles
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/LICENSE.txt
%doc %{_pkgdocdir}/NOTICE.txt
%doc %{_pkgdocdir}/README.txt

%files javadoc
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/LICENSE.txt
%doc %{_pkgdocdir}/NOTICE.txt
%doc %{_pkgdocdir}/README.txt
%doc %{_javadocdir}/%{name}

%files manual
%{_pkgdocdir}

%files scripts
%attr(0755,root,root) %{_bindir}/*


%changelog
* Mon Aug 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.6.0-6
- Install docs to %%{_pkgdocdir} where available (#993883).

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.6.0-4
- Update to latest packaging guidelines

* Sun Mar 03 2013 Matt Spaulding <mspaulding06@gmail.com> - 2.6.0-3
- Fixed classpath issue with scripts (#892690)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 13 2012 Matt Spaulding <mspaulding06@gmail.com> - 2.6.0-1
- Updated to latest version 2.6.0 (#824022)
- Compiles with target 1.5 (#842625)
- Source encoding properly set as ISO-8859-1
- Updated Requires and BR for current java guidelines

* Mon May 28 2012 gil cattaneo <puntogil@libero.it> - 2.4.0-10
- Add maven POMs, RHBZ#825844

* Wed May 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.0-9
- Update to newer saxon API

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 09 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.4.0-6
- Rebuild without bootstrapping

* Fri Nov 27 2009 Lubomir Rintel <lkundrak@v3.sk> - 2.4.0-5
- Fix up saxon dependency
- Drop epoch
- Drop gcj

* Tue Nov 03 2009 Lubomir Rintel <lkundrak@v3.sk> 0:2.4.0-4
- Update to 2.4.0
- Tidy up a bit for Fedora

* Wed Sep 06 2006 Ralph Apel <r.apel at r-apel.de> 0:2.1.0-3jpp
- BuildRequire saxon8 instead of saxonb8
- (B)Require bea-stax-api instead of bea-stax
- Patch maven-plugin's project.xml for bea-stax-api instead of stax-bea-api
- Patch XbeanXQuery to saxon 8.7
- Add gcj_support option
- Add post/postun Requires for javadoc

* Wed Feb 01 2006 Ralph Apel <r.apel at r-apel.de> 0:2.1.0-2jpp
- Install plugin to /usr/share/maven/repository/JPP/plugins

* Mon Jan 30 2006 Ralph Apel <r.apel at r-apel.de> 0:2.1.0-1jpp
- Upgrade to 2.1.0
- Add -maven-plugin subpackage

* Fri Jun 03 2005 Fernando Nasser <fnasser@redhat.com> 0:1.0.4-2jpp
- Add missing build requires for jaxen

* Fri Jun 03 2005 Fernando Nasser <fnasser@redhat.com> 0:1.0.4-1jpp
- Upgrade to 1.0.4

* Thu Sep 30 2004 Ralph Apel <r.apel at r-apel.de> 0:1.0.3-1jpp
- First JPackage build
