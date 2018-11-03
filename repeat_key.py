import itertools

message='''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key='ICE'

cycler=itertools.cycle(key)
long_key=''.join([cycler.next() for _ in range(len(message))])
c=''
for i in range(len(message)):
	c+=chr(ord(message[i])^ord(long_key[i]))
if c.encode('hex')=="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f":
	print "that gooooooooooooood"
