%define name	gf2x
%define major	1
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Name:		%{name}
Version:	1.0
Release:	%mkrel 1
Group:		Sciences/Mathematics
License:	GPL
Summary:	Library for multiplying polynomials over the binary field
Source0:	http://gforge.inria.fr/frs/download.php/27999/gf2x-1.0.tar.gz
URL:		http://gforge.inria.fr/projects/gf2x/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libgmp-devel
BuildRequires:	ntl-devel

%package	-n %{libname}
Group:		System/Libraries
License:	GPL
Summary:	Library for multiplying polynomials over the binary field
Provides:	lib%{name} = %{version}-%{release}

%description	-n %{libname}
Library for multiplying polynomials over the binary field.
This package contains the gf2x runtime library.

%package	-n %{devname}
Group:		Development/C
License:	GOL
Summary:	Library for multiplying polynomials over the binary field
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	lib%{name} = %{version}-%{release}

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

%clean
rm -rf %{buildroot}

%files		-n %{libname}
%defattr(-,root,root)
%{_libdir}/libgf2x.so.*

%files		-n %{devname}
%defattr(-,root,root)
%{_includedir}/*.h
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libgf2x.la
%{_libdir}/libgf2x.so
