# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control_code import (
    ConsumerControlCode,
)  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "Launcher - Life",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        ([0, 60, 98, 74], "< Back", "sequence", [Keycode.ALT, Keycode.LEFT_ARROW]),
        ([0, 60, 98, 74], "Fwd >", "sequence", [Keycode.ALT, Keycode.RIGHT_ARROW]),
        ([0, 60, 98, 74], "Up", "sequence", [ConsumerControlCode.VOLUME_INCREMENT]),  # Scroll up
        # 2nd row ----------
        ([0, 60, 98, 74], "- Size", "sequence", [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        ([0, 60, 98, 74], "Size +", "sequence", [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        ([0, 60, 98, 74], "Down", "sequence", " "),  # Scroll down
        # 3rd row ----------
        ([0, 60, 98, 74], "<", "control", [ConsumerControlCode.SCAN_PREVIOUS_TRACK]),
        ([0, 60, 98, 74], "=>", "control", [ConsumerControlCode.PLAY_PAUSE]),
       (
            [0, 60, 98, 74],
            "Chrome",
            "macro",
            [Keycode.GUI, "Chrome", Keycode.ENTER],
        ),  # Adafruit in new window
        # 4th row ----------
        (
            [0, 60, 98, 74],
            "FFXIV",
            "macro",
            [Keycode.GUI, "Final Fantasy XIV", Keycode.ENTER],
        ),  # Adafruit in new window
        (
            [0, 60, 98, 74],
            "DISCORD",
            "macro",
            [Keycode.GUI, "DISCORD", Keycode.ENTER],
        ),  # Digi-Key in new window
        ([0, 60, 98, 74], "NULL", "sequence", [Keycode.GUI]),  # Hack-a-Day in new win
        # Encoder button ---
        ([0, 60, 98, 74], "", "sequence", [Keycode.CONTROL, "w"]),  # Close tab
    ],
}
