# revision 32311
# category Package
# catalog-ctan /macros/latex/required/babel/base
# catalog-date 2013-12-03 18:59:06 +0100
# catalog-license lppl1.3
# catalog-version 3.9h
Name:		texlive-babel
Version:	3.9h
Release:	1
Summary:	Multilingual support for Plain TeX or LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/babel/base
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel.source.tar.xz
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
%{_texmfdistdir}/makeindex/babel/bbglo.ist
%{_texmfdistdir}/makeindex/babel/bbind.ist
%{_texmfdistdir}/tex/generic/babel/UKenglish.sty
%{_texmfdistdir}/tex/generic/babel/USenglish.sty
%{_texmfdistdir}/tex/generic/babel/afrikaans.sty
%{_texmfdistdir}/tex/generic/babel/albanian.sty
%{_texmfdistdir}/tex/generic/babel/american.sty
%{_texmfdistdir}/tex/generic/babel/austrian.sty
%{_texmfdistdir}/tex/generic/babel/babel.def
%{_texmfdistdir}/tex/generic/babel/babel.sty
%{_texmfdistdir}/tex/generic/babel/bahasa.sty
%{_texmfdistdir}/tex/generic/babel/bahasam.sty
%{_texmfdistdir}/tex/generic/babel/basque.sty
%{_texmfdistdir}/tex/generic/babel/blplain.tex
%{_texmfdistdir}/tex/generic/babel/bplain.tex
%{_texmfdistdir}/tex/generic/babel/breton.sty
%{_texmfdistdir}/tex/generic/babel/british.sty
%{_texmfdistdir}/tex/generic/babel/bulgarian.sty
%{_texmfdistdir}/tex/generic/babel/catalan.sty
%{_texmfdistdir}/tex/generic/babel/croatian.sty
%{_texmfdistdir}/tex/generic/babel/czech.sty
%{_texmfdistdir}/tex/generic/babel/danish.sty
%{_texmfdistdir}/tex/generic/babel/dutch.sty
%{_texmfdistdir}/tex/generic/babel/english.sty
%{_texmfdistdir}/tex/generic/babel/esperanto.sty
%{_texmfdistdir}/tex/generic/babel/estonian.sty
%{_texmfdistdir}/tex/generic/babel/finnish.sty
%{_texmfdistdir}/tex/generic/babel/francais.sty
%{_texmfdistdir}/tex/generic/babel/galician.sty
%{_texmfdistdir}/tex/generic/babel/germanb.sty
%{_texmfdistdir}/tex/generic/babel/greek.sty
%{_texmfdistdir}/tex/generic/babel/hebrew.sty
%{_texmfdistdir}/tex/generic/babel/hyphen.cfg
%{_texmfdistdir}/tex/generic/babel/icelandic.sty
%{_texmfdistdir}/tex/generic/babel/interlingua.sty
%{_texmfdistdir}/tex/generic/babel/irish.sty
%{_texmfdistdir}/tex/generic/babel/italian.sty
%{_texmfdistdir}/tex/generic/babel/latin.sty
%{_texmfdistdir}/tex/generic/babel/lsorbian.sty
%{_texmfdistdir}/tex/generic/babel/luababel.def
%{_texmfdistdir}/tex/generic/babel/magyar.sty
%{_texmfdistdir}/tex/generic/babel/naustrian.sty
%{_texmfdistdir}/tex/generic/babel/ngermanb.sty
%{_texmfdistdir}/tex/generic/babel/nil.ldf
%{_texmfdistdir}/tex/generic/babel/norsk.sty
%{_texmfdistdir}/tex/generic/babel/plain.def
%{_texmfdistdir}/tex/generic/babel/polish.sty
%{_texmfdistdir}/tex/generic/babel/portuges.sty
%{_texmfdistdir}/tex/generic/babel/romanian.sty
%{_texmfdistdir}/tex/generic/babel/russianb.sty
%{_texmfdistdir}/tex/generic/babel/samin.sty
%{_texmfdistdir}/tex/generic/babel/scottish.sty
%{_texmfdistdir}/tex/generic/babel/serbian.sty
%{_texmfdistdir}/tex/generic/babel/slovak.sty
%{_texmfdistdir}/tex/generic/babel/slovene.sty
%{_texmfdistdir}/tex/generic/babel/spanish.sty
%{_texmfdistdir}/tex/generic/babel/swedish.sty
%{_texmfdistdir}/tex/generic/babel/switch.def
%{_texmfdistdir}/tex/generic/babel/turkish.sty
%{_texmfdistdir}/tex/generic/babel/ukraineb.sty
%{_texmfdistdir}/tex/generic/babel/usorbian.sty
%{_texmfdistdir}/tex/generic/babel/welsh.sty
%{_texmfdistdir}/tex/generic/babel/xebabel.def
%doc %{_texmfdistdir}/doc/latex/babel/CONTRIB
%doc %{_texmfdistdir}/doc/latex/babel/FIXES39
%doc %{_texmfdistdir}/doc/latex/babel/README
%doc %{_texmfdistdir}/doc/latex/babel/babel.pdf
#- source
%doc %{_texmfdistdir}/source/latex/babel/babel.dtx
%doc %{_texmfdistdir}/source/latex/babel/babel.ins
%doc %{_texmfdistdir}/source/latex/babel/bbcompat.dtx
%doc %{_texmfdistdir}/source/latex/babel/bbidxglo.dtx
%doc %{_texmfdistdir}/source/latex/babel/bbunicode.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
