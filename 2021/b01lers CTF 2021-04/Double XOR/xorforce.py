#!/usr/bin/env python3

import random
from Crypto.Util.number import long_to_bytes

with open('chall2.enc','rb') as f:

	ct = f.read()

	f.close()

keylen = int(input("Keylen please: "))

with open('keylen_{}.txt'.format(keylen),'r') as f:

	keyspace = [[int(j) for j in i.split(': [')[-1][:-1].split(', ')] for i in f.read().split('\n')]

	f.close()

print(keyspace[0])

while True:

	key = b''

	for ki in range(keylen):

		key += long_to_bytes(random.choice(keyspace[ki]))


	pt = b''

	for i,c in enumerate(ct):

		pt += long_to_bytes( c ^ key[ i % keylen ] )


	print(key)
	print()
	print(pt)


	input("\nPress enter to continue...")