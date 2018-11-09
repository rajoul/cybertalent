import numpy as np
import string
import re,time

# by brute forcing
flag ='t'
a=string.printable
m='100110000'
output='1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
while(1):
	for y in a:
		inter=flag+y
		np.random.seed(12345)
		arr = np.array([ord(c) for c in inter])
		other = np.random.randint(1,5,(len(inter)))
		arr = np.multiply(arr,other)

		b = [x for x in arr]
		lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
		c = [b[i]^lmao[i] for i,j in enumerate(b)]
		d=''
		for x in c:
			d+=''.join(bin(x)[2:].zfill(8))
		print 'trying............',flag+y
		if output==(d+output[len(d):]):
			flag+=y
			print 'good',flag
			break
		time.sleep(0.25)
			
#the flag :tjctf{pYth0n_1s_tr1v14l}