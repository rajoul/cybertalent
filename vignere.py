import string
import itertools
import collections
import hashlib

cipher_text='uucbxsimbjyaqyvzbzfdatshktkbde'
key='blais'

for ele in itertools.permutations(string.ascii_lowercase,4):
	key='blais'
	key=key+''.join(list(ele))
	cycler=itertools.cycle(key.lower())
	key=''.join([cycler.next() for _ in range(len(cipher_text))])
	key=list(key)
	plain_text=''
	for i in range(len(cipher_text)):
		mot=collections.deque(string.ascii_lowercase)
		index_message=string.ascii_lowercase.index(key[i])
		mot.rotate(-index_message)
		text=''.join(list(mot))
		index_key=text.index(cipher_text[i])
		plain_text+=string.ascii_lowercase[index_key]

	flag=plain_text[:5]+'{'+plain_text[5:]+'}'
	s=hashlib.sha256()
	s.update(flag)
	flag_hex=s.hexdigest()
	if flag_hex=='8304c5fa4186bbce7ac030d068fdd485040e65bf824ee70b0bdbac03862bec93':
		print 'CONGRAT!!!! '+flag
		break;
	else:
		print 'trying.....'+flag

# CONGRAT!!!! tjctf{one_vinaigrette_salad_please}