# (str) Title of your application
title = Mi Aplicacion

# (str) Package name
package.name = miapli

# (str) Package domain (needed for android packaging)
package.domain = org.ex

# (list) Source files to include (let the default or match your structure)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Asegúrate de incluir python3, kivy y las librerías necesarias
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True
