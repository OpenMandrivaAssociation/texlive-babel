Name:		texlive-babel
Version:	72134
Release:	1
Summary:	Multilingual support for Plain TeX or LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/babel/base
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package manages culturally-determined typographical (and
other) rules, and hyphenation patterns for a wide range of
languages. A document may select a single language to be
supported, or it may select several, in which case the document
may switch from one language to another in a variety of ways.
Babel uses contributed configuration files that provide the
detail of what has to be done for each language. Users of XeTeX
are advised to use polyglossia rather than Babel.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/babel
%{_texmfdistdir}/tex/generic/babel
%doc %{_texmfdistdir}/doc/latex/babel
#- source
%doc %{_texmfdistdir}/source/latex/babel

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
