#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-build-helper-maven-plugin
Version  : 1.12
Release  : 1
URL      : https://repo1.maven.org/maven2/org/codehaus/mojo/build-helper-maven-plugin/1.12/build-helper-maven-plugin-1.12.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/mojo/build-helper-maven-plugin/1.12/build-helper-maven-plugin-1.12.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/mojo/build-helper-maven-plugin/1.12/build-helper-maven-plugin-1.12.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-build-helper-maven-plugin-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-build-helper-maven-plugin package.
Group: Data

%description data
data components for the mvn-build-helper-maven-plugin package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/build-helper-maven-plugin/1.12
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/build-helper-maven-plugin/1.12

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/build-helper-maven-plugin/1.12
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/build-helper-maven-plugin/1.12


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/mojo/build-helper-maven-plugin/1.12/build-helper-maven-plugin-1.12.jar
/usr/share/java/.m2/repository/org/codehaus/mojo/build-helper-maven-plugin/1.12/build-helper-maven-plugin-1.12.pom
