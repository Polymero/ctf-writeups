# NetOn CTF 2021-03

I was excited to participate in my first ever CTF and enjoyed the experienced very much. Thanks to all of those involved in setting it up! ~<3

We were set a total of 43 challenges across nine different categories:
- Pwn
- Web
- Stego
- OSINT
- Crypto
- Coding
- Forensics
- Reversing
- Misc

Below you can find my solutions to the challenges I was able to solve and some fruitless tries to some of those I could not solve (in time). So be sure to check other participants' writeups as well! The points are displayed as well, some of which are reduced due to the dynamic scoring system (more solves = fewer points). Within the screenshots, the authors of each individual puzzle is displayed as well.

If you have any questions and/or comments, please do not hesitate to contact me. :)

CTF Rules:

![](CTF%20Rules.png)

Final Top 10:

I placed 3rd :).

![](CTF%20Top%2010.png)

## Pwn Category

### Limited - 499

![](Challenge%20Screenshots/Pwn%20-%20Limited.png)

Upon connecting it promptly tells us we have 3 tries to guess a 3-digit code. Well... if you do not want to let me in if I ask nicely, I will just guess my way in >:). I use pwntools in Python to spam the address with password guesses:
```py
#!/usr/bin/env python3

# Imports
from pwn import *

# Connect parameters
host = "167.99.129.209"
port = 10002

pwd = 0
while pwd < 1000:
	# Open connection
	s = remote(host, port)
	s.recvuntil("\n")
	# Loop over given tries (re-connect afterwards)
	for j in range(3):
		# Increment trial 3-digit password and send
		pwd += 1
		s.sendline(str(pwd))
		# Get return
		rstr = s.recvuntil("\n", drop=True).decode("latin-1")
		print(rstr)
		s.recvuntil("\n")
		# Check return string
		if rstr[0] != 'S':
			print(rstr)
			pwd += 1000
		# Visual check of progress
		if pwd % 100 == 0:
			print(pwd)
	# Close connection
	s.close()
```

Although the password is randomised (as could be deduced from the provided ELF), a 3-digit password can be easily brute-forced. So to no surprise, after some guessing this script got lucky and got returned:

```
Nice! The flag is NETON{N1c3_ByP4sS_My_Fr13eND!}
```

I'm not sure whether or not this counts as a bypass... but hey, it worked. : )



## Web Category

### Welcome to FilterLand - 208

![](Challenge%20Screenshots/Web%20-%20Welcome%20to%20FilterLand.png)

The website asks us for a password, nothing more, nothing less. By using the browser inspect tool (F-12) we see it posts our input to check.php. It also tells us they have made the PHP file available to us, so of course, we take a look :).

```php
<?php
    $FLAG =  (file_get_contents("/flag.txt")); //SECRET
    $PASSWORD = $_POST['password']; //User password

    if(isset($PASSWORD)){
    
    $PASSWORD = str_replace("s4cuRe_p4sW0rD","Nice_try!",$PASSWORD); //Replace

    if(strcmp('s4cuRe_p4sW0rD', $PASSWORD) == 0){ //Check
            
            echo $FLAG;
        
        }
        else{
            header("Location: /fail.html");
            die();
        }

    }
    else {
        echo "Give me what I'm looking for ):";
    }

?>
```

So the correct password is 's4cuRe_p4sW0rD', but they filter it out of our responses, how cheeky :c. Fortunately, or rather unfortunately, there is a vulnerability to the PHP strcmp functions. If instead of a string, we pass on something PHP recognises as a list it will return True, regardless of our input :).

I first tried to use HTML by going to the link
```
http://167.99.129.209:8000/check.php?password[]=oops
```
However, this did not work so I used curl instead
```sh
$ curl -d password[]=oops 167.99.129.209:8000/check.php
```
which happily returns our desired flag
```
NETON{arrays_FOR_the_WIN!}
```



### Picnicnic - 222

![](Challenge%20Screenshots/Web%20-%20Picnicnic.png)

Upon visiting the given website we are greeted with four appetising pictures of some cookies. Yum! However, there is a fifth. If we inspect the page (F-12) and check the 'Storage' tab we see another cookie, named 'flag' with the value 'TkVUT057MHV'. This looks a lot like base64 encoding, and indeed we find
```
NETON{0u
```

However, this is only a part of the flag...
Deleting our cookie and refreshing the connection just gives us the same cookie.
What about visiting through curl and sending this cookie with us. (Or setting the cookie value in your browser through inspect.)

```sh
$ curl -v --cookie "flag=TkVUT057MHV" http://167.99.129.209:8001
```
*Remember to use the verbose option '-v' in order to see the cookie information.*

Suddenly, our cookie value has changed! In fact, we can do this process four times to find all four pieces of the flag.

In base64 encoding
```
TkVUT057MHV  
yX2MwMGtpZV
NfNHJlXzR3Z
XMwbWUhfQ==
```
which gives us the flag
```
NETON{0ur_c00kieS_4re_4wes0me!}
```



### Let me in! - 245

