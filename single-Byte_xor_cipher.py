import time
from binascii import hexlify,unhexlify

enc='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

message=enc.decode('hex')
for i in range(ord('A'),ord('z')+1):
	c=''
	for ele in message:
		c+=chr(ord(ele)^i)
	print (c,'   ',i)
	
	time.sleep(0.25)