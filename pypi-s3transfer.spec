#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-s3transfer
Version  : 0.5.1
Release  : 61
URL      : https://files.pythonhosted.org/packages/66/e2/cc19f36aade1ef40cba69555fcf713d942ec9e31ecff2415948bd885911d/s3transfer-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/e2/cc19f36aade1ef40cba69555fcf713d942ec9e31ecff2415948bd885911d/s3transfer-0.5.1.tar.gz
Summary  : An Amazon S3 Transfer Manager
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-s3transfer-license = %{version}-%{release}
Requires: pypi-s3transfer-python = %{version}-%{release}
Requires: pypi-s3transfer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(botocore)

%description
=====================================================
s3transfer - An Amazon S3 Transfer Manager for Python
=====================================================

%package license
Summary: license components for the pypi-s3transfer package.
Group: Default

%description license
license components for the pypi-s3transfer package.


%package python
Summary: python components for the pypi-s3transfer package.
Group: Default
Requires: pypi-s3transfer-python3 = %{version}-%{release}

%description python
python components for the pypi-s3transfer package.


%package python3
Summary: python3 components for the pypi-s3transfer package.
Group: Default
Requires: python3-core
Provides: pypi(s3transfer)
Requires: pypi(botocore)

%description python3
python3 components for the pypi-s3transfer package.


%prep
%setup -q -n s3transfer-0.5.1
cd %{_builddir}/s3transfer-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643907364
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-s3transfer
cp %{_builddir}/s3transfer-0.5.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-s3transfer/2b8b815229aa8a61e483fb4ba0588b8b6c491890
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-s3transfer/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
