# ctf-writeups
My workings on the challenges of various CTF events, mainly crypto, stego, and coding challenges :)

If you like these kind of puzzles, check out my own online cryptographic puzzle series:
- Apply now for a position as Intergalactic Diplomat at Hyperspatial Engineering: www.sebven.com/HE/overview
- Unravel the mysteries and climb the towers in the Mysteries of Kumaon: www.sebven.com/MoK/coming-soon

------
# 2021

- **Foobar CTF 2021**
	- [Profezzor revenge](./tree/master/2021/Foobar%20CTF%202021/Profezzor%20revenge) - Crypto 100 (66)\
		&#8250; XOR entire PDF with key derived from hex signature
	- [Lost-N](./tree/master/2021/Foobar%20CTF%202021/Lost-N) - Crypto 100 (47)\
		&#8250; RSA, unknown modulus recovery from cipher- plaintext pairs
	- [Hill-Kill](./tree/master/2021/Foobar%20CTF%202021/Hill-Kill) - Crypto 436 (15)\
		&#8250; Hill cipher, pwn automatic decryption
	- [Back to the future](./tree/master/2021/Foobar%20CTF%202021/Back%20to%20the%20future) - Crypto 453 (13)\
		&#8250; RSA, modular square roots, time seeded random()
	- [Pascal's Chemistry Lab](./tree/master/2021/Foobar%20CTF%202021/Pascal_s%20Chemistry%20Lab) - Crypto 453 (13)\
		&#8250; Fermat factorisation, Paillier cryptosystem
	- [Intern](./tree/master/2021/Foobar%20CTF%202021/Intern) - Crypto 461 (12)\
		&#8250; RSA, LCG prediction, Franklin-Reiter related message attack, (Coppersmith's short-pad attack)
	- [From Japan with Love](./tree/master/2021/Foobar%20CTF%202021/From%20Japan%20with%20Love) - Stego 383 (20)\
		&#8250; QR decoy, LSB hidden ascii

- **picoCTF 2021**
	- [Easy Peasy](./tree/master/2021/picoCTF%202021-03/) - Crypto 40 (424)\
		&#8250; XOR cipher disguised as an OTP, len(key) != len(msg)
	- [New Caesar](./tree/master/2021/picoCTF%202021-03/) - Crypto 60 (586)\
		&#8250; Caesar cipher-like, simple reverse and brute-force, small key
	- [Mini RSA](./tree/master/2021/picoCTF%202021-03/) - Crypto 70 (374)\
		&#8250; RSA, small public exponent e, brute-force e-th root of k\*N
	- [Dachshund Attacks](./tree/master/2021/picoCTF%202021-03/) - Crypto 80 (587)\
		&#8250; RSA, small private exponent d, brute-force d
	- [No Padding, No Problem](./tree/master/2021/picoCTF%202021-03/) - Crypto 90 (326)\
		&#8250; RSA, chosen chiphertext attack (no padding)
	- [Pixelated](./tree/master/2021/picoCTF%202021-03/) - Crypto 100 (586)\
		&#8250; Image XOR
	- [Play Nice](./tree/master/2021/picoCTF%202021-03/) - Crypto 110 (414)\
		&#8250; Playfair cipher
	- [Double DES](./tree/master/2021/picoCTF%202021-03/) - Crypto 120 (214)\
		&#8250; 2DES-ECB, meet in the middle attack
	- [Compress and Attack](./tree/master/2021/picoCTF%202021-03/) - Crypto 130 (163)\
		&#8250; Compression before encryption leak
	- [Scrambled: RSA](./tree/master/2021/picoCTF%202021-03/) - Crypto 140 (99)\
		&#8250; coming soon
	- [It's Not My Fault 1](./tree/master/2021/picoCTF%202021-03/) - Crypto 300 (82)\
		&#8250; coming soon
	- [New Vignere](./tree/master/2021/picoCTF%202021-03/) - Crypto 300 (255)\
		&#8250; Vigenère cipher-like, reverse and brute-force, small character space
	- [Clouds](./tree/master/2021/picoCTF%202021-03/) - Crypto 500 (16)\
		&#8250; coming soon

- **UMassCTF 2021**
	- [malware](./tree/master/2021/UMassCTF%202021-03/malware) - Crypto 434 (78)\
		&#8250; AES-CTR with re-used iv/counter and known plaintext
	- [Factoring is Fun](./tree/master/2021/UMassCTF%202021-03/Factoring%20is%20Fun) - Crypto 500 (7)\
		&#8250; Iterative Lattice Factorisation with 'random' known bits of p
	- [Weird RSA](./tree/master/2021/UMassCTF%202021-03/Weird%20RSA) - Crypto 500 (10)\
		&#8250; LUC-RSA cryptosystem (based on 2nd order Lucas sequence) and close prime Fermat factorisation
	- [warandpieces](./tree/master/2021/UMassCTF%202021-03/warandpieces) - Stego 499 (13)\
		&#8250; 16-bit encoding (hex)

- **Securinets CTF Quals 2021**
	- [MiTM](./tree/master/2021) - Crypto 559 (36)\
		&#8250; Diffie-Hellman exchange man in the middle attack (w/ ghost-check)
	- [MiTM Revenge](./tree/master/2021) - Crypto 757 (27)\
		&#8250; Diffie-Hellman exhange delayed man in the middle attack, with XOR vuln (w/ ghost-check)
	- [Special](./tree/master/2021) - Crypto 908 (17)\
		&#8250; RSA LSB attack with small root finding
	- [Shilaformi](./tree/master/2021) - Crypto 940 (14)\
		&#8250; coming soon
	- [Sign it!](./tree/master/2021) - Crypto 949 (13)\
		&#8250; coming soon
	- [Exfiltration](./tree/master/2021) - Stego 793 (25)\
		&#8250; coming soon 

- **LINE CTF 2021**
	- [babycrypto1](./tree/master/2021) - Crypto 50 (106)\
		&#8250; coming soon 
	- [babycrypto2](./tree/master/2021) - Crypto 50 (98)\
		&#8250; coming soon 
	- [babycrypto3](./tree/master/2021) - Crypto 50 (58)\
		&#8250; coming soon
	- [babycrypto4](./tree/master/2021) - Crypto 50 (35)\
		&#8250; coming soon

- **BlueHens CTF 2021**
	- [hot_diggity_dog](./tree/master/2021) - Crypto 75 (48)\
		&#8250; RSA, large public exponent e, brute-force small private exponent d
	- [PHEnomenal](./tree/master/2021) - Crypto 212 (29)\
		&#8250; Paillier Homomorphic Encryption
	- [OTP1](./tree/master/2021) - Crypto 284 (26)\
		&#8250; coming soon
	- [OTP2](./tree/master/2021) - Crypto 422 (17)\
		&#8250; coming soon
	- [OPT3](./tree/master/2021) - Crypto 482 (9)\
		&#8250; coming soon
	- [aHead Of The curve (Probably)](./tree/master/2021) - Crypto 493 (6)\
		&#8250; coming soon
	- [hot_diggity_dog_2](./tree/master/2021) - Crypto 500 (1)\
		&#8250; coming soon
	- [conFidential searcH and dEstroy](./tree/master/2021) - Crypto 500 (1)\
		&#8250; coming soon

- **Codefest CTF 2020**
	- [RSA 1.0](./tree/master/2021) - Crypto ? (?)\
		&#8250; RSA, multi-prime factorisation, insufficient padding
	- [RSA 2.0](./tree/master/2021) - Crypto ? (?)\
		&#8250; RSA, even public exponent e, Tonelli-Shanks decryption
	- [Anime is Love](./tree/master/2021) - Stego ? (?)\
		&#8250; coming soon
	- [Telephone](./tree/master/2021) - Stego ? (?)\
		&#8250; coming soon
	- [b1n4rY](./tree/master/2021) - Stego ? (?)\
		&#8250; QR code
	- [Sanity Check 2](./tree/master/2021) - OSINT ? (?)\
		&#8250; Simple ciphers and encoding
	- [E-mail](./tree/master/2021) - OSINT ? (?)\
		&#8250; Google
	- [C is hard](./tree/master/2021) - Pwn ? (?)\
		&#8250; Buffer overflow exploit

- **NahamCon CTF 2021**
	- [Dice Roll \[Medium\]](./tree/master/2021) - Crypto 406 (201)\
		&#8250; Mersenne-twister based RNG prediction
	- [Elliptical \[Hard\]](./tree/master/2021) - Crypto 500 (19)\
		&#8250; ECDSA re-used nonce exploit
	- [Treasure \[Easy\]](./tree/master/2021) - Crypto 448 (154)\
		&#8250; Book cipher
	- [Eaxy \[Easy\]](./tree/master/2021) - Crypto 433 (172)\
		&#8250; Iterative XOR encryption
	- [DDR \[Medium\]](./tree/master/2021) - Scripting 497 (51)\
		&#8250; Pixel values, PIL Python script

- **DaVinciCTF 2021**
	- [Bootless RSA](./tree/master/2021) - Crypto 25 (127)\
		&#8250; RSA, small public exponent e
	- [The more, the less](./tree/master/2021) - Crypto 41 (62)\
		&#8250; RSA, multi-prime factorisation
	- [Substitution](./tree/master/2021) - Crypto 25 (266)\
		&#8250; Substitution cipher
	- [Kanagawa](./tree/master/2021) - Pwn 59 (92)\
		&#8250; Buffer overflow exploit
	- [Format me](./tree/master/2021) - Pwn 90 (47)\
		&#8250; String format exploit

- **NetOn CTF 2021**
	- [Just win](./tree/master/2021) - Pwn 250 (4)\
		&#8250; coming soon
	- [Limited](./tree/master/2021) - Pwn 499 (4)\
		&#8250; Simple password brute-force
	- [Darkness](./tree/master/2021) - Pwn 500 (1)\
		&#8250; coming soon
	- [Side Login](./tree/master/2021) - Pwn 500 (2)\
		&#8250; coming soon
	- [Welcome to FilterLand](./tree/master/2021) - Web 208 (24)\
		&#8250; PHP strcmp() exploit
	- [Picnicnic](./tree/master/2021) - Web 222 (20)\
		&#8250; Cookie trail
	- [Let me in!](./tree/master/2021) - Web 245 (9)\
		&#8250; Captcha with PHPSESSID cookie
	- [Grades](./tree/master/2021) - Web 486 (10)\
		&#8250; JavaScript encryption de-obfuscation and brute-force
	- [Jungle Meeting](./tree/master/2021) - Stego 50 (33)\
		&#8250; Strings and grep
	- [Seeing blurry](./tree/master/2021) - Stego 50 (16)\
		&#8250; - Autostereogram
	- [Winter](./tree/master/2021) - Stego 218 (21)\
		&#8250; Whitespace ssteganography (snow, stegsnow)
	- [Step by step](./tree/master/2021) - Stego 250 (4)\
		&#8250; Pixel value masking and steghide
	- [Invisibility](./tree/master/2021) - Stego 500 (3)\
		&#8250; Unicode zero-width steganography
	- [Caesar's Secret](./tree/master/2021) - OSINT 163 (34)\
		&#8250; Waybackmachine, Twitter
	- [Capture The Flag](./tree/master/2021) - OSINT 436 (20)\
		&#8250; Google, Google Maps
	- [PawN PawN](./tree/master/2021) - Crypto 188 (29)\
		&#8250; Morse-code, chess board set-up code and visual encoding
	- [Weak xor](./tree/master/2021) - Crypto 239 (13)\
		&#8250; Small XOR key and partly known plaintext
	- [BritishScientific](./tree/master/2021) - Crypto 242 (11)\
		&#8250; Playfair cipher
	- [Facts Br0!](./tree/master/2021) - Crypto 244 (10)\
		&#8250; RSA, PEM file, simple factorisation
	- [Not Morse](./tree/master/2021) - Crypto 249 (5)\
		&#8250; Baconian cipher
	- [RSA... no primEs, no problEm]() - Crypto 500 (2)\
		&#8250; Unkown e with known phi(n), brute-force values for e
	- [Run Run Run](./tree/master/2021) - Coding 215 (22)\
		&#8250; Python automated HTML requests
	- [Step by step](./tree/master/2021) - Coding 239 (13)\
		&#8250; Trial and error with substrings
	- [SecretMessage](./tree/master/2021) - Coding 247 (8)\
		&#8250; Reverse encryption function
	- [Infiltration](./tree/master/2021) - Forensics 183 (30)\
		&#8250; PCAP investigation
	- [Picasso01](./tree/master/2021) - Forensics 225 (19)\
		&#8250; Binwalk, strings and grep
	- [Lost in Lab](./tree/master/2021) - Forensics 479 (12)\
		&#8250; Disk image
	- [File Bomb](./tree/master/2021) - Reversing 475 (13)\
		&#8250; ELF disassembly
	- [Inception](./tree/master/2021) - Misc 183 (30)\
		&#8250; QR codes
	- [Photogra.fy](./tree/master/2021) - Misc 227 (18)\
		&#8250; Simple flag search
	- [Kasiski the magician](./tree/master/2021) - Misc 235 (15)\
		&#8250; Magic numbers fix (hex signature fix)
	- [MathTomata](./tree/master/2021) - Misc 245 (9)\
		&#8250; Deterministic finite automaton
	- [Gotta catch em flag](./tree/master/2021) - Misc 248 (6)\
		&#8250; GBA Emulator, Pokémon FireRed

-------
# Backtracks

- **picoCTF 2019**
	- [john_pollard](./tree/master/2021) - Crypto 500 (591)\
		&#8250; RSA certificate factorisation
	- [b00tl3gRSA3](./tree/master/2021) - Crypto 450 (222)\
		&#8250; RSA, multi-prime factorisation
	- [AES-ABC](./tree/master/2021) - Crypto 400 (230)\
		&#8250; coming soon
	- [b00tl3gRSA2](./tree/master/2021) - Crypto 400 (368)\
		&#8250; RSA, switched public and private component 
		