![](Challenge%20Screenshots/Web%20-%20Let%20me%20in!.png)

An empty page, with just a taunting 'Try to catch me!'... Pff, dare provoke me? Alright, alright. Let's see what you do _click_ nothing... Hah?
Upon inspection it sends us to flag.php, but visiting it immediately sends us back to index.php... Let's curl!

```sh
$ curl http://167.99.129.209:8002/flag.php
```
reveals the structure of flag.php
```html
<html>
        <head>
                <title>Try to catch the flag!</title>
        </head>
        <body>
                <form method="POST">
                        <p>
                                <label for="captcha">Please Enter the Captcha Text</label><br />
                                <img src="captcha.php" alt="CAPTCHA" class="captcha-image">
                        </p>
                        <p>
                                <input type="text" id="captcha" name="captcha_challenge">
                                <input type="submit" value="Send">
                        </p>
                </form>
        </body>
</html>
```
So it actually sends us to captcha.php instead of index.php. Okay, let's curl once more to find... gibberish... oh. Visiting the URL with a browser gives us a captcha image. Mmh, how do we feed this captcha code to the HTML form. Every time we request (refresh) the page, we get a new captcha... How about this: we empty out our cookie jar and visit captcha.php to get a captcha image and a PHP session cookie. Now let's curl both the captcha code and the session cookie to captcha.php

```sh
$ curl -d captcha_challenge=d1ctXg --cookie "PHPSESSID=eh9nn1eko8aj2oe88d9oj542ec" http://167.99.129.209:8002/flag.php
```

Succes! Within the returned HTML we find

```
Nice evade! Take the flag: <b>NETON{7c49af83a2a68304273a8d330cebd93c}</b>
```

_Other combinations of captcha codes and PHP session ID cookies also work!_



### Grades - 486

![](Challenge%20Screenshots/Web%20-%20Grades.png)

So somebody hacked the final exam grades to inflate their own... up to 1337, alright. Well in that case it seems our friend 'nUK<,IDt-.bvKL|./EO$%;k}@\_' is the culprit. However, his name is encrypted...

Within the html file we find some obfuscated javascript

```js
function encrypt(_0x40a681) {
    var _0x16b830 = 0x20, _0x561689 = 0x5e, _0x3db275 = 0x0, _0x38a41d = '';
    for (var _0x278871 = 0x0; _0x278871 < _0x40a681['length']; _0x278871++) {
         _0x38a41d = _0x38a41d + String['fromCharCode']((_0x40a681['charCodeAt'](_0x278871) + _0x3db275) % _0x561689 + _0x16b830), _0x3db275 = _0x3db275 + _0x40a681['charCodeAt'](_0x278871);
    }
    return _0x38a41d;
```
We can de-obfuscate this simple function by replacing the nonsense variable names with names that make sense, and by inserting values wherever possible. After this, we find a more readable encrypt function
```js
function encrypt(input) {
    var output = '', c0 = 0;
    for (var i = 0; i < input['length']; i++) {
        output = output + String['fromCharCode']((input['charCodeAt'](i) + c0) % 94 + 32),
        c0 = c0 + input['charCodeAt'](i);
    }
    return output;
```
Because of the modulo in there, it might be a bit rough to reverse directly, so let's just brute-force it instead. We can do so by simply trying out a character and seeing if our trial flag matches with the given encrypted flag. I used the following script
```py
#!/usr/bin/env python3

# Encryption function
def encrypt(msg):
    out = ''; c0 = 0
    # Loop over input message
    for i in range(len(msg)):
        # Increment character ord value
        out += chr(((ord(msg[i]) + c0) % 94) + 32)
        # Increment addition variable
        c0 += ord(msg[i])
    # Return
    return out

# Character set
chars = list(r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_}!?.,')

# Trial flag and given mystery flag
flag = 'NETON{'
mystery = 'nUK<,IDt-.bvKL|./EO$%;k}@_'

i = 0 # iterator
while flag[-1] != '}':
    trial = encrypt(flag+chars[i])
    # Check if our encrypted trial flag matches the mystery one
    if trial == mystery[:len(flag)+1]:
        flag += chars[i]
        i = 0
    else:
        i += 1
    # If we run out of characters
    if i >= len(chars):
        print('Expand character list!')
        break
        
print('Gottem!:', flag)
```
Which neatly returns our desired flag
```
Gottem!: NETON{Y0u_4r3_0n_th3_t0p!}
```



## Stego Category

### Jungle Meeting - 50

![](Challenge%20Screenshots/Stego%20-%20Jungle%20Meeting.png)

The four provided image files represent four of the character of Disney's 'Jungle Book'. Nothing too fancy here, the image with Kaa has an interesting meta-tag
```
<photoshop:City>NETON{l00k_at_m3tadata}</photoshop:City>
``` 
which I found using by looking at the strings output
```sh
strings kaa.jpg | grep 'NETON'
```
*Note that piping the output to grep means you will filter out anything that does not contain 'NETON', but it could also lead you to miss other hidden information.*

### Seeing blurry - UNSOLVED (50)

