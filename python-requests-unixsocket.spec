%define module requests-unixsocket
%define oname requests_unixsocket

Name:		python-requests-unixsocket
Version:	0.4.1
Release:	2
Summary:	Use requests to talk HTTP via a UNIX domain socket
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/requests_unixsocket
Source0:	https://files.pythonhosted.org/packages/source/r/%{oname}/%{oname}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
Use requests to talk HTTP via a UNIX domain socket

%files
%{py_sitedir}/%{oname}
%{py_sitedir}/%{oname}-%{version}.dist-info
