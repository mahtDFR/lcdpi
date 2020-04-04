Utilities to cast content to a Raspberry Pi connected to a 3.5" TFT screen.

#### Hardware requirements

- Raspberry Pi (I used a 3)
- [3.5" TFT display](https://wiki.dfrobot.com/3.5_inches_TFT_Touchscreen_for_Raspberry_Pi_SKU__DFR0428)

#### Software requirements

- Python 3
- Chromium

#### How to use

- SSH into your pi
- Navigate to `lcdpi`
- Run `$ python3 <script>.py`

#### What's included?

- [urldrop.py](https://github.com/mahtDFR/lcdpi/blob/master/urldrop.py) is a utility to drop a URL into your SSH session that will be cast to the lcd
- [yturldrop.py](https://github.com/mahtDFR/lcdpi/blob/master/yturldrop.py) is a utility to drop a YouTube URL into your SSH session that will be cast to the lcd (semi-working)
- [giphytv.py](https://github.com/mahtDFR/lcdpi/blob/master/giphytv.py) allows you to input a keyword into your SSH session that will display random gifs related to that keyword on the lcd (using [giphytv](http://tv.giphy.com/work%20remote))


![walk into the club like...](https://media.giphy.com/media/ZdU3bTTc1WWStZM5lm/giphy.gif)

Comments and contributions welcome.
