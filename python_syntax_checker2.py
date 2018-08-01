#!/usr/bin/env python
"""Emulate python -m py_compile, but without generating the bytecode file."""

import sys

for filename in sys.argv[1:]:
    with open(filename, 'r') as handle:
        sys.stderr.write('*** %s ***\n' % filename)
        source = handle.read() + '\n'
        compile(source, filename, 'exec')

sys.stderr.write('=== Done ===\n')
