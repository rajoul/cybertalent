import random


random.seed("random")
flag='BNZQ:6m3bd631074ov60jxu1zov1380l3i959'
encflag = ""
for c in flag:
  if c.islower():
    d=ord(c)-random.randrange(0,26)
    if d in range(97,123):
    	encflag+=chr(d)
    else:
    	encflag+=chr(d+26)
  elif c.isupper():
    d=ord(c)-random.randrange(0,26)
    if d in range(65,91):
    	encflag+=chr(d)
    else:
    	encflag+=chr(d+26)
  elif c.isdigit():
    d=ord(c)-random.randrange(0,10)
    if d in range(48,58):
    	encflag+=chr(d)
    else:
    	encflag+=chr(d+10)
  else:
    encflag += c
print encflag

# FLAG:3b1fa718577cd90efb2fdf5832b6a849