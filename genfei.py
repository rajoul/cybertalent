

from struct import pack,unpack

message="P\r\xc4\xfe\xd9\x8a \xdc\xae\xf9\x8e\x16\x1eh\x10q\x8e>\xde\x92\xbcb\t\x8f\xc0M\xc0S\\\x9b\xa8j"
def F(w):
	return ((w * 31337) ^ (w * 1337 >> 16)) % 2**32
def decrypt(block):
	a,b,c,d=unpack("<4I",block)
	for _ in range(32):
		d1=d^1337
		a1=F(d1 | F(d1) ^ d1)^c
		b1=F(d1 ^ F(a1) ^ (d1 | a1))^b
		c1=F(d1 | F(b1 ^ F(a1)) ^ F(d1 | b1) ^ a1)^a

		a=d1^31337
		d=c1^ F(a | F(a) ^ a)
		c=b1^ F(a ^ F(d) ^ (a | d))
		b=a1^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d)
	return pack("<4I",a,b,c,d)
plaintext= "".join(decrypt(message[i:i+16]) for i in range(0, len(message), 16))

print plaintext



# FLAG{G3N3R4L123D_F31573L_EZ!}
# it was very hard to find the way
