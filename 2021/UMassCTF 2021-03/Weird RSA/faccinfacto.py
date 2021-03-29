#!/usr/bin/evn python3

# Imports
from math import factorial as fac
import chall
import gmpy2
import random
import numpy.random as npr
import os
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Modulus
n = 18378141703504870053256589621469911325593449136456168833252297256858537217774550712713558376586907139191035169090694633962713086351032581652760861668116820553602617805166170038411635411122411322217633088733925562474573155702958062785336418656834129389796123636312497589092777440651253803216182746548802100609496930688436148522617770670087143010376380205698834648595913982981670535389045333406092868158446779681106756879563374434867509327405933798082589697167457848396375382835193219251999626538126258606572805220878283429607438382521692951006432650132816122705167004219371235964716616826653226062550260270958038670427

# Construct our prime
p = '?'*512 + '0'*256 + '?'*256
#print(p)





# Get 768 MSBs of n
nmsb = int(bin(n)[2:2+512+256],2) << (2048-512-256)
assert len(bin(nmsb)[2:]) == 2048

rtnmsb = int(gmpy2.iroot(nmsb,2)[0])
#print(bin(rtnmsb)[2:])

pmsb = bin(rtnmsb)[2:2+256+128]
#print(pmsb)

p = pmsb + p[256+128:]
print(p)





# Get 512 LSBs of n
nlsb = bin(n)[-512:]
assert len(nlsb) == 512

#print('Factorize me! ^w^')
#print(int(nlsb,2))

# Factorization complete!
pstr = "27 × 25 × 7 × 19 × 179779 × 344 414383 × 630 168533 × 36229 907850 622309 477663 × 11 140616 700044 253820 247009 075680 741591 × 146533 705965 347157 224632 736630 732999 962552 705792 616142 976444 170589".replace(' ','').split('×')
ps = [int(i) for i in pstr]

# Check
ncheck = 1
for pi in ps:
    ncheck *= pi
    
assert( int(nlsb,2) == ncheck )




print("I'm gonna start cracking now, oki? ^w^")
ite = 0
while True:
    trime = 1
    i = 0
    
    while i < 16:
        pick = npr.choice(ps)
        
        if trime % pick == 0:
            i += 1
            continue
        if trime * pick > 2**256:
            i += 1
            continue
            
        trime *= pick
        
    if int(nlsb,2) % trime == 0:
        
        plsb = trime
        qlsb = int(nlsb,2)//trime
        
        assert plsb*qlsb == int(nlsb,2)
        
        if len(bin(plsb)[2:]) > 256:
            continue
        if len(bin(qlsb)[2:]) > 256:
            continue
        
        #print('Gottem!')
        #print(plsb)
        #print(qlsb)
        
        u = 0
        while u < 100000:
            
            rbyts = os.urandom(128)
            
            pry = p[:-256].replace('?'*128,'{:0128d}'.format(int(bin(bytes_to_long(rbyts))[2:])))
            pry += '{:0256d}'.format(int(bin(qlsb)[2:]))
            
            pry = int(pry,2)
            
            if n % pry == 0:
                
                print('AAAAAAAAAAAAAHH')
                
                print(pry)
                print(n//pry)
                
                assert pry*(n//pry) == n
                
                exit()

                break
            
            u += 1
        
        if n % pry == 0:
            break

    ite += 1
    print("I've done {} so far, I'm getting tired".format(ite))