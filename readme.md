**Description**

Controller for various Windows functions via external Raspberry Pi w/ touchscreen

Functions including, but not limited to:

* windows audio mix                              -- 90% needs polish -- jace fix
* overworld to switch between apps               -- 90% needs polish -- jace fix
* spotify integration                            -- 90% needs polish -- jace fix
* movie mode/plex integration                    -- 0% medium-hard   -- meet
* drawing pad / touch mouse pad (like laptop)    -- 0% easy          -- everyone
* windows/google calendar integration            -- 0% hard          -- idk
* in game scoreboards, like discord side-bar     -- 0% hard          -- apurva
* launch applications                            -- 0% medium        -- tri pham
* twitch/twitch chat integration                 -- 0% medium-hard   -- max
* obs/streamlabs integration                     -- 0% medium-hard   -- max
* switch desktop/windows                         -- 90% needs polish -- jace fix
* zoom controls                                  -- 0% medium-hard   -- jace


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

`npm install` in the SeniorDesign/device directory

**Python**

To install all imports

`pip3 install -r requirements.txt`

Also note that Microsoft Visual C++ 14.0 is required for pycaw (can be installed by searching online)


