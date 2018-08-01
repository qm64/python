#!/usr/bin/env python
"""Generic tool for dealing with JSON"""

import sys
import pprint
import json
import pytest

pp = pprint.PrettyPrinter(indent=4).pprint


def list_keys(data, *args, print_it=True, **kwargs):
    """List all keys at all levels

    Args:
        data: A dict or list of dicts
    """
    assert isinstance(data, (dict,list)), "data is not a dict or list"
    if not isinstance(data, list):
        data = [data]

    if 'key_list' not in list_keys.__dict__:
        list_keys.key_list = {}

    for blob in data:
        assert isinstance(blob, dict), "blob is not a dict, but a {}, ({})".format(type(blob), pp(blob))
        for k in blob.keys():
            if k not in list_keys.key_list:
                list_keys.key_list[k] = 0
            list_keys.key_list[k] += 1
            if isinstance(blob[k], dict):
                list_keys(blob[k], print_it=False)

    if print_it:
        print("Key counts:")
        for k in sorted(list_keys.key_list, key=str.lower):
            print("    {}: {}".format(k, list_keys.key_list[k]))

def some_keys(data, mykeys):
    """Print the values of given keys/indexes from a dict or list (top level only)

    Args:
        mykeys: key or list of keys (or indexes) in data
        data: A Python dict or list (list keys must be integers)
    """
    if not isinstance(mykeys, list):
        mykeys = [mykeys]

    for blob in data:
        printed = False
        for k in mykeys:
            if k in blob:
                print("{}=>{} ".format(k,blob[k]), end='')
                printed = True
        if printed:
            print("")

if __name__ == '__main__':

    doit = some_keys
    keyit = ['messageType','protocol']
    if sys.stdin.isatty:
        for file_arg in sys.argv[1:]:
            with open(file_arg) as json_file:
                data = json.load(json_file)
            doit(data, keyit)
    else:
        json_string = sys.stdin.readlines()
        data = json.load(json_string)
        process(data, keyit)

    sys.exit
