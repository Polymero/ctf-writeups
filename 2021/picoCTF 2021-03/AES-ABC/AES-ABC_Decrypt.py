#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes, bytes_to_long
import math

BLOCK_SIZE = 16
UMAX = int(math.pow(256, BLOCK_SIZE))

def remove_line(s):
    # returns the header line, and the rest of the file
    return s[:s.index(b'\n') + 1], s[s.index(b'\n')+1:]


def parse_header_ppm(f):
    data = f.read()

    header = b""

    for i in range(3):
        header_i, data = remove_line(data)
        header += header_i

    return header, data

with open("body.enc.ppm",'rb') as f:

	fhead, fdat = parse_header_ppm(f)

print(fhead)