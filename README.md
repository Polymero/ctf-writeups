# ctf-writeups
My workings on the challenges of various CTF events, mainly crypto, stego, and coding challenges :)

If you like these kind of puzzles, check out my own online cryptographic puzzle series:
- Apply now for a position as Intergalactic Diplomat at Hyperspatial Engineering: www.sebven.com/HE/overview
- Unravel the mysteries and climb the towers in the Mysteries of Kumaon: www.sebven.com/MoK/coming-soon

------
# 2021

- **b01lers CTF 2021**
	- [RSASSS](./2021/b01lers%20CTF%202021-04/RSASSS) - Crypto 493 (13)\
		&#8250; RSA, Shamir's secret sharing
	- [Baby Double XOR](./2021/b01lers%20CTF%202021-04/Baby%20Double%20XOR) - Crypto 497 (8)\
		&#8250; Double XOR cipher cryptanalysis, all unknowns
	- [Unlucky Strike](./2021/b01lers%20CTF%202021-04/Unlucky%20Strike) - Crypto 498 (7)\
		&#8250; AES-CBC padding oracle attack to forge encryption
	- [Cold War Gets Hotter](./2021/b01lers%20CTF%202021-04/Cold%20War%20Gets%20Hotter) - Crypto 499 (4)\
		&#8250; coming soon
	- [Reasonable Security Ahead](./2021/b01lers%20CTF%202021-04/Reasonable%20Security%20Ahead) - Crypto 500 (2)
		&#8250; coming soon
	- [Double XOR](./2021/b01lers%20CTF%202021-04/Double%20XOR) - Crypto 500 (1)
		&#8250; coming soon

