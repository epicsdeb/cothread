#!/usr/bin/python

'''Channel Access Get Structure'''

import require
from cothread.catools import *
from cothread import Timedout


# get failed - raise exception
try:
    result = caget('this_is_not_a_channel_name', timeout = 1)
except Timedout:
    print 'caget timed out'

# get failed on one channel - raise exception
try:
    results = caget(
        ['this_is_not_a_channel_name', 'SR21C-DI-DCCT-01:SIGNAL'], timeout = 1)
except Timedout:
    print 'caget timed out'


# get failed on one channel - don't raise exception, return partial result
results = caget(
    ['this_is_not_a_channel_name', 'SR21C-DI-DCCT-01:SIGNAL'],
    timeout = 1, throw = False)
for r in results:
    if r.ok:
        print r.name, 'ok'
    else:
        print r.name, str(r)