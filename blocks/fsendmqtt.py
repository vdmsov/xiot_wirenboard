#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : fsendmqtt.py
#	Data   : 03-05-2019
#==============================================================================

import paho.mqtt.publish as pub

class fSendMqtt:

	id_number = None
	val1 = None
	in1 = None
	prev_in1 = None


	def __init__(self, id_number):
		self.id_number = id_number
		self.val1 = None
		self.in1 = None

	def set_val1(self, value):
		self.val1 = value

	def set_in1(self, value):
		self.in1 = value

	def publisher(self):
		if (self.val1 != None) and (self.in1 != None):

			if (self.prev_in1 != self.in1):
				self.prev_in1 = self.in1
				pub.single(str(self.val1), str(self.in1), hostname="localhost")

		#print '\n'
		#print 'ID:', self.id_number , 'fSendMqtt: val1 = ' , self.val1
		#print 'ID:', self.id_number , 'fSendMqtt: in1 = ' , self.in1