#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : fval.py
#	Data   : 03-05-2019
#==============================================================================

class fVal:

	id_number = None
	val1 = None
	in1 = False
	link1 = None


	def __init__(self, id_number):
		self.id_number = id_number
		self.val1 = None
		self.in1 = False
		self.link1 = None
	
	def set_val1(self, value):
		self.val1 = value

	def set_in1(self, value):
		self.in1 = value

	def set_link1(self):
		if (self.in1 == True):
			self.link1 = self.val1
		else:
			self.val1 = None
			self.link1 = None

		#print '\n'
		#print 'ID:', self.id_number , 'fVal: val1 = ' , self.val1
		#print 'ID:', self.id_number , 'fVal: in1 = ' , self.in1
		#print 'ID:', self.id_number , 'fVal: link1 = ' , self.link1