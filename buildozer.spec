[app]

# (str) Title of your application
title = Mi Aplicacion

# (str) Package name
package.name = miapli

# (str) Package domain (needed for android packaging)
package.domain = org.ex

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True
