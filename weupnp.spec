Summary:	A tiny UPnP client library written in Java
Name:		weupnp
Version:	0.1.4
Release:	1
License:	LGPLv2.1+
Group:		Development/Java
URL:		https://bitletorg.github.io/%{name}/
Source0:	https://github.com/bitletorg/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom:)

Requires:	java-headless
Requires:	jpackage-utils

%description
Weupnp is a lightweight Java library designed to implement the UPnP protocol
to handle port mappings on Gateway Devices.

%files -f .mfiles
%doc README.md
%doc src/main/resources/license.txt

#----------------------------------------------------------------------------

%package		javadoc
Summary:		Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{name}-%{version}
# Delete prebuild JARs and classes
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Set the right name to fit the packaging guidelines
%mvn_file :%{name} %{name}-%{version} %{name}

%build
%mvn_build

%install
%mvn_install

