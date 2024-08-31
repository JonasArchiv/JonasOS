# JonasOS
This isn't really a hole OS. It is more like a VoiceAssistant for my own Interest.<br>
## Installation
Install the requirements with `pip install -r requirements.txt` <br>
Setup in config.py your own settings. <br>
Run `python main.py` to start the Assistant mit all features. <br>

## Features
### Mail
You need to insert your mail and app_password from google. For a app password you need 2FA. <br>
When you like to use another mail provider you need to change the smtp server and port. <br>
Setup then in config.py

### Fingerprint Sensor
#### Raspery Pi
- VCC of the sensor to 5V of the Raspberry Pi. <br>
- GND of the sensor to GND of the Raspberry Pi. <br>
- TX of the sensor to GPIO14 (TXD) of the Raspberry Pi. <br>
- RX of the sensor to GPIO15 (RXD) of the Raspberry Pi. <br>
#### Skript
- Make sure the command for communication with the fingerprint sensor are right.

### QR Code Tools:
- Generate QR Code
- Generate QR Code with picture in the mittel
- Read QR Code from Image
- Read QR Code from Webcam

### Timezone
- Get the current time in Germany
- Get the current time in a specific timezone