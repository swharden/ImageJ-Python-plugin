ImageJ-Python-plugin
====
This is a boilerplate Python plugin for ImageJ intended for use with FIJI_. Its primary advantege is that it uses a bit of python magic to reload itself every time its called. This means that **you do not have to resatart ImageJ for code changes to take effect**! Recompiling code at evey execution can decrease performance, so this feature is only activated when the computer's user is in the list of "developers" at the top of the plugin source code. 

Installation
  Copy the "SWH" folder from this project into FIJI's plugins folder and restart ImageJ. That's it!
  
Configuration
 - Only python files containing an underscore (_) will appear as a plugin. Let's call them "plugin files"
 - "plugin files" should contain *no custom code* related to the task of your plugin. Instaed, write your code in a separate python script (without any underscores), and have your "plugin file" import it as a module and call its functions. 
 - When your plugin is run (by someone listed as a developer), the old module will be unloaded, the compiled code (a java class) will be deleted from the hard drive, and the new python module will be reloaded.
 - ensure you customize your "plugin files" by changing the values of `THIS_FOLDER <SWH/boilerplate/python_boiler.py#L14>`_, `developerIDs <SWH/boilerplate/python_boiler.py#L17>`_, and the contents of the main program (at the `very bottom <SWH/boilerplate/python_boiler.py#L66>`_ of the script).
 
Tips
 - It's easy to write 1 module with all the code in it, then several "plugin files" to call different parts of that same module. Perhaps it's convenient to call the same functions, but with different arguments.
 - Uses are encouraged to use an external editor (like Spyder_) when coding Python rather than hacking in the included `script editor <http://imagej.net/Using_the_Script_Editor>`_ (which isn't really built for with Python programming in mind).

Screenshot
  .. image:: screenshot.jpg

Links
----
  There's a pypi package which allows reading of ImageJ ROIs in python:
    - https://pypi.python.org/pypi/PymageJ
    - https://github.com/Jhsmit/PymageJ/

  You can now write ImageJ macros in Python (Python 2 / Jython)
    - http://marcora.caltech.edu/jython_imagej_howto.htm
    - https://pypi.python.org/pypi/PymageJ
    - https://www.ini.uzh.ch/~acardona/fiji-tutorial/

  This is far more convenient than ImageJ's macro language (which is still useful):
    - https://imagej.nih.gov/ij/developer/macro/macros.html
    - https://imagej.nih.gov/ij/developer/macro/functions.html




.. _FIJI: https://fiji.sc/
.. _spyder: https://pythonhosted.org/spyder/
