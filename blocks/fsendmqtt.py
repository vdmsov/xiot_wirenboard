#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : fsendmqtt.py
#	Data   : 03-05-2019
#==============================================================================

import os
import paho.mqtt.publish as pub


def get_wirenboard_sn():
		sn = os.popen("cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2").read()
		sn = sn.strip()
		return sn


def get_topic_head():
	serial_number = get_wirenboard_sn()
	topic_head = '/xiot/wb' + serial_number + '/'
	return topic_head


class fSendMqtt:

	id_number = None
	val1 = None
	in1 = None
	prev_in1 = None

	global topic


	def __init__(self, id_number):
		self.id_number = id_number
		self.val1 = None
		self.in1 = None

		self.topic = 'None'


	def set_val1(self, value):
		self.val1 = value


	def set_in1(self, value):
		self.in1 = value


	def publisher(self):		
		if ((self.val1 != None) and (self.in1 != None)):
			if (self.prev_in1 != self.in1):
				self.prev_in1 = self.in1

				self.topic = get_topic_head() + self.val1
				
				pub.single(self.topic, str(self.in1), retain=True, hostname="localhost", port=1883, keepalive=60)

		
		#print '\n'
		#print '*'*50
		#print 'Name:',  'fSendMqtt'
		#print 'ID:',    self.id_number
		#print 'val1:',  self.val1
		#print 'in1:',   self.in1
		#print 'Topic:', self.topic
		#print '*'*50
