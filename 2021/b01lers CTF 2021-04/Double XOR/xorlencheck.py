#!/usr/bin/env python3

import gmpy2
from gmpy2 import mpz



def factors(n):
    result = set()
    n = mpz(n)
    for i in range(2, gmpy2.isqrt(n) + 1):
        div, mod = divmod(n, i)
        if not mod:
            result |= {int(i), int(div)}
    if result == set():
    	return "prime !"
    else:
    	return result



with open("chall2.enc", 'rb') as f:

	ct = f.read()

	f.close()

ALP = [ord(i) for i in list(

	  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,!?'\"()}{_0123456789:;\n-`/"

	  )]

EXT_ALP = True

if EXT_ALP:

	ALP += [ord(i) for i in list(

		"+=\t^*@~#$%&ßáäèéëñóöúü|"

		)]

minlen = 1
maxlen = len(ct)//2


print("Checking from {} to {} keylens in {} chars".format(minlen, maxlen, len(ct)))
print("Allowed char set:")
print(''.join( chr(i) for i in ALP ))


stop = False
pos_len_dic = {}

# For every key length
for kli in range(minlen, maxlen):

	pos_byt_dic = {}

	# For every byte in the key
	for kbi in range(kli):

		if stop:

			stop = False
			break

		# Create keybyte column
		column = ct[kbi::kli]

		pos_byt_lst = []

		# All possible bytes
		for bi in range(256):

			# XOR the column
			xorcol = [char ^ bi for char in column]

			# Any non-ALP characters?
			if any([x not in ALP for x in xorcol]):

				continue

			else:

				pos_byt_lst.append(bi)

		# Possible?
		if pos_byt_lst == []:

			stop = True
			break

		else:

			pos_byt_dic[kbi] = pos_byt_lst

	# Mismatch?
	if len(pos_byt_dic) != kli:

		continue

	else:

		pos_len_dic[kli] = pos_byt_dic



# Print
for pl in pos_len_dic:

	print(pl, factors(pl))

	with open("keylen_{}.txt".format(pl),'w') as f:

		f.write(']\n'.join(str(pos_len_dic[pl]).split('], '))[1:-1])

		f.close()

#print()
#print(pos_len_dic[697])