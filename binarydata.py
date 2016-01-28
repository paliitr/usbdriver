import os
import struct
import array
from fcntl import ioctl

axis_states = {}
button_states = {}

axis_names = {
    0x00: 'x',
    0x01: 'y',
    0x02: 'z',
    0x05: 'rz',
    0x10: 'hat0x',
    0x11: 'hat0y',
}

button_names = {
    0x120: '1',
    0x121: '2',
    0x122: '3',
    0x123: '4',
    0x124: 'top2',
    0x125: 'R1',
    0x126: 'L2',
    0x127: 'R2',
    0x128: 'SELECT',
    0x129: 'START',
    0x12a: 'Left Joystick',
    0x12b: 'Right Joystick',
}

axis_map = []
button_map = []
jsdev = open('/dev/input/js0', 'rb')

buf = array.array('c', ['\0'] * 64)
ioctl(jsdev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
js_name = buf.tostring()
print('Device name: %s' % js_name)

buf = array.array('B', [0])
ioctl(jsdev, 0x80016a11, buf) # JSIOCGAXES
num_axes = buf[0]

buf = array.array('B', [0])
ioctl(jsdev, 0x80016a12, buf) # JSIOCGBUTTONS
num_buttons = buf[0]

buf = array.array('B', [0] * 0x40)
ioctl(jsdev, 0x80406a32, buf) # JSIOCGAXMAP

for axis in buf[:num_axes]:
    axis_name = axis_names.get(axis, 'unknown(0x%02x)' % axis)
    axis_map.append(axis_name)
    axis_states[axis_name] = 0.0

buf = array.array('H', [0] * 200)
ioctl(jsdev, 0x80406a34, buf) # JSIOCGBTNMAP

for btn in buf[:num_buttons]:
    btn_name = button_names.get(btn, 'unknown(0x%03x)' % btn)
    button_map.append(btn_name)
    button_states[btn_name] = 0

print '%d axes found: %s' % (num_axes, ', '.join(axis_map))
print '%d buttons found: %s' % (num_buttons, ', '.join(button_map))

while True:
    evbuf = jsdev.read(8)
    if evbuf:
        time, value, type, number = struct.unpack('IhBB', evbuf)

        if type & 0x80:
             print "(initial)",

        if type & 0x01:
            button = button_map[number]
            if button:
                button_states[button] = value
                if value:
                    print "%s pressed" % (button)
                else:
                    print "%s released" % (button)

        if type & 0x02:
            axis = axis_map[number]
            if axis:
                fvalue = value
                axis_states[axis] = fvalue
                print "%s: %.3f" % (axis, fvalue)