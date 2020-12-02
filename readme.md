**Description**
Controller for various Windows functions via external Raspberry Pi w/ touchscreen
Functions including, but not limited to:

* windows audio mix -- done
* overworld to switch between apps -- mostly done
* spotify integration -- mostly done
* movie mode/plex integration
* drawing pad / touch mouse pad (like laptop)
* windows/google calendar integration with clock/date time.
* in game scoreboards, like how discord tracks stuff like that idk
* launch applications
* twitch/twitch chat integration
* obs/streamlabs integration
* switch desktop/windows
* zoom controls


**Emulation**

Without a Raspberry Pi with serial cable, you will need to emulate COM ports to develop/test

you can do this with the a null-modem emulator which can be downloaded 

here: https://sourceforge.net/projects/com0com/

Run the x64 or x84 exe (doesnt matter which), tick all boxes and run setup

do not close the program yet

Then open device manager in windows

expand "com0com - serial port emulators"

right click one of the devices and "update drivers"

choose "search automatically for updates"

it should find and update the drivers

Then hit the reset button on com0com

The second pair should change "COM#->COM#" to something like "COM4->COM5"

to check this, expand "ports(COM & LPT)" in device manager

and check that "com0com - serial port emulator(COM5)" and "com0com - serial port emulator(COM6)" are listed

You will need to do this with two connections for two-way emulation so something like COM4, COM5, COM6, and COM7 need to be enabled

where "COM4->COM5" and "COM6->COM7" in the com0com settings, these need to be reflected in the code as well in the globals of device/server.py and coms/Main.py


**Electron**

Set up the nodejs by running 

`npm install` and then running with `npm start` in devices directory

**Python**

To install all imports

`pip3 install -r requirements.txt`

Also note that Microsoft Visual C++ 14.0 is required for pycaw (can be installed by searching online)