![](Challenge%20Screenshots/Stego%20-%20Seeing%20blurry.png)

To be added later.



### Winter - 218

![](Challenge%20Screenshots/Stego%20-%20Winter.png)

At first glance the provided text file seems to only contain a simple quote. However, it seems like we can select much more than just the visible text. There are some hidden tabs and spaces as well! 

![](Solution%20Screenshots/Winter%20-%20Tabs%20and%20Spaces.png)

This kind of whitespace steganography is often referred to as 'snow', hence the title of the challenge. To recover the flag I used 'stegsnow' on Ubuntu,
```sh
stegsnow -C Winter.txt
```
and it revealed
```
NETON{wh1t3_spac3_tr1cks}
```

### Step by step - UNSOLVED (250)

![](Challenge%20Screenshots/Stego%20-%20Step%20by%20step.png)

We are giving the following, seemingly uinteresting picture.

![](Challenge%20Files/neton.bmp)

If we take a closer look, either with image processing software or a simple hexdump command, we see that there is a small variation in the pixel values. So let's try to inflate these variations. To do this, we can either use the magic selection tool (threshold: 0), the fill bucket (threshold: 0), or simply apply an auto-contrast. The latter option yields the following image

![](Solution%20Screenshots/StegSBS%20-%20Contrasted.png)

In which we can read the following code
```
n38f298hsjf
```
but no flag... :c


### Invisibility - UNSOLVED (500)

![](Challenge%20Screenshots/Stego%20-%20Invisibility.png)

So we are given a txt file with some lorem ipsum...
```
Lorem ipsum dolor ‍‍⁡‌⁤‌⁤‍⁡‌⁤‍‍⁢⁢‌⁡‍⁣⁢‍⁤⁢⁡‌‍‌⁤⁤⁢‍‌‍‌⁤‍‍‌⁡‍⁢⁡⁢⁢‍⁡‍‌⁢‌⁡⁢‍⁡‍‍⁢‍‌⁡‍⁡‍⁢⁡⁣⁢⁡⁢⁢⁤‍⁡⁢⁡⁢‍‍⁢‌⁤⁡⁢‍⁡⁢‍⁣‍‌‍⁢⁣⁣⁢⁡⁢‌⁢⁢⁢‌⁢‌sit amet consectetur adipiscing elit imperdiet leo, 
magnis non praesent diam sociosqu mi placerat pellentesque primis neque, 
congue cras pretium semper bibendum potenti natoque cum. 
Bibendum sed erat imperdiet habitant nostra dapibus massa parturient eros urna leo, 
ultrices felis curabitur potenti lobortis montes justo magnis suscipit ridiculus purus feugiat, 
eget lectus per mollis inceptos litora orci ante maecenas risus. 
Torquent suscipit sem ridiculus cubilia a id habitant consequat ad laoreet blandit sollicitudin, 
lacus imperdiet nascetur fringilla neque felis natoque nulla ac aliquet mus.
```

When I pasted it into Python, I was met by a little surprise.

![](Solution%20Screenshots/LoremIpsum.png)

which, converted to bytes leaves us with

```
\u200d\u200d\u2061\u200c\u2064\u200c\u2064\u200d\u2061\u200c\u2064\u200d\u200d\u2062\u2062\u200c\u2061\u200d\u2063\u2062\u200d\u2064\u2062\u2061\u200c\u200d\u200c\u2064\u2064\u2062\u200d\u200c\u200d\u200c\u2064\u200d\u200d\u200c\u2061\u200d\u2062\u2061\u2062\u2062\u200d\u2061\u200d\u200c\u2062\u200c\u2061\u2062\u200d\u2061\u200d\u200d\u2062\u200d\u200c\u2061\u200d\u2061\u200d\u2062\u2061\u2063\u2062\u2061\u2062\u2062\u2064\u200d\u2061\u2062\u2061\u2062\u200d\u200d\u2062\u200c\u2064\u2061\u2062\u200d\u2061\u2062\u200d\u2063\u200d\u200c\u200d\u2062\u2063\u2063\u2062\u2061\u2062\u200c\u2062\u2062\u2062\u200c\u2062\u200c
```

Some zero-width steganography, huh. Checking numpy.unique(x, return_counts=True) tells us there are 6 different unicode values. 

```
array(['\u200c', '\u200d', '\u2061', '\u2062', '\u2063', '\u2064'], dtype='<U1'), array([17, 28, 18, 27,  5,  9], dtype=int64)
```

Although the length of the code is divisible by 8, I was unable to convert it to binary... Also interpreting it as some base-6 code did not reveal anything...



## OSINT Category

### Caesar's Secret - 163

