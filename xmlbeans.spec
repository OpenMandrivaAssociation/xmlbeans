
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'

Name:		xmlbeans
Version:	2.6.0
Release:	6.0
License:	GPLv3+
Source0:	xmlbeans-2.6.0-6.0-omv2014.0.noarch.rpm
Source1:	xmlbeans-manual-2.6.0-6.0-omv2014.0.noarch.rpm
Source2:	xmlbeans-scripts-2.6.0-6.0-omv2014.0.noarch.rpm
Source3:	xmlbeans-javadoc-2.6.0-6.0-omv2014.0.noarch.rpm

URL:		https://abf.rosalinux.ru/openmandriva/xmlbeans
BuildArch:	noarch
Summary:	xmlbeans bootstrap version
Requires:	javapackages-bootstrap
Requires:	java
Requires:	jpackage-utils >= 0:1.6
Provides:	mvn(org.apache.xmlbeans:xmlbeans) = 2.6.0
Provides:	mvn(org.apache.xmlbeans:xmlbeans-xmlpublic) = 2.6.0
Provides:	mvn(org.apache.xmlbeans:xmlbeans-xpath) = 2.6.0
Provides:	xmlbeans = 2.6.0-6.0:2014.0

%description
xmlbeans bootstrap version.

%files
/usr/share/doc/xmlbeans-2.6.0
/usr/share/doc/xmlbeans-2.6.0/LICENSE.txt
/usr/share/doc/xmlbeans-2.6.0/NOTICE.txt
/usr/share/doc/xmlbeans-2.6.0/README.txt
/usr/share/java/xmlbeans/xbean.jar
/usr/share/java/xmlbeans/xbean_xpath.jar
/usr/share/java/xmlbeans/xmlpublic.jar
/usr/share/maven-fragments/xmlbeans
/usr/share/maven-poms/JPP.xmlbeans-xbean.pom
/usr/share/maven-poms/JPP.xmlbeans-xbean_xpath.pom
/usr/share/maven-poms/JPP.xmlbeans-xmlpublic.pom

#------------------------------------------------------------------------
%package	-n xmlbeans-manual
Version:	2.6.0
Release:	6.0
Summary:	xmlbeans-manual bootstrap version
Requires:	javapackages-bootstrap
Provides:	xmlbeans-manual = 2.6.0-6.0:2014.0

%description	-n xmlbeans-manual
xmlbeans-manual bootstrap version.

%files		-n xmlbeans-manual
/usr/share/doc/xmlbeans-2.6.0
/usr/share/doc/xmlbeans-2.6.0/LICENSE.txt
/usr/share/doc/xmlbeans-2.6.0/NOTICE.txt
/usr/share/doc/xmlbeans-2.6.0/README.txt
/usr/share/doc/xmlbeans-2.6.0/guide
/usr/share/doc/xmlbeans-2.6.0/guide/antXmlbean.html
/usr/share/doc/xmlbeans-2.6.0/guide/conGettingStartedwithXMLBeans.html
/usr/share/doc/xmlbeans-2.6.0/guide/conHandlingAny.html
/usr/share/doc/xmlbeans-2.6.0/guide/conIntroToTheSchemaTypeSystem.html
/usr/share/doc/xmlbeans-2.6.0/guide/conJavaTypesGeneratedFromUserDerived.html
/usr/share/doc/xmlbeans-2.6.0/guide/conMethodsForGeneratedJavaTypes.html
/usr/share/doc/xmlbeans-2.6.0/guide/conNavigatingXMLwithCursors.html
/usr/share/doc/xmlbeans-2.6.0/guide/conSelectingXMLwithXQueryPathXPath.html
/usr/share/doc/xmlbeans-2.6.0/guide/conUnderstandingXMLTokens.html
/usr/share/doc/xmlbeans-2.6.0/guide/conUsingBookmarksToAnnotateXML.html
/usr/share/doc/xmlbeans-2.6.0/guide/conValidationWithXmlBeans.html
/usr/share/doc/xmlbeans-2.6.0/guide/conXMLBeansSupportBuiltInSchemaTypes.html
/usr/share/doc/xmlbeans-2.6.0/guide/tools.html
/usr/share/doc/xmlbeans-2.6.0/images
/usr/share/doc/xmlbeans-2.6.0/images/conCursorTokenLocations.gif
/usr/share/doc/xmlbeans-2.6.0/images/conXMLTypeHierarchy.gif
/usr/share/doc/xmlbeans-2.6.0/xmlbeans.css

