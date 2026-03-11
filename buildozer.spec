[app]
title = Pro Trading Terminal
package.name = tradingterminal
package.domain = org.trading
source.dir = .
source.include_exts = py,kv
version = 0.1

# 'openssl' અને 'certifi' ઉમેરવા ખૂબ જરૂરી છે
requirements = python3,kivy,requests,openssl,certifi

orientation = portrait
fullscreen = 0

# Android specific settings
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
android.permissions = INTERNET
