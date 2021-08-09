def HandleMacro(macropad, last_position, apps, last_encoder_switch, config, logy):
    position = macropad.encoder
    if position != last_position:
        app_index = position % len(apps)
        apps[app_index].switch()
        last_position = position

    # Handle encoder button. If state has changed, and if there's a
    # corresponding macro, set up variables to act on this just like
    # the keypad keys, as if it were a 13th key/macro.
    macropad.encoder_switch_debounced.update()
    encoder_switch = macropad.encoder_switch_debounced.pressed
    if encoder_switch != last_encoder_switch:
        last_encoder_switch = encoder_switch
        key_number = 12  # else process below as 13th macro
        pressed = encoder_switch
    else:
        event = macropad.keys.events.get()
        if not event or event.key_number >= len(apps[app_index].macros):
            return  # No key events, or no corresponding macro, resume loop
        key_number = event.key_number
        pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop. 
    sequence = apps[app_index].macros[key_number][3]
    macroType = apps[app_index].macros[key_number][2]
    color = apps[app_index].macros[key_number][0]
    if pressed:
        if key_number == 12:
            config["is_menu"] = True
            return
        if key_number < 12:  # No pixel for encoder button
            # TODO: Add Press Color to app setup
            macropad.pixels[key_number] = [0, color[1] / 3, color[2] / 3, color[3] / 3]
            macropad.pixels.show()
        try:
            for item in sequence:
                if type(item) == int:
                    logy.debug("%d", item)
                else:
                    logy.debug(item)
                # l.debug("item %d", item)
                if macroType == "macro":
                    if type(item) == int:
                        macropad.keyboard.send(item)
                        # macropad.keyboard.release(item)
                    else:
                        macropad.keyboard_layout.write(item)
                elif macroType == "control":
                    macropad.consumer_control.send(item)
                else:
                    if isinstance(item, int):
                        if item >= 0:
                            macropad.keyboard.press(item)
                        else:
                            macropad.keyboard.release(item)
                    else:
                        macropad.keyboard_layout.write(item)
        except:
            logy.error("failed Macro %d", macroType)
    else:
        # Release any still-pressed modifier keys
        if macroType == "sequence":
            for item in sequence:
                if isinstance(item, int) and item >= 0:
                    macropad.keyboard.release(item)
        if key_number < 12:  # No pixel for encoder button
            macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
            macropad.pixels.show()
    return
