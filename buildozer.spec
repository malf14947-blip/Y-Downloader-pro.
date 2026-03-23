[app]
title = Y-Downloader Pro
package.name = ydownloader
package.domain = org.ydl
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# هذه المكتبات ضرورية جداً للكود الجديد
requirements = python3, kivy==2.3.0, kivymd, pillow, certifi, chardet, idna, requests, urllib3, yt-dlp

orientation = portrait
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.allow_backup = True
android.release_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
