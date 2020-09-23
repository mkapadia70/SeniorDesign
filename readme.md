readme for the guys


**Emulation**

Without a PI with serial cable handy, you will need to emulate COM ports to develop/test
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


**Electron**

Set up the nodejs by running 
`npm install` and then running with `npm start` in devices directory

**Diagram**
![alt text](https://github.com/EECSisFUN/SeniorDesign/blob/master/image.png)





