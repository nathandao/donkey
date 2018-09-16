#!/bin/bash

#https://pimylifeup.com/xbox-controllers-raspberry-pi/
sudo apt-get update

sudo apt-get install xboxdrv

sudo bash -c "echo 1 > /sys/module/bluetooth/parameters/disable_ertm"
#if you want a better solution to disable bluetooth ertm, then edit /etc/default/grub and add the kernel flag 'bluetooth.disable_ertm=1' to the GRUB_CMDLINE_LINUX line. Then run 'sudo grub-mkconfig -o /boot/grub/grub.cfg' and reboot.#

#reboot after this

sudo bluetoothctl
#agent on
#scan on
#Press button on xbox ctrl, you should see a mac address
#pair :MAC:
#trust :MAC:
#connect :MAC:
#quit

sudo apt-get install joystick
#test it:
jstest /dev/input/js0

