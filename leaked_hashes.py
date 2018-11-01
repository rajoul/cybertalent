import hashlib

tab=['be3f7de032d2e398ec542a7df71e0417','a14ca920b8a9c1ee742b4248e7f9f56c', '08a81fafe787c93d02eb338b75f61819', 
     'b6eae1ba4ea6610cb0d12f0c21e1d2ec', '2cb699789d11d94fee780859adfabb91', '510251930c07bbcbeb1908e2c22d8d66', 
     'ee4d5bc25a2771d95fdbd24452e355ad', 'c2463a810b82134c6844a1ae1bcd1625', '21b6a74930ef75e32f69bc0b49fbe8ff', 
     '3a663354e45f1dbf9702ffa5dc799c2f', '0710f636e10edae58aea9a30125239ae', 'a64bb7fd1868a7bac23a384d014d352d', 
     '08a81fafe787c93d02eb338b75f61819', 'f8d4a51d618d84e02e2914901b6e59c8', '6cf6041fc2df249eaf313a269c5bd200', 
     'ca63eab394b98edb1f1990b5fe94c0b7', '66bf6b80df55195cfa25d48ce38f2b60', '6a8cd19a61e34f8ca4e0e7a14bb0e45b', 
     'cc5847ba595f097885b2bbe5eb940e22', '189dbb843e5420471ba9f10f03d8e9dc', '9472604ded1bcfac3b006331195a3163', 
     'cee42b4df8a585981a591220ece71c65', 'a64bb7fd1868a7bac23a384d014d352d', '699c0be567e2cbc16214dc4bc531cf4d',
     '7a4a8a79bdc17144c3b10226e1b92d60', '8b1660cfc5ce8217cb9188cc6b652e91','3f4e535a671209f394817559372286f2']


def decryptMD5(testHash):
        s = []
        while True:
                m = hashlib.md5()
                for c in s:
                        m.update(chr(c))
                hash = m.hexdigest()
                if hash == testHash:
                        return ''.join([chr(c) for c in s])
                wrapped = True
                for i in range(0, len(s)):
                        s[i] = (s[i] + 1) % 256
                        if s[i] != 0:
                                wrapped = False
                                break
                if wrapped:
                        s.append(0)
for x in tab:
	print decryptMD5(x)
#this programm may take more time
#there is an other way -->>https://hashkiller.co.uk/md5-decrypter.aspx 
# the account that was cracked is :christene :r3ckr3ck
# the flag is:  3977df525282eaf0e99f86efd2b645ed
