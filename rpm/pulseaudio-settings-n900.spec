# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       pulseaudio-settings-n900

# >> macros
# << macros

Summary:    PulseAudio settings for Nokia N900
Version:    2.1.3
Release:    1
Group:      System/Libraries
License:    GPLv2
BuildArch:  noarch
URL:        https://github.com/nemomobile/pulseaudio-settings-n900
Source0:    %{name}-%{version}.tar.gz
Source100:  pulseaudio-settings-n900.yaml
Requires:   pulseaudio >= 2.1
Requires:   pulseaudio-modules-nemo-music >= 2.1.4
Requires:   pulseaudio-modules-nemo-record >= 2.1.4
Requires:   pulseaudio-modules-nemo-stream-restore >= 2.1.4
Requires:   pulseaudio-modules-nemo-voice >= 2.1.4
Requires:   pulseaudio-module-cmtspeech-n9xx >= 2.1.3
Requires:   pulseaudio-policy-enforcement
Obsoletes:   pulseaudio-modules-nokia-common-bin
Obsoletes:   pulseaudio-modules-nokia-algorithms-bin
Obsoletes:   pulseaudio-modules-nokia-audiots-bin
Obsoletes:   pulseaudio-modules-nokia-parameters-bin

%description
PulseAudio settings for Nokia N900



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
install -d $RPM_BUILD_ROOT/etc/pulse/
cp -a etc/pulse/arm_nokia_rx_51_board.pa $RPM_BUILD_ROOT/etc/pulse/
cp -a etc/pulse/x-maemo-route.table $RPM_BUILD_ROOT/etc/pulse/
cp -a etc/pulse/x-maemo-stream-restore-nemo.table $RPM_BUILD_ROOT/etc/pulse/

install -d $RPM_BUILD_ROOT/usr/share/pulseaudio/alsa-mixer/paths/
cp -a usr/share/pulseaudio/alsa-mixer/paths/*.conf $RPM_BUILD_ROOT/usr/share/pulseaudio/alsa-mixer/paths/

install -d $RPM_BUILD_ROOT/usr/share/pulseaudio/alsa-mixer/profile-sets/
cp -a usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf $RPM_BUILD_ROOT/usr/share/pulseaudio/alsa-mixer/profile-sets/
# << install pre

# >> install post
# << install post


%files
%defattr(-,root,root,-)
# >> files
%config(noreplace) %{_sysconfdir}/pulse/arm_nokia_rx_51_board.pa
%config(noreplace) %{_sysconfdir}/pulse/x-maemo-route.table
%config(noreplace) %{_sysconfdir}/pulse/x-maemo-stream-restore-nemo.table
%{_datadir}/pulseaudio/alsa-mixer/paths/*.conf
%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*.conf
# << files
