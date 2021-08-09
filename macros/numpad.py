# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        ([0, 60, 98, 74], '7', "sequence", ['7']),
        ([0, 60, 98, 74], '8', "sequence", ['8']),
        ([0, 60, 98, 74], '9', "sequence", ['9']),
        # 2nd row ----------
        ([0, 60, 98, 74], '4', "sequence", ['4']),
        ([0, 60, 98, 74], '5', "sequence", ['5']),
        ([0, 60, 98, 74], '6', "sequence", ['6']),
        # 3rd row ----------
        ([0, 60, 98, 74], '1', "sequence", ['1']),
        ([0, 60, 98, 74], '2', "sequence", ['2']),
        ([0, 60, 98, 74], '3', "sequence", ['3']),
        # 4th row ----------
        ([0, 60, 98, 74], '*', "sequence", ['*']),
        ([0, 60, 98, 74], '0', "sequence", ['0']),
        ([0, 60, 98, 74], '#', "sequence", ['#']),
        # Encoder button ---
        ([0, 60, 98, 74], '', "sequence", [Keycode.BACKSPACE])
    ]
}
