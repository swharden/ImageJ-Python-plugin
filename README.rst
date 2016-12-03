ImageJ-Python-plugin
=============================
boilerplate python plugin for ImageJ / FIJI

Notes for Developers
====================

getProperty
-------------
Running code like `getProperty('fiji.dir')` is in a lot of the documentation I find online, but what other properties are there? Here's a list of what's what on my system:

=======================  =================
this argument            returns this
=======================  =================
getProperty('fiji.dir')  c:/some/long/path
getProperty('fiji.dir')  c:/some/long/path
=======================  =================
