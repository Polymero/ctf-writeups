# NahamCon CTF 2021-03

<insert intro text here>

## Crypto Category

### Dice Roll [Medium] - 406
Tags: Pwn, DNG prediction

![](Challenge%20Screenshots/Dice%20Roll.png)

...

```py
#!/usr/bin/env python3

# Imports
from pwn import *
from randcrack import RandCrack
import time

# Set-up remote connection
host = "challenge.nahamcon.com"
port = 31784
s = remote(host, port)

# 'Shake the dice' -- set the random.seed()
s.recvuntil(">")
s.sendline("1")

# Initiate the random cracker
rc = RandCrack()

# We need 624 entries before we can predict the RNG
for i in range(624):
	# Get entry
	s.recvuntil(">")
	s.sendline("2")
	s.recvuntil(":\n")
	# Extract the roll value from the output
	roll = int(s.recvuntil("\n", drop=True).decode("latin-1"))
	print(roll)
	# Progress tracker
	if (624-i) % 100 == 0:
		print(f" ONLY {624-i} LEFT TO GO ")
	# Add the roll to the cracker
	rc.submit(roll)

s.recvuntil(">")

# Predict the next roll
predict = rc.predict_getrandbits(32)

# Add mandatory HYPE
print(" HERE WE GO BOIS ")
for i in range(10):
	print(10-i)
	time.sleep(1)

print(predict)

# Send prediction
s.sendline("3")
s.recvuntil(">")
s.sendline(str(predict))

# Print the flag
print(s.recvuntil("}"))

# Close connection
s.close()
```

```
flag{e915b62b2195d76bfddaac0160ed3194}
```



### Elliptical [Hard] - 500 (Overdue)

![](Challenge%20Screenshots/Elliptical.png)
Tags: ECDSA, Re-used nonce exploit, Web

...

```py
# Imports
import base64
import hashlib

# Get modular inverse of x (mod n)
def eulinv(x, n):
    a, b, u = 0, n, 1
    while x > 0:
        q = b // x 
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % n
    else:
        return None

# Disassemble a token into r,s EC coords and z-value of message
def disassemble_token(token, n):
    # Get token elements
    header, payload, signature = token.split(".")
    # Decode the signature from base64 (auto-padding)
    while True:
        try:
            sign = int.from_bytes(base64.urlsafe_b64decode(signature), 'big')
        except:
            signature += '='
            continue
        break
    # Get r,s EC coordinates
    r = int(bin(sign)[2:2+256], 2)
    s = int(bin(sign)[2+256:], 2)
    # Get message hash (SHA-256)
    message = header + '.' + payload
    m = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
    # Derive z-value of message (= header + payload)
    Ln = len(bin(n)[2:])
    z = int(bin(m)[2:Ln+2], 2)
    # Return
    return r, s, z

# Construct a token given header, payload, and (n,k,d) for the signature
def sign_token(header, payload, n, k, d, r):
    # Construct message
    msg = base64.urlsafe_b64encode(header.encode()) + b'.' + base64.urlsafe_b64encode(payload.encode())
    msg = msg.replace(b'=', b'')
    # Derive signature parameters
    m = int.from_bytes(hashlib.sha256(msg).digest(), 'big')
    Ln = len(bin(n)[2:])
    z = int(bin(m)[2:Ln+2], 2)
    r = r
    s = (eulinv(k, n) * (z + r * d)) % n
    # Create signature
    sign = bytes.fromhex(hex(r)[2:]) + bytes.fromhex(hex(s)[2:])
    # Sign token
    token = msg + b'.' + base64.urlsafe_b64encode(sign).replace(b'=', b'')
    # Return
    return token

# Two tokens taken from the website (it does not matter what the chosen usernames are)
token1 = "eyJhbGciOiAiRVMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJQb2x5bWVybyJ9.wN0kGlDUj5n8x6GGptROB2PskEeOHe-ONvXE6VDWevvRpSzxAc0wrO0ziQdKBUvpjO8BSnU9_amK88PIsJNH5w"
token2 = "eyJhbGciOiAiRVMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VybmFtZSI6ICJTZWJhc3RpYWFuIn0.wN0kGlDUj5n8x6GGptROB2PskEeOHe-ONvXE6VDWevtS_ScXs5MI9Pi2ZJSOTIXe9L3ZKlr3Xw8xUOfHU9Dg0A"

# P-256 curve order (of G)
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369; print('n:', n)

# Disassemble the two tokens that we got
r1, s1, z1 = disas_token(token1, n); print('\n(r,s)1:', (r1,s1)); print('    z1:', z1)
r2, s2, z2 = disas_token(token2, n); print('\n(r,s)2:', (r2,s2)); print('    z2:', z2)

# Derive the nonce used
# Technically there are four possible solutions, but the first one is correct
# I checked this by trying to reconstruct the signature of one of the above tokens
k1 = (z1 - z2) * eulinv((s1 - s2) % n, n) % n; print('\nk1:', k1)
# k2 = (z1 - z2) * eulinv((s1 + s2) % n, n) % n; print(k2)
# k3 = (z1 - z2) * eulinv((-s1 - s2) % n, n) % n; print(k3)
# k4 = (z1 - z2) * eulinv((-s1 + s2) % n, n) % n; print(k4)

# Derive the corresponding private key
d1 = (s1 * k1 - z1) * eulinv(r1, n) % n; print('\nd1:', d1)
# d2 = (s1 * k2 - z1) * eulinv(r1, n) % n; print(d2)
# d3 = (s1 * k3 - z1) * eulinv(r1, n) % n; print(d3)
# d4 = (s1 * k4 - z1) * eulinv(r1, n) % n; print(d4)

# Let's make that admin token and the flag shall be ours!
header = '{"alg": "ES256", "typ": "JWT"}'
payload = '{"username": "admin"}'
admin_token = sign_token(header, payload, n, k1, d1, r1)
# Print our token
print('\nAdmin token:', admin_token.decode())
```

