#!/usr/bin/env sage -python

# Imports
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from functools import reduce
from math import gcd


# Functions
# Euclidean greatest common divisor
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# Modular inverse
def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n



# LCG as RN_n+1 = ( increment + multiplier * RN_n ) % modulus
def LCG_Constructor(rolls):
    # Recover modulus
    diffs = [c1 - c0 for c0, c1 in zip(rolls, rolls[1:])]
    zeroes = [d2*d0 - d1*d1 for d0, d1, d2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs( reduce(gcd, zeroes) )
    # Recover multiplier
    multiplier = (rolls[2] - rolls[1]) * modinv(rolls[1] - rolls[0], modulus) % modulus
    # Recover increment
    increment = (rolls[1] - rolls[0] * multiplier) % modulus
    return modulus, multiplier, increment



# Connection
host = "chall.nitdgplug.org"
port = 30205

s = remote(host, port)



# Get RSA parameters
s.recvuntil('N : ', drop=True)
N = int(s.recvuntil('\n', drop=True))
s.recvuntil('e : ', drop=True)
e = int(s.recvuntil('\n', drop=True))



roll_lst = []
# Take some rolls to predict the LCG
for i in range(154):

	s.recvuntil('$ ')

	s.sendline('1')
	s.recvuntil('you: ',timeout=.4)

	roll = int(s.recvuntil('\n', drop=True))
	print(roll)

	roll_lst.append(roll)



# Construct the LCG
n, a, b = LCG_Constructor(roll_lst)

# Check LCG prediction
chck_num = ( a * roll_lst[-1] + b ) % n

s.recvuntil('$ ')

s.sendline('1')
s.recvuntil('you: ',timeout=.4)

roll = int(s.recvuntil('\n', drop=True))
assert roll == chck_num

# Next 2 rolls
next_num1 = ( a * roll + b ) % n
next_num2 = ( a * next_num1 + b ) % n



# Get 2 encrypted flags
s.recvuntil('$ ')

s.sendline('2')
s.recvuntil('num): ')

c1 = s.recvuntil('\n', drop=True).decode('ascii')

s.recvuntil('$ ')

s.sendline('2')
s.recvuntil('num): ')

c2 = s.recvuntil('\n', drop=True).decode('ascii')



# Close connection
s.close()



# Print
print('Got it, here you go :)')
print('N:', N)
print('e:', e)
print('c1:', next_num1, c1)
print('c2:', next_num2, c2)
print()
