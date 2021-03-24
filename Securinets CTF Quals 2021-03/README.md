# Securinets CTF Quals 2021-03

<insert intro text here>

## Crypto Category

### MiTM - 559

![](Challenge%20Screenshots/MiTM.png)

A man in the middle attack, exciting! So let's just make our own key pairs and juggle them with all our three unsuspecting victims... wait a minute what's that at the end? A ghost check? It seems they are able to check their secrets with each other without us intercepting :c. That makes this challenge a lot more interesting, we need to make sure they all have the same secret, whilst also finding out what it is. The problem boils down to the diagram below, where our injections are red and the ghost check green.

![](Solution%20Screenshots/DHx_setup.png)

Below you can find the solved diagram, although without the boxes.

![](Solution%20Screenshots/DHx_solution.png)

...

```
Securinets{monkey-in-the-middle_efa8cf7dad56f238cc1ff49473da3ae3}
```



### MiTM Revenge - 757 (Overdue)

![](Challenge%20Screenshots/MiTM%20Revenge.png)

...

![](Solution%20Screenshots/DHx2_setup.png)

Below you can find the solved diagram, although without the boxes.

![](Solution%20Screenshots/DHx2_solution.png)

...

```
Securinets{master-in-the-middle_bb8f4b012d02284aea258723179dff83}
```



### Special - 908 (Overdue)

![](Challenge%20Screenshots/Special.png)

```py
# Imports
import gmpy2
from Crypto.Util.number import long_to_bytes

# Integer abc-formula
def int_abc(a, b, c):
    
    # Calculate D
    D = pow(b,2) - 4*a*c
    
    # Check for negative D
    if D < 0:
        return ()
    
    # Check for zero D
    if D == 0:
        # Make sure it is integer divisible
        if b % (2 * a) != 0:
            return ()
        return (-b // (2 * a))
    
    # Double root for positive D, but only if integer root
    sqr, intrt = gmpy2.iroot(D, 2)
    if not intrt:
        return ()
    
    # Collect roots if integer divisible
    # First root
    if (-b - sqr) % (2 * a) == 0:
        rt1 = (-b - sqr) // (2 * a)
    else:
        rt1 = None
    # Second root
    if (-b + sqr) % (2 * a) == 0:
        rt2 = (-b + sqr) // (2 * a)
    else:
        rt2 = None
        
    # Return
    return tuple( int(i) for i in (rt1,rt2) if i is not None )

# Simple euler inverse function
def eulinv(x, n):
    a, b, u = 0, n, 1
    while x > 0:
        q = b // x 
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % n
    else:
        return None

# Simple ceil function
def ceil(a,b):
    return int(-(-a // b))

# RSA parameters
n = 9205101698706979739826801043045342787573860852370120009782047065091267165813818945944938567077767109795693195306758124184300669243481673570359620772491153042678478312809811432352262322016591328649959068333993409371541201650938826630256112619578125044564261211415732174900162604077497313177347706230511508892968172603494805342653386527679619380762253476920434736431368696225307809325876263469267138456334317623292049963916185087736277032965175422891773251267119088153064627668031982940139865703040003065759250189294830016815658342491949959721771171008624698225901660128808998889116825507743256985320474353400908203
e = 65537

rp = 1337
rq = 1187

# Ciphertext
c = 7936922632477179427776336441674861485950589109838466370248848810603305227730610589646741819313897162184198914593449584513298801516246072184328924490958302064664202813944180474377318619755541891685799909623945111729243482919086734358170659346187530089396234296268433976153029353575494866263288471212406042845186256151549768916089844077364464961133610687655801313809083988904726871667971720011220619598069236604397523051054337851497256894302257378216064087800301371122182309897203436049352850483968349573626245496903689129366737214112517774597434631637719018819317503710042658242522690613437843118568709251604555104

# Attack inspired by: https://doi.org/10.3390/sym12050838
# 'A New LSB Attack on Special-Structured RSA Primes'

# Get attack parameters
i = ceil( pow(rp * rq, 1/2), 1)
s = pow( int(gmpy2.iroot(n, 2)[0]) - i , 2) # inherent floor
z = (n - (rp*rq)) % s

# Solve for x1,2 = X**2 - z*X + s*rp*rq = 0
x12 = int_abc(1, -z, s*rp*rq)
#print(x12)

# Not the right answer :c -> so let us iterate up from i

p = None; q = None
while p is None and q is None:
    
    # Increment i and get new attack parameters
    i += 1
    s = pow( int(gmpy2.iroot(n, 2)[0]) - i , 2) # inherent floor
    z = (n - (rp*rq)) % s
    
    # Get the roots
    x12 = int_abc(1, -z, s*rp*rq)
    
    # If the roots exist, check for primes!
    if x12 != ():
        if x12[1] % rq == 0:
            p = x12[1]//rq + rp
        if x12[0] % rp == 0:
            q = x12[0]//rp + rq
            
#print(x12)
print(p);print()
print(q);print()
print(p*q == n)
print()

# Get secret exponent
d = eulinv(e, (p-1)*(q-1))

# Get message
m = pow(c,d,n)

# And we can enjoy our flag :)
print(long_to_bytes(m))
```

```
Securinets{6650b577b4be574b9180a52631d6d431513f6981ade2d5c81efdea43bb365d98}
```



### Shilaformi - 940 (Overdue)

![](Challenge%20Screenshots/Shilaformi.png)



```

```



### Sign it! - 949 (Overdue)

![](Challenge%20Screenshots/Sign%20it.png)



```

```



## Stego Category

### Exfiltration - 793 (Overdue)

![](Challenge%20Screenshots/Exfiltration.png)



```

```