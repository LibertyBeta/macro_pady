import board
import digitalio
import storage
import time
import usb_cdc
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

# switch = digitalio.DigitalInOut(board.ENCODER_SWITCH)
isPressed = False

# led = digitalio.DigitalInOut(board.LED)
# led.switch_to_output()
print("")
print("")
print("")
print("")
for x in range(10):
    # if not switch.value:
        # If the switch pin is connected to ground CircuitPython can write to the drive
        # storage.remount("/", readonly=False)
        # while not switch.value:
        #    led.value = not led.value
        #    time.sleep(0.04)
        # break
    time.sleep(0.5)
    isPressed = button.value
    print("")
    print("")
    print("Key is pressed:", isPressed)
    print("Booting in:", 10 - x)
    print("")
# led.value = False
if not isPressed:
    print("Locking device")
    storage.remount("/", readonly=True)
    usb_cdc.disable()
    storage.disable_usb_drive()
else:
    print("dev Mode")
    storage.remount("/", readonly=True)
    usb_cdc.enable(console=True, data=True)
    storage.enable_usb_drive()
