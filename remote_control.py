# Remote control for Raspberry Pi robot using 8BitDo SF30 gamepad

# Imports
import explorerhat
from evdev import InputDevice, categorize, ecodes

# Creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event0')

# Prints out device info at start
print(gamepad)

# Evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    # Filters by event type
    if event.type == ecodes.EV_KEY:
        # Code for buttons goes here
        print(event)
    elif event.type == ecodes.EV_ABS:
        if event.code == 16:
            if event.value == 0:
                # Stop
                explorerhat.motor.one.stop()
                explorerhat.motor.two.stop()
            elif event.value == -1:
                # Left
                explorerhat.motor.one.forward(50)
                explorerhat.motor.two.backwards(50)
            elif event.value == 1:
                # Right
                explorerhat.motor.one.backwards(50)
                explorerhat.motor.two.forward(50)
        elif event.code == 17:
            if event.value == 0:
                # Stop
                explorerhat.motor.one.stop()
                explorerhat.motor.two.stop()   
            elif event.value == -1:
                # Forward
                explorerhat.motor.one.backwards(100)
                explorerhat.motor.two.backwards(100)
            elif event.value == 1:
                # Backwards
                explorerhat.motor.one.forward(100)
                explorerhat.motor.two.forward(100)

