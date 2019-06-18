from itertools import product
import string,time
s=list("\x0f\x05\x08\x0e2\x04\x1c\x05\x1dx\x16\x19\x08\r\x16x= $,\x16\x11y\x1b\x1b4")
d=1
voca=string.printable
for ele in product(voca,repeat=4):
	key=''.join(ele)
	for i in xrange(len(s)):
	    s[i] = chr(ord(s[i]) ^ ord(key[i % len(key)]))

	for j in xrange(1,len(key)):
	    key =  key[-1:]+key[:-1]
	    for i in xrange(len(s)):
	        s[i] = chr(ord(s[i]) ^ ord(key[i % len(key)]))
	final=''.join(s)
	print key
	time.sleep(0.02)
	if final.find('FLAG')!=-1:
		print final
		break
# FLAG{MULT1_PAD_1time_X0RR}

