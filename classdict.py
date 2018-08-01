#!/usr/bin/env python3
"""Demo a class based on a dict"""

class MyDict(dict):
    def __init__(self, init=None, *args, **kw):
        """Create the initial dict, possibly passed in.

        Parameters:
            init: Initialise with this dict
        """
        if init:
            self.update(init)
        super().__init__(*args, **kw)

x = MyDict()
x[1] = 'One'
x[2] = 'Two'

for key, value in x.items():
    print("x.[%s]=%s" % (key, value))

print("Done!")
