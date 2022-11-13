Name:		texlive-iitem
Version:	29613
Release:	1
Summary:	Multiple level of lists in one list-like environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iitem
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iitem.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iitem.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iitem.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
