# Weird RSA

UMassCTF 2021 - Crypto 500 (10)

## Challenge

![](Weird%20RSA.png)

We are only given the Python script shown below and I expect it to be RSA, but with a weird twist. Spoiler alert, it is indeed weird :). Let's take a look at the script!

```py
import random
from Crypto.Util.number import isPrime

m, Q = """REDACTED""", 1 

def genPrimes(size):
    base = random.getrandbits(size // 2) << size // 2
    base = base | (1 << 1023) | (1 << 1022) | 1
    while True:
        temp = base | random.getrandbits(size // 4)
        if isPrime(temp):
            p = temp
            break
    while True:
        temp = base | random.getrandbits(size // 4)
        if isPrime(temp):
            q = temp
            break
    return (p, q)

def pow(m, e, n):     
    return v(e)

def v(n):
    if n == 0:
        return 2
    if n == 1:
        return m
    return (m*v(n-1) - Q*v(n-2)) % N

p, q = genPrimes(1024)

N = p * q
e = 0x10001

print("N:", N)
print("c:", pow(m, e, N))

"""
N: 18378141703504870053256589621469911325593449136456168833252297256858537217774550712713558376586907139191035169090694633962713086351032581652760861668116820553602617805166170038411635411122411322217633088733925562474573155702958062785336418656834129389796123636312497589092777440651253803216182746548802100609496930688436148522617770670087143010376380205698834648595913982981670535389045333406092868158446779681106756879563374434867509327405933798082589697167457848396375382835193219251999626538126258606572805220878283429607438382521692951006432650132816122705167004219371235964716616826653226062550260270958038670427
c: 14470740653145070679700019966554818534890999807830802232451906444910279478539396448114592242906623394239703347815141824698585119347592990685923384931479024856262941313458084648914561375377956072245149926143782368239175037299219241806241533201175001088200209202522586119648246842120571566051381821899459346757935757111233323915022287370687524912870425787594648397524189694991735372527387329346198018567010117587531474035014342584491831714256980975368294579192077738910916486139823489975038981139084864837358039928972730135031064241393391678984872799573965150169368237298603189344477806873779325227557835790957023000991
"""
```

Now there are two things weird here. First is the custom prime generation. The 1024-bit primes for this challenge follow the following scheme:
```py
p = A1 (256-bit) + A2 (256-bit) + 0 (256-bit) + r_p (256-bit)
q = A1 (256-bit) + A2 (256-bit) + 0 (256-bit) + r_q (256-bit)
```
So the first 75% of the bits of both primes are exactly the same, this means the values for p and q are quite close.

Second is the custom encryption function. Instead of the classic RSA modular exponentiation, we are using some kind of recursive function, huh... Writing out a few steps on paper, we find v(e) generates a polynomial of order e with (e//2)+1 terms. Something along the lines of
```py
v(e) = m**e - a_1 * m**(e-2) + a_2 * m**(e-4) - ... +- a_(e//2+1) * m
```
where a_i are the polynomial coefficients.

## Solution

So... this challenge is quite unique. Its implementation of a different encryption function within our well known RSA shell makes it a true non-textbook challenge. Therefore, there are many ways we can approach this problem. Some of which might be feasible, some of which are just a plain waste of time :).

However, it should be clear our first priority is to work out what the implications are of this different encryption function. Does it perhaps have any vulnerabilities we can make use of? So I tried to rewrite the encryption function in something... less recursive. :)

**Rabbit Hole #1: Vectorising the Encryption Function**

With my confidence still intact and enough energy to be reckless, I wrote out v(e) for some values of e to try to find a pattern of sorts. As I filled multiple papers full of m's and numbers, I though I had found a pattern. The lower values for e make the polynomial coefficients of v(e) follow a binomial distribution, but this behaviour quickly shifts for higher e... So this was pointless...

**Rabbit Hole #2: Roots of Encryption Polynomial**

Another approach is to find the roots of the encryption polynomial. We could try to find the coefficients by iterative process, but this quickly proves to be slow for e=0x10001. On top of that, without using some clever tricks finding the root of such a big polynomial would take a while. Since I'm not clever like that, I steered away from this solution.

**Rabbit Hole #3: N Factorisation through Bit Recovery**

Instead of solving the encryption function for m, we could try to factorise N to recover p and q such that we can construct the decryption exponent d. One way to do this would be to consider that the first 768 bits of both p and q are the same, such that we can simply get these bits from taking the square of N. This means that we are left with a search space of 'just' 256 bits:
```
110000010000110101101010000010001101000000011011011000010000010111101001011001001101110110010001100000011101001110101111010111110000110011000010001100101010010000000110001000110011010101110010001101011111000110010011010000100010001100101001110010100001101000010010011011110101001100010111110110000011010001001101001101000000100011101100101110101010111100001111011000111101101101111011110001000001001011110000111101000111010010000011110111110110010011110000000001011110010110000010100101101010010011001101001100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
```
Brute-forcing this is not really feasible for us. So this does not help...

