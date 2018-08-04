# Setup scripts for PiDeck

These customisation scripts do not form part of any standard package on the [PiDeck](http://pideck.com) system. 
So we put them in the __pideck__ package installed as part of the [PiDeck distro](https://github.com/pideck/pideck-distro).

The scrips include:

* _pideck_ - kills any old processes, starts xwax with either alsa or jackd backends, starts the touchscreen controls and sets the path to the music files
* _touchscreen_controls_ - creates a row of buttons on the screen, sends fake key presses to control xwax without a real keyboard
* _soundcard-setup.service_ - configuration snippet for systemd to setup the soundcard mixer levels and routing using the soundcard.state file
* _soundcard.state_ - example configuration for the [Audio Injector](http://www.audioinjector.net/#!/rpi-hat) soundcard levels and routing

Go nuts! Please file any bugs or suggestions as [issues](https://github.com/pideck/pideck/issues) in this GitHub project. Pull requests are very welcome.

Build the package using:
```sh
dpkg-buildpackage -aarmhf -uc -us -b
```

Please see [Soundcard status](soundcards.md) for tips on which soundcard(s) to use with your PiDeck. Your help confirming which soundcards work for you would be appreciated.

For keyboard shortcuts please see [Keyboard control](keyboard_control.md).
