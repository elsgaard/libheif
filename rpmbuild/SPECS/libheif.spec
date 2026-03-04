Name:           libheif
Version:        1.21.2
Release:        1%{?dist}
Summary:        HEIF/HEIC image format library

License:        LGPLv3+
URL:            https://github.com/strukturag/libheif
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake ninja-build pkgconfig
BuildRequires:  libde265-devel
BuildRequires:  x265-devel

Requires:       libde265
Requires:       x265

%description
libheif is a library for HEIF and HEIC image formats.

%package devel
Summary: Development files for libheif
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and development libraries for libheif.

%package tools
Summary: Command-line tools for libheif
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line utilities for working with HEIF/HEIC images.

%prep
%autosetup

%build
%cmake \
  -DWITH_LIBDE265=ON \
  -DWITH_X265=ON \
  -DWITH_AOM_DECODER=OFF -DWITH_AOM_ENCODER=OFF \
  -DWITH_DAV1D=OFF \
  -DWITH_RAV1E=OFF \
  -DWITH_SvtEnc=OFF \
  -DWITH_OpenJPEG=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_AOM=TRUE \
  -DCMAKE_DISABLE_FIND_PACKAGE_OpenH264=TRUE

%cmake_build

%install
%cmake_install

%files
%license COPYING*
%{_libdir}/libheif.so.*

%files devel
%{_includedir}/libheif
%{_libdir}/libheif.so
%{_libdir}/pkgconfig/libheif.pc
%{_libdir}/cmake/libheif

%files tools
%{_bindir}/heif-*
%{_mandir}/man1/heif-*.1*

%changelog
* Tue Mar 03 2026 Thomas <thomas.elsgaard@gmail.com> - 1.21.2-1
- Initial HEIC-only build for AlmaLinux 10
