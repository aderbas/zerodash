# zerodash

## Requirements
 - Raspberry Pi Zero W. 
 - Micro SD with Raspberry Pi OS Bullseye.
 - 3.5inch LCD Display.

## Get Started
- Install Raspberry Pi OS using [Raspberry Pi Imager](https://www.raspberrypi.com/software/).   
OBS: If you using Linux: ``$ sudo apt install rpi-imager``.

- Choose a image: Raspberry Pi OS 32Bit (for Pi Zero W).
- Click the gear icon at right corner and configure: Wi-Fi, Change Default Password, Enable SSH and Set Timezone.

On finish, put the card in the RPI and boot normally.

### SSH
Discover the IP DHCP of your RPI and access via SSH.
```bash
$ ssh pi@<raspberry pi ip>
pi@ password:
```

### Configure LCD
```bash
$ git clone https://github.com/goodtft/LCD-show.git
$ chmod -R 755 LCD-show
$ cd LCD-show/
$ sudo ./LCD35-show
```

## Boot configuration
Edit autostart file
```bash
$ sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
- Comment out the line by adding # at the beginning on line: ``@lxpanel --profile LXDE-pi`` to hide App bar from Raspberry Pi OS.
- Disable screensaver adding the lines below:
```
@xset s off
@xset -dpms
```
The file looks like:
```
#@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
@xscreensaver -no-splash
@xset s off
@xset -dpms
```


## Instalation

Requires Python 3.3 or newer.

```bash
$ pip install pyqt5
```
Or you can install from apt
```bash
$ sudo apt-get install python3-pyqt5
```

```bash
$ cd ~
$ git clone https://github.com/aderbas/zerodash.git
$ cd zerodash
$ cp .env.example .env # open file and edit variable values
$ pip3 install -r requirements.txt
$ sudo ln -s /home/pi/zerodash/zerodash.service /lib/systemd/system/zerodash.service
$ sudo systemctl enable zerodash.service
$ sudo reboot
```