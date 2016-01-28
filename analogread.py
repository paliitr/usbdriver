import sys
device = open('/dev/input/js0', 'r')
data = []
flag = ''

while True:
        for a in device.read(1):
                data += [ord(a)]
                if len(data) == 8:
                        if data[6] == 2:
                            if data[7] == 3:
                                    coord = 'x'
                                    data4 = data[4]
                                    data5 = data[5]
                                    print('Data 4: {0}, Data 5: {1}, Coordinate: {2}'.format(data4, data5, coord))
                            elif data[7] == 2:
                                    coord = 'y'
                                    data4 = data[4]
                                    data5 = data[5]
                                    print('Data 4: {0}, Data 5: {1}, Coordinate: {2}'.format(data4, data5, coord))        
                            data = []