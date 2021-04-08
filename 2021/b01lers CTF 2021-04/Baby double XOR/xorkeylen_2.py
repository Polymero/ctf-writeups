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

low = 1
hig = clen//3

kpmin = 10
kpmax = 60


chcknums = [30,39,115,130,79,237,251,53,49,77]

for step in range(low, hig):

	if step >= clen:
		break

	#print('Now testing length', step)

	match = 0
	total = 0

	for i in range(clen):

		for j in range(i + step, clen, step):

			total += 1

			if ciphertext[i] == ciphertext[j]: 

				match += 1

	ioc = float(match) / float(total)
	ioc_lst.append(ioc)

	print("%3d%7.2f%% %s" % (step, 100*ioc, "#" * int(0.5 + 10000*ioc)))

print()

si = [list(range(low,hig))[i] for i in np.argsort(ioc_lst)[::-1]]
sl = np.sort(ioc_lst)[::-1]

for i in range(50):

	if gmpy2.is_prime(int(si[i])):
		prime_check = "(!)"
	else:
		prime_check = ""

	mod_check = ""
	for cn in chcknums:
		if int(si[i]) % cn == 0:
			mod_check += "({}) ".format(cn)

	print("%3d%7.2f%% %s %s" % (si[i], 100*sl[i], prime_check, mod_check))

print(clen)

kplst = []
kpscore = []

for i1 in range(kpmin,kpmax):

	for i2 in range(kpmin,kpmax):

		kplst.append([i1, i2])

		score = 0
		kk = 0

		for i,ioc in enumerate(sl):

			if (si[i] % i1 == 0) or (si[i] % i2 == 0):

				kk += 1

				score += ioc

		kpscore.append(score/kk)

kpscore_sort = np.sort(kpscore)[::-1]
kplst_sort = [kplst[i] for i in np.argsort(kpscore)[::-1]]

print()
for i in range(40):

	check = ''
	for cn in chcknums:
		if (kplst_sort[i][0] % cn == 0) or (kplst_sort[i][1] % cn == 0):
			check += "({}) ".format(cn)

	print("{}   {:.4f}   {}".format(kplst_sort[i], kpscore_sort[i], check))