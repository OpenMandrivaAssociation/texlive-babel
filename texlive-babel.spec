# revision 24756
# category Package
# catalog-ctan /macros/latex/required/babel
# catalog-date 2011-10-07 15:38:55 +0200
# catalog-license lppl
# catalog-version 3.8m
Name:		texlive-babel
Version:	3.8m
Release:	2
Summary:	Multilingual support for Plain TeX or LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/required/babel
License:	LPPL
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
Note that the package has contributions for several languages
that remain to be incorporated. Examples are: Arabic; Magyar
(Hungarian); Serbian written in cyrillic; Spanish; and Spanish,
using Mexican conventions.. Users of XeTeX are advised to use
polyglossia rather than Babel.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/babel/bbglo.ist
%{_texmfdistdir}/makeindex/babel/bbind.ist
%{_texmfdistdir}/tex/generic/babel/8859-8.def
%{_texmfdistdir}/tex/generic/babel/UKenglish.sty
%{_texmfdistdir}/tex/generic/babel/USenglish.sty
%{_texmfdistdir}/tex/generic/babel/afrikaans.sty
%{_texmfdistdir}/tex/generic/babel/albanian.ldf
%{_texmfdistdir}/tex/generic/babel/albanian.sty
%{_texmfdistdir}/tex/generic/babel/american.sty
%{_texmfdistdir}/tex/generic/babel/athnum.sty
%{_texmfdistdir}/tex/generic/babel/austrian.sty
%{_texmfdistdir}/tex/generic/babel/babel.def
%{_texmfdistdir}/tex/generic/babel/babel.sty
%{_texmfdistdir}/tex/generic/babel/bahasa.sty
%{_texmfdistdir}/tex/generic/babel/bahasai.ldf
%{_texmfdistdir}/tex/generic/babel/bahasam.ldf
%{_texmfdistdir}/tex/generic/babel/bahasam.sty
%{_texmfdistdir}/tex/generic/babel/basque.ldf
%{_texmfdistdir}/tex/generic/babel/basque.sty
%{_texmfdistdir}/tex/generic/babel/blplain.tex
%{_texmfdistdir}/tex/generic/babel/bplain.tex
%{_texmfdistdir}/tex/generic/babel/breton.ldf
%{_texmfdistdir}/tex/generic/babel/breton.sty
%{_texmfdistdir}/tex/generic/babel/british.sty
%{_texmfdistdir}/tex/generic/babel/bulgarian.ldf
%{_texmfdistdir}/tex/generic/babel/bulgarian.sty
%{_texmfdistdir}/tex/generic/babel/catalan.ldf
%{_texmfdistdir}/tex/generic/babel/catalan.sty
%{_texmfdistdir}/tex/generic/babel/cp1255.def
%{_texmfdistdir}/tex/generic/babel/cp862.def
%{_texmfdistdir}/tex/generic/babel/croatian.ldf
%{_texmfdistdir}/tex/generic/babel/croatian.sty
%{_texmfdistdir}/tex/generic/babel/czech.ldf
%{_texmfdistdir}/tex/generic/babel/czech.sty
%{_texmfdistdir}/tex/generic/babel/danish.ldf
%{_texmfdistdir}/tex/generic/babel/danish.sty
%{_texmfdistdir}/tex/generic/babel/dutch.ldf
%{_texmfdistdir}/tex/generic/babel/dutch.sty
%{_texmfdistdir}/tex/generic/babel/english.ldf
%{_texmfdistdir}/tex/generic/babel/english.sty
%{_texmfdistdir}/tex/generic/babel/esperanto.ldf
%{_texmfdistdir}/tex/generic/babel/esperanto.sty
%{_texmfdistdir}/tex/generic/babel/estonian.ldf
%{_texmfdistdir}/tex/generic/babel/estonian.sty
%{_texmfdistdir}/tex/generic/babel/finnish.ldf
%{_texmfdistdir}/tex/generic/babel/finnish.sty
%{_texmfdistdir}/tex/generic/babel/francais.sty
%{_texmfdistdir}/tex/generic/babel/frenchb.cfg
%{_texmfdistdir}/tex/generic/babel/frenchb.ldf
%{_texmfdistdir}/tex/generic/babel/galician.ldf
%{_texmfdistdir}/tex/generic/babel/galician.sty
%{_texmfdistdir}/tex/generic/babel/germanb.ldf
%{_texmfdistdir}/tex/generic/babel/germanb.sty
%{_texmfdistdir}/tex/generic/babel/glbst.tex
%{_texmfdistdir}/tex/generic/babel/glromidx.tex
%{_texmfdistdir}/tex/generic/babel/greek.ldf
%{_texmfdistdir}/tex/generic/babel/greek.sty
%{_texmfdistdir}/tex/generic/babel/grmath.sty
%{_texmfdistdir}/tex/generic/babel/grsymb.sty
%{_texmfdistdir}/tex/generic/babel/he8OmegaHebrew.fd
%{_texmfdistdir}/tex/generic/babel/he8aharoni.fd
%{_texmfdistdir}/tex/generic/babel/he8cmr.fd
%{_texmfdistdir}/tex/generic/babel/he8cmss.fd
%{_texmfdistdir}/tex/generic/babel/he8cmtt.fd
%{_texmfdistdir}/tex/generic/babel/he8david.fd
%{_texmfdistdir}/tex/generic/babel/he8drugulin.fd
%{_texmfdistdir}/tex/generic/babel/he8enc.def
%{_texmfdistdir}/tex/generic/babel/he8frankruehl.fd
%{_texmfdistdir}/tex/generic/babel/he8miriam.fd
%{_texmfdistdir}/tex/generic/babel/he8nachlieli.fd
%{_texmfdistdir}/tex/generic/babel/he8yad.fd
%{_texmfdistdir}/tex/generic/babel/hebcal.sty
%{_texmfdistdir}/tex/generic/babel/hebfont.sty
%{_texmfdistdir}/tex/generic/babel/hebrew.ldf
%{_texmfdistdir}/tex/generic/babel/hebrew.sty
%{_texmfdistdir}/tex/generic/babel/hebrew_newcode.sty
%{_texmfdistdir}/tex/generic/babel/hebrew_oldcode.sty
%{_texmfdistdir}/tex/generic/babel/hebrew_p.sty
%{_texmfdistdir}/tex/generic/babel/hyphen.cfg
%{_texmfdistdir}/tex/generic/babel/icelandic.ldf
%{_texmfdistdir}/tex/generic/babel/icelandic.sty
%{_texmfdistdir}/tex/generic/babel/interlingua.ldf
%{_texmfdistdir}/tex/generic/babel/interlingua.sty
%{_texmfdistdir}/tex/generic/babel/irish.ldf
%{_texmfdistdir}/tex/generic/babel/irish.sty
%{_texmfdistdir}/tex/generic/babel/italian.ldf
%{_texmfdistdir}/tex/generic/babel/italian.sty
%{_texmfdistdir}/tex/generic/babel/kurmanji.ldf
%{_texmfdistdir}/tex/generic/babel/latin.ldf
%{_texmfdistdir}/tex/generic/babel/latin.sty
%{_texmfdistdir}/tex/generic/babel/lgrcmr.fd
%{_texmfdistdir}/tex/generic/babel/lgrcmro.fd
%{_texmfdistdir}/tex/generic/babel/lgrcmss.fd
%{_texmfdistdir}/tex/generic/babel/lgrcmtt.fd
%{_texmfdistdir}/tex/generic/babel/lgrenc.def
%{_texmfdistdir}/tex/generic/babel/lgrlcmss.fd
%{_texmfdistdir}/tex/generic/babel/lgrlcmtt.fd
%{_texmfdistdir}/tex/generic/babel/lgrlmr.fd
%{_texmfdistdir}/tex/generic/babel/lgrlmro.fd
%{_texmfdistdir}/tex/generic/babel/lgrlmss.fd
%{_texmfdistdir}/tex/generic/babel/lgrlmtt.fd
%{_texmfdistdir}/tex/generic/babel/lheclas.fd
%{_texmfdistdir}/tex/generic/babel/lhecmr.fd
%{_texmfdistdir}/tex/generic/babel/lhecmss.fd
%{_texmfdistdir}/tex/generic/babel/lhecmtt.fd
%{_texmfdistdir}/tex/generic/babel/lhecrml.fd
%{_texmfdistdir}/tex/generic/babel/lheenc.def
%{_texmfdistdir}/tex/generic/babel/lhefr.fd
%{_texmfdistdir}/tex/generic/babel/lheredis.fd
%{_texmfdistdir}/tex/generic/babel/lheshold.fd
%{_texmfdistdir}/tex/generic/babel/lheshscr.fd
%{_texmfdistdir}/tex/generic/babel/lheshstk.fd
%{_texmfdistdir}/tex/generic/babel/lsorbian.ldf
%{_texmfdistdir}/tex/generic/babel/lsorbian.sty
%{_texmfdistdir}/tex/generic/babel/magyar.ldf
%{_texmfdistdir}/tex/generic/babel/magyar.sty
%{_texmfdistdir}/tex/generic/babel/naustrian.sty
%{_texmfdistdir}/tex/generic/babel/ngermanb.ldf
%{_texmfdistdir}/tex/generic/babel/ngermanb.sty
%{_texmfdistdir}/tex/generic/babel/norsk.ldf
%{_texmfdistdir}/tex/generic/babel/norsk.sty
%{_texmfdistdir}/tex/generic/babel/plain.def
%{_texmfdistdir}/tex/generic/babel/polish.ldf
%{_texmfdistdir}/tex/generic/babel/polish.sty
%{_texmfdistdir}/tex/generic/babel/portuges.ldf
%{_texmfdistdir}/tex/generic/babel/portuges.sty
%{_texmfdistdir}/tex/generic/babel/rlbabel.def
%{_texmfdistdir}/tex/generic/babel/romanian.ldf
%{_texmfdistdir}/tex/generic/babel/romanian.sty
%{_texmfdistdir}/tex/generic/babel/romanidx.sty
%{_texmfdistdir}/tex/generic/babel/russianb.ldf
%{_texmfdistdir}/tex/generic/babel/russianb.sty
%{_texmfdistdir}/tex/generic/babel/samin.ldf
%{_texmfdistdir}/tex/generic/babel/samin.sty
%{_texmfdistdir}/tex/generic/babel/scottish.ldf
%{_texmfdistdir}/tex/generic/babel/scottish.sty
%{_texmfdistdir}/tex/generic/babel/serbian.ldf
%{_texmfdistdir}/tex/generic/babel/serbian.sty
%{_texmfdistdir}/tex/generic/babel/si960.def
%{_texmfdistdir}/tex/generic/babel/slovak.ldf
%{_texmfdistdir}/tex/generic/babel/slovak.sty
%{_texmfdistdir}/tex/generic/babel/slovene.ldf
%{_texmfdistdir}/tex/generic/babel/slovene.sty
%{_texmfdistdir}/tex/generic/babel/spanish.ldf
%{_texmfdistdir}/tex/generic/babel/spanish.sty
%{_texmfdistdir}/tex/generic/babel/swedish.ldf
%{_texmfdistdir}/tex/generic/babel/swedish.sty
%{_texmfdistdir}/tex/generic/babel/switch.def
%{_texmfdistdir}/tex/generic/babel/turkish.ldf
%{_texmfdistdir}/tex/generic/babel/turkish.sty
%{_texmfdistdir}/tex/generic/babel/ukraineb.ldf
%{_texmfdistdir}/tex/generic/babel/ukraineb.sty
%{_texmfdistdir}/tex/generic/babel/usorbian.ldf
%{_texmfdistdir}/tex/generic/babel/usorbian.sty
%{_texmfdistdir}/tex/generic/babel/welsh.ldf
%{_texmfdistdir}/tex/generic/babel/welsh.sty
%doc %{_texmfdistdir}/doc/generic/babel/00readme.heb
%doc %{_texmfdistdir}/doc/generic/babel/00readme.txt
%doc %{_texmfdistdir}/doc/generic/babel/GreekFonts.txt
%doc %{_texmfdistdir}/doc/generic/babel/announce.txt
%doc %{_texmfdistdir}/doc/generic/babel/athnum.pdf
%doc %{_texmfdistdir}/doc/generic/babel/babel.pdf
%doc %{_texmfdistdir}/doc/generic/babel/bbcompat.pdf
%doc %{_texmfdistdir}/doc/generic/babel/bbidxglo.pdf
%doc %{_texmfdistdir}/doc/generic/babel/bugs.txt
%doc %{_texmfdistdir}/doc/generic/babel/changes.txt
%doc %{_texmfdistdir}/doc/generic/babel/fixes.txt
%doc %{_texmfdistdir}/doc/generic/babel/greek-fdd.pdf
%doc %{_texmfdistdir}/doc/generic/babel/greek-usage.pdf
%doc %{_texmfdistdir}/doc/generic/babel/grmath.pdf
%doc %{_texmfdistdir}/doc/generic/babel/grsymb.pdf
%doc %{_texmfdistdir}/doc/generic/babel/howtoget.txt
%doc %{_texmfdistdir}/doc/generic/babel/install.OzTeX-4
%doc %{_texmfdistdir}/doc/generic/babel/install.OzTeX-pre4
%doc %{_texmfdistdir}/doc/generic/babel/install.txt
%doc %{_texmfdistdir}/doc/generic/babel/language.dat
%doc %{_texmfdistdir}/doc/generic/babel/language.skeleton
%doc %{_texmfdistdir}/doc/generic/babel/legal.bbl
%doc %{_texmfdistdir}/doc/generic/babel/manifest.bbl
%doc %{_texmfdistdir}/doc/generic/babel/tb1202.pdf
%doc %{_texmfdistdir}/doc/generic/babel/tb1401.pdf
%doc %{_texmfdistdir}/doc/generic/babel/tb1604.pdf
%doc %{_texmfdistdir}/doc/generic/babel/todo.txt
#- source
%doc %{_texmfdistdir}/source/generic/babel/albanian.dtx
%doc %{_texmfdistdir}/source/generic/babel/albanian.ins
%doc %{_texmfdistdir}/source/generic/babel/athnum.dtx
%doc %{_texmfdistdir}/source/generic/babel/babel.dtx
%doc %{_texmfdistdir}/source/generic/babel/babel.ins
%doc %{_texmfdistdir}/source/generic/babel/bahasa.dtx
%doc %{_texmfdistdir}/source/generic/babel/bahasa.ins
%doc %{_texmfdistdir}/source/generic/babel/bahasam.dtx
%doc %{_texmfdistdir}/source/generic/babel/base.ins
%doc %{_texmfdistdir}/source/generic/babel/basque.dtx
%doc %{_texmfdistdir}/source/generic/babel/basque.ins
%doc %{_texmfdistdir}/source/generic/babel/bbcompat.dtx
%doc %{_texmfdistdir}/source/generic/babel/bbidxglo.dtx
%doc %{_texmfdistdir}/source/generic/babel/bbplain.dtx
%doc %{_texmfdistdir}/source/generic/babel/breton.dtx
%doc %{_texmfdistdir}/source/generic/babel/breton.ins
%doc %{_texmfdistdir}/source/generic/babel/bulgarian.dtx
%doc %{_texmfdistdir}/source/generic/babel/bulgarian.ins
%doc %{_texmfdistdir}/source/generic/babel/catalan.dtx
%doc %{_texmfdistdir}/source/generic/babel/catalan.ins
%doc %{_texmfdistdir}/source/generic/babel/croatian.dtx
%doc %{_texmfdistdir}/source/generic/babel/croatian.ins
%doc %{_texmfdistdir}/source/generic/babel/czech.dtx
%doc %{_texmfdistdir}/source/generic/babel/czech.ins
%doc %{_texmfdistdir}/source/generic/babel/danish.dtx
%doc %{_texmfdistdir}/source/generic/babel/danish.ins
%doc %{_texmfdistdir}/source/generic/babel/dutch.dtx
%doc %{_texmfdistdir}/source/generic/babel/dutch.ins
%doc %{_texmfdistdir}/source/generic/babel/english.dtx
%doc %{_texmfdistdir}/source/generic/babel/english.ins
%doc %{_texmfdistdir}/source/generic/babel/esperanto.dtx
%doc %{_texmfdistdir}/source/generic/babel/esperanto.ins
%doc %{_texmfdistdir}/source/generic/babel/estonian.dtx
%doc %{_texmfdistdir}/source/generic/babel/estonian.ins
%doc %{_texmfdistdir}/source/generic/babel/finnish.dtx
%doc %{_texmfdistdir}/source/generic/babel/finnish.ins
%doc %{_texmfdistdir}/source/generic/babel/frenchb.dtx
%doc %{_texmfdistdir}/source/generic/babel/frenchb.ins
%doc %{_texmfdistdir}/source/generic/babel/galician.dtx
%doc %{_texmfdistdir}/source/generic/babel/galician.ins
%doc %{_texmfdistdir}/source/generic/babel/german.ins
%doc %{_texmfdistdir}/source/generic/babel/germanb.dtx
%doc %{_texmfdistdir}/source/generic/babel/greek.dtx
%doc %{_texmfdistdir}/source/generic/babel/greek.fdd
%doc %{_texmfdistdir}/source/generic/babel/greek.ins
%doc %{_texmfdistdir}/source/generic/babel/grmath.dtx
%doc %{_texmfdistdir}/source/generic/babel/grsymb.dtx
%doc %{_texmfdistdir}/source/generic/babel/heb209.dtx
%doc %{_texmfdistdir}/source/generic/babel/hebinp.dtx
%doc %{_texmfdistdir}/source/generic/babel/hebrew.dtx
%doc %{_texmfdistdir}/source/generic/babel/hebrew.fdd
%doc %{_texmfdistdir}/source/generic/babel/hebrew.ins
%doc %{_texmfdistdir}/source/generic/babel/icelandic.dtx
%doc %{_texmfdistdir}/source/generic/babel/icelandic.ins
%doc %{_texmfdistdir}/source/generic/babel/interlingua.dtx
%doc %{_texmfdistdir}/source/generic/babel/interlingua.ins
%doc %{_texmfdistdir}/source/generic/babel/irish.dtx
%doc %{_texmfdistdir}/source/generic/babel/irish.ins
%doc %{_texmfdistdir}/source/generic/babel/italian.dtx
%doc %{_texmfdistdir}/source/generic/babel/italian.ins
%doc %{_texmfdistdir}/source/generic/babel/kurmanji.dtx
%doc %{_texmfdistdir}/source/generic/babel/kurmanji.ins
%doc %{_texmfdistdir}/source/generic/babel/language.dat
%doc %{_texmfdistdir}/source/generic/babel/latin.dtx
%doc %{_texmfdistdir}/source/generic/babel/latin.ins
%doc %{_texmfdistdir}/source/generic/babel/lsorbian.dtx
%doc %{_texmfdistdir}/source/generic/babel/magyar.dtx
%doc %{_texmfdistdir}/source/generic/babel/magyar.ins
%doc %{_texmfdistdir}/source/generic/babel/ngermanb.dtx
%doc %{_texmfdistdir}/source/generic/babel/norsk.dtx
%doc %{_texmfdistdir}/source/generic/babel/norsk.ins
%doc %{_texmfdistdir}/source/generic/babel/polish.dtx
%doc %{_texmfdistdir}/source/generic/babel/polish.ins
%doc %{_texmfdistdir}/source/generic/babel/portuges.dtx
%doc %{_texmfdistdir}/source/generic/babel/portuges.ins
%doc %{_texmfdistdir}/source/generic/babel/romanian.dtx
%doc %{_texmfdistdir}/source/generic/babel/romanian.ins
%doc %{_texmfdistdir}/source/generic/babel/russianb.dtx
%doc %{_texmfdistdir}/source/generic/babel/russianb.ins
%doc %{_texmfdistdir}/source/generic/babel/samin.dtx
%doc %{_texmfdistdir}/source/generic/babel/samin.ins
%doc %{_texmfdistdir}/source/generic/babel/scottish.dtx
%doc %{_texmfdistdir}/source/generic/babel/scottish.ins
%doc %{_texmfdistdir}/source/generic/babel/serbian.dtx
%doc %{_texmfdistdir}/source/generic/babel/serbian.ins
%doc %{_texmfdistdir}/source/generic/babel/slovak.dtx
%doc %{_texmfdistdir}/source/generic/babel/slovak.ins
%doc %{_texmfdistdir}/source/generic/babel/slovene.dtx
%doc %{_texmfdistdir}/source/generic/babel/slovene.ins
%doc %{_texmfdistdir}/source/generic/babel/sorbian.ins
%doc %{_texmfdistdir}/source/generic/babel/spanish.dtx
%doc %{_texmfdistdir}/source/generic/babel/spanish.ins
%doc %{_texmfdistdir}/source/generic/babel/swedish.dtx
%doc %{_texmfdistdir}/source/generic/babel/swedish.ins
%doc %{_texmfdistdir}/source/generic/babel/tb1202.tex
%doc %{_texmfdistdir}/source/generic/babel/tb1401.tex
%doc %{_texmfdistdir}/source/generic/babel/tb1604.tex
%doc %{_texmfdistdir}/source/generic/babel/turkish.dtx
%doc %{_texmfdistdir}/source/generic/babel/turkish.ins
%doc %{_texmfdistdir}/source/generic/babel/ukraineb.dtx
%doc %{_texmfdistdir}/source/generic/babel/ukraineb.ins
%doc %{_texmfdistdir}/source/generic/babel/usage.tex
%doc %{_texmfdistdir}/source/generic/babel/usorbian.dtx
%doc %{_texmfdistdir}/source/generic/babel/welsh.dtx
%doc %{_texmfdistdir}/source/generic/babel/welsh.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
