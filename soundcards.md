# Soundcard status for PiDeck

Based on our tests so far, these are the soundcards known to work, those which potentially could work, and those which will not be supported by the PiDeck project. We make no promises about the performance of soundcards we have not personally tested!

A feature matrix is provided below to help you choose the soundcard which is right for your PiDeck. Some of these are current hardware, others are discontinued or obsolete models. Recycling is encouraged! :recycle: :sunglasses:

Please note that xwax supports up to three decks, and single deck USB soundcards can be combined to provide additional decks. This is not currently the case for single deck I²S soundcards such as the audioinjector.net stereo and Fe-Pi Audio HATs, due the two-channel limit of the Raspberry Pi I²S implementation.

Most full duplex soundcards have stereo line input and output. If a soundcard only supports line input, you will need an additional hardware pre-amp to use phono input. This pre-amp does not need to be very high quality for control vinyl (timecode) use. A basic DJ mixer with phono pre-amps can be used for testing a single vinyl deck. If you have a classic turntable with an earth wire, you will also need a grounding stud on the soundcard or preamp to reduce hum. Software pre-amps are not recommended for use with timecode, as their gain (being post-input) is sometimes not clean enough for a pure signal.  

Some USB phono interfaces are not full duplex and do not feature a line output from the CPU, even though the hardware features line output sockets, such as turntables and pre-amps with built in USB which are meant for recording only. The line outputs are routed from the built-in pre-amp, not the USB interface. These recording interfaces sometimes have fixed input gain which is not meant for DJs, as fast scratches and backspins can cause signal peaks which distort timecode. In these cases it is better to use the line output of the turntable into a full duplex soundcard with input level adjustment.

If you play any analogue vinyl or regular CDs without timecode, you will benefit from a hardware bypass or input mix control which enables you to play through without loss of quality, or disconnecting cables. 


## Known to work

Soundcard | Line input | Phono input | Number of decks | Hardware bypass
--------- | ---------- | ----------- | --------------- | ---------------
American Audio Genie II / Citronic AC-1 USB / KAM USBH100 Mk II / MixVibes Easy REC / MixVibes U-RIP 22 | :heavy_check_mark: | :heavy_check_mark: | 1 |
audioinjector.net stereo HAT | :heavy_check_mark: || 1 | :heavy_check_mark: (via amixer)
Behringer UCA 202 / Behringer UCA 222 | :heavy_check_mark: || 1 |
Behringer UFO 202 | :heavy_check_mark: | :heavy_check_mark: | 1 (with [hardware modification](https://mixxx.org/forums/viewtopic.php?t=2438)) |
Hercules Mk2 | :heavy_check_mark: | :heavy_check_mark: | 2 | :heavy_check_mark: (audio source buttons)
Numark Stereo IO | :heavy_check_mark: | :heavy_check_mark: | 1 |
Rane SL-1 | :heavy_check_mark: | :heavy_check_mark (soft. via xwax) | 2 | :heavy_check_mark: (need to find how to toggle, but both receive signal @ LINE level)
Reloop Digital Jockey 2 Interface Edition | :heavy_check_mark: | :heavy_check_mark: | 1 |
Traktor Audio 4 | :heavy_check_mark: | :heavy_check_mark: | 2 |
Traktor Audio 6 | :heavy_check_mark: | :heavy_check_mark: | 3 | :heavy_check_mark: (via amixer)
Traktor Audio 8 | :heavy_check_mark: | :heavy_check_mark: | 3 | :heavy_check_mark: (via input mode button)

## Potentially could work

Soundcard | Line input | Phono input | Number of decks | Hardware bypass
--------- | ---------- | ----------- | --------------- | ---------------
American Audio Versaport / MixVibes U-MIX44 / Reloop Spin! / iScratch Mixlive / Omnitronix DDI | :heavy_check_mark: | 1 deck only | 2 | ?
American Audio VMS2 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
American Audio VMS4.1 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Creative Sound Blaster X-Fi HD | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Denon DJ DS1 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Dynavox UPR-2.0 | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
ESI MAYA44 USB / MAYA44 USB+ | :heavy_check_mark: | | 2 | ?
Fe-Pi Audio v1.3 HAT | :heavy_check_mark: | | 1 | ?
Hercules Deejay Trim | :heavy_check_mark: | :heavy_check_mark: | ? | ?
Hercules RMX | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
McLelland UP-2.0 / American Audio Genie Pro | :heavy_check_mark: | :heavy_check_mark: | 1 | :heavy_check_mark: (input mix control)
MixVibes U46 mk2 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Power Dynamics PDX015 | :heavy_check_mark: | :heavy_check_mark: | 1 |
Reloop Iphono | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
Reloop Iphono 2 | :heavy_check_mark: | :heavy_check_mark: | 1 | ?
SM Pro XP203 | :heavy_check_mark: | :heavy_check_mark: | 1 | :heavy_check_mark: (input mix control)
Sonneteer Sedley USB | | :heavy_check_mark: | 1 | ?
Stanton Final Scratch ScratchAmp v1 | :heavy_check_mark: | :heavy_check_mark: | 2 | ?
Synchroscience by M-audio Conectiv | :heavy_check_mark: | :heavy_check_mark: | 2 | :heavy_check_mark: (via Mix knobs)
Traktor Audio 10 | :heavy_check_mark: | :heavy_check_mark: | 3 | via amixer?

## Needs more research

Soundcard | Why?
--------- | ----
Furutech ADL GT40A | Is it USB class compliant?
Furutech ADL Stratos | Is it USB class compliant?
Novation Twitch | Does capture work in ALSA?
Pioneer DJ INTERFACE 2 | Needs an ALSA driver
Rane Sixty-Two | Is it USB class compliant?
Reloop RMX-90 DVS | Needs an ALSA driver

## Will not be supported

Soundcard | Why?
--------- | ----
American Audio VMS4 | Buggy audio and distortion
Art USB Phono Plus | USB output to analogue on headphone jack only
ESI Gigaport HD/HD+ | No suitable inputs
Ion Record 2 PC | No suitable outputs from USB
NAD PP4 | No suitable outputs from USB
Numark DJ iO | No suitable inputs
Numark DJ iO 2 | No suitable inputs
Phonic Digitrack | Line input distortion
Pro-ject Phono Box USB / Pro-ject Phono Box USB V | No suitable outputs from USB
Rega Fono Mini A2D | No suitable outputs from USB
Reloop Digital Jockey 2 (not Interface Edition) | No suitable inputs
Stanton Final Scratch ScratchAmp v2 | It's FireWire, not USB
Terratec PhonoPreAmp iVinyl | No suitable outputs from USB
Traktor Audio 2 | No suitable inputs
USB turntable built-in (generic) | No suitable outputs from USB
