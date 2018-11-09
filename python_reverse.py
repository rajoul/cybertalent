import numpy as np
import re
output='1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
mes=re.findall('........',output)


print mes
m=[]
b=[]
for x in mes:
	m.append(int(x,2))
lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
print m
m=[304, 189, 161, 133, 7]
b=[lmao[i]^m[i] for i in range(len(m))]

b=np.array(b)
print len(b)
longeur=25

np.random.seed(12345)
other = np.random.randint(1,5,longeur)
arr = np.divide(b,other)
	
plain=[ 81 ,27  ,91  ,87 ,226 , 69 , 62 , 51 , 91 , 50 , 24  ,35  ,24  , 2 , 54  ,64  ,69 , 26, 50,  70, 237 , 81  , 6  ,44 ,  0]
d=[chr(x) for x in plain]
print d

