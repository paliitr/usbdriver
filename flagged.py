import sys
device = open('/dev/input/js0', 'r')
data = []
flag = ''
button_flags = {'b1': 0, 'b2': 0, 'b3': 0, 'b4': 0, 'l1': 0, 'l2': 0, 'r1': 0, 'r2': 0,  'jl': 0, 'jr': 0}
count = 0

def run():
        global data
        global flag
        global button_flags
        global count
        while True:
                count = count + 1
                print('Before reading {0}'.format(count))
                for a in device.read(1):
                        data += [ord(a)]
                        if len(data) == 8:
                                if data[6] == 1:
                                        if data[7] == 0:
                                                if data[4] == 1:
                                                        button_flags['b1'] = 1
                                                elif data[4] == 0:
                                                        button_flags['b1'] = 0
                                        if data[7] == 1:
                                                if data[4] == 1:
                                                        button_flags['b2'] = 1
                                                elif data[4] == 0:
                                                        button_flags['b2'] = 0
                                        if data[7] == 2:
                                                if data[4] == 1:
                                                        button_flags['b3'] = 1
                                                elif data[4] == 0:
                                                        button_flags['b3'] = 0
                                        if data[7] == 3:
                                                if data[4] == 1:
                                                        button_flags['b4'] = 1
                                                elif data[4] == 0:
                                                        button_flags['b4'] = 0
                                        if data[7] == 4:
                                                if data[4] == 1:
                                                        button_flags['l1'] = 1
                                                elif data[4] == 0:
                                                        button_flags['l1'] = 0
                                        if data[7] == 5:
                                                if data[4] == 1:
                                                        button_flags['r1'] = 1
                                                elif data[4] == 0:
                                                        button_flags['r1'] = 0
                                        if data[7] == 6:
                                                if data[4] == 1:
                                                        button_flags['l2'] = 1
                                                elif data[4] == 0:
                                                        button_flags['l2'] = 0
                                        if data[7] == 7:
                                                if data[4] == 1:
                                                        button_flags['r2'] = 1
                                                elif data[4] == 0:
                                                        button_flags['r2'] = 0
                                        if data[7] == 10:
                                                if data[4] == 1:
                                                        button_flags['jl'] = 1
                                                elif data[4] == 0:
                                                        button_flags['jl'] = 0
                                        if data[7] == 11:
                                                if data[4] == 1:
                                                        button_flags['jr'] = 1
                                                elif data[4] == 0:
                                                        button_flags['jr'] = 0
                                # elif data[6] == 2:
                                #         if data[7] == 1:
                                #                 if data[5] == 128:
                                #                         if data[4] == 1:
                                #                                 print 'Key Up pressed.'
                                #                                 flag = 'up'
                                #                 elif data[5] == 127:
                                #                         if data[4] == 255:
                                #                                 print 'Key Down pressed.'
                                #                                 flag = 'down'
                                #                 elif data[5] == 0:
                                #                         if flag == 'up':
                                #                                 print 'Key Up Released.'
                                #                                 flag = ''
                                #                         elif flag == 'down':
                                #                                 print 'Key Down Released.'
                                #                                 flag = ''
                                #         elif data[7] == 0:
                                #                 if data[5] == 128:
                                #                         if data[4] == 1:
                                #                                 print 'Key Left pressed.'
                                #                                 flag = 'left'
                                #                 elif data[5] == 127:
                                #                         if data[4] == 255:
                                #                                 print 'Key Right pressed.'
                                #                                 flag = 'right'
                                #                 elif data[5] == 0:
                                #                         if flag == 'left':
                                #                                 print 'Key Left Released.'
                                #                                 flag = ''
                                # elif flag == 'right':
                                #                                 print 'Key Right Released.'
                                #                                 flag = ''
                                data = []
                print('After reading'.format(count))
                if(button_flags['b1'] or button_flags['b2'] or button_flags['b3'] or button_flags['b4'] or button_flags['l1'] or button_flags['l2'] or button_flags['r1'] or button_flags['r2'] or button_flags['jl'] or button_flags['jr']):
                        print button_flags

run()