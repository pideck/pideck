# Soundcard status for PiDeck

Based on our tests so far, these are the soundcards known to work, those which potentially could work, and those which will not be supported by the PiDeck project. We make no promises about the performance of soundcards we have not personally tested!

A feature matrix is provided below to help you choose the soundcard which is right for your PiDeck. Some of these are current hardware, others are discontinued or obsolete models. Recycling is encouraged!

Please note that xwax supports up to three decks, and single deck USB soundcards can be combined to provide additional decks. This is not currently the case for single deck I²S soundcards such as the audioinjector.net stereo and Fe-Pi Audio HATs, due the two-channel limit of the Raspberry Pi I²S implementation.

Most full duplex soundcards have stereo line input and output, except those designed only for use with turntables, such as the Pro-ject Phono Box USB and Rega Fono Mini A2D. If a soundcard only supports line input, you will need an additional hardware pre-amp or mixer to use phono input. If you have a classic turntable with an earth wire, you will need a grounding stud on the soundcard or preamp to reduce hum. Software pre-amps are not recommended for use with timecode, as their gain (being post-input) is often not clean enough for a pure signal.  

Some USB phono interfaces may not be full duplex or feature a line output, such as turntables with built in USB which is meant for recording only. These recording interfaces sometimes have fixed input gain which is not meant for DJs, as fast scratches and backspins can cause signal peaks which distort timecode.

If you play any analogue vinyl or regular CDs without timecode, you will benefit from a hardware bypass or input mix control which enables you to play through without loss of quality, or disconnecting cables. 


## Known to work

Soundcard | Line input | Phono input | Number of decks | Hardware bypass
--------- | ---------- | ----------- | --------------- | ---------------
American Audio Genie II / Citronic AC-1 USB / KAM USBH100 Mk II | :heavy_check_mark: | :heavy_check_mark: | 1 |
audioinjector.net stereo HAT | :heavy_check_mark: || 1 | :heavy_check_mark: (via amixer)
Behringer UCA 202 / Behringer UCA 222 | :heavy_check_mark: || 1 |
Behringer UFO 202 | :heavy_check_mark: | :heavy_check_mark: | 1 (with [hardware modification](https://mixxx.org/forums/viewtopic.php?t=2438)) |
Hercules Mk2 | :heavy_check_mark: | :heavy_check_mark: | 2 | :heavy_check_mark: (audio source buttons)
Numark Stereo IO | :heavy_check_mark: | :heavy_check_mark: | 1 |
Reloop Digital Jockey 2 IE | :heavy_check_mark: | :heavy_check_mark: | 1 |
Traktor Audio 4 | :heavy_check_mark: | :heavy_check_mark: | 2 | :heavy_check_mark:
Traktor Audio 6 | :heavy_check_mark: | :heavy_check_mark: | 3 | :heavy_check_mark:
Traktor Audio 8 | :heavy_check_mark: | :heavy_check_mark: | 3 | :heavy_check_mark:

## Potentially could work

Soundcard | Line input | Phono input | Number of decks | Hardware bypass
--------- | ---------- | ----------- | --------------- | ---------------
American Audio VMS2 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
American Audio VMS4.1 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Art USB Phono Plus | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Creative Sound Blaster X-Fi HD | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Denon DJ DS1 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Dynavox UPR-2.0 | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Fe-Pi Audio v1.3 HAT | :heavy_check_mark: | | 1 | ?
Hercules Deejay Trim | :heavy_check_mark: | :heavy_check_mark: | ? | ?
Hercules RMX | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
McLelland UP-2.0 | :heavy_check_mark: | :heavy_check_mark: | 1 | :heavy_check_mark: (input mix control)
Phonic Digitrack | :heavy_check_mark: || 1 | ?
Power Dynamics PDX015 | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Pro-ject Phono Box USB | | :heavy_check_mark: | 1 | ?
Rega Fono Mini A2D | | :heavy_check_mark: | 1 | ?
Reloop Iphono | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Reloop Iphono 2 | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
SM Pro XP203 | :heavy_check_mark: | :heavy_check_mark: | 1 | :heavy_check_mark: (input mix control)
Stanton Final Scratch | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Traktor Audio 10 | :heavy_check_mark: | :heavy_check_mark: | 3 | :heavy_check_mark:

## Will not be supported

Soundcard | Why?
--------- | ----
American Audio VMS4 | Buggy audio and distortion
Numark DJ IO | No suitable inputs
Reloop Digital Jockey 2 (not Interface Edition) | No suitable inputs
Stanton Final Scratch 2 | It's FireWire, not USB
Traktor Audio 2 | No suitable inputs
