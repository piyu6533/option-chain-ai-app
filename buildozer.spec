[app]
title = Pro Trading Terminal
package.name = tradingterminal
package.domain = org.trading
source.dir = .
source.include_exts = py,kv
version = 0.1

# Android પર HTTPS ડેટા માટે openssl અને certifi જરૂરી છે
requirements = python3,kivy==2.2.1,requests,openssl,certifi,hostpython3

orientation = portrait
fullscreen = 0

# Android specific settings
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET
android.archs = armeabi-v7a, arm64-v8a

# એરર શોધવા માટે લોગ લેવલ 2
log_level = 2

[buildozer]
log_level = 2
warn_on_root = 1
