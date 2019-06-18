
from itertools import product


r="0123456"
for ele in product(r,repeat=6):
    ele=tuple('4')+ele
    
    secret = "L{NTP#AGLCSF.#OAR4A#STOL11__}PYCCTO1N#RS.S"
    for i in range(100):
        final=""
        for j in range(0, len(secret), 7):
            for k in range(7):
                final += secret[j:j + 7][int(ele[k])]
        secret = final
        secret = secret[-1] + secret[:-1]
        d=""
        for t in range(len(secret)//2):
            d+=secret[t]+secret[(len(secret)//2)+t]
        secret=d
        secret = secret[-1] + secret[:-1]
    if secret.find("FLAG{")!=-1:
        print("good",ele,'=====>>',secret)
        break
    else:
        print(''.join(ele))
#FLAG{##CL4SS1CAL_CRYPTO_TRANSPOS1T1ON##}