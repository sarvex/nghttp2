#!/usr/bin/env python3
import sys

def name(i):
    if i < 0x20:
        return \
            ['NUL ', 'SOH ', 'STX ', 'ETX ', 'EOT ', 'ENQ ', 'ACK ', 'BEL ',
             'BS  ', 'HT  ', 'LF  ', 'VT  ', 'FF  ', 'CR  ', 'SO  ', 'SI  ',
             'DLE ', 'DC1 ', 'DC2 ', 'DC3 ', 'DC4 ', 'NAK ', 'SYN ', 'ETB ',
             'CAN ', 'EM  ', 'SUB ', 'ESC ', 'FS  ', 'GS  ', 'RS  ', 'US  '][i]
    elif i == 0x7f:
        return 'DEL '

for i in range(256):
    if chr(i) == ' ':
        sys.stdout.write(f'{i} /* SPC  */, ')
    elif chr(i) == '\t':
        sys.stdout.write(f'{i} /* HT   */, ')
    elif 'A' <= chr(i) <= 'Z':
        sys.stdout.write(f"{i - ord('A') + ord('a')} /* {chr(i)}    */, ")
    elif 0x21 <= i < 0x7F:
        sys.stdout.write(f'{i} /* {chr(i)}    */, ')
    elif i >= 0x80:
        sys.stdout.write(f'{i} /* {hex(i)} */, ')
    elif i == 0:
        sys.stdout.write(f'{i} /* NUL  */, ')
    else:
        sys.stdout.write(f'{i} /* {name(i)} */, ')
    if (i + 1)%4 == 0:
        sys.stdout.write('\n')
