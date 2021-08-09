"""
A fairly straightforward macro/hotkey program for Adafruit MACROPAD.
Macro key setups are stored in the /macros folder (configurable below),
load up just the ones you're likely to use. Plug into computer's USB port,
use dial to select an application macro set, press MACROPAD keys to send
key sequences.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import displayio
import terminalio
import usb_cdc
import time
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from adafruit_macropad import MacroPad
import adafruit_logging as logging
from adafruit_hid.consumer_control import ConsumerControl
from macro_handler import HandleMacro
from menu_handler import HandleMenu
import board

print(board)

# CONFIGURABLES ------------------------

MACRO_FOLDER = "/macros"


# Default State --------
config = {"is_menu": False, "is_led": True}
# SETUP LOGGER ------------------------
logy = logging.getLogger("test")
# l.addHandler(FileHandler('log.txt'))
logy.setLevel(logging.DEBUG)
logy.debug("Booting Up....")
# CLASSES AND FUNCTIONS ----------------


class App:
    def __init__(self, appdata):
        self.name = appdata["name"]
        self.macros = appdata["macros"]

    def switch(self):
        group[13].text = self.name  # Application name
        for i in range(12):
            if i < len(self.macros):  # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
                group[i].text = ""
        macropad.keyboard.release_all()
        macropad.pixels.show()
        macropad.display.refresh()


# INITIALIZATION -----------------------

macropad = MacroPad()
macropad.display.auto_refresh = False
macropad.pixels.auto_write = False

# Set up displayio group with all the labels
group = displayio.Group()
for key_index in range(12):
    x = key_index % 3
    y = key_index // 3
    group.append(
        label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            anchored_position=(
                (macropad.display.width - 1) * x / 2,
                macropad.display.height - 1 - (3 - y) * 12,
            ),
            anchor_point=(x / 2, 1.0),
        )
    )
group.append(Rect(0, 0, macropad.display.width, 12, fill=0xFFFFFF))
group.append(
    label.Label(
        terminalio.FONT,
        text="",
        color=0x000000,
        anchored_position=(macropad.display.width // 2, -2),
        anchor_point=(0.5, 0.0),
    )
)
macropad.display.show(group)

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith(".py"):
        try:
            module = __import__(MACRO_FOLDER + "/" + filename[:-3])
            apps.append(App(module.app))
        except (
            SyntaxError,
            ImportError,
            AttributeError,
            KeyError,
            NameError,
            IndexError,
            TypeError,
        ) as err:
            logy.error("error is %d:", err)
            pass
print(type(files))
if not apps:
    group[13].text = "NO MACRO FILES FOUND"
    macropad.display.refresh()
    while True:
        pass

last_position = None
last_encoder_switch = macropad.encoder_switch_debounced.pressed
app_index = 0
apps[app_index].switch()


# MAIN LOOP ----------------------------

while True:
    if config['is_menu']:
        HandleMenu(macropad, config, logy, group)
    else:
        HandleMacro(macropad, last_position, apps, last_encoder_switch, config, logy)