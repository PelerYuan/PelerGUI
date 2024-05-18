PelerGUI
=====

This library is designed to help beginners to create their command line application to GUI easily,
so that they can share their applications to others who does not be familiar with the command line environment, such as their friends.

The usage is simple, just add:

``from PelerGUI import *``

at the beginning of the python file, and replace all `print()` to `pprint()` and `input()` to `pinput()`.

These two new functions will create messagebox for users to input and read the information, thus successfully turn the application to the GUI mode.

----

The default title of messagebox is "pprint" and "pinput", you can change them by writing the code like this:

``pprint("foo", title="This is new title")``

``pinput("foo", title="This is new title")``

-------

you can also assign the type of message when using the function `pprint`.

``pprint("foo", message_type=INFO)``

``pprint("foo", message_type=WARNING)``

``pprint("foo", message_type=ERROR)``

Thank you for using this library :)