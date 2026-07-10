%global tl_name dlrg-templates
%global tl_revision 74633

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.0
Release:	%{tl_revision}.1
Summary:	Templates for the German Lifesaving Association (DLRG)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dlrg-templates
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dlrg-templates.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dlrg-templates.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides templates for members of the German Lifesaving
Association (DLRG). This includes the letter template, presentations,
specialist publications and press releases. These templates are based on
the current cooperative design. They can be adapted to the local
structure with simple settings.

