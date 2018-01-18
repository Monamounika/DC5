#!/usr/bin/env python

# example string: 110536896.20480.0000

import struct
import sys

if len(sys.argv) != 2:
        print "Usage: %s encoded_string" % sys.argv[0]
        exit(1)

encoded_string = sys.argv[1]
print "\n[*] String to decode: %s\n" % encoded_string

(host, port, end) = encoded_string.split('.')

(a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]


print "[*] Decoded IP: %s.%s.%s.%s.\n" % (a,b,c,d)
Then when you run the program:

root@bt:~/bigip# python bigip.py 110536896.20480.0000

[*] String to decode: 110536896.20480.0000

[*] Decoded IP: 192.168.150.6.

root@bt:~/bigip#