#------------------------------------------------------------------------
%package	-n xmlbeans-scripts
Version:	2.6.0
Release:	6.0
Summary:	xmlbeans-scripts bootstrap version
Requires:	javapackages-bootstrap
Requires:	xmlbeans = 2.6.0-6.0
Provides:	xmlbeans-scripts = 2.6.0-6.0:2014.0

%description	-n xmlbeans-scripts
xmlbeans-scripts bootstrap version.

%files		-n xmlbeans-scripts
/usr/bin/dumpxsb
/usr/bin/inst2xsd
/usr/bin/scomp
/usr/bin/sdownload
/usr/bin/sfactor
/usr/bin/svalidate
/usr/bin/validate
/usr/bin/xpretty
/usr/bin/xsd2inst
/usr/bin/xsdtree
/usr/bin/xstc

#------------------------------------------------------------------------
%package	-n xmlbeans-javadoc
Version:	2.6.0
Release:	6.0
Summary:	xmlbeans-javadoc bootstrap version
Requires:	javapackages-bootstrap
Requires:	jpackage-utils
Provides:	xmlbeans-javadoc = 2.6.0-6.0:2014.0

%description	-n xmlbeans-javadoc
xmlbeans-javadoc bootstrap version.

%files		-n xmlbeans-javadoc
/usr/share/doc/xmlbeans-2.6.0
/usr/share/doc/xmlbeans-2.6.0/LICENSE.txt
/usr/share/doc/xmlbeans-2.6.0/NOTICE.txt
/usr/share/doc/xmlbeans-2.6.0/README.txt
/usr/share/javadoc/xmlbeans
/usr/share/javadoc/xmlbeans/allclasses-frame.html
/usr/share/javadoc/xmlbeans/allclasses-noframe.html
/usr/share/javadoc/xmlbeans/constant-values.html
/usr/share/javadoc/xmlbeans/deprecated-list.html
/usr/share/javadoc/xmlbeans/help-doc.html
/usr/share/javadoc/xmlbeans/index-all.html
/usr/share/javadoc/xmlbeans/index.html
/usr/share/javadoc/xmlbeans/javax
/usr/share/javadoc/xmlbeans/javax/xml
/usr/share/javadoc/xmlbeans/javax/xml/namespace
/usr/share/javadoc/xmlbeans/javax/xml/namespace/NamespaceContext.html
/usr/share/javadoc/xmlbeans/javax/xml/namespace/QName.html
/usr/share/javadoc/xmlbeans/javax/xml/namespace/package-frame.html
/usr/share/javadoc/xmlbeans/javax/xml/namespace/package-summary.html
/usr/share/javadoc/xmlbeans/javax/xml/namespace/package-tree.html
/usr/share/javadoc/xmlbeans/org
/usr/share/javadoc/xmlbeans/org/apache
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/BindingConfig.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/CDataBookmark.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/DelegateXmlObject.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/Filer.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/FilterXmlObject.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/GDate.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/GDateBuilder.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/GDateSpecification.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/GDuration.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/GDurationBuilder.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/GDurationSpecification.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/InterfaceExtension.MethodSignature.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/InterfaceExtension.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/ObjectFactory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/PrePostExtension.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/QNameCache.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/QNameSet.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/QNameSetBuilder.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/QNameSetSpecification.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/ResourceLoader.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaAnnotated.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaAnnotation.Attribute.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaAnnotation.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaAttributeGroup.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaAttributeGroup.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaAttributeModel.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaBookmark.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaCodePrinter.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaComponent.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaComponent.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaField.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaGlobalAttribute.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaGlobalAttribute.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaGlobalElement.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaGlobalElement.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaIdentityConstraint.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaIdentityConstraint.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaLocalAttribute.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaLocalElement.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaModelGroup.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaModelGroup.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaParticle.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaProperty.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaStringEnumEntry.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaType.Ref.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaType.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaTypeElementSequencer.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaTypeLoader.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaTypeLoaderException.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SchemaTypeSystem.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SimpleValue.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/StringEnumAbstractBase.Table.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/StringEnumAbstractBase.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/SystemProperties.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/UserType.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XMLStreamValidationException.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlAnySimpleType.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlAnySimpleType.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlAnyURI.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlAnyURI.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlBase64Binary.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlBase64Binary.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlBeans.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlBoolean.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlBoolean.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlByte.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlByte.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlCalendar.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlCursor.ChangeStamp.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlCursor.TokenType.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlCursor.XmlBookmark.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlCursor.XmlMark.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlCursor.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDate.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDate.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDateTime.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDateTime.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDecimal.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDecimal.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDocumentProperties.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDouble.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDouble.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDuration.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlDuration.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlENTITIES.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlENTITIES.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlENTITY.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlENTITY.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlError.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlErrorCodes.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlException.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlFactoryHook.ThreadContext.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlFactoryHook.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlFloat.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlFloat.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGDay.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGDay.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGMonth.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGMonth.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGMonthDay.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGMonthDay.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGYear.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGYear.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGYearMonth.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlGYearMonth.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlHexBinary.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlHexBinary.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlID.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlID.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlIDREF.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlIDREF.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlIDREFS.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlIDREFS.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlInt.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlInt.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlInteger.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlInteger.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlLanguage.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlLanguage.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlLineNumber.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlLong.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlLong.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNCName.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNCName.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNMTOKEN.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNMTOKEN.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNMTOKENS.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNMTOKENS.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNOTATION.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNOTATION.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlName.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlName.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNegativeInteger.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNegativeInteger.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNonNegativeInteger.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNonNegativeInteger.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNonPositiveInteger.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNonPositiveInteger.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNormalizedString.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlNormalizedString.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlObject.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlObject.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlOptionCharEscapeMap.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlOptions.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlOptionsBean.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlPositiveInteger.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlPositiveInteger.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlQName.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlQName.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlRuntimeException.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlSaxHandler.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlShort.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlShort.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlSimpleList.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlString.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlString.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlTime.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlTime.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlToken.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlToken.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlTokenSource.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedByte.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedByte.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedInt.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedInt.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedLong.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedLong.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedShort.Factory.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlUnsignedShort.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/XmlValidationError.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/package-frame.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/package-summary.html
/usr/share/javadoc/xmlbeans/org/apache/xmlbeans/package-tree.html
/usr/share/javadoc/xmlbeans/overview-frame.html
/usr/share/javadoc/xmlbeans/overview-summary.html
/usr/share/javadoc/xmlbeans/overview-tree.html
/usr/share/javadoc/xmlbeans/package-list
/usr/share/javadoc/xmlbeans/resources
/usr/share/javadoc/xmlbeans/resources/background.gif
/usr/share/javadoc/xmlbeans/resources/tab.gif
/usr/share/javadoc/xmlbeans/resources/titlebar.gif
/usr/share/javadoc/xmlbeans/resources/titlebar_end.gif
/usr/share/javadoc/xmlbeans/serialized-form.html
/usr/share/javadoc/xmlbeans/stylesheet.css

#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id
rpm2cpio %{SOURCE1} | cpio -id
rpm2cpio %{SOURCE2} | cpio -id
rpm2cpio %{SOURCE3} | cpio -id
