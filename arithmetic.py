#-*- coding:utf-8 -*-

import os,time
from hashlib import sha256
import string

def H(v):
    return int(sha256(str(v)).hexdigest(), 16)

def STEP(v):
    return (31338 * v**3 + 17 * v**2 + 2017 * v + 10) % 2**256

def encrypt(pt, key):
    state =key
    ct = ""
    for c in pt:
        c = ord(c)
        for i in xrange(32):
            op = state % 4
            state = STEP(state)

            v = state % 256
            state = STEP(state)

            if op == 0:
                c = (c + v) % 256
            elif op == 1:
                c = (c ^ v) % 256
            elif op == 2:
                c = (c - v) % 256
            elif op == 3:
                c = (c * (v | 1)) % 256
        state ^= c
        ct += chr(c)
    return ct

encr="868c017b7bef15e04ccc5f2d6b4c372fdff881080155"
flag=""
alphabet=string.printable
while (1):
	for ele in alphabet:
		inter=flag+ele
		pro=encrypt(inter, 47).encode("hex") # urandom peut etre remplace par 47
		if encr[:len(pro)]==pro:
			flag=flag+ele
			break
		else:
			print "trying.....",inter
		time.sleep(0.05)
# the flag: FLAG{SM4LL_57473_HAHA}
 