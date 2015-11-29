#TODO: Add docs, package examples
%define		module	processing
Summary:	Package for using processes which mimics the threading module
Summary(pl.UTF-8):	Pakiet używający procesów do naśladownia modułu threading
Name:		python-%{module}
Version:	0.52
Release:	4
License:	BSD
Group:		Development/Languages/Python
Source0:	http://download.berlios.de/pyprocessing/%{module}-%{version}.zip
# Source0-md5:	62772fa3002d003b2395ed669072d51d
URL:		http://pyprocessing.berlios.de/
BuildRequires:	python-devel
%if "%{py_ver}" < "2.5"
BuildRequires:	python-ctypes
%endif

BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
%if "%{py_ver}" < "2.5"
Requires:	python-ctypes
%endif

#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package for the Python language which supports the spawning of
processes using the API of the standard library's threading module. It
runs on both Unix and Windows.

%description -l pl.UTF-8
Pakiet Pythona który pozwala na tworzenie procesów używająć API z
modułu threading. Działa na Unixach i Windowsach.


%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/_processing.so
%{py_sitedir}/%{module}/dummy


%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
