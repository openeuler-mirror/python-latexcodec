%global bootstrap       0

Name:           python-latexcodec
Version:        2.0.1
Release:        1
Summary:        A lexer and codec to work with LaTeX code in Python.

License:        MIT
URL:            https://github.com/mcmtroffaes/latexcodec/
Source0:        https://files.pythonhosted.org/packages/84/2f/fd47712130b303ff179c819cc5c63aa39586fc8d430bc299c0f5f56ec42c/latexcodec-2.0.1.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel python3-pytest python3-setuptools python3-six python3-sphinx
%if ! %{bootstrap}
BuildRequires:  python3-latexcodec
%endif

%description
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

%build
cd latexcodec-%{version}
%py3_build
PYTHONPATH=$PWD make -C doc html SPHINXBUILD=%{_bindir}/sphinx-build-3
rm -f doc/_build/html/.buildinfo
cd ..

%install
cd latexcodec-%{version}
%py3_install
cd ..

%if ! %{bootstrap}
%check
pytest
%endif

%files -n python3-latexcodec
%doc latexcodec-%{version}/doc/_build/html/* latexcodec-%{version}/LICENSE.rst
%{python3_sitelib}/latexcodec*

%changelog
* Tue May 31 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 2.0.1-1
- update to 2.0.1

* Thu Mar 5 2020 chenli <chenli147@huawei.com> - 1.0.5-6
- Init Package.

