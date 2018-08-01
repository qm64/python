#!/usr/bin/env python

# Convert an iterator that returns too much, into
# a generator that returns chunks of 1000

def batched(iterator, size):
    """Generator to return elements of an iterator in chunks of size,
    for effecient processor/memory usage.
    
    Parameters:
        iterator: an iterator
        size: number of chunks to yield each time
        
    Returns, as a list:
        subrange: the start and stop index of the oritinal iterator, as a list
        batch: list of elements
    """
    stop = 0
    for batch in [iterator[0:1000]]:
        start = stop
        stop = stop + len(batch)
        yield [start, stop], batch


    