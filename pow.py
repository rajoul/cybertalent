from Crypto.Util.number import inverse
from binascii import unhexlify

N = 29376184821108156618286183148714771792276652929137914081529218159551556583417
E = 31337, 313337, 3133337
result=25141551253203903049478219501897633456478106882428713823304640429548556653914
#print pow(pow(pow(M, E[0], N)+1, E[1], N)+1, E[2], N)

P=6980725708436535193
Q=12560041438154300011
R=335045466549163140819709404768107130979

d1=inverse(E[2],(P-1)*(Q-1)*(R-1))
result1=pow(result,d1,N)-1

d2=inverse(E[1],(P-1)*(Q-1)*(R-1))
result2=pow(result1,d2,N)-1

d3=inverse(E[0],(P-1)*(Q-1)*(R-1))
M=pow(result2,d3,N)


original = hex(result3)[2:].strip("L")
if len(original)%2:
	original="0"+original

print(unhexlify(original))

# FLAG{TRRRIPLE_PR!M3_RRRSSSAA}!
