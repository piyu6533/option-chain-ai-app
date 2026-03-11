[app]

title = Pro Trading Terminal
package.name = tradingterminal
package.domain = org.trading

source.dir = .
source.include_exts = py,kv

# આ લાઈન ઉમેરો (વર્ઝન સેટ કરવા માટે)
version = 0.1

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0
# (વધારે સ્ટેબલ વર્ઝન માટે આ સેટિંગ્સ જરૂરી છે)
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.permissions = INTERNET
