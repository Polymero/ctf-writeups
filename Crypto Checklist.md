# Crypto Checklist

<insert introduction here>

## Simple Ciphers

- (Keyed) Caesar Cipher
- Viginere 
- Rail fence
- XOR
- Chess codes
- Baconian
- Morse (telegraph) code
- Book cipher
- (Mono-alphabetic) substitution 

## More Complex Ciphers

- Playfair (digrams)

## RSA Attack

- Factorisation of n
- Brute-forcing missing parameters
- Small public exponent (no or weak padding)
- gcd(e,phi) != 1 -> Tonelli-Shanks
- Huge e (\~N) -> guess d, or use Wiener Attack
- If c < known prime, dr = \~e % r is enough
- RSA Certificate CRT fault attack

## AES

- ECB-mode is not semantically secure

## ECC (Elliptic Curve Cryptography)

- ECDSA nonce re-use

## Diffie-Hellman

- Man in the middle attack

## DNGs (Deterministic Number Generator)

- RandCrack for predicting Mersenne-twisters