#!/usr/bin/env python2

# https://codegolf.stackexchange.com/questions/170398/primality-testing-formula

import re
for n in range(2,100):
    if not re.match(r'(11+?)\1+$','1'*n):
        print n
