#==============================================================================
#	Author : Vadim Kuznetsov
#	E-mail : vdmsov@yandex.ru
#	File   : blocks_testing.py
#	Data   : 03-05-2019
#==============================================================================

import time

from fstart import fStart

id0 = fStart()

i = 0

while (True):
	time.sleep(1)	
	
	if i == 5:
		id0.in1 = True
	else:
		i = i + 1
	
	print id0.link1