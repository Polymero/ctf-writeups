#!/usr/bin/env python3

from pwn import *
import numpy as np 
import numpy.linalg as la

host = "chall.nitdgplug.org"
port = 30211

context.log_level = "debug"

s = remote(host, port)

alp = "abcdefghijklmnopqrstuvwxyz"

while True:

	_, key, ct, _ = s.recv().decode('ascii').split('\n')

	key = key.split(': ')[-1]
	ct  = ct.split(': ')[-1]

	print(key)
	print(ct)

	key_size = int(np.sqrt(len(key)))
	#print(key_size, key_size)

	enc_keyarr = np.array([alp.index(i) for i in list(key)]).reshape(key_size, key_size)
	#print(enc_keyarr)

	ctvec = np.array([alp.index(i) for i in list(ct)])
	ctarr = np.array([list(ctvec)[i:i+key_size] for i in range(0,len(ct),key_size)])
	#print(ctarr)

	keyarr_det = int(round(la.det(enc_keyarr)))

	dec_keyarr = np.round(( la.inv(enc_keyarr) * keyarr_det * pow(keyarr_det, -1, 26) ) % 26 ).astype(int)
	#print(dec_keyarr)

	mvec = [np.dot(dec_keyarr, vec) % 26 for vec in ctarr]
	#print(mvec)


	flag = ''
	for vec in mvec:
		for val in vec:
			flag += alp[val]

	print(flag)

	s.sendline(flag)

# GLUG{17_15_34513r_70_g0_d0wn_4_h1ll_7h4n_up_bu7_7h3_v13w _15_fr0m_7h3_70p}