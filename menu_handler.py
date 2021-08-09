import displayio
from adafruit_display_text import label
import terminalio
import time

def HandleMenu(macropad, config, logy, group):
    macropad.display.show(UpdateMessage(False, 0, macropad))
    macropad.display.refresh()

    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch and config['is_menu']:
        config['is_menu'] = False
        macropad.display.show(group)
        macropad.display.refresh()
        print("good bye")
    return


def UpdateMessage(isPress, remaining, macropad):
    group = displayio.Group()
    group.append(
        label.Label(
            terminalio.FONT,
            text="Is Writeable:",
            color=0xFFFFFF,
            anchored_position=(
                0,
                0,
            ),
            anchor_point=(0, 0),
        )
    )

    group.append(
        label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            anchored_position=(
                0,
                (macropad.display.height / 4) * 1,
            ),
            anchor_point=(0.1, 0),
        )
     )

    group.append(
        label.Label(
            terminalio.FONT,
            text="Remaning",
            color=0xFFFFFF,
            anchored_position=(
                0,
                (macropad.display.height / 4) * 2,
            ),
            anchor_point=(0, 0),
        )
    )
    group.append(
        label.Label(
            terminalio.FONT,
            text="",
            color=0xFFFFFF,
            anchored_position=(
                0,
                (macropad.display.height / 4) * 3,
            ),
            anchor_point=(0.3, 0),
        )
    )
    return group
