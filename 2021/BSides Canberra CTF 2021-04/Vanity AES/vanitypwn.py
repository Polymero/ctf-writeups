#!/usr/bin/env python3

from pwn import *


host = "vanity-aes.chal.cybears.io"
port = 2323

#context.log_level = 'debug'

s = remote(host, port)


iv_lst = []

while len(iv_lst) < 30:

	s.recvuntil("menu >>> ")

	s.sendline('2')

	s.recvuntil("beacon data >>> ")

	s.sendline('00')

	s.recvuntil('00: ')
	iv = s.recvuntil('\n', drop=True).decode()[:48]#.replace(' ','').lower()

	print(iv)
	iv_lst.append(iv)

	s.sendline('')
