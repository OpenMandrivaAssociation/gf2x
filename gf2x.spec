%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		gf2x
Version:	1.1
Release:	3
Group:		Sciences/Mathematics
License:	GPL
Summary:	Library for multiplying polynomials over the binary field
Source0:	http://gforge.inria.fr/frs/download.php/27999/%{name}-%{version}.tar.gz
URL:		http://gforge.inria.fr/projects/gf2x/
BuildRequires:	gmp-devel

%package	-n %{libname}
Group:		System/Libraries
License:	GPL
Summary:	Library for multiplying polynomials over the binary field

%description	-n %{libname}
Library for multiplying polynomials over the binary field.
This package contains the gf2x runtime library.

%package	-n %{devname}
Group:		Development/C
License:	GOL
Summary:	Library for multiplying polynomials over the binary field
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description	-n %{devname}
Library for multiplying polynomials over the binary field.
This package contains the gf2x development files.

%description
gf2x is a library for multiplying polynomials over the binary field.

%prep
%setup -q

%build
# don't disable sse2 by default - this mean it may need to be rebuilt
# from source on pentium 3 or older
%configure2_5x --disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libgf2x.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libgf2x.so

