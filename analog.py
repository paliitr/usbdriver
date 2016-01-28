import sys
device = open('/dev/input/js0', 'r')
data = []
flag = ''
msg = [0, 0, 0, 0, 0, 0, 0, 0]

while True:
	for a in device.read(1):
		data += [ord(a)]
		if len(data) == 8:
			msg = data
			data = []
	print('{0} {1} {2} {3}'.format(msg[6], msg[7], msg[4], msg[5]))