[app]

# (str) Title of your application
title = Mi Aplicacion

# (str) Package name
package.name = miapk

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the include files are located
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Indicate whether the application should be full screen or not
fullscreen = 0

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

