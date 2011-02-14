Summary:	This library can be used to do some weather related routines and solar calculations in Lua
Name:		lua-weather
Version:	20110123
Release:	0.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://carme.pld-linux.org/~uzsolt/sources/%{name}-%{version}.tar.xz
# Source0-md5:	4b44a6203172736940e299377d7d5cd3
URL:		http://solitudo.net/software/lua/weatherlib/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library can be used to do some weather related routines and solar
calculations in Lua. Also provides unit conversion routines

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lua/5.1
install src/weatherlib.lua $RPM_BUILD_ROOT%{_datadir}/lua/5.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc api/html api/ikiwiki README.txt
%{_datadir}/lua/5.1/weatherlib.lua
