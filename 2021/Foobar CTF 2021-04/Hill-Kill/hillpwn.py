#!/usr/bin/env python3

# Imports
from pwn import *
import numpy as np 
import numpy.linalg as la

# Connection
host = "chall.nitdgplug.org"
port = 30211

context.log_level = "debug"

s = remote(host, port)

# Used alphabet
alp = "abcdefghijklmnopqrstuvwxyz"

# Loop to kill all the hills >:)
while True:

	# Retrieve the key and ciphertext
	_, key, ct, _ = s.recv().decode('ascii').split('\n')

	key = key.split(': ')[-1]
	ct  = ct.split(': ')[-1]

	# Visual check
	print(key)
	print(ct)

	# Extract key size (NxN) from N**2 length key
	key_size = int(np.sqrt(len(key)))
	#print(key_size, key_size)

	# Construct the key array (size NxN)
	enc_keyarr = np.array([alp.index(i) for i in list(key)]).reshape(key_size, key_size)
	#print(enc_keyarr)

	# Construct the cipher text vectors (size Nx1)
	ctvec = np.array([alp.index(i) for i in list(ct)])
	ctarr = np.array([list(ctvec)[i:i+key_size] for i in range(0,len(ct),key_size)])
	#print(ctarr)

	# Get key array determinant
	keyarr_det = int(round(la.det(enc_keyarr)))

	# Construct decryption key array in a nice format :)
	dec_keyarr = np.round(( la.inv(enc_keyarr) * keyarr_det * pow(keyarr_det, -1, 26) ) % 26 ).astype(int)
	#print(dec_keyarr)

	# Multiple the decryption key array with each cipher text vector to obtain the message vectors
	mvec = [np.dot(dec_keyarr, vec) % 26 for vec in ctarr]
	#print(mvec)

	# Construct the answer from msg vecs
	ans = ''
	for vec in mvec:
		for val in vec:
			ans += alp[val]

	# Visual check
	print(ans)

	# Send the answer to the server
	s.sendline(ans)

# GLUG{17_15_34513r_70_g0_d0wn_4_h1ll_7h4n_up_bu7_7h3_v13w _15_fr0m_7h3_70p}