![](Challenge%20Screenshots/OSINT%20-%20Caesar's%20Secret.png)

So it seems Brutus has taken over Caesar's Twitter account after the 'incident'. Nothing interesting, apart from the bottom comment...

![](Solution%20Screenshots/JC%20-%20Brutus.png)

Let's try to retrieve this by checking the waybackmachine. Aha, there is a snapshot from 19 feb, let's check it out!

![](Solution%20Screenshots/JC%20-%20Caesar.png)

His bio contains something noteworthy, 'HjqbxiPcndct'. Likely to be in Caesar shift. Yup, ROT15 reveals 'SubmitAnyone'. This allows us to open up a zip file the challenge gave us, it contains a txt file with

```
flag: 01001110 01000101 01010100 01001111 01001110 01111011 01001010 01110101 01101100 01101001 01110101 01110011 01000011 01100001 01100101 01110011 01100001 01110010 01111101
```
which, in binary, trivially translates to ASCII as
```
NETON{JuliusCaesar}
```



### Caputure The Flag - 436

![](Challenge%20Screenshots/OSINT%20-%20Capture%20The%20Flag.png)

We are given the following image, nothing more. However, the image has some obvious clues.

![](Challenge%20Files/location.png)

Aha, some chinese characters and what seems to be a big '2019'.

![](Solution%20Screenshots/Loc%20-%20CN2019.png)

A quick simple Google search 'CTF China 2019' brings us to Zhengzhou. Looking around a bit we quickly stumble upon the Zhengzhou Greenland Plaza, which matches the environment of the photo. They just left the most iconic landmark out of it :).

```
NETON{REAL_WORLD_CTF}
```



## Crypto Category

### PawN PawN - 188

![](Challenge%20Screenshots/Crypto%20-%20PawN%20PawN.png)

This challenge provides us with two files, an WAV sound file and a password protected zip file. The WAV file clearly contains morse code that says
```
the zip password is 75757575
```
With this, we unlock the zip file to find a txt file containing some weird codes.
```
8/1P4P1/1PP3P1/1P1P2P1/1P2P1P1/1P3PP1/1P4P1/8 w - - 0 1
8/1PPPPP2/1P6/1P6/1PPPPP2/1P6/1PPPPP2/8 w - - 0 1
8/1PPPPPP1/1PPPPPP1/3PP3/3PP3/3PP3/3PP3/8 w - - 0 1
8/1PPPPPP1/1P4P1/1P4P1/1P4P1/1P4P1/1PPPPPP1/8 w - - 0 1
8/1P4P1/1PP3P1/1P1P2P1/1P2P1P1/1P3PP1/1P4P1/8 w - - 0 1
5P2/3PP3/3P4/3P4/2PP4/3P4/3PP3/5P2 w - - 0 1
8/1PPPPPP1/1P6/1P6/1P6/1P6/1PPPPPP1/8 w - - 0 1
8/1P4P1/1P4P1/1PPPPPP1/1P4P1/1P4P1/1P4P1/8 w - - 0 1
8/1PPPPPP1/1P6/1P6/1PPPPPP1/1P6/1PPPPPP1/8 w - - 0 1
8/1PPPPPP1/1P6/1P6/1P6/1P6/1PPPPPP1/8 w - - 0 1
8/1P2P3/1P1P4/1PP5/1P1P4/1P2P3/1P3P2/8 w - - 0 1
8/8/8/8/8/8/1PPPPPP1/8 w - - 0 1
8/1P4P1/1PP2PP1/1P1PP1P1/1P1PP1P1/1P4P1/1P4P1/8 w - - 0 1
8/3PP3/2P2P2/1P4P1/1PPPPPP1/1P4P1/1P4P1/8 w - - 0 1
8/1PPPPPP1/1PPPPPP1/3PP3/3PP3/3PP3/3PP3/8 w - - 0 1
8/1PPPPP2/1P6/1P6/1PPPPP2/1P6/1PPPPP2/8 w - - 0 1
3P4/4PP2/5P2/5P2/5PP1/5P2/4PP2/3P4 w - - 0 1
```
I recognised this to be a kind of chess code to display board setups, and a quick Google search confirmed this. Every line represents a single chess board, with eight segments, separated by a '/', each with 8 spaces. The spaces can be empty, represented by the numbers, or occupied by a piece, in which case there is a 'P'.

If we create these boards, we find something peculiar... a flag!

![](Solution%20Screenshots/Pawn%20-%20Boards.png)

```
NETON{CHECK_MATE}
```


### Weak xor - 239

![](Challenge%20Screenshots/Crypto%20-%20Weak%20xor.png)

The challenge provides us with an XOR encoded flag in hex, and the code they used to encode it
```py
#!/usr/bin/python3
import os
flag = open('flag.txt', 'r').read().strip().encode()
key = os.urandom(6)
xored = b''
for i in range(len(flag)):
    xored += bytes([flag[i] ^ key[i % len(key)]])
print(f"Flag : {xored.hex()}")
```
So they used 6 random bytes as the XOR key... Well, time to brute-force our way to this key. 6 bytes is an incredibly short key length and can be cracked in no time. I made a simple Python script to do this.

