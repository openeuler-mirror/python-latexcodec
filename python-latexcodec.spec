Name:           python-latexcodec
Version:        1.0.5
Release:        6
Summary:        A lexer and codec to work with LaTeX code in Python.

License:        MIT
URL:            https://github.com/mcmtroffaes/latexcodec/
Source0:        https://files.pythonhosted.org/packages/source/l/latexcodec/latexcodec-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel python2-nose python2-setuptools python2-six python2-sphinx
BuildRequires:  python3-devel python3-nose python3-nose-cov python3-setuptools python3-six python3-sphinx

%description
The codec provides a convenient way of going between text written in LaTeX and unicode. Since it is not a LaTeX
compiler, it is more appropriate for short chunks of text, such as a paragraph or the values of a BibTeX entry,
and it is not appropriate for a full LaTeX document.

%package -n python2-latexcodec
Summary:        A lexer and codec to work with LaTeX code in Python.
Requires:       python2-six

Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%python_provide python2-latexcodec

%description -n python2-latexcodec
The codec provides a convenient way of going between text written in LaTeX and unicode. Since it is not a LaTeX
compiler, it is more appropriate for short chunks of text, such as a paragraph or the values of a BibTeX entry,
and it is not appropriate for a full LaTeX document.

%package -n python3-latexcodec
Summary:        A lexer and codec to work with LaTeX code in Python.
Requires:       python3-six

Provides:       bundled(jquery)
Provides:       bundled(js-underscore)
%python_provide python3-latexcodec

%description -n python3-latexcodec
The codec provides a convenient way of going between text written in LaTeX and unicode. Since it is not a LaTeX
compiler, it is more appropriate for short chunks of text, such as a paragraph or the values of a BibTeX entry,
and it is not appropriate for a full LaTeX document.

%prep
%autosetup -n latexcodec-%{version} -p1 -c
sed -i 's/"rb"/"rt"/' latexcodec-%{version}/doc/conf.py
cp -a latexcodec-%{version} python3-latexcodec-%{version}

%build
cd latexcodec-%{version}
%py2_build
PYTHONPATH=$PWD make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build
rm -f doc/_build/html/.buildinfo
cd ..

cd python3-latexcodec-%{version}
%py3_build
PYTHONPATH=$PWD make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build-3
rm -f doc/_build/html/.buildinfo
cd ..

%install
cd latexcodec-%{version}
%py2_install
cd ..

cd python3-latexcodec-%{version}
%py3_install
cd ..

%check
cd latexcodec-%{version}
nosetests-%{python2_version} -v
cd ..

cd python3-latexcodec-%{version}
nosetests-%{python3_version} -v
cd ..

%files -n python2-latexcodec
%doc latexcodec-%{version}/doc/_build/html/* latexcodec-%{version}/LICENSE.rst
%{python2_sitelib}/latexcodec*


%files -n python3-latexcodec
%doc python3-latexcodec-%{version}/doc/_build/html/* python3-latexcodec-%{version}/LICENSE.rst
%{python3_sitelib}/latexcodec*

%changelog
* Thu Mar 5 2020 chenli <chenli147@huawei.com> - 1.0.5-6
- Init Package.

