# Build the latest libheif source into RPMs
This guide shows how to build libheif from an upstream release tarball into RPM packages on an RPM-based distro such as RHEL, Rocky, AlmaLinux, or Fedora.

Install required build tools
```shell
sudo dnf -y install dnf-plugins-core rpmdevtools rpmlint
sudo dnf config-manager --set-enabled crb
sudo dnf -y groupinstall "Development Tools"
sudo dnf -y install cmake ninja-build pkgconfig curl libde265 libde265-devel x265 x265-devel
```

# Create the RPM build tree
```console
rpmdev-setuptree
```


# This creates
```plain text
~/rpmbuild/
├── BUILD
├── BUILDROOT
├── RPMS
├── SOURCES
├── SPECS
└── SRPMS
```

# Download the libheif source tarball
Replace the version below with the version you want to build.
```shell
curl -L -o libheif-1.21.2.tar.gz https://github.com/strukturag/libheif/releases/download/v1.21.2/libheif-1.21.2.tar.gz
cp libheif-1.21.2.tar.gz ~/rpmbuild/SOURCES/
```

# Create or update the spec file
Create ~/rpmbuild/SPECS/libheif.spec and ensure the Version: and Source0: entries match the tarball you downloaded.
Example CMake build options for enabling libde265 and x265 while disabling optional codecs you do not want:

```spec
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
```

# Build the RPMs
```console
cd ~/rpmbuild/SPECS
rpmbuild -ba libheif.spec
```

The resulting RPMs will be placed under:
```plain text
~/rpmbuild/RPMS/$(uname -m)/
```

The source RPMs will be placed under:
```plain text
~/rpmbuild/SRPMS/
```




