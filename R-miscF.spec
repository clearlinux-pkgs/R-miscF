#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-miscF
Version  : 0.1.5
Release  : 21
URL      : https://cran.r-project.org/src/contrib/miscF_0.1-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/miscF_0.1-5.tar.gz
Summary  : Miscellaneous Functions
Group    : Development/Tools
License  : GPL-2.0
Requires: R-miscF-lib = %{version}-%{release}
Requires: R-MCMCpack
Requires: R-R2jags
Requires: R-mvtnorm
BuildRequires : R-MCMCpack
BuildRequires : R-R2jags
BuildRequires : R-mvtnorm
BuildRequires : buildreq-R

%description
estimation, classification, curve fitting, and spatial 
             data analysis.

%package lib
Summary: lib components for the R-miscF package.
Group: Libraries

%description lib
lib components for the R-miscF package.


%prep
%setup -q -c -n miscF
cd %{_builddir}/miscF

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589581143

%install
export SOURCE_DATE_EPOCH=1589581143
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miscF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miscF
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library miscF
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc miscF || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/miscF/DESCRIPTION
/usr/lib64/R/library/miscF/INDEX
/usr/lib64/R/library/miscF/Meta/Rd.rds
/usr/lib64/R/library/miscF/Meta/features.rds
/usr/lib64/R/library/miscF/Meta/hsearch.rds
/usr/lib64/R/library/miscF/Meta/links.rds
/usr/lib64/R/library/miscF/Meta/nsInfo.rds
/usr/lib64/R/library/miscF/Meta/package.rds
/usr/lib64/R/library/miscF/NAMESPACE
/usr/lib64/R/library/miscF/R/miscF
/usr/lib64/R/library/miscF/R/miscF.rdb
/usr/lib64/R/library/miscF/R/miscF.rdx
/usr/lib64/R/library/miscF/help/AnIndex
/usr/lib64/R/library/miscF/help/aliases.rds
/usr/lib64/R/library/miscF/help/miscF.rdb
/usr/lib64/R/library/miscF/help/miscF.rdx
/usr/lib64/R/library/miscF/help/paths.rds
/usr/lib64/R/library/miscF/html/00Index.html
/usr/lib64/R/library/miscF/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/miscF/libs/miscF.so
/usr/lib64/R/library/miscF/libs/miscF.so.avx2
/usr/lib64/R/library/miscF/libs/miscF.so.avx512
