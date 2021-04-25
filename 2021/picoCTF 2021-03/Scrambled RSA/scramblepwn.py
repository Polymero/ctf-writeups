#!/usr/bin/env python3

# Imports
from pwn import *

# Connection
host = "mercury.picoctf.net"
port = 50075

s = remote(host, port)

#context.log_level = 'debug'



# Get encoded flag and other parameters (not that we need them)
s.recvuntil("flag: ")
flag_enc = s.recvuntil("\n", drop=True).decode()

s.recvuntil("n: ")
N = int(s.recvuntil("\n", drop=True).decode())

s.recvuntil("e: ")
E = int(s.recvuntil("\n", drop=True).decode())



# Set up internal parameters
ALP = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}{'

flag = ''

eggs = []

# Loop to construct the flag
while True:

	# Loop over all possible
	for char in ALP:

		# Trial flag
		tryflag = flag + char
		# Send it
		s.recv()
		s.sendline(tryflag)
		# Retrieve encrypted trial flag
		s.recvuntil("go: ")
		res = s.recvuntil("\n", drop=True).decode()

		# Get rid of all previous determined encryption parts (eggs)
		for e in eggs:

			res = res.replace(e, '', 1)

		# If the remainder is in the encoded flag we have a hit
		if res in flag_enc:

			flag += char

			flag_enc = flag_enc.replace(res, '', 1)

			eggs.append(res)

			break

	# Win condition
	if flag[-1] == '}':

		break

	print(flag)

# Print our flag :)
print()
print('Gottem boss!')
print(flag)