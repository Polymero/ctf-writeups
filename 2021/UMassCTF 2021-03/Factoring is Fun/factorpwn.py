#!/usr/bin/env python3

# Imports
from pwn import *
import hashlib
import os
import time
from Crypto.Util.number import long_to_bytes

context.log_level = 'critical'

# Connection
host = "34.69.184.228"
port = 8080

def gogo():

	s = remote(host, port)

	t1 = time.time()

	# Proof of work
	s.recvuntil(b'begins with ')


	pow_hash = s.recvuntil('\n', drop=True)
	s.recvuntil('> ')
	print(pow_hash)

	while True:

		pow_try = b'UMass-' + os.urandom(32)

		pow_sha = hashlib.sha256(pow_try).hexdigest().encode()

		if pow_hash == pow_sha[:5]:

			s.sendline(pow_try)
			break

	# Get RSA parameters
	#n
	s.recvuntil('N: ')
	n = int(s.recvuntil('\n', drop=True))
	# e
	s.recvuntil('e: ')
	e = int(s.recvuntil('\n', drop=True))
	# p MSBs
	s.recvuntil('p: ')
	pbits = s.recvuntil('\n', drop=True).decode('ascii')[2:]
	plen = len(pbits)

	print(n)
	print()
	print(e)
	print()
	print(pbits)
	print()

	print('plen', plen)
	print('qlen', len(bin(n)[2:])-plen)
	print()
	print('known %', len(pbits.replace('?',''))/plen*100)
	print()
	print('search space', '2**{}'.format(plen-len(pbits.replace('?',''))), 2**(plen-len(pbits.replace('?',''))))
	print()

	print(s.recv(timeout=2))

	#ohoh = long_to_bytes(int(input('Give me the d pls:')))
	ohoh = input('Give me the d pls:')
	print(ohoh)
	s.sendline(ohoh)
	
	print(s.recv(timeout=5))
	s.interactive()

	# print()
	# print('Imma cwack now! >m<')
	# while True:
	    
	#     pt = pbits
	#     while '?' in pt:
	#         pt = pt.replace('?',random.choice(['0','1']),1)
	    
	#     #print(pt)
	    
	#     pti = int(pt,2)
	    
	#     if n % pti == 0:
	        
	#         print('Gottem!')
	#         print(pti)
	#         print(n//pti)

	#         e = 0x10001
	#         phi = (pti-1)*(n//pti-1)
	#         d = pow(e,-1,)
	#         print(d)
	#         print('Sending...')

	#         print(s.recv(timeout=5))
	#         s.sendline(d)
	#         print(s.recv(timeout=5))

	#         s.interactive()
	        
	#         exit()

	#     t2 = time.time()
	#     if (t2-t1) > 5*60:
	#     	return



while True:

	gogo()

