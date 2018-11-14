# EuroPi

Put a Pi in your Eurorack! [Hackaday.io Project](https://hackaday.io/project/162308-europi)

## Hardware

Nothing fancy, just a regular 128x32 SSD1306 OLED __i2c__ display and a 24 click (forgot what the right term is) rotatory encoder with switch.

So in my configuration, the two outer pins (on the 3 pins side) of the rotatory encoder goes to GPIO 14 and 15, and one of the swich pin goes to GPIO 4. The middle pin and the other of the switch pin goes to ground. We're talking about __BCM__ GPIO mode here.

OLED display is wired with SDA going to BCM 2 and SCL goes to BCM 3.

If you need a [pinout reference](https://pinout.xyz/).

__Note__ Depending on the type of encoder you get, you might have the different rotation than mine. In this case, simply buy the correct one. OK, I'm joking, just change the code in `encoder_ev` function inside `menu.py` (swap `self.prev()` & `self.next()`, FYI).

## Install

### Dependencies
Uhh I forgot the details, but you need to get your OLED working first.

Check out the tutorial [here](https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black) and set it up!

After you get that working with their examples, you can clone this repo and run it.

## Run
```
python3 main.py
```

## License

[MIT](https://poyu.mit-license.org/)

BTW, I don't know what to do if I copy and modifies someone else's code (GPLv3, I think) that has a different license. If you know better, please tell me. Thanks!

There's also a font, [DejaVuSans](https://dejavu-fonts.github.io/) I'm distributing here. Hope that's okay under their license. Again, please tell me if you know better.
