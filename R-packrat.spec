#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-packrat
Version  : 0.5.0
Release  : 29
URL      : https://cran.r-project.org/src/contrib/packrat_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/packrat_0.5.0.tar.gz
Summary  : A Dependency Management System for Projects and their R Package
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
on in an isolated, portable, and reproducible way.

%prep
%setup -q -c -n packrat
cd %{_builddir}/packrat

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589576235

%install
export SOURCE_DATE_EPOCH=1589576235
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc packrat || :


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
/usr/lib64/R/library/packrat/tests/test-all.R
/usr/lib64/R/library/packrat/tests/test-cranlike-repositories.R
"/usr/lib64/R/library/packrat/tests/testthat/Ugly, but legal, path for a project (long)/bread/DESCRIPTION"
"/usr/lib64/R/library/packrat/tests/testthat/Ugly, but legal, path for a project (long)/breakfast/DESCRIPTION"
"/usr/lib64/R/library/packrat/tests/testthat/Ugly, but legal, path for a project (long)/oatmeal/DESCRIPTION"
"/usr/lib64/R/library/packrat/tests/testthat/Ugly, but legal, path for a project (long)/packrat/DESCRIPTION"
"/usr/lib64/R/library/packrat/tests/testthat/Ugly, but legal, path for a project (long)/toast/DESCRIPTION"
/usr/lib64/R/library/packrat/tests/testthat/lockfiles/lockfile-multipleRepos.txt
/usr/lib64/R/library/packrat/tests/testthat/other-packages/packrat/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/packages/bread/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/packages/breakfast/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/packages/egg/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/packages/oatmeal/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/packages/packrat/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/packages/toast/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/projects/carbs/flour.R
/usr/lib64/R/library/packrat/tests/testthat/projects/empty/empty.R
/usr/lib64/R/library/packrat/tests/testthat/projects/emptydesc/DESCRIPTION
/usr/lib64/R/library/packrat/tests/testthat/projects/emptydesc/app.R
/usr/lib64/R/library/packrat/tests/testthat/projects/healthy/healthy.R
/usr/lib64/R/library/packrat/tests/testthat/projects/libraries/library.R
/usr/lib64/R/library/packrat/tests/testthat/projects/libraries/packrat/lib/lib-current.R
/usr/lib64/R/library/packrat/tests/testthat/projects/libraries/packrat/library.new/lib-new.R
/usr/lib64/R/library/packrat/tests/testthat/projects/partlyignored/ignoreme/ignorethis.R
/usr/lib64/R/library/packrat/tests/testthat/projects/partlyignored/notignored.R
/usr/lib64/R/library/packrat/tests/testthat/projects/sated/sated.R
/usr/lib64/R/library/packrat/tests/testthat/projects/smallbreakfast/bread.R
/usr/lib64/R/library/packrat/tests/testthat/projects/smallbreakfast/oatmeal.R
/usr/lib64/R/library/packrat/tests/testthat/repo-empty/src/contrib/PACKAGES
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/PACKAGES
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/PACKAGES.gz
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/PACKAGES.rds
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/bread/bread_1.0.0.tar.gz
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/breakfast/breakfast_1.0.0.tar.gz
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/egg/egg_1.0.0.tar.gz
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/oatmeal/oatmeal_1.0.0.tar.gz
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/packrat/packrat_0.4.9-15.tar.gz
/usr/lib64/R/library/packrat/tests/testthat/repo/src/contrib/toast/toast_1.0.0.tar.gz
/usr/lib64/R/library/packrat/tests/testthat/resources/alternate-engines.Rmd
/usr/lib64/R/library/packrat/tests/testthat/resources/emoji.Rmd
/usr/lib64/R/library/packrat/tests/testthat/resources/evaluate-deps.Rmd
/usr/lib64/R/library/packrat/tests/testthat/resources/interactive-doc-example.Rmd
/usr/lib64/R/library/packrat/tests/testthat/resources/knitr-minimal.Rnw
/usr/lib64/R/library/packrat/tests/testthat/resources/no-chunks.Rmd
/usr/lib64/R/library/packrat/tests/testthat/resources/params-example.Rmd
/usr/lib64/R/library/packrat/tests/testthat/resources/test-sweave.Rnw
/usr/lib64/R/library/packrat/tests/testthat/test-aaa.R
/usr/lib64/R/library/packrat/tests/testthat/test-bitbucket.R
/usr/lib64/R/library/packrat/tests/testthat/test-bundle.R
/usr/lib64/R/library/packrat/tests/testthat/test-cache.R
/usr/lib64/R/library/packrat/tests/testthat/test-dependencies.R
/usr/lib64/R/library/packrat/tests/testthat/test-downloader.R
/usr/lib64/R/library/packrat/tests/testthat/test-git.R
/usr/lib64/R/library/packrat/tests/testthat/test-github.R
/usr/lib64/R/library/packrat/tests/testthat/test-hash.R
/usr/lib64/R/library/packrat/tests/testthat/test-ignores.R
/usr/lib64/R/library/packrat/tests/testthat/test-local-repositories.R
/usr/lib64/R/library/packrat/tests/testthat/test-lockfile.R
/usr/lib64/R/library/packrat/tests/testthat/test-packrat-mode.R
/usr/lib64/R/library/packrat/tests/testthat/test-packrat.R
/usr/lib64/R/library/packrat/tests/testthat/test-rmarkdown.R
/usr/lib64/R/library/packrat/tests/testthat/test-shiny.R
/usr/lib64/R/library/packrat/tests/testthat/test-utils.R
/usr/lib64/R/library/packrat/tests/testthat/test-with_extlib.R
