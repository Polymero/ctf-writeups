#!/usr/bin/env python3

from pwn import *


host = "chal.b01lers.com"
port = 25000 

s = remote(host, port)

#context.log_level = "debug"

with open("ciphertext.txt",'rb') as f:

	ct = f.read()

	f.close()

for ci in range(0, len(ct), 1):

	blcs = ct[ci : ci + 33*16]

	assert len(blcs) == 512+16

	print(s.recv()[1:35].decode())
	s.sendline('3')
	s.recv()
	s.sendline(blcs.hex())