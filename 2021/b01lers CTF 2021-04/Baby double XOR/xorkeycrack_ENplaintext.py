#!/usr/bin/env python3

from collections import Counter
from Crypto.Util.number import long_to_bytes, bytes_to_long
  
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

keylen = 1363 # from xorkeylen.py

most_freq_chars = [' ','e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z',
				   '.','\n','"','!','?','E','T','A','I','N','O','S','H','R','D','L','C','U','M','W','F','G','Y','P','B','V','K','J','X','Q','Z',
				   '(',')','0','1','2','3','4','5','6','7','8','9',"'",':','-','`']

ALP = [ord(i) for i in list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?'\"()}{_0123456789:;\n-`/")]

with open("baby_double_xor.enc",'rb') as f:

	ciphertext = f.read()

	f.close()

key = b''
loss_num = 0
fci = 0
while len(key) < keylen:

	hitlst = ciphertext[len(key)::keylen]

	for bi in range(256):

		xorlst = [c ^ bi for c in hitlst]

		if most_frequent(xorlst) != ord(most_freq_chars[fci]):
			continue

		if any([ x not in ALP for x in xorlst ]):
			fci += 1

			if fci >= len(most_freq_chars):

				# for bbb in range(256):

				# 	xxx = [c ^ bbb for c in hitlst]

				# 	if any([ ((x<32) and x not in [10,]) or ((x>127) and x not in [10,]) for x in xorlst ]):

				# 		continue

				# 	key += long_to_bytes(bbb)
				# 	fci = 0

				loss_num += 1
				key += b'\x00'
				fci = 0

			break
		
		key += long_to_bytes(bi)
		fci = 0

print('Key:')
print(key)
print()

print('Loss:', loss_num)

plaintext = b''

for i,c in enumerate(ciphertext):

	plaintext += long_to_bytes( c ^ key[i % keylen] )

with open("plaintext.txt",'wb') as f:

	f.write(plaintext)

	f.close()

print(plaintext)