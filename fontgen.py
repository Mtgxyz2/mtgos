#!/usr/bin/env python3
"""
Generates a kernel/src/include/genfont.h from stdin
"""

import binascii
import sys
f = open("kernel/src/include/genfont.h", "w")
f.write("//Generated by fontgen.py\n")
lines = sys.stdin.readlines()
font = {}
#font -> unicode, font pair
print("Parsing")
for l in lines:
    font[int.from_bytes(binascii.unhexlify(
        l[:4]), byteorder="big")] = binascii.unhexlify(l[5:-1])


fontbytes = bytearray()
widths = []
offs = []

for i in range(65536):
    if not i in font:
        widths.append(0)
        offs.append(None)
    else:
        fo = font[i]
        widths.append(len(fo)//2)
        offs.append(len(fontbytes))
        fontbytes += font[i]
print("Writing")
f.write("char font_widths[] = {\n")
for i,width in enumerate(widths):
    if not i % 32:
        f.write("    ")
    f.write(str(width)+",")
    if i % 32 == 31:
        f.write("\n")
f.write("};\n")
f.write("char font_data[] = {\n")
for i,c in enumerate(fontbytes):
    if not i % 32:
        f.write("    ")
    if c < 0x80:
        f.write(hex(c)+", ")
    else:
        f.write("(char)"+hex(127-c^0x7F)+", ")
    if i % 32 == 31:
        f.write("\n")
f.write("\n};\n")
f.write("char *font_ptr[] = {\n")
for i,off in enumerate(offs):
    if not i % 8:
        f.write("    ")
    if off is None:
        f.write("0,")
    else:
        f.write("&(font_data["+hex(off)+"]),")
    if i % 8 == 7:
        f.write("\n")
f.write("};")
print("done.")
