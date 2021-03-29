#!/usr/bin/env python3

# Imports
from math import factorial as fac
import gmpy2
import random
import numpy.random as npr

n = 18378141703504870053256589621469911325593449136456168833252297256858537217774550712713558376586907139191035169090694633962713086351032581652760861668116820553602617805166170038411635411122411322217633088733925562474573155702958062785336418656834129389796123636312497589092777440651253803216182746548802100609496930688436148522617770670087143010376380205698834648595913982981670535389045333406092868158446779681106756879563374434867509327405933798082589697167457848396375382835193219251999626538126258606572805220878283429607438382521692951006432650132816122705167004219371235964716616826653226062550260270958038670427

# MSB of n
nmsb = int(bin(n)[2:2+256*2],2) << 6*256

# Square root the MSB of n
offset=8
nrootmsb = bin(gmpy2.iroot(nmsb,2)[0])[2:2+256*2-offset]

# Create leaked primes
pleak = nrootmsb + offset*'?' + 256*'0' + 256*'?'
qleak = pleak

# Visual checks
assert len(pleak) == 4*256
print('P_leak:')
print(pleak[:256])
print(pleak[256:2*256])
print(pleak[2*256:3*256])
print(pleak[-256:])

nmsb = bin((int(nrootmsb,2) << 512+offset)**2)[2:]
#print(len(nmsb))
nmrlsb = bin(n - int(nmsb,2))[-512:]; #print(len(nmrlsb), nmrlsb)
print('Factorize please!\n'+str(int(nmrlsb,2)))





pstr = "27 × 25 × 7 × 19 × 179779 × 344 414383 × 630 168533 × 36229 907850 622309 477663 × 11 140616 700044 253820 247009 075680 741591 × 146533 705965 347157 224632 736630 732999 962552 705792 616142 976444 170589".replace(' ','').split('×')
ps = [int(i) for i in pstr]
ncheck = 1
for p in ps:
    ncheck *= p
assert( int(nmrlsb,2) == ncheck )



print('Starting my adventure!')

rrr = 0

while True:
    
    trime = 1
    i = 0
    
    while i<100:
        
        pick = npr.choice(ps)

        if trime % pick == 0:
            i += 1
            continue

        if trime * pick > 2**256:
            i+= 1
            continue

        trime *= pick

    #print(trime)

    p = pleak[:-256]

    #print(len(bin(trime)[2:]))
    
    p += '{:0256d}'.format(int(bin(trime)[2:]))

    for i in range(2**offset):

        tryp = int(p.replace('?'*offset,'{:0{of}d}'.format(int(bin(i)[2:]),of=offset)),2)
        
        #print(tryp)
        #print(n % tryp)
        
        if n % tryp == 0:
            print(tryp)
            print('Gottem!')
            break
            
    rrr += 1