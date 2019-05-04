#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : fstart.py
#	Data   : 03-05-2019
#==============================================================================

from threading import Thread
import time


class fStart:

	in1 = False
	link1 = None

	def set_link1(self):
		fStart.link1 = 'start'
		print 'fStart: link1 = \'start\''

	def get_in1(self):
		while (self.in1 == False):
			time.sleep(0.5)
		print 'fStart: in1 = True'
		self.set_link1()

	def __init__(self):
		thr = Thread(target = self.get_in1)
		thr.start()
		print 'fStart: Expecting starting command on in1 input ("True" is START)'