%define debug_package %{nil}
%define module	encore

Summary:	Enthought Tool Suite - scimath project
Name:		python-%{module}
Version:	0.3
Release:	3.3
Source0:	https://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	LGPL-2.1 and Apache-2.0
Group:		Development/Python
Url:		https://github.com/enthought/encore/
BuildRequires:  fdupes
BuildRequires:	python-sphinx
BuildRequires:  python-pygraphviz
BuildRequires:  python-setuptools
%description
This package consists of a collection of core utility packages useful for
building Python applications.  This package is intended to be at the
bottom of the software stack and have zero required external dependencies
aside from the Python Standard Library.

Part of the Enthought Tool Suite (ETS).

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
%fdupes -s %{buildroot}

%files 
%defattr(-,root,root,-)
%doc LICENSE.txt  README.rst dataflow.txt
%doc examples/
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{py_ver}.egg-info/