```py
#!/usr/bin/env python3

# Encrypted flag
chex = '5bbed19a19234dcbf78a3e0b4abcb5e5330721a4b5a3322a7397b5a22a'
cbyt = cint.to_bytes(29,'big')
# Example flag
tag = b'NETON{'
# Final key
key = b''

# We know the length of the key is 6 bytes (!)
while len(key) < 6:
    # Loop over possible bytes
    for i in range(256):
        # Get the byte
        if i < 16:
            tryhex = bytes.fromhex('0'+hex(i)[2:])
        else:
            tryhex = bytes.fromhex(hex(i)[2:])
        # Create trial key
        trykey = key + tryhex
        # XOR encrypted flag bytes with trial key
        xor = b''
        for i in range(len(cbyt)):
            xor += bytes([cbyt[i] ^ trykey[i % len(trykey)]])
        # Check XOR result with example flag
        if xor[:len(key)+1] == tag[:len(key)+1]:
            key += tryhex
            break
# Print results
print(key)
print(xor)
```
which happily returns us our desired key and flag : )
```
b'\x15\xfb\x85\xd5WX'
b'NETON{X0r_iS_G00d_4_0verfl0w}'
```



### BritishScientific - 242

![](Challenge%20Screenshots/Crypto%20-%20BritishScientific.png)

This challenge is surprisingly straightforward, we are provided with the following quote in a txt file
```
Viewing the laws of the electric circuit from the point at which 
the labours of Ohm has placed us, there is scarcely any branch of 
experimental science in which so many and such various phenomena 
are expressed by formulae of such simplicity and generality...

QRRXDRPCKESRSNSWWY
```
Google tells us that the quote comes from Charles Wheatstone, who also invented the Playfair cipher! So the encrypted txt at the bottom is likely to be encoded in a playfair cipher. However, to decipher it, we need a 5x5 'key' matrix.

The challenge also tells us that 'He always signs with his name and surname...'. This led me to believe he used the matrix as follows
```
C H A R L
E S W T O
N B D F G
I K M P Q
U V X Y Z
```
Indeed he did as deciphering the code with the above 'key' matrix nicely gives us our flag
```
NETON{PLAYFAIRISTHEBESTX}
```


### Facts Br0! - 244

![](Challenge%20Screenshots/Crypto%20-%20Facts%20Br0!.png)

The challenge provides us a long integer as flag and a public key in a PEM file format. Ding ding ding, RSA alert!

The public key is too short, which allows us to crack it! The PEM file contains the public parts of RSA cryptography, namely 'n' and 'e', encoded in base64. _If you do not recognise these variables it might be nice to read up a little on RSA cryptography, the encoding itself is fairly straightforward._
```
-----BEGIN PUBLIC KEY-----
MDEwDQYJKoZIhvcNAQEBBQADIAAwHQIWAN4vdj9ZJ337BgYayd9cb2tF0QoJAwID
AQAB
-----END PUBLIC KEY-----
```
However (!), I did not realise that the PEM file format has some additional encoding elements such that you cannot simply convert the two base64 strings to integers and call it a day. I naively found
```
n = 74174491295044795964181854285195495718964397093731395961824370391827799637138867436334319587298835673227084716446
e = 65537
```
Although the 'e' has a commonly used value, the 'n' does not factor nicely into two primes...  So I used a Python library to do it for me properly
```py
from Crypto.PublicKey import RSA

f = open('../public.pem')
key = RSA.importKey(f.read())
print(key.n)
print(key.e)
```
which gave the public RSA elements as
```
n = 324724323060034233289551751185171379596941511493891
e = 65537
```
This time around, the 'n' actually factors nicely (using factordb) into the two primes
```
p = 25001545096244227516337
q = 12988170203481337861511552243
```
Using these and an Euler inverse function, I was able to derive the private key, the private RSA component 'd' to be
```py
def eulinv(x, m):
    a, b, u = 0, m, 1
    while x > 0:
        q = b // x # integer division
        x, a, b, u = b % x, u, x, a - q * u
    if b == 1:
        return a % m
    else:
        return None

d = eulinv(key.e,(p-1)*(q-1)); print(d)
```
```
323728403366806485896597412434387317854754383435009
```
Now we are able to decrypt the provided 'flag' using m = pow(c, d, n). In Python
```py
# Get message from encrypted flag
pow(flag,d,key.n)
# Turn integer into binary (0 added in front )
mbit = bin(26634179113006760524799996616930504110973)[2:]
# Pad with 0s in front to make sure it is in byte format
while len(mbit) % 8 != 0:
    mbit = '0' + mbit
# Bytes -> ASCII
m = ''.join([chr(int(mbit[i:i+8],2)) for i in range(0,len(mbit),8)])
print(m)
```
which happily returns
```
NETON{3z_F4ct0rs}
```


### Not Morse - UNSOLVED (249)

![](Challenge%20Screenshots/Crypto%20-%20Not%20Morse.png)

To be added later.



### RSA... no primEs, no problEm - 500

![](Challenge%20Screenshots/Crypto%20-%20RSA...%20no%20primEs,%20no%20problEm.png)

