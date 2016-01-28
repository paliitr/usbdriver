import sys
 
device = open('/dev/input/js0', 'r')
data = []
flag = ''
button_flags = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def run():
        global data
        global flag
        global button_flags
        while True:
                for a in device.read(1):
                        data += [ord(a)]
                        if len(data) == 8:
                                if data[6] == 1:
                                        if data[7] == 0:
                                                if data[4] == 1:
                                                        print 'Button 1 pressed.'
                                                elif data[4] == 0:
                                                        print 'Button 1 Released.'
                                        if data[7] == 1:
                                                if data[4] == 1:
                                                        print 'Button 2 pressed.'
                                                elif data[4] == 0:
                                                        print 'Button 2 Released.'
                                        if data[7] == 2:
                                                if data[4] == 1:
                                                        print 'Button 3 pressed.'
                                                elif data[4] == 0:
                                                        print 'Button 3 Released.'
                                        if data[7] == 3:
                                                if data[4] == 1:
                                                        print 'Button 4 pressed.'
                                                elif data[4] == 0:
                                                        print 'Button 4 Released.'
                                        if data[7] == 4:
                                                if data[4] == 1:
                                                        print 'Trigger L1 pressed.'
                                                elif data[4] == 0:
                                                        print 'Trigger L1 Released.'
                                        if data[7] == 5:
                                                if data[4] == 1:
                                                        print 'Trigger R1 pressed.'
                                                elif data[4] == 0:
                                                        print 'Trigger R1 Released.'
                                        if data[7] == 6:
                                                if data[4] == 1:
                                                        print 'Trigger L2 pressed.'
                                                elif data[4] == 0:
                                                        print 'Trigger L2 Released.'
                                        if data[7] == 7:
                                                if data[4] == 1:
                                                        print 'Trigger R2 pressed.'
                                                elif data[4] == 0:
                                                        print 'Trigger R2 Released.'
                                        if data[7] == 10:
                                                if data[4] == 1:
                                                        print 'Left Joystick pressed.'
                                                elif data[4] == 0:
                                                        print 'Left Joystick Released.'
                                        if data[7] == 11:
                                                if data[4] == 1:
                                                        print 'Right Joystick pressed.'
                                                elif data[4] == 0:
                                                        print 'Right Joystick Released.'
                                elif data[6] == 2:
                                        if data[7] == 1:
                                                if data[5] == 128:
                                                        if data[4] == 1:
                                                                print 'Key Up pressed.'
                                                                flag = 'up'
                                                elif data[5] == 127:
                                                        if data[4] == 255:
                                                                print 'Key Down pressed.'
                                                                flag = 'down'
                                                elif data[5] == 0:
                                                        if flag == 'up':
                                                                print 'Key Up Released.'
                                                                flag = ''
                                                        elif flag == 'down':
                                                                print 'Key Down Released.'
                                                                flag = ''
                                        elif data[7] == 0:
                                                if data[5] == 128:
                                                        if data[4] == 1:
                                                                print 'Key Left pressed.'
                                                                flag = 'left'
                                                elif data[5] == 127:
                                                        if data[4] == 255:
                                                                print 'Key Right pressed.'
                                                                flag = 'right'
                                                elif data[5] == 0:
                                                        if flag == 'left':
                                                                print 'Key Left Released.'
                                                                flag = ''
                                                        elif flag == 'right':
                                                                print 'Key Right Released.'
                                                                flag = ''
                                data = []

run()