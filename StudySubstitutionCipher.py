#######################
# Substitution Cipher 
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
key = 'KYQBAILWEODMZJTFGVCXNPUHRS'

ptext = 'Men willingly believe what they wish.' 
ctext = Enc(ptext, alphabet, key)
dtext = Enc(ctext, key, alphabet)
print('plaintext:', ptext)
print('ciphertext:', ctext)
print('decoded ciphertext:', dtext)
