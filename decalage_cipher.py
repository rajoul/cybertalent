import time
import re

mes='4c7c6b80792b2a5e7f2a7a6f7f822a806b76736e6f7c2a6b806f6d2a766f2a7a6b7d7d2a6379766b73727f140a'
message=re.findall('..',mes)

for i in range(1,255):
	c=''
	for ele in message:
		c+=chr((int(ele,16)+i)%256)
	print c,i
	time.sleep(0.25)