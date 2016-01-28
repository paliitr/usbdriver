from threading import Thread
import time
import flagged

count = 0

def timer(name, delay, repeat):
	print "Timer: " + name + " started"
	while repeat > 0:
		time.sleep(delay)
		print name + ": " + str(time.ctime(time.time()))
		repeat -= 1
	print "Timer: " + name + " complete"

def counter():
	while True:
		global count
		count += 1
		print "Counter Process: " + str(count)
		time.sleep(0.05)

def printer():
	while True:
		global count
		print "Printer Process: " + str(count)
		time.sleep(0.1)

def acquire():
	flagged.run()

def joystickPrint():
	if(button_flags['b1'] or button_flags['b2'] or button_flags['b3'] or button_flags['b4'] or button_flags['l1'] or button_flags['l2'] or button_flags['r1'] or button_flags['r2'] or button_flags['jl'] or button_flags['jr']):
		print button_flags

def Main():
	# thread1 = Thread(target=timer, args=("Timer1", 0.1, 50))
	# thread2 = Thread(target=timer, args=("Timer2", 0.2, 50))

	# thread3 = Thread(target=counter)
	# thread4 = Thread(target=printer)

	thread5 = Thread(target=acquire)
	thread6 = Thread(target=joystickPrint)

	thread5.start()
	thread6.start()

	print "Main complete"

if __name__ == '__main__':
	Main()