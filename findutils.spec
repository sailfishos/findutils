# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       findutils
Summary:    The GNU versions of find utilities (find and xargs)
Version:    4.2.31
Release:    1
Group:      Applications/File
License:    GPLv2+
URL:        http://www.gnu.org/software/findutils/
Source0:    ftp://ftp.gnu.org/gnu/findutils/%{name}-%{version}.tar.gz
Source100:  findutils.yaml
Patch0:     findutils-4.2.31-no-locate.patch
Patch1:     findutils-bmc12931-find-ls-stack-overflow.patch
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gzip
BuildRequires:  gettext-devel
BuildRequires:  texinfo


%description
The findutils package contains programs which will help you locate
files on your system.  The find utility searches through a hierarchy
of directories looking for files which match a certain set of criteria
(such as a filename pattern).  The xargs utility builds and executes
command lines from standard input arguments (usually lists of file
names generated by the find command).

You should install findutils because it includes tools that are very
useful for finding things on your system.



%package docs
Summary:    Document files for %{name}
Group:      Applications/File
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description docs
%{summary}.



%prep
%setup -q -n %{name}-%{version}

# findutils-4.2.31-no-locate.patch
%patch0 -p1
# findutils-bmc12931-find-ls-stack-overflow.patch
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
# << build pre

%configure --disable-static \
    --without-selinux

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

mkdir -p %{buildroot}/bin
pushd %{buildroot}/bin
ln -sf ../usr/bin/find
popd
# << install post
%find_lang %{name}







%post docs
%install_info --info-dir=%_infodir %{_infodir}/find.info.gz

%postun docs
if [ $1 = 0 ] ;then
%install_info_delete --info-dir=%{_infodir} %{_infodir}/find.info.gz
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
# >> files
%doc COPYING
%{_bindir}/find
/bin/find
%{_bindir}/xargs
# << files


%files docs
%defattr(-,root,root,-)
# >> files docs
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_mandir}/man1/find.1*
%{_mandir}/man1/xargs.1*
%{_infodir}/find.info.gz
# << files docs