The better way to approach this is to realise that because p and q share their first 756 bits, they are close to each other and thus also sqrt(N). So we can easily factorise N using Fermat's method, which I did in a Jupyter Notebook with Sage integration.
```py
def factor_fermat(N):
    """Factorize N into p and q for p and q share half of their leading bits.
    i.e., if the gap between p and q is below the square root of p

    Source: http://facthacks.cr.yp.to/fermat.html
    """
    if N <= 0: return [N]
    if is_even(N): return [2,N/2]
    a = ceil(sqrt(N))
    while not is_square(a^2 - N):
        a = a + 1
    b = sqrt(a^2-N)
    return [a - b,a + b]
```

**LUC-RSA Solution**

Only after the CTF ended did I realise the form of the recursive encryption function. It's a second order Lucas sequence V(P,Q) with P=m and Q=1 (see Wikipedia)! This might seem as a weird form of RSA, but it is not unheard of. In fact, it's called the LUC-RSA (or just LUC) Cryptosystem, a nice paper on it can be read [here](https://www.researchgate.net/publication/26623030_A_New_Computation_Algorithm_for_a_Cryptosystem_Based_on_Lucas_Functions).

So how does it work? Well to encrypt (as we've seen) we calculate the e-th order Lucas sequence with P=m and Q=1. Then, to decrypt we calculate the d-th order Lucas sequence with P=c and Q=1. Huh, sounds quite neat. Our next step is to find the private exponent d, however there's a catch. We cannot use our familiar 
```py
d = ~e % phi(N),
```
 instead we use 
```py
d = ~e % LCM( (p +- 1), (q +- 1) ).
```
Now we end up with four possible decryption keys. We could easily try them all out, but we can also find the proper form from
```py
d = ~e % LCM( (p - LS(D/p)), (q - LS(D/q)) )
```
where LS is the Legendre symbol and D = C^2 - 4 the discriminant (abc-formula, anyone?). Finally, just to speed things up, we implement a more efficient encryption function (provided by the chall's author: Soul). Now we can go and get ourselves a nice flag :).

```py
#!/usr/bin/env python3

# Imports
import gmpy2
from Crypto.Util.number import long_to_bytes
import sys

# Increase the Python recursion limit
sys.setrecursionlimit(5000)

# RSA Parameters
N = 18378141703504870053256589621469911325593449136456168833252297256858537217774550712713558376586907139191035169090694633962713086351032581652760861668116820553602617805166170038411635411122411322217633088733925562474573155702958062785336418656834129389796123636312497589092777440651253803216182746548802100609496930688436148522617770670087143010376380205698834648595913982981670535389045333406092868158446779681106756879563374434867509327405933798082589697167457848396375382835193219251999626538126258606572805220878283429607438382521692951006432650132816122705167004219371235964716616826653226062550260270958038670427
C = 14470740653145070679700019966554818534890999807830802232451906444910279478539396448114592242906623394239703347815141824698585119347592990685923384931479024856262941313458084648914561375377956072245149926143782368239175037299219241806241533201175001088200209202522586119648246842120571566051381821899459346757935757111233323915022287370687524912870425787594648397524189694991735372527387329346198018567010117587531474035014342584491831714256980975368294579192077738910916486139823489975038981139084864837358039928972730135031064241393391678984872799573965150169368237298603189344477806873779325227557835790957023000991
E = 0x10001

# I used Fermat's factorisation method to get p and q using SAGE
P = 135566004969921829046861317679102794894163252891621004552763069255612086965641424719754859767153782381891044077537624735662301899417143962916558791489710971298124937969427903581890089403413545652984524659790357002447801666607195021452029447206533810446315939039775701027454771450154054624400219767469987538497
Q = 135566004969921829046861317679102794894163252891621004552763069255612086965641424719754859767153782381891044077537624735662301899417143962916558791489710971298124937969427903581890089403413545652984524659790357002447801666607195021441224446867180097273643121640903324702747770969633717818870639347019154977691

# LUCRSA Cryptosystem (based on second order Lucas sequence (!))
# See https://www.researchgate.net/publication/26623030_A_New_Computation_Algorithm_for_a_Cryptosystem_Based_on_Lucas_Functions
D = C**2 - 4
LS_P = gmpy2.legendre(D,P)
LS_Q = gmpy2.legendre(D,Q)

# Get that decryption bread
d = gmpy2.invert(E, gmpy2.lcm(P-LS_P, Q-LS_Q))

# If you can, prevent v_dict{} from initialising again as it'll save you time for future computations :)
v_dict = {}

# Function I got from Soul, what a nice guy!
def v(n):
    if n == 0:
        return 2
    if n == 1:
        return m
    if n in v_dict.keys():
        return v_dict[n]
    if(n % 2 == 0):
        ret = (pow(v(n // 2), 2, N) - 2 * pow(Q, n, N)) % N
    else:
        ret = (m * pow(v(n // 2), 2, N) - Q * v(n // 2) * v((n // 2) - 1) - m * pow(Q, n, N)) % N
    v_dict[n] = ret
    return ret

m = C; Q = 1

print('Capturing the flag...')
print()

flag = v(d)
print('Got it!')
print(long_to_bytes(flag))
```
Voilá!
```
UMASS{who_said_we_had_to_multiply_117a1b8a68814dc478ad78bc67d7d7d4}
```