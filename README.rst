ImageJ-Python-plugin
=============================
boilerplate python plugin for ImageJ / FIJI

Notes for Developers
====================

getProperty
-------------
Running code like `getProperty('fiji.dir')` is in a lot of the documentation I find online, but what other properties are there? Here's a list of what's what on my system:

===========================================================================  ===========================================================================
this argument                                                                returns this                                                               
===========================================================================  ===========================================================================
awt.toolkit                                                                  sun.awt.windows.WToolkit
fiji.defaultLibPath                                                          bin/server/jvm.dll
fiji.dir                                                                     C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app
fiji.executable                                                              C:\Users\scott\Documents\important\fiji-win64\Fiji.app\ImageJ-win64.exe
file.encoding                                                                Cp1252
file.encoding.pkg                                                            sun.io
file.separator                                                               \
ij.dir                                                                       C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app
ij.executable                                                                C:\Users\scott\Documents\important\fiji-win64\Fiji.app\ImageJ-win64.exe
imagej.dir                                                                   C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app
java.awt.graphicsenv                                                         sun.awt.Win32GraphicsEnvironment
java.awt.printerjob                                                          sun.awt.windows.WPrinterJob
java.class.path                                                              C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app/jars/imagej-launcher-...
java.class.version                                                           52.0
java.endorsed.dirs                                                           C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app\java\win64\jdk1.8.0_6...
java.ext.dirs                                                                C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app\java\win64\jdk1.8.0_6...
java.home                                                                    C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app\java\win64\jdk1.8.0_6...
java.io.tmpdir                                                               C:\Users\scott\AppData\Local\Temp\
java.library.path                                                            C:\Users\scott\DOCUME~1\IMPORT~1\FIJI-W~1\Fiji.app/lib/win64;C:\Users\sc...
java.runtime.name                                                            Java(TM) SE Runtime Environment
java.runtime.version                                                         1.8.0_66-b18
java.specification.name                                                      Java Platform API Specification
java.specification.vendor                                                    Oracle Corporation
java.specification.version                                                   1.8
==============================  ===========================================================================
this argument                   returns this                                                               
==============================  ===========================================================================
awt.toolkit                     sun.awt.windows.WToolkit
fiji.defaultLibPath             bin/server/jvm.dll
fiji.dir                        C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app
fiji.executable                 C:\\Users\\scott\\Documents\\important\\fiji-win64\\Fiji.app\\ImageJ-win64.exe
file.encoding                   Cp1252
file.encoding.pkg               sun.io
file.separator                  \\
ij.dir                          C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app
ij.executable                   C:\\Users\\scott\\Documents\\important\\fiji-win64\\Fiji.app\\ImageJ-win64.exe
imagej.dir                      C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app
java.awt.graphicsenv            sun.awt.Win32GraphicsEnvironment
java.awt.printerjob             sun.awt.windows.WPrinterJob
java.class.path                 C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app/jars/imagej-launcher-...
java.class.version              52.0
java.endorsed.dirs              C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app\\java\\win64\\jdk1.8.0_6...
java.ext.dirs                   C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app\\java\\win64\\jdk1.8.0_6...
java.home                       C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app\\java\\win64\\jdk1.8.0_6...
java.io.tmpdir                  C:\\Users\\scott\\AppData\\Local\\Temp\\
java.library.path               C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app/lib/win64;C:\\Users\\sc...
java.runtime.name               Java(TM) SE Runtime Environment
java.runtime.version            1.8.0_66-b18
java.specification.name         Java Platform API Specification
java.specification.vendor       Oracle Corporation
java.specification.version      1.8
java.vendor                     Oracle Corporation
java.vendor.url                 http://java.oracle.com/
java.vendor.url.bug             http://bugreport.sun.com/bugreport/
java.version                    1.8.0_66
java.vm.info                    mixed mode
java.vm.name                    Java HotSpot(TM) 64-Bit Server VM
java.vm.specification.name      Java Virtual Machine Specification
java.vm.specification.vendor    Oracle Corporation
java.vm.specification.version   1.8
java.vm.vendor                  Oracle Corporation
java.vm.version                 25.66-b18
line.separator                  
os.arch                         amd64
os.name                         Windows 10
os.version                      10.0
path.separator                  ;
plugins.dir                     C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app
python.cachedir.skip            true
python.console.encoding         cp0
sun.arch.data.model             64
sun.awt.enableExtraMouseButtons  true
sun.boot.class.path             C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app\\java\\win64\\jdk1.8.0_6...
sun.boot.library.path           C:\\Users\\scott\\DOCUME~1\\IMPORT~1\\FIJI-W~1\\Fiji.app\\java\\win64\\jdk1.8.0_6...
sun.cpu.endian                  little
sun.cpu.isalist                 amd64
sun.desktop                     windows
sun.io.unicode.encoding         UnicodeLittle
sun.java2d.noddraw              true
sun.jnu.encoding                Cp1252
sun.management.compiler         HotSpot 64-Bit Tiered Compilers
sun.os.patch.level              
user.country                    US
user.dir                        C:\\Users\\scott\\Documents\\important\\fiji-win64\\Fiji.app
user.home                       C:\\Users\\scott
user.language                   en
user.name                       scott
user.script                     
user.timezone                   America/New_York
user.variant                    
==============================  ===========================================================================

BTW, this list was created by running the following inside ImageJ:

.. code:: python

        from java.lang.System import getProperties, getProperty
        maxSizeA=30 # width of the columns for an RST table
        maxSizeB=75 # width of the columns for an RST table
        print("="*maxSizeA+"  "+"="*maxSizeB)
        print("this argument".ljust(maxSizeA)+"  "+"returns this".ljust(maxSizeB))
        print("="*maxSizeA+"  "+"="*maxSizeB)
        for propName in sorted(getProperties()):
            value = str(getProperty(propName)).strip().replace("\n",'\\n')
            if len(value)>maxSizeB:
                value=value[:maxSizeB-3]+"..."
            print("%s  %s"%(propName.ljust(maxSizeA),value.replace('\\','\\\\')))
        print("="*maxSizeA+"  "+"="*maxSizeB)
