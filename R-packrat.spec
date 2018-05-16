#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-packrat
Version  : 0.4.9.2
Release  : 9
URL      : https://cran.r-project.org/src/contrib/packrat_0.4.9-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/packrat_0.4.9-2.tar.gz
Summary  : A Dependency Management System for Projects and their R Package
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
on in an isolated, portable, and reproducible way.

%prep
%setup -q -c -n packrat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524231218

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1524231218
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library packrat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library packrat
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library packrat
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library packrat|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/packrat/DESCRIPTION
/usr/lib64/R/library/packrat/INDEX
/usr/lib64/R/library/packrat/Meta/Rd.rds
/usr/lib64/R/library/packrat/Meta/features.rds
/usr/lib64/R/library/packrat/Meta/hsearch.rds
/usr/lib64/R/library/packrat/Meta/links.rds
/usr/lib64/R/library/packrat/Meta/nsInfo.rds
/usr/lib64/R/library/packrat/Meta/package.rds
/usr/lib64/R/library/packrat/NAMESPACE
/usr/lib64/R/library/packrat/R/packrat
/usr/lib64/R/library/packrat/R/packrat.rdb
/usr/lib64/R/library/packrat/R/packrat.rdx
/usr/lib64/R/library/packrat/help/AnIndex
/usr/lib64/R/library/packrat/help/aliases.rds
/usr/lib64/R/library/packrat/help/packrat.rdb
/usr/lib64/R/library/packrat/help/packrat.rdx
/usr/lib64/R/library/packrat/help/paths.rds
/usr/lib64/R/library/packrat/html/00Index.html
/usr/lib64/R/library/packrat/html/R.css
/usr/lib64/R/library/packrat/resources/init-rprofile.R
/usr/lib64/R/library/packrat/resources/init.R
/usr/lib64/R/library/packrat/resources/mac_r_userlib.sh
/usr/lib64/R/library/packrat/rstudio/rstudio-protocol
