#!/usr/bin/env python3
#
# Read json strings from a curl response, and pretty print them out.
# Ignore anything that doesn't convert to json.

import json
import sys

for line in sys.stdin:
    try:
        blob = json.loads(line.rstrip())
        try:
            print(json.dumps(blob, sort_keys=True, indent=4))
        except:
            print("Skipping blob: %s" % blob)
    except:
#        print("Skipping line: %s" % line.rstrip())
        pass