- **ångstromCTF 2021**
	- [Home Rolled Crypto](./2021/angstromCTF%202021-04/Home%20Rolled%20Crypto) - Crypto 70 (173)\
		&#8250; Bit-wise encryption, input-output reverse
	- [Follow the Currents](./2021/angstromCTF%202021-04/Follow%20the%20Currents) - Crypto 70 (270)\
		&#8250; Simple XOR cipher brute-force
	- [Circle of Trust](./2021/angstromCTF%202021-04/Circle%20of%20Trust) - Crypto 100 (85)\
		&#8250; Custom secret sharing scheme, math reverse
	- [I'm so Random](./2021/angstromCTF%202021-04/I_m%20so%20Random) - Crypto 100 (237)\
		&#8250; Custom PRNG, weak PRNG
	- [Oracle of Blair](./2021/angstromCTF%202021-04/Oracle%20of%20Blair) - Crypto 160 (136)\
		&#8250; AES-CBC decryption oracle exploit (not a padding oracle attack)

- **Foobar CTF 2021**
	- [Profezzor revenge](./2021/Foobar%20CTF%202021-04/Profezzor%20revenge) - Crypto 100 (66)\
		&#8250; XOR entire PDF with key derived from hex signature
	- [Lost-N](./2021/Foobar%20CTF%202021-04/Lost-N) - Crypto 100 (47)\
		&#8250; RSA, unknown modulus recovery from cipher- plaintext pairs
	- [Hill-Kill](./2021/Foobar%20CTF%202021-04/Hill-Kill) - Crypto 436 (15)\
		&#8250; Hill cipher, linear algebra, pwn automatic decryption
	- [Back to the future](./2021/Foobar%20CTF%202021-04/Back%20to%20the%20future) - Crypto 453 (13)\
		&#8250; RSA, modular square roots, time seeded random()
	- [Pascal's Chemistry Lab](./2021/Foobar%20CTF%202021-04/Pascal_s%20Chemistry%20Lab) - Crypto 453 (13)\
		&#8250; Fermat factorisation, Paillier cryptosystem
	- [Intern](./2021/Foobar%20CTF%202021-04/Intern) - Crypto 461 (12)\
		&#8250; RSA, LCG prediction, Franklin-Reiter related message attack, (Coppersmith's short-pad attack)
	- [From Japan with Love](./2021/Foobar%20CTF%202021-04/From%20Japan%20with%20Love) - Stego 383 (20)\
		&#8250; QR, red herring, LSB hidden ascii

- **picoCTF 2021**
	- [Easy Peasy](./2021/picoCTF%202021-03/) - Crypto 40 (424)\
		&#8250; XOR cipher disguised as an OTP, len(key) != len(msg)
	- [New Caesar](./2021/picoCTF%202021-03/) - Crypto 60 (586)\
		&#8250; Caesar cipher-like, simple reverse and brute-force, small key
	- [Mini RSA](./2021/picoCTF%202021-03/) - Crypto 70 (374)\
		&#8250; RSA, small public exponent e, brute-force e-th root of k\*N
	- [Dachshund Attacks](./2021/picoCTF%202021-03/) - Crypto 80 (587)\
		&#8250; RSA, small private exponent d, brute-force d
	- [No Padding, No Problem](./2021/picoCTF%202021-03/) - Crypto 90 (326)\
		&#8250; RSA, chosen chiphertext attack (no padding)
	- [Pixelated](./2021/picoCTF%202021-03/) - Crypto 100 (586)\
		&#8250; Image XOR
	- [Play Nice](./2021/picoCTF%202021-03/) - Crypto 110 (414)\
		&#8250; Playfair cipher
	- [Double DES](./2021/picoCTF%202021-03/) - Crypto 120 (214)\
		&#8250; 2DES-ECB, meet in the middle attack
	- [Compress and Attack](./2021/picoCTF%202021-03/) - Crypto 130 (163)\
		&#8250; Compression before encryption leak
	- [Scrambled: RSA](./2021/picoCTF%202021-03/) - Crypto 140 (99)\
		&#8250; coming soon
	- [It's Not My Fault 1](./2021/picoCTF%202021-03/) - Crypto 300 (82)\
		&#8250; coming soon
	- [New Vignere](./2021/picoCTF%202021-03/) - Crypto 300 (255)\
		&#8250; Vigenère cipher-like, reverse and brute-force, small character space
	- [Clouds](./2021/picoCTF%202021-03/) - Crypto 500 (16)\
		&#8250; coming soon

- **UMassCTF 2021**
	- [malware](./2021/UMassCTF%202021-03/malware) - Crypto 434 (78)\
		&#8250; AES-CTR with re-used iv/counter and known plaintext
	- [Factoring is Fun](./2021/UMassCTF%202021-03/Factoring%20is%20Fun) - Crypto 500 (7)\
		&#8250; Iterative Lattice Factorisation with 'random' known bits of p
	- [Weird RSA](./2021/UMassCTF%202021-03/Weird%20RSA) - Crypto 500 (10)\
		&#8250; LUC-RSA cryptosystem (based on 2nd order Lucas sequence) and close prime Fermat factorisation
	- [warandpieces](./2021/UMassCTF%202021-03/warandpieces) - Stego 499 (13)\
		&#8250; 16-bit encoding (hex)

- **Securinets CTF Quals 2021**
	- [MiTM](./2021) - Crypto 559 (36)\
		&#8250; Diffie-Hellman exchange man in the middle attack (w/ ghost-check)
	- [MiTM Revenge](./2021) - Crypto 757 (27)\
		&#8250; Diffie-Hellman exhange delayed man in the middle attack, with XOR vuln (w/ ghost-check)
	- [Special](./2021) - Crypto 908 (17)\
		&#8250; RSA LSB attack with small root finding
	- [Shilaformi](./2021) - Crypto 940 (14)\
		&#8250; coming soon
	- [Sign it!](./2021) - Crypto 949 (13)\
		&#8250; coming soon
	- [Exfiltration](./2021) - Stego 793 (25)\
		&#8250; coming soon 

- **LINE CTF 2021**
	- [babycrypto1](./2021) - Crypto 50 (106)\
		&#8250; coming soon 
	- [babycrypto2](./2021) - Crypto 50 (98)\
		&#8250; coming soon 
	- [babycrypto3](./2021) - Crypto 50 (58)\
		&#8250; coming soon
	- [babycrypto4](./2021) - Crypto 50 (35)\
		&#8250; coming soon

- **BlueHens CTF 2021**
	- [hot_diggity_dog](./2021) - Crypto 75 (48)\
		&#8250; RSA, large public exponent e, brute-force small private exponent d
	- [PHEnomenal](./2021) - Crypto 212 (29)\
		&#8250; Paillier Homomorphic Encryption
	- [OTP1](./2021) - Crypto 284 (26)\
		&#8250; coming soon
	- [OTP2](./2021) - Crypto 422 (17)\
		&#8250; coming soon
	- [OPT3](./2021) - Crypto 482 (9)\
		&#8250; coming soon
	- [aHead Of The curve (Probably)](./2021) - Crypto 493 (6)\
		&#8250; coming soon
	- [hot_diggity_dog_2](./2021) - Crypto 500 (1)\
		&#8250; coming soon
	- [conFidential searcH and dEstroy](./2021) - Crypto 500 (1)\
		&#8250; coming soon

- **Codefest CTF 2020**
	- [RSA 1.0](./2021) - Crypto ? (?)\
		&#8250; RSA, multi-prime factorisation, insufficient padding
	- [RSA 2.0](./2021) - Crypto ? (?)\
		&#8250; RSA, even public exponent e, Tonelli-Shanks decryption
	- [Anime is Love](./2021) - Stego ? (?)\
		&#8250; coming soon
	- [Telephone](./2021) - Stego ? (?)\
		&#8250; coming soon
	- [b1n4rY](./2021) - Stego ? (?)\
		&#8250; QR code
	- [Sanity Check 2](./2021) - OSINT ? (?)\
		&#8250; Simple ciphers and encoding
	- [E-mail](./2021) - OSINT ? (?)\
		&#8250; Google
	- [C is hard](./2021) - Pwn ? (?)\
		&#8250; Buffer overflow exploit

- **NahamCon CTF 2021**
	- [Dice Roll \[Medium\]](./2021) - Crypto 406 (201)\
		&#8250; Mersenne-twister based RNG prediction
	- [Elliptical \[Hard\]](./2021) - Crypto 500 (19)\
		&#8250; ECDSA re-used nonce exploit
	- [Treasure \[Easy\]](./2021) - Crypto 448 (154)\
		&#8250; Book cipher
	- [Eaxy \[Easy\]](./2021) - Crypto 433 (172)\
		&#8250; Iterative XOR encryption
	- [DDR \[Medium\]](./2021) - Scripting 497 (51)\
		&#8250; Pixel values, PIL Python script

- **DaVinciCTF 2021**
	- [Bootless RSA](./2021) - Crypto 25 (127)\
		&#8250; RSA, small public exponent e
	- [The more, the less](./2021) - Crypto 41 (62)\
		&#8250; RSA, multi-prime factorisation
	- [Substitution](./2021) - Crypto 25 (266)\
		&#8250; Substitution cipher
	- [Kanagawa](./2021) - Pwn 59 (92)\
		&#8250; Buffer overflow exploit
	- [Format me](./2021) - Pwn 90 (47)\
		&#8250; String format exploit

- **NetOn CTF 2021**
	- [Just win](./2021) - Pwn 250 (4)\
		&#8250; coming soon
	- [Limited](./2021) - Pwn 499 (4)\
		&#8250; Simple password brute-force
	- [Darkness](./2021) - Pwn 500 (1)\
		&#8250; coming soon
	- [Side Login](./2021) - Pwn 500 (2)\
		&#8250; coming soon
	- [Welcome to FilterLand](./2021) - Web 208 (24)\
		&#8250; PHP strcmp() exploit
	- [Picnicnic](./2021) - Web 222 (20)\
		&#8250; Cookie trail
	- [Let me in!](./2021) - Web 245 (9)\
		&#8250; Captcha with PHPSESSID cookie
	- [Grades](./2021) - Web 486 (10)\
		&#8250; JavaScript encryption de-obfuscation and brute-force
	- [Jungle Meeting](./2021) - Stego 50 (33)\
		&#8250; Strings and grep
	- [Seeing blurry](./2021) - Stego 50 (16)\
		&#8250; - Autostereogram
	- [Winter](./2021) - Stego 218 (21)\
		&#8250; Whitespace ssteganography (snow, stegsnow)
	- [Step by step](./2021) - Stego 250 (4)\
		&#8250; Pixel value masking and steghide
	- [Invisibility](./2021) - Stego 500 (3)\
		&#8250; Unicode zero-width steganography
	- [Caesar's Secret](./2021) - OSINT 163 (34)\
		&#8250; Waybackmachine, Twitter
	- [Capture The Flag](./2021) - OSINT 436 (20)\
		&#8250; Google, Google Maps
	- [PawN PawN](./2021) - Crypto 188 (29)\
		&#8250; Morse-code, chess board set-up code and visual encoding
	- [Weak xor](./2021) - Crypto 239 (13)\
		&#8250; Small XOR key and partly known plaintext
	- [BritishScientific](./2021) - Crypto 242 (11)\
		&#8250; Playfair cipher
	- [Facts Br0!](./2021) - Crypto 244 (10)\
		&#8250; RSA, PEM file, simple factorisation
	- [Not Morse](./2021) - Crypto 249 (5)\
		&#8250; Baconian cipher
	- [RSA... no primEs, no problEm]() - Crypto 500 (2)\
		&#8250; Unkown e with known phi(n), brute-force values for e
	- [Run Run Run](./2021) - Coding 215 (22)\
		&#8250; Python automated HTML requests
	- [Step by step](./2021) - Coding 239 (13)\
		&#8250; Trial and error with substrings
	- [SecretMessage](./2021) - Coding 247 (8)\
		&#8250; Reverse encryption function
	- [Infiltration](./2021) - Forensics 183 (30)\
		&#8250; PCAP investigation
	- [Picasso01](./2021) - Forensics 225 (19)\
		&#8250; Binwalk, strings and grep
	- [Lost in Lab](./2021) - Forensics 479 (12)\
		&#8250; Disk image
	- [File Bomb](./2021) - Reversing 475 (13)\
		&#8250; ELF disassembly
	- [Inception](./2021) - Misc 183 (30)\
		&#8250; QR codes
	- [Photogra.fy](./2021) - Misc 227 (18)\
		&#8250; Simple flag search
	- [Kasiski the magician](./2021) - Misc 235 (15)\
		&#8250; Magic numbers fix (hex signature fix)
	- [MathTomata](./2021) - Misc 245 (9)\
		&#8250; Deterministic finite automaton
	- [Gotta catch em flag](./2021) - Misc 248 (6)\
		&#8250; GBA Emulator, Pokémon FireRed

-------
# Backtracks

- **picoCTF 2019**
	- [john_pollard](./2021) - Crypto 500 (591)\
		&#8250; RSA certificate factorisation
	- [b00tl3gRSA3](./2021) - Crypto 450 (222)\
		&#8250; RSA, multi-prime factorisation
	- [AES-ABC](./2021) - Crypto 400 (230)\
		&#8250; coming soon
	- [b00tl3gRSA2](./2021) - Crypto 400 (368)\
		&#8250; RSA, switched public and private component 
		