Another RSA challenge! But this time, the numbers are substantially bigger :c
The challenge provided us with an encrypted flag, public component 'n' and phi(n).
```
ciphertext = 4803486620985796010075216068877609455871383897640323954843756796800173149437251687733347664192572117005126499615124844328373675595265268457208063073063362666296732488986704487923437514493478565848183238995971938189096941670496102571815095353480403637698691345512049769785098395967252710672386044217321956851169565136849198146328368935680111095304534054866044961612091553409953330964655033765906224029250112390318273915843693588625005937293557999267431911756800430138791635421069977

n = 14243345730631857177062718957286458295344875661901393577745661535671731182469817848719170841079560124200634261984946297612967896241817034756539493737449488275719622652895734552547316101216424483474862911698249829751472886166538635034783417821365701447757997511751589750140515711946334390780520161779493842518544535120769290658501358009251342540552113786916173497963072314840842823842101868020523794699586378835932131301349396908327821519900075538365718554522120543219846421981750367

phi(n) = 14243345730631857177062718957286458295344875661901393577745661535671731182469817848719170841079560124200634261984946297612967896241817034756539493737449488275719622652895734552547316101216424483474862911698249829751472886166538635034783417813763312676513662599184910888148679300475389478079315732593163367616609472566305826936916314217502538829723285645468007039496239828709581450294608647853663479553932636891934128772821535614594114832137463330741228691150099997156720502848674840
```
Note that this time, 'n' is too large for us to factorise it. Even factordb cannot help us here. However, we are given a phi(n)... which we can use to derive the private component 'd' using d = \~e mod phi(n). There is one catch though, we do not know 'e'... Luckily, for computational reasons, 'e' is usually not too big and we know it must be a coprime of phi(n), so we can use our previously used Euler inverse function. Now we just brute-force our way by incrementing a test value for 'e' and checking whether or not the output makes sense :). To do this, I used some Python again (I left out the flag, n, phi_n and eulinv() definitions)
```py
itere = 3 # trial 'e'
while itere < int(1e6):
    # Euler inverse (see previous RSA challenge)
    d = eulinv(itere,phi_n)
    # If d returned an actual value (i.e. e is a coprime)
    if not d is None:
        # Set RSA components
        e = itere
        d = eulinv(e, phi_n)
        # Get message
        mint = pow(flag,d,n)
        mbit = bin(mint)[2:];
        while len(mbit)%8 != 0:
            mbit = '0' + mbit
        m = [int(mbit[i:i+8],2) for i in range(0,len(mbit),8)]
        # Check whether all message characters are within common ASCII range
        if (min(m) >= 33) & (max(m) <= 125):
            flag = ''.join([chr(i) for i in m])
            print(e, flag)
            break
    # Increment 'e'
    itere += 1
```
After a few seconds of thinking, it finds our flag at an 'e' value of 15049!
```
NETON{RSA_1s_r34lly_fun!}
```



## Coding Category

### Run Run Run - 215

![](Challenge%20Screenshots/Coding%20-%20Run%20Run%20Run.png)

So this site shows a simple equation and challenges us to send the answer, encoded in an MD5 hash, before the time runs out. Doing it by hand is not an option... Furthermore, it seems like the equation is always of the form A * B - C, were all of the variables are 3-digit integers. So we can just set-up an easy static Python script, using the requests and hashlib libraries. _Note that the equation on the site does not refresh upon request, but on a small time interval. This allows us to first request the page (GET) and then send the answer back to the server (POST), as long as we supply it our cookie as well (!)_
```py
#!/usr/bin/env python

# Imports
import requests
import hashlib

# Headers
headers = {
	"Connection": "keep-alive",
	"Cookie": "PHPSESSID=mfn12kjrqc85sb83rf0v0dm5af"
}

# Request page
push = requests.get("http://167.99.129.209:7777/index.php",headers=headers)

# Extract the equation 
strsum = push.text[196:211]
print strsum

# Compute the answer of the equation
res = int(strsum[0:3]) * int(strsum[6:9]) - int(strsum[12:15])
print res

# Get the MD5 hash
md5 = hashlib.md5(str(res)).hexdigest()
print md5

data = {
	"md5": md5
}

# Send it back
push = requests.post("http://167.99.129.209:7777/index.php",headers=headers,data=data)

print push.text
```
Within the printed HTML we find our flag, along with a nice compliment
```
Nice script! Take your flag: NETON{ScR1pT1ng_5a9522b8a3a9d3e2a3bf373803fa8e6c}
```



### Step by step - 239

![](Challenge%20Screenshots/Coding%20-%20Step%20by%20step.png)

So... they leave us to guess a password once again. More specifically, we are supposed to just guess the flag. To help us a bit, they tell us whenever we send in *part* of the flag. This makes it just another simple brute-force challenge through trail and error. Here is the Python script I used
```py
#!/usr/bin/env python

# Imports
import requests

# All ASCII characters
chrs = [chr(i) for i in range(256)]
# All characters that returned 'getting closer'
chrs = '0134:ABCDEFGLNOSTU_abcdefghilmnorstuv{}' 

#  Trial flag
flag = "S"

i = 0
while i<len(chrs):
	# Create new flag to try
	new_flag = chrs[i] + flag 
	# Push the flag to the website
	push = requests.post("http://167.99.129.209:7788/index.php",data={'flag':new_flag})
	# Check return html
	pt = push.text[50:80]
	# Check for return
	print new_flag, pt
	if pt[0] == 'H':
		flag = new_flag
		i = 0
		print flag
	elif pt[0] == 'S':
		i += 1
	else:
		print 'Found it?:', flag
		break

# Print found result
print flag
```

