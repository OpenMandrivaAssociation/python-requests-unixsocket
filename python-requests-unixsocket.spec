Name:		python-requests-unixsocket
Version:	0.4.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/r/requests_unixsocket/requests_unixsocket-%{version}.tar.gz
Summary:	Use requests to talk HTTP via a UNIX domain socket
URL:		https://pypi.org/project/requests_unixsocket/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Use requests to talk HTTP via a UNIX domain socket

%files
%{py_sitedir}/requests_unixsocket
%{py_sitedir}/requests_unixsocket-*.*-info
