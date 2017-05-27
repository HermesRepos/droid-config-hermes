# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device hermes
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 2
%define dcd_path ./
%define community_adaptation 1
# Adjust this for your device
%define pixel_ratio 1.70
# We assume most devices will
%define have_modem 1

Provides: ofono-configs

%include droid-configs-device/droid-configs.inc
