Name:           ooapparmor
Version:        0.2.0
Release:        1%{?dist}
Summary:        Generates and loads AppArmor security profiles for individual utilities.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/ooapparmor
Source0:        ooapparmor-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooapparmor is a sovereign, capability-bounded AppArmor profile manager written
in pure openOODA, featuring zero ambient authority, confinement rule synthesis,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooapparmor
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooapparmor-uninstall

%files
/usr/bin/ooapparmor
/usr/bin/ooapparmor-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to pure openOODA 0.2.0 with MCP server and multi-distro packaging parity
