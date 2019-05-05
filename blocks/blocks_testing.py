#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : blocks_testing.py
#	Data   : 03-05-2019
#==============================================================================

from threading import Thread
import time

from fstart import fStart
from fval import fVal
from fattr import fAttr
from fsendmqtt import fSendMqtt

id0 = fStart(0)
id1 = fVal(1)
id2 = fAttr(2)
id3 = fSendMqtt(3)


def extended_name(id_name):
	return id_name + ' '*(20 - len(id_name))


none_name = extended_name('None')
id0_name = extended_name(id0.__class__.__name__)
id1_name = extended_name(id1.__class__.__name__)
id2_name = extended_name(id2.__class__.__name__)
id3_name = extended_name(id3.__class__.__name__)

print '-'*50
print 'id0:', id0_name
print 'id1:', id1_name
print 'id2:', id2_name
print 'id3:', id3_name


def log_print(src_name, src_id, dst_name, dst_id, data):
	print '-'*50
	print 'Name:', src_name, '\t', 'Src ID:', src_id, '\n', 'Name:', dst_name, '\t', 'Dst ID:', dst_id, '\n', 'Data:', data


def main_threding():

	i = 0

	while (True):
	
		time.sleep(2)
		i = i + 1
	
		if i == 2:
			id0.set_in1(True)
	
			
		id1.set_in1(id0.out1)
		log_print(id0_name, id0.id_number, id1_name, id1.id_number, id0.out1)
	
		id2.set_in1(id0.out1)
		log_print(id0_name, id0.id_number, id2_name, id2.id_number, id0.out1)
	
		id1.set_val1(i)
		id1.set_out1()
	
		id3.set_val1('devices/wb-adc/controls/A1')
		id3.set_in1(id1.out1)
		id3.publisher()
		log_print(id1_name, id1.id_number, id3_name, id3.id_number, id1.out1)

		id2.set_val1(i*10)
		id2.set_out1()
		log_print(id2_name, id2.id_number, none_name, 'None', id2.out1)


thr = Thread(target = main_threding)
thr.start()
