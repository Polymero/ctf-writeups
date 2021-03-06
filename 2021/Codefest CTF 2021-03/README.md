# CodeFest CTF 2021-03

<insert intro text here>

## Crypto Category

### RSA 1.0 - ? (Overdue)
Tags: RSA, Multi-prime

![](Challenge%20Screenshots/RSA%201.png)

```py
# RSA parameters
n = 750663646847528873168937831391907810647591913965562495296199585082759057318274521553757550724463451891668175905206221877858317290777877060166997790624527965837837993129383290402509996587556406778482067347232022225466937668396768390983554357611376057823852179263682649072729435912583278183812954787442057976301035654942470184201720410477691326653029842426252391647509934740335989269071438620690320401576861478427178128804784352142271832603194431176323445880836139
pq = 80970512687406090889060992576336286518763523653333428346066206717567693624044162491796922556346210471950404967161997779545603412053582932354160368128117099634532601019309976159157713252768640669410333127578132624183514430252557952811102781031315190048386214745340936679285725364013916829276058253922234988379
c = 221975957171552618997196127189899209276336291387640550554967727731818563960555600691881715668156105819191779108737770660990397331961689607338541452069797368288215716485835439777459317512238532636172979397173548812054679237802827275184091619620252887678664409116710340000218841023351238456144820005968602870644031701303645229364391309952172259686888808938835775360009896210855708140351244441167461823250549764537506364091367096196182191704433664638829177854628679
e = 0x10001

# Get the third prime
r = n//pq

# Let's make the decryption key
d = pow(e, -1, r-1)

# Recover the message
m = pow(c, d, r)

# Convert integer message to ascii-chars
mb = bin(m)[2:]

while len(mb)%8 != 0:
    mb = '0'+mb

mstr = ''.join([chr(int(mb[i:i+8],2)) for i in range(0,len(mb),8)])

# Our flag!
print(mstr)
```

```
codefest{p4dding_i5_r3quir3d}
```



### RSA 2.0 - ? 
Tags: RSA, Even e, Tonelli-Shanks

![](Challenge%20Screenshots/RSA%202.png)

However, we should note that gcd(e,phi) = 16 != 1, such that we can find d_16 = \~(e//16) % phi which will lead us to pow(ct, d_16, n) = M\*\*16 % n. However, if we find a root of x mod p, then p-x is also a root. So we can have a total of 16\*16 = 256 possible values for m :S. Some of which turn out to be the flag we are looking for!

```py
#!/usr/env/bin python3

# Imports
from Crypto.Util.number import long_to_bytes

# Simple greatest common divisor function
def gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

# Non-trivial function to calculate modular square root of a modulo p
def modular_sqrt(a, p):

    # Compute legendre symbol
    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # "Square roots from 1; 24, 51, 10 to Dan Shanks" - Ezra Brown
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

# Get euler inverse of x (mod n)
def eulinv(x, n):
    a, b, u = 0, n, 1
    while x > 0:
        q = b // x 
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % n
    else:
        return None

# Ciphertext
c = 7376083179301871727319662441290512768979499624954698397165424050024666168943377478129926304132046879741349597229411809080978573590530226067752606719487158834511752336008287600324551704896881690547279678544392014784520001523240813365339789395536491039305623640655624806350548548554437985830405020169663539939018239643445566882380359742208558132490655657280619850656880232036155057833081215187526442724687828214045430674207843841122060416377750502505640447395732809699800028565067081780511133517020113861405502897034245617267331520262877918693182867532420288135211820606290453667200638642871988519470430475958049806666

# Given RSA parameters
p = 151504136086085116766143566124150275674073392929821608731193313303579549567486780984882103878189021716475112187664571076380701312144707968796469474077396203079356104319166539457117762979236714826426908047910529451429037552027255450267166159899155876867790669696867818896423172168830285791913854195932438702321
q = 103830664295009091893886752305087173101905116416231118984740125697489572383920741106883033358012404414250903398273361420080940861355058896027909558044477593238426139173175903469841531670082355641543985372882381822644581374082868518234109972478903771291945965032201075848195104712153515556622192413687460682033
e = 112

# Calculate other RSA parameters
n = p*q
phi = (p-1)*(q-1)

# Get the secret component with e//16
d16 = eulinv(e//16,phi)

# Now we can find m**16 % n
m16 = pow(c,d16,n)

# Get all 16*16 = 256 possible roots
entry = [m16]
roots1 = [entry[0]]
roots2 = []
for i in range(4):
    for e in roots1:
        r1 = modular_sqrt(e,p)
        r2 = p - r1
        r3 = modular_sqrt(e,q)
        r4 = q - r3
        [roots2.append(r) for r in [r1,r2,r3,r4]]
    print(i, len(roots2))
    roots1 = roots2[::1]
    roots2 = []

print()
# Let's check em out
for r in roots1:
    b = long_to_bytes(r)
    if b[:4] == b'code':
        print(b)
```

```
codefest{neverUseEvenE}
```



## Stego Category

### Anime is Love - ? (Overdue)
Tags: Zipcracker

![](Challenge%20Screenshots/Anime%20is%20Love.png)



```

```



### Telephone - ? (Overdue)
Tags: LSB, DTMF tones

![](Challenge%20Screenshots/Telephone.png)



```

```



### b1n4rY - ?
Tags: QR code

![](Challenge%20Screenshots/b1n4rY.png)



```
codefest{1t_w4s_4_kYu_4r3}
```



## OSINT Category

### Sanity Check 2 - ?
Tags: Web, Encoding, Ciphers

![](Challenge%20Screenshots/Sanity%20Check%202.png)



```
codefest{D0ub1y_3nc0d3d_Str1n8}
```



### E-mail - ?
Tags: People tracking

![](Challenge%20Screenshots/E-mail.png)



```
codefest{mayank.shubham94@gmail.com}
```



## Pwn Category

### C is hard - ?
Tags: Buffer overflow

![](Challenge%20Screenshots/C%20is%20hard.png)



```
codefest{overflowing_stacks_for_flags_and_fun_768999766}
```



