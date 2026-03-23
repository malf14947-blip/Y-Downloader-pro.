[app]
# (str) Title of your application
title = Y-Downloader Pro

# (str) Package name
package.name = ydownloader

# (str) Package domain (needed for android packaging)
package.domain = org.ydl

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
# تم إضافة yt-dlp و pillow و requests لضمان عمل المحرك والواجهة بشكل صحيح
requirements = python3, kivy==2.3.0, kivymd, pillow, certifi, chardet, idna, requests, urllib3, yt-dlp

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
# تم إضافة أذونات الإنترنت والتخزين المطلوبة
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (list) Android architectures to build for
# الاكتفاء بمعمارية واحدة لتسريع البناء وتجنب خطأ Broken pipe
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) Custom source code for the icon
# icon.filename = %(source.dir)s/icon.png

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
