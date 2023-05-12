#!/usr/bin/env python3
import sys

def name(i):
    if i < 0x21:
        return \
            ['NUL ', 'SOH ', 'STX ', 'ETX ', 'EOT ', 'ENQ ', 'ACK ', 'BEL ',
             'BS  ', 'HT  ', 'LF  ', 'VT  ', 'FF  ', 'CR  ', 'SO  ', 'SI  ',
             'DLE ', 'DC1 ', 'DC2 ', 'DC3 ', 'DC4 ', 'NAK ', 'SYN ', 'ETB ',
             'CAN ', 'EM  ', 'SUB ', 'ESC ', 'FS  ', 'GS  ', 'RS  ', 'US  ',
             'SPC '][i]
    elif i == 0x7f:
        return 'DEL '

for i in range(256):
    if (
        chr(i)
        in {
            "!",
            "#",
            "$",
            "%",
            "&",
            "'",
            "*",
            "+",
            "-",
            ".",
            "^",
            "_",
            "`",
            "|",
            "~",
        }
        or '0' <= chr(i) <= '9'
        or 'A' <= chr(i) <= 'Z'
        or 'a' <= chr(i) <= 'z'
    ):
        sys.stdout.write(f'1 /* {chr(i)}    */, ')
    elif 0x21 <= i < 0x7F:
        sys.stdout.write(f'0 /* {chr(i)}    */, ')
    elif i >= 0x80:
        sys.stdout.write(f'0 /* {hex(i)} */, ')
    else:
        sys.stdout.write(f'0 /* {name(i)} */, ')
    if (i + 1)%4 == 0:
        sys.stdout.write('\n')
