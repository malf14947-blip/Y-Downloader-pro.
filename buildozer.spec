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

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# تم إضافة pillow و تحديث إصدارات المكتبات لضمان التوافق
requirements = python3, kivy==2.3.0, kivymd, pillow, certifi, chardet, idna, requests, urllib3

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
# تحديث إلى API 34 ليتوافق مع متطلبات متجر جوجل الحالية
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (list) Android architectures to build for
# الاكتفاء بمعمارية واحدة حالياً لتسريع البناء وتقليل الأخطاء
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