With some tempering of the initial trial flag, I managed to get back

```
SuBsTr1nGs_4r3_FuN_4nD_C0uLD_b3_vUln3rAbL3
```

which, submitted as NETON{SuBsTr1nGs_4r3_FuN_4nD_C0uLD_b3_vUln3rAbL3}, turned out to be correct. : )



### SecretMessage - 247

![](Challenge%20Screenshots/Coding%20-%20SecretMessage.png)

So we already have our flag
```
̜͍͑͋˻͒̽͊˼˻͇̽̓˻͍͉̼͍̀͌˻͑͂̇˻͉͓͍͂˻͇̽̓̀˻͉͉̀͌̕ͅ˻̢̜̭̝̜͖̼̺͍̺͕͇̺͎̼̌͋̎͋̋͌̀̌̎͌͘
```
but it looks kind of weird... Luckily, they tell us how they encrypted it
```py
def encrypt(pwd, s):
	n = 0
	for c in pwd: n += ord(c)
	lc = string.ascii_lowercase
	uc = string.ascii_uppercase
	tcyph = str.translate(s, str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13]))
	fcyph = ''
	for c in tcyph: fcyph += chr(ord(c) + n)
	return fcyph
```

Seems we have a simple translation mapping, by swapping the halves of the lower- and uppercase alphabet, and an addition factor. This factor is made by adding the ord values of all charaters in a password. Knowing this factor is zero at the beginning we can find it by guessing the first letter to be 'N'. Using a simple Python script
```py
# Imports
import string

lc = string.ascii_lowercase
uc = string.ascii_uppercase
# Alphabet in, alphabet out
dic_in = lc + uc
dic_out = lc[13:] + lc[:13] + uc[13:] + uc[:13]
# Offset guess
n = 731
# Flag
flag = [chr(ord(i)-n) for i in list('̜͍͑͋˻͒̽͊˼˻͇̽̓˻͍͉̼͍̀͌˻͑͂̇˻͉͓͍͂˻͇̽̓̀˻͉͉̀͌̕ͅ˻̢̜̭̝̜͖̼̺͍̺͕͇̺͎̼̌͋̎͋̋͌̀̌̎͌͘')]
# Loop over flag 
for i,char in enumerate(flag):
    if char in lc+uc:
        flag[i] = dic_in[dic_out.index(char)]

print(''.join(flag))
```
we find
```
Nice job! you earned it, take your award: NETON{n1c3_c0de_my_fr13nd}
```
Note that we got lucky. I guessed 'N' to be the first letter because of the flag format (NETON{}), however it did not start with the flag. Second option would have been to guess the final character to be '}', so we would have found it either way :).


## Forensics Category

### Infiltration - 183

![](Challenge%20Screenshots/Forensics%20-%20Infiltration.png)

We have a capture.pcapng, so let's fire up that WireShark! We find some connections to various websites, of which there are some POSTS to http://www.eljoselillo7.tech/action.php as well. Seems like our 'hacker' tried an invalid username and password combo before submitting a correct one.

![](Solution%20Screenshots/INF%20-%20Login.png)

![](Solution%20Screenshots/INF%20-%20Try1.png)

![](Solution%20Screenshots/INF%20-%20Try2.png)

So we can login ourselves now on the website, or just retrieve the flag from the OK the server send back to our 'hacker' buddy. :)

![](Solution%20Screenshots/INF%20-%20Flag.png)

```
NETON{N1c3_4n4l1s1s!}
```

### Picasso01 - 225

![](Challenge%20Screenshots/Forensics%20-%20Picasso01.png)

Binwalking through the provided file we find there is a secret.txt inside, interesting. Using strings and grep
```sh
$ strings dump.raw | grep "NETON"
```
we quickly find the flag
```
NETON{7h15_w1ll_no7_b3_7h3_ncl}
```



### Lost in Lab - UNSOLVED (479)

![](Challenge%20Screenshots/Forensics%20-%20Lost%20in%20Lab.png)

We got some kind of disk image. Binwalking it reveals a whole bunch of stuff, probably not the right way to do this, but hey ¯\\\_(ツ)\_/¯. Anyway, we find a password protected zip file with LabPractical.xlsx, which looks promising. But I do not know the password, nor could I find it within any of the files. Although I did find out about this... Flavio Oliveira, which sadly did not turn out to be the answer :c.

![](Solution%20Screenshots/LIL%20-%20Flavio.png)



## Reversing Category

### File Bomb - UNSOLVED (475)

To be added later.

## Misc Category

### Inception - 183

![](Challenge%20Screenshots/Misc%20-%20Inception.png)

