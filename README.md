# Setup scripts for PiDeck

These customisation scripts do not form part of any standard package on the [PiDeck](http://pideck.com) system. 
So we put them in the __pideck__ package installed as part of the [PiDeck distro](https://github.com/pideck/pideck-distro).

The scrips are:

* _pideck_ - kills any old processes, starts xwax with either alsa or jackd backends, starts the touchscreen controls and sets the path to the music files
* _touchscreen_controls_ - creates a row of buttons on the screen, sends fake key presses to control xwax without a real keyboard
* _soundcard-setup.service_ - configuration snippet for systemd to setup the soundcard mixer levels and routing using the soundcard.state file
* _soundcard.state_ - example configuration for the [Audio Injector](http://www.audioinjector.net/#!/rpi-hat) soundcard levels and routing

Go nuts! Please file any bugs or suggestions as [issues](https://github.com/pideck/pideck/issues) in this GitHub project. Pull requests are very welcome.