```
flag{b3be177d016ebf9753079c7adc9c28c3} 
```



### Treasure [Easy] - 448 (Overdue)
Tags: Book cipher

![](Challenge%20Screenshots/Treasure.png)

...

```py
#!/usr/bin/env python3

# Imports
import re

# Open and read the txt file
f = open("hackers.txt")
fulltxt = f.read()

# Split at all non-alphanumeric characters (and remove final '')
wordlst = re.split('[^a-zA-Z0-9]+', fulltxt)[:-1]

# Book cipher codes
numlst = [4661, 5099, 13243, 11578, 14382, 734, 14024, 10621, 14382, 2, 3383, 8702, 6087, 10621, 7417, 
          14382, 12352, 615, 1208, 4246, 4657, 9975, 7203, 2658, 770, 4, 10621, 8702, 6125, 980, 9522, 
          2659, 14784, 7203, 8701, 38]

# Take first character of every word
charlst = [i[0] for i in wordlst]
# Print number of characters / words
print('Number of words:', len(charlst))

# Get the flag characters from the book cipher (at offset -1)
offset = -1
flaglst = [charlst[i+offset] for i in numlst]

# Create and print the flag :)
flag = ''.join(flaglst[:4])+'{'+''.join(flaglst[4:])+'}'
print(flag.lower())
```

```
flag{62d869c6b886dac2dd743086e451f76b}
```



### Eaxy [Easy] - 433 (Overdue)
Tags: XOR

![](Challenge%20Screenshots/Eaxy.png)

...

```py
to be added.
```

```
flag{16edfce5c12443b61828af6cab90dc79}
```



## Scripting Category

### DDR [Medium] - 497 (Overdue)
Tags: PIL, Scripting

![](Challenge%20Screenshots/DDR.png)

...

```py
# Imports
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Open image and get image size
ddr = Image.open('ddr.png').convert('RGB')
width, height = ddr.size
print('Image size:', width, height)
# Get block size
block_w, block_h = int(width / 21), int(height / 15)
print('Block size:', block_w, block_h)
# Assert blocks are squares
assert block_w == block_h

# Convert image to numpy  array
npddr = np.array(ddr)

# Move position according to the DDR arrow
def moveCursor(px, py):
    # Get pixel rgb tuble
    rgb = npddr[py*block_w+6, px*block_w+32]
    # Check only the R colour value
    if rgb[0] == (74, 142, 66)[0]:
        return px-1, py
    if rgb[0] == (134, 46, 123)[0]:
        return px, py-1
    if rgb[0] == (243, 137, 197)[0]:
        return px, py+1
    if rgb[0] == (27, 133, 206)[0]:
        return px+1, py

# Get R colour value from background of specified block
def getColour(px, py):
    return npddr[py*block_w+10, px*block_w+10][0]

# Starting flag
flag = 'f'
# Initial position (red block)
px = 10; py = 7
# Keep adding to the flag until we hit the end
while flag[-1] != '}':
    # Move
    px, py = moveCursor(px, py)
    # Get colour, add character to flag
    flag += chr(getColour(px, py))

# Print result :)
print('\nFlag found:', flag)
```

```
Image size: 1344 960
Block size: 64 64

Flag found: flag{2a4c670674023b972f4ef2bc19224e25}
```