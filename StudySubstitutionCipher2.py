#######################
# Substitution Cipher 2
#######################
import re
def Enc(text, org, key):
    tmp = re.sub(r'\W+', '', text)
    text = tmp.upper()
    res = ''
    for lett in text:
        index = org.index(lett)
        res += key[index]
    return res

alphabet  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#key = 'KYQBAILWEODMZJTFGVCXNPUHRS'
key = 'LODMZJTWEXNRSPUKYQBACHIFGV'
#f1 = open('test.txt','r')
f1 = open('Gettysburg.txt','r')
f2 = open('cipher.txt','w')
s = f1.read()
ptext = s.upper()
ctext = Enc(ptext, alphabet, key)
dtext = Enc(ctext, key, alphabet)
print('plaintext:', ptext)
print('ciphertext:', ctext)
print('decoded ciphertext:', dtext)
f2.write(ctext)

f1.close()
f2.close()