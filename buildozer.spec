[app]

title = Mi Aplicación
package.name = miapk
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# (list) Application requirements
# Usamos python3 para que pille una versión estable compatible
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.accept_sdk_license = True
