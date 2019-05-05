#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : fstart.py
#	Data   : 03-05-2019
#==============================================================================

from threading import Thread
import time

class fStart:
	
	id_number = None
	in1 = False
	out1 = False


	def set_in1(self, value):
		self.in1 = value

	def set_out1(self):
		if (self.in1 == True):
			self.out1 = True
		else:
			self.out1 = False


		#print '\n'
		#print '*'*50
		#print 'Name:', 'fStart'
		#print 'ID:',   self.id_number
		#print 'in1:',  self.in1
		#print 'out1:', self.out1
		#print '*'*50


	def get_in1(self):
		while (True):
			time.sleep(1)			
			self.set_out1()


	def __init__(self, id_number):
		self.id_number = id_number
		thr = Thread(target = self.get_in1)
		thr.start()
		print 'fStart: Expecting starting command on in1 input ("True" is START)'