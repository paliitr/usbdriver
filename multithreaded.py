import pygame
from threading import Thread, Lock

lock = Lock()
axis_data = []
button_data = []
hat_data = []


def acquireData():
	# lock.acquire()
	global axis_data
	global button_data
	global hat_data

	clock = pygame.time.Clock()
	pygame.joystick.init()

	while True:
		joystick = pygame.joystick.Joystick(0)
		joystick.init()

		axes = joystick.get_numaxes()
		for i in range(axes):
			axis_data[i] = joystick.get_axis(i)
			
		buttons = joystick.get_numbuttons()
		for i in range(buttons):
			button = joystick.get_button(i)
			button_data += [button]
		
		hats = joystick.get_numhats()
		for i in range(hats):
			hat = joystick.get_hat(i)
			hat_data += [hat]
		clock.tick(100)
	# lock.release()


def printer():
	global axis_data
	global button_data
	global hat_data

	while True:
		print(axis_data+button_data+hat_data)

thread1 = Thread(target=acquireData)
thread2 = Thread(target=printer)

thread1.start()
thread2.start()