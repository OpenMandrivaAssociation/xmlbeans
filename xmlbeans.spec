%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

# If you don't want to build maven plugin
# give rpmbuild option '--without maven'

%define with_maven %{!?_without_maven:1}%{?_without_maven:0}
%define without_maven %{?_without_maven:1}%{!?_without_maven:0}

Summary:	XML-Java binding tool
Name:           xmlbeans
Version:	2.5.0
Release:	%mkrel 2
Epoch:		0
License:	Apache Software License 2
Group:		Development/Java
URL:		http://xmlbeans.apache.org
Source0:	%{name}-%{version}-src.tgz
# svn export http://svn.apache.org/repos/asf/xmlbeans/tags/2.1.0
Source1:	http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans/2.5.0/xmlbeans-2.5.0.pom
Source2:	http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans-xpath/2.5.0/xmlbeans-xpath-2.5.0.pom
Source3:	http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans-xmlpublic/2.5.0/xmlbeans-xmlpublic-2.5.0.pom
Source4:	http://repo1.maven.org/maven2/org/apache/xmlbeans/xmlbeans-qname/2.5.0/xmlbeans-qname-2.5.0.pom
Patch0:		xmlbeans-2.5.0-no-jar-download.patch
BuildRequires:	jpackage-utils >= 0:1.7.5
BuildRequires:	ant >= 0:1.6.5
BuildRequires:	ant-junit
BuildRequires:	ant-nodeps
BuildRequires:  ant-contrib
BuildRequires:	junit
BuildRequires:	xml-commons-resolver11
BuildRequires:	bea-stax-api
BuildRequires:	saxon9
BuildRequires:	java-rpmbuild
Requires:	jpackage-utils >= 0:1.7.5
Requires:	bea-stax-api
Requires(post):	jpackage-utils >= 0:1.7.5
Requires(postun):	jpackage-utils >= 0:1.7.5
%if %{gcj_support}
BuildRequires:	gnu-crypto
BuildRequires:	java-gcj-compat-devel
Requires(post):	java-gcj-compat
Requires(postun):	java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:	noarch
%endif
Requires:	java >= 1.5
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Summary:	Javadoc for %{name}
Group:		Development/Java

%description javadoc
Javadoc for %{name}.

%package manual
Summary:	Documents for %{name}
Group:		Development/Java

%description manual
Documents for %{name}.

%package scripts
Summary:	Scripts for %{name}
Group:		Development/Java
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description scripts
Scripts for %{name}.

%prep
%setup -q
%patch0 -p1

#Piccolo and jam are rebuilt from source and bundled with xbean
# ant clean.jars leaves some dangling jars around, do not use it
find . \( -name '*.jar' -o -name '*.zip' \) \
-not -name 'piccolo*.jar' -not -name 'jam*.jar' \
-not -name 'oldxbean.jar' \
-print -delete

# Replace bundled libraries
mkdir -p build/lib
ln -sf $(build-classpath xml-commons-resolver) build/lib/resolver.jar
ln -sf $(build-classpath xmlbeans/xbean) external/lib/oldxbean.jar
ln -sf $(build-classpath bea-stax-api) external/lib/jsr173_1.0_api.jar
ln -sf $(build-classpath saxon9) external/lib/saxon9.jar
ln -sf $(build-classpath saxon9) external/lib/saxon9-dom.jar
ln -sf $(build-classpath junit) external/lib/junit.jar

# Fix CRLF
sed 's/\r//' -i LICENSE.txt NOTICE.txt README.txt docs/stylesheet.css 

%build
export XMLBEANS_EXTERNALS=/usr/share/java
export XMLBEANS_HOME=`pwd`
%ant default docs

%install
rm -rf %{buildroot}

# jar
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -d -m 0755 %{buildroot}%{_datadir}/maven2/poms

install -m 0644 build/lib/xmlbeans-qname.jar %{buildroot}%{_javadir}/%{name}/xmlbeans-qname-%{version}.jar
install -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xmlbeans-qname.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans-qname %{version} JPP/%{name} xmlbeans-qname

install -m 0644 build/lib/xmlpublic.jar %{buildroot}%{_javadir}/%{name}/xmlpublic-%{version}.jar
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xmlpublic.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans-xmlpublic %{version} JPP/%{name} xmlpublic

install -m 0644 build/lib/xbean_xpath.jar %{buildroot}%{_javadir}/%{name}/xbean_xpath-%{version}.jar
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xbean_xpath.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans-xpath %{version} JPP/%{name} xbean_xpath

install -m 0644 build/lib/xbean.jar %{buildroot}%{_javadir}/%{name}/xbean-%{version}.jar
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-xbean.pom
%add_to_maven_depmap org.apache.xmlbeans xmlbeans %{version} JPP/%{name} xbean

ln -s xmlbeans-qname-%{version}.jar %{buildroot}%{_javadir}/%{name}/xmlbeans-qname.jar
ln -s xmlpublic-%{version}.jar %{buildroot}%{_javadir}/%{name}/xmlpublic.jar
ln -s xbean_xpath-%{version}.jar %{buildroot}%{_javadir}/%{name}/xbean_xpath.jar
ln -s xbean-%{version}.jar %{buildroot}%{_javadir}/%{name}/xbean.jar

# bin
install -d -m 0755 %{buildroot}%{_bindir}
install -p -m 0755 bin/dumpxsb   %{buildroot}%{_bindir}
install -p -m 0755 bin/inst2xsd  %{buildroot}%{_bindir}
install -p -m 0755 bin/scomp     %{buildroot}%{_bindir}
install -p -m 0755 bin/sdownload %{buildroot}%{_bindir}
install -p -m 0755 bin/sfactor   %{buildroot}%{_bindir}
install -p -m 0755 bin/svalidate %{buildroot}%{_bindir}
install -p -m 0755 bin/validate  %{buildroot}%{_bindir}
install -p -m 0755 bin/xpretty   %{buildroot}%{_bindir}
install -p -m 0755 bin/xsd2inst  %{buildroot}%{_bindir}
install -p -m 0755 bin/xsdtree   %{buildroot}%{_bindir}
install -p -m 0755 bin/xstc      %{buildroot}%{_bindir}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/docs/reference/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink
rm -rf build/docs/reference

# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr build/docs/* %{buildroot}%{_docdir}/%{name}-%{version}
cp LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf %{buildroot}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -sf %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%post
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%postun
%update_maven_depmap
%if %{gcj_support}
if [ -x %{_bindir}/rebuild-gcj-db ]
then
  %{_bindir}/rebuild-gcj-db
fi
%endif

%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/LICENSE.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}
%if %{gcj_support}
%attr(-,root,root) %dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/x*-%{version}.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%ghost %doc %{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}

%files scripts
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
