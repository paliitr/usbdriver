import pygame

axis_data = [0, 0, 0, 0]
button_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
hat_data = [(0, 0)]

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

while True:
	print "Start of Reading......"
	js = pygame.joystick.Joystick(0)
	js.init()
	axes = js.get_numaxes()
	buttons = js.get_numbuttons()
	hats = js.get_numhats()
	for i in range(axes):
		# axis_data[i] = js.get_axis(i)
		print js.get_axis(i)

	for i in range(buttons):
		# button_data[i] = js.get_button(i)
		print js.get_button(i)

	for i in range(hats):
		# hat_data[i] = js.get_hat(i)
		print js.get_hat(i)

	# display_axis = ', '.join([str(a) for a in axis_data])
	# display_button = ', '.join([str(b) for b in button_data])
	# display_hat = ', '.join([str(c) for c in hat_data])
	# print "Data: " + display_axis + " " + display_button + " " + display_axis + " \n"
	print "End of Reading........"
	clock.tick(10)