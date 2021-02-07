Name:           serene-autostart
Version:        0.0.1
Release:        0
Summary:        serene-autostart

Group:          System Environment/Base
License:        GPLv2

URL:            https://fascode.net

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
This package contains autostarts.

%prep

%build

%install
rm -rf rm -rf $RPM_BUILD_ROOT

#GPG Key
mkdir -p %{buildroot}/etc/xdg/autostart/
cat <<EOF > %{buildroot}/etc/xdg/autostart/packagekit_clean.desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=PackageKit Cleaner
Exec=pkcon refresh force
EOF

%clean
rm -rf rm -rf $RPM_BUILD_ROOT

%files
/etc/xdg/autostart/packagekit_clean.desktop

%changelog
* Mon Feb 08 2021 kokkiemouse <kokkiemouse@fascode.net> - 0.0.1
- Create Package