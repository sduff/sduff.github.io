---
title: Building an Android App with Phaser and Apache Cordova
date: 2017-01-01
tags: [phaser, gamedev]
published: false
layout: default
series: code
---

cordova create petri net.simonduff.petri Petri
cd petri

cordova platform ls
cordova platform add android
cordova platform add ios
cordova platform add browser
...

I have found the following apps to be useful for semi-commercial games

cordova plugins add cc.fovea.cordova.purchase 
cordova plugin add cc.fovea.cordova.purchase --variable BILLING_KEY="MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoDEL9T4SocBsdY8B9sioDBlF121wCc7Phy05sTaxSONPh9/eKRUuSydkAnuR7OmHqOf0tWTVrXPygfBixL6bA8amoYG8CaqUt1oQ4BaQRoaZmQhTLcDbrjRg2zVM1C8nc7ik6FAR3EnxJTCWXV/RMETWPR8wO+W/alv77ea80/U2fGhPB4hCgORasVc1jT3xeauburfiYg54QE+N/P98M3IkJzPlgUHbD5qD/rvN4ofWKpc89DJ2oFqBopPxx5nJhit/yZrW0uOQKMB7Z1FHI0i/hXLrVxx70+X6ZIJ7yBEC8C8qZE3J7uQ+fqsumEvC/QtHB9bMZoQER3r2Ziv8AwIDAQAB"

FIXME: Can I publish this?

cordova plugins add cordova-plugin-admob-free

npm install cordova-icon -g
( javascript obfsucator)

get the latest phaser js and copy to www/js

# Including Ads in your game
# Adding a "Remove Ads" In-App Purchase

# Generating relevant icons
1024x1024 icon in project root directory
Run cordova-icon

# Debugging the app
## Running on an android device
cordova run android -device

# Hiding the source code
(Obfuscate the source code if you so wish, and test it)
Make sure you test afterwards
Recomended flags
Google's Pro Guard ??? 

# Preparing for release

Ensure you have generated a signing key
```bash
keytool -genkey -v -keystore ~/app_keys/my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias
```

Create the final release APK by following these steps
```bash
cordova build android --release
/opt/android-sdk/build-tools/26.0.2/zipalign -v -p 4 platforms/android/build/outputs/apk/android-release-unsigned.apk platforms/android/build/outputs/apk/android-unsigned-aligned.apk
/opt/android-sdk/build-tools/26.0.2/apksigner sign --ks ~/app_keys/my-release-key.jks --out platforms/android/build/outputs/apk/android-release.apk aplatforms/android/build/outputs/apk/android-unsigned-aligned.apk
```

Congratulations, you have built an Android App using Phaser and Cordova, and its ready to be submitted to the Google Play Store.

# Play Store next steps
## Icons, Banners, etc...
## Ratings
## Privacy Policy
## Version numbering
## Google Play Store Badge

687  cordova build android --release
  688  cd platforms/android/build/outputs/apk/
  689  ls
  690  /opt/android-sdk/build-tools/26.0.2/zipalign -v -p 4 android-release.apk android-release-unsigned.apk
  691  /opt/android-sdk/build-tools/26.0.2/zipalign -v -p 4 android-release-unsigned.apk android-release.apk
  692  ls
  693  /opt/android-sdk/build-tools/26.0.2/apksigner sign --ks ~/app_keys/my-release-key.jks --out invisilink.apk android-release.apk
  694  ls
  695  ls -al
  696  cd
  697  cd app_keys/
  698  ls
  699  keytool -rlist -v keystore my-release-key.jks
  700  keytool -list -v keystore my-release-key.jks
  701  keytool -list -v -keystore my-release-key.jks
  702  keytool -genkey -v -keystore my-release-key.jks
  703  keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias
  704  ls
  705  mv my-release-key.jks my-release-key.jks.old
  706  keytool -genkey -v -keystore my-release-key.jks -keyalg RSA -keysize 2048 -validity 10000 -alias my-alias
  707  ls
  708  cd ../Projects/invisilink/
  709  cd platforms/android/build/outputs/apk/
  710  history
sduff@sduff-mbpr15:~/Projects/invisilink/platforms/android/build/outputs/apk $ /opt/android-sdk/build-tools/26.0.2/apksigner sign --ks ~/app_keys/my-release-key.jks --out invisilink.apk android-release.apk