Fairly straightforward challenge. It provides us a QR-code, which leads to a mega.nz link containing a txt file with xml data encoded in base64

![](Challenge%20Files/qr.png)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<svg version="1.1" baseProfile="tiny" xmlns="http://www.w3.org/2000/svg" width="200" height="200">
<rect shape-rendering="optimizeSpeed"  x="0" y="0" width="200" height="200" fill="white" />
<rect shape-rendering="optimizeSpeed"  x="12" y="12" width="7" height="7" fill="black" />

...

<rect shape-rendering="optimizeSpeed"  x="180" y="180" width="7" height="7" fill="black" /></svg>
```

This shows us another QR code...

![](Challenge%20Files/qr2.png)

Scanning it reveals the flag
```
NETON{ThatsRoughBuddy}
```



### Photogra.fy - 227

![](Challenge%20Screenshots/Misc%20-%20Photogra.fy.png)

The Twitter feed contains a link to a website. Although this website itself does not seem too interesting, it refers to a login.js file which contains the following
```js
function validate() {
    console.log(String['\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65'](0x4e, 0x45, 0x54, 0x4f, 0x4e, 0x7b, 0x4e, 0x61, 0x54, 0x69, 0x30, 0x6e, 0x61, 0x31, 0x5f));
}
```
Which, if we convert the bytes to ASCII, would print
```
NETON{NaTi0na1_
```
Mmh... so not the end of the story it seems... Maybe it has something to do with national parks, or a national building, considering the images on the website. Yup, the final image contains the second part of the flag as metadata.
```
_CiB3rL4gu3}
```
In the end, it was referring to something completely different, the National Cyber League. Well whatever, we got what we came for :).
```
NETON{NaTi0na1_CiB3rL4gu3}
```


### Kasiski the magician - UNSOLVED (235)

![](Challenge%20Screenshots/Misc%20-%20Kasiski%20the%20magician.png)

To be added later.



### MathTomata - 245

![](Challenge%20Screenshots/Misc%20-%20MathTomata.png)

So a 'DFA', or Deterministic Finite Automaton, is a kind of finite-state machine. This means we can put in some input and out comes something depending on its structure. A quick read on Wikipedia explain enough in order to figure this puzzle out. We are given the following information about our DFA
```
Parameter 		Meaning						Value
------------------------------------------------------------------
Q 				States / nodes				Q0 through Q9
Σ				Possible messages			{d,m,n,p,s,t,0,1,3}
δ 				Transition function 		_see Table below_
q0 				Initial state 				Q0
F 				Accept / final state 		Q9
```
```
  δ	 |	d 	m 	n 	p 	s 	t 	0 	1 	3
------------------------------------------------------------------
 Q0  |						Q1
 Q1  |									Q2
 Q2  |	Q3
 Q3  |		Q8		Q4
 Q4  | 							Q5
 Q5  | 			Q7 					Q6
 Q6  | 					Q4
 Q7  | 									Q2
 Q8  | 									Q9
 Q9  |
```
In other words, we can picture this as a collection of 10 nodes, or stepping stones, that are connected to each other according to the transition function. For every step we take, we pick up one of the possible messages in order to string our flag together. Furthermore, we need to start at Q0, end at Q9, and take exactly 13 steps (as denoted in the challenge description). A sketch of this system is given below.

![](Solution%20Screenshots/DFA%20-%20Sketch.png)

Following the stepping stones, we can derive the following flag
```
NETON{t3dp01s0n3dm3}
```
F.   o7



### Gotta catch em flag - 248

![](Challenge%20Screenshots/Misc%20-%20Gotta%20catch%20em%20flag.png)

With such a title, I'm expecting some kind of link to Pokémon, which would be amazing :). Anyway, we are given a simple JPG image, nothing suspicous so far. However, a quick binwalk tells us otherwise
```sh
$ binwalk NETON.jpg 
```
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
476           0x1DC           Copyright string: "Copyright (c) 1998 Hewlett-Packard Company"
122067        0x1DCD3         RAR archive data, version 5.x

```
Mmh... a RAR file attached to the image, okay. Let's extract it. Now we find a File.zip which is password protected :c, and a folder called 'EmuCR-no$gba-w'. An GBA emulator of some sorts??? Are we actually going to play Pokémon, that would be great. Hey, there's a Pokémon Fire Red save file in here. After sneaking in a ROM file, and booting up the emulator, we are greeted by a lovely surprise

![](Solution%20Screenshots/Catch%20-%20Save.png)

![](Solution%20Screenshots/Catch%20-%20Team.png)

Alright, sure thing! Let's look at our box.

![](Solution%20Screenshots/Catch%20-%20Guacamole.png)

![](Solution%20Screenshots/Catch%20-%20Fries.png)

So the password for the zip is '334355GUACAMOLEFRIES', lovely! In it, we find Flag.txt containing our flag safely encoded in base64... but not for long!
```
NETON{7h3_r34l_fl46_15_h3r3}
```


# Thanks once again to those at NetOn for organising this wonderful CTF!