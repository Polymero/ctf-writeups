#!/usr/bin/env python3

# Imports
from pwn import *
from Crypto.Util.number import bytes_to_long, long_to_bytes
from functools import reduce
from math import gcd


# Functions
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)



# Connection
host = "chall.nitdgplug.org"
port = 30205

s = remote(host, port)



# Get RSA parameters
s.recvuntil('N : ', drop=True)
N = int(s.recvuntil('\n', drop=True))
s.recvuntil('e : ', drop=True)
e = int(s.recvuntil('\n', drop=True))



nums = []
# Take some entries to predict the LCG
for i in range(154):

	s.recvuntil('$ ')

	s.sendline('1')
	s.recvuntil('you: ',timeout=.4)

	roll = int(s.recvuntil('\n', drop=True))
	print(roll)

	nums.append(roll)



# Predict LCG
n, a, b = crack_unknown_modulus(nums)

chck_num = ( a * nums[-1] + b ) % n

# Check LCG
s.recvuntil('$ ')

s.sendline('1')
s.recvuntil('you: ',timeout=.4)

roll = int(s.recvuntil('\n', drop=True))
assert roll == chck_num

next_num1 = ( a * roll + b ) % n
next_num2 = ( a * next_num1 + b ) % n


# Get encrypted flag
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

c1 = bytes_to_long(c1.encode())
c2 = bytes_to_long(c2.encode())

alpha = 1
beta = next_num2 - next_num1
beta  = bytes_to_long(str(next_num2).encode()) - bytes_to_long(str(next_num1).encode())

m1 = (beta * ( c2 + 2*alpha**3*c1 - beta**3 )) // (alpha * ( c2 - alpha**3*c1 + 2*beta**3 ))

print('alhpa:', alpha)
print('beta:', beta)
print('m1:', long_to_bytes(m1))


