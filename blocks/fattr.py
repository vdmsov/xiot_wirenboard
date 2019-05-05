#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : fattr.py
#	Data   : 03-05-2019
#==============================================================================

class fAttr:
	
	id_number = None
	val1 = None
	in1 = False
	out1 = None


	def __init__(self, id_number):
		self.id_number = id_number
		self.val1 = None
		self.in1 = False
		self.out1 = None


	def set_val1(self, value):
		self.val1 = value


	def set_in1(self, value):
		self.in1 = value


	def set_out1(self):
		if (self.in1 == True):
			self.out1 = self.val1
		else:
			self.val1 = None
			self.out1 = None


		#print '\n'
		#print '*'*50
		#print 'Name:', 'fAttr'
		#print 'ID:',   self.id_number
		#print 'val1:', self.val1
		#print 'in1:', 	self.in1
		#print 'out1:', self.out1
		#print '*'*50