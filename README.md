

# pyham
## HAM Radio with Python
*This program is under development and no working version is released yet.*

### About
The server connects many HAM radios together trough the Internet. The server needs to be connected to real HAM radio hardware.

The client is for using your PC as it would be a HAM radio. No real radio needed.

It is supposed to be compatible with eQSO, FRN and Echolink. It also introduces its own protocol.

### Software requirements
This program requires [Python](https://www.python.org/) 3.x to be installed. Tested with Python 3.6 on Windows.

[wxPython](https://pypi.org/project/wxPython/) is required for graphical interface.

[PyAudio](https://pypi.org/project/PyAudio/) is required for sound in the client. Not required for the server.

### How to install required libraries:
> pip install wx
>
> pip install pyaudio

Or use some other tool to install Python modules/libraries/packages called 'wx' and 'pyaudio'.

### How to run client:
Start with graphical user interface:

> python pyham_client.py

Start with command line user interface:

> python pyham_client.py --nogui

Get help on command line parameters:

> python pyham_client.py --help

### How to run server:
Start with graphical user interface:

> python pyham_server.py

Start with command line user interface:

> python pyham_server.py --nogui

Get help on command line parameters:

> python pyham_server.py --help

### Configuration
Configuration can be changed and saved at runtime. It is saved in files **pyham_client.conf** and **pyham_server.conf**.

You'll find commented configuration file templates in files **pyham_client.conf.template** and **pyham_server.conf.template**. 

#### Screenshots:

![alt text](http://titanix.net/~japek/pyham-client-0001.png)

Ver. 0.001
