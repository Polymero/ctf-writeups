# FLAG
"""
apoly@erazer:~/Downloads/drive-download-20210328T133840Z-001/Factoring is Fun$ nc 34.69.184.228 8080
Enter a string with the prefix 'UMass-' that when sha-256 hashed begins with bd7f3
> UMass-NrBy7cqgoIAWopAxqWmgDF3kNTNCheEs
N: 83053629859775920711567812747186440767081481550602251188553309206324295681965330133627944485866485070999764911856916661666341055580506407138328928582102280441307404997028414990454411914585618511541665346003685339249951173834579019444763896855008180436531017231173187615328630282433643469979677583481033456767
e: 65537
p: 0b11011101000001010000101110000011????????0000111000110101111001110101111110101000000101101100110100101100011111011100010011111101100100001010100010101010110010110011001111111110111110001111100000100110100100011000001111000001101100010111000111011110001101010001001010111000101010011011011101100011011001110011110011110101001100111010100111110000011101110001111110110011001111101011100000100001001111000010011111110000????????11001001????????0001111000100110010100000010011010100110????????010100111010010111111001
Prove you can factor N by sending me the decryption key!
> 24191078938512024512307825770649281593646617961143268274994188312549010181623147030239770393681513244736782464904354519653764810869833632999123562532672384659276928302606548427115360875761532829984154985536440361298729500271499634436855857117746802664326542046945303769897910083401629018251404323722514321233
UMASS{0n1y_4_f3w_m0r3_y34rs_t1ll_sh0rs}
"""

# SAGE (!) I used a Jupyter Notebook with Sage integration

import hashlib
import numpy.random as npr

alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def poww(pow_hash):
    
    while True:
        
        pow_try = b'UMass-' + ''.join(npr.choice(list(alp),32)).encode()
        #print(pow_try)
        pow_sha = hashlib.sha256(pow_try).hexdigest().encode()
        
        if pow_hash == pow_sha[:5]:
            
            return pow_try
    
poww(b'bd7f3')


N = 83053629859775920711567812747186440767081481550602251188553309206324295681965330133627944485866485070999764911856916661666341055580506407138328928582102280441307404997028414990454411914585618511541665346003685339249951173834579019444763896855008180436531017231173187615328630282433643469979677583481033456767

precv = "11011101000001010000101110000011????????0000111000110101111001110101111110101000000101101100110100101100011111011100010011111101100100001010100010101010110010110011001111111110111110001111100000100110100100011000001111000001101100010111000111011110001101010001001010111000101010011011011101100011011001110011110011110101001100111010100111110000011101110001111110110011001111101011100000100001001111000010011111110000????????11001001????????0001111000100110010100000010011010100110????????010100111010010111111001"
pmsb = precv[:-96] + '0'*96


for i in range(0,256):

    ptry = pmsb.replace('????????','{:08d}'.format(int(bin(i)[2:])))
    #print(bin(i)[2:])

    facco = factor_lattice(N, int(ptry,2), 2**96, 8, 4)
    
    if facco[0] != 1:
        print(facco)
        p,q = facco
        
assert p*q == N

phi = (p-1)*(q-1)
print(phi)

d = pow(0x10001, -1, phi)
print(d)