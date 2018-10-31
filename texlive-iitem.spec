# revision 29613
# category Package
# catalog-ctan /macros/latex/contrib/iitem
# catalog-date 2013-04-02 15:23:02 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-iitem
Version:	1.0
Release:	10
Summary:	Multiple level of lists in one list-like environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iitem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iitem.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iitem.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iitem.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines multiple level lists within one list-like
environment. instead of writing \begin{enumerate} \item 1
\begin{enumerate} \item 2 \begin{enumerate} \item 3
\begin{enumerate} \item 4 \end{enumerate} \end{enumerate} \item
2.1 \end{enumerate} \item 1.1 \begin{enumerate} \item 2
\end{enumerate} \end{enumerate} this package allows you to
write \begin{enumerate} \item 1 \iitem 2 \iiitem 3 \ivtem 4
\iitem 2.1 \item 1.1 \iitem 2 \end{enumerate}.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/iitem/iitem.sty
%doc %{_texmfdistdir}/doc/latex/iitem/README
%doc %{_texmfdistdir}/doc/latex/iitem/iitem.pdf
#- source
%doc %{_texmfdistdir}/source/latex/iitem/iitem.dtx
%doc %{_texmfdistdir}/source/latex/iitem/iitem.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
