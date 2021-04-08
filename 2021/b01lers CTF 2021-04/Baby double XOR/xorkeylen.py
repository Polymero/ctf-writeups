#!/usr/bin/env python3

import numpy as np
import gmpy2

with open("baby_double_xor.enc",'rb') as f:

	ciphertext = f.read()

	f.close()

clen = len(ciphertext)
print(clen, ciphertext[:10])
print()

ioc_lst = []

for step in range(1, 1500):

	if step >= clen:
		break

	#print('Now testing length', step)

	match = 0
	total = 0

	for i in range(step):

		for j in range(i + step, len(ciphertext), step):

			total += 1

			if ciphertext[i] == ciphertext[j]: 

				match += 1

	ioc = float(match) / float(total)
	ioc_lst.append(ioc)

	#print("%3d%7.2f%% %s" % (step, 100*ioc, "#" * int(0.5 + 2000*ioc)))

print()

si = np.argsort(ioc_lst)[::-1] + 1
sl = np.sort(ioc_lst)[::-1]

for i in range(20):

	if gmpy2.is_prime(int(si[i])):
		prime_check = "(!)"
	else:
		prime_check = ""

	print("%3d%7.2f%% %s" % (si[i], 100*sl[i], prime_check))