from Crypto.Cipher import AES

iv="1234567890123456" # it is just an example
key='1234567890123456'

def padding(message,taille_block):
	return message+'?'*(taille_block-len(message)%taille_block)
def xor(str1,str2):
	cipher=""
	for i in range(len(str1)):
		cipher+=chr(ord(str1[i])^ord(str2[i]))
	return cipher

def encrypt_ECB(payload,taille_block):
    obj = AES.new(key, AES.MODE_ECB)
    str1 = padding(payload,taille_block)
    ciphertext=""
    ciphertext+=obj.encrypt(xor(str1[:taille_block],iv))
    for i in xrange(1,len(str1)//taille_block):
        ciphertext += obj.encrypt(xor(str1[taille_block*i:taille_block*(i+1)],ciphertext[taille_block*(i-1):taille_block*i]))
    
    return ciphertext

def encrypt_CBC(ciphertext,taille_block):
	
    obj1 = AES.new(key,AES.MODE_CBC,iv)
    lol=padding(ciphertext,taille_block)
    plaintext = obj1.encrypt(lol)
    return plaintext
# we can resume that aes_cbc=aes_ecb+xor_block
# test if aes'message generated with ecb_mode+xor is equal to aes_cbc message
if encrypt_CBC('hello from the other side',16)==encrypt_ECB('hello from the other side',16): 
	print "that good,they are similar"
