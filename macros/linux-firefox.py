# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Linux Firefox', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        ([0, 60, 98, 74], '< Back', "sequence", [Keycode.CONTROL, '[']),
        ([0, 60, 98, 74], 'Fwd >', "sequence", [Keycode.CONTROL, ']']),
        ([0, 60, 98, 74], 'Up', "sequence", [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        ([0, 60, 98, 74], '< Tab', "sequence", [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        ([0, 60, 98, 74], 'Tab >', "sequence", [Keycode.CONTROL, Keycode.TAB]),
        ([0, 60, 98, 74], 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        ([0, 60, 98, 74], 'Reload', "sequence", [Keycode.CONTROL, 'r']),
        ([0, 60, 98, 74], 'Home', "sequence", [Keycode.CONTROL, 'h']),
        ([0, 60, 98, 74], 'Private', "sequence", [Keycode.CONTROL, Keycode.SHIFT, 'p']),
        # 4th row ----------
        ([0, 60, 98, 74], 'Ada', "sequence", [Keycode.CONTROL, 't', -Keycode.CONTROL,
                           'www.adafruit.com\n']),   # adafruit.com in a new tab
        ([0, 60, 98, 74], 'Dev Mode', "sequence", [Keycode.F12]),    # dev mode
        ([0, 60, 98, 74], 'Digi', "sequence", [Keycode.CONTROL, 't', -Keycode.CONTROL,
                             'digikey.com\n']), # digikey in a new tab
        # Encoder button ---
        ([0, 60, 98, 74], '', "sequence", [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
