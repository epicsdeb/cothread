# This file is part of the Diamond cothread library.
#
# Copyright (C) 2007 James Rowland, 2007-2012 Michael Abbott,
# Diamond Light Source Ltd.
#
# The Diamond cothread library is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the License,
# or (at your option) any later version.
#
# The Diamond cothread library is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#
# Contact:
#      Dr. Michael Abbott,
#      Diamond Light Source Ltd,
#      Diamond House,
#      Chilton,
#      Didcot,
#      Oxfordshire,
#      OX11 0DE
#      michael.abbott@diamond.ac.uk

# As discovering the location of libca (or whatever it's called in this
# particular system) is somewhat involved the work is gathered into this file.
# This file can also be run as a standalone script to discover the path to
# libca.

# Original version replaced by Debian specific version
# Problems with library detection should therefore be
# reported to mdavidsaver@bnl.gov

from __future__ import print_function

import ctypes
import platform
import os

load_library = ctypes.cdll.LoadLibrary
system = platform.system()

if system!='Linux':
    raise OSError('This version of cothread has been patched in a way which only works on Linux')


# Known to be ABI compatible SO names for libca
# Extend the list of directories search in the usual way (eg. LD_LIBRARY_PATH)
libnames = [
	'libca.so.3.14.11',
	'libca.so.3.14.12',
	'libca.so.3.14.12.3',
]
# Allow user to provide additional names (eg "libca.so.3.15:libca.so.3.15.1")
# These are checked first.
libnames = filter(len, os.environ.get('LIBCA_NAMES',"").split(':') ) + libnames

def findca():
    for name in libnames:
        try:
            lib = load_library(name)
            return (lib, name)
        except OSError:
            pass # file didn't exist
    raise OSError("""Couldn't find libca.
Looked for: %s
If libca is installed in an uncommon location try setting LD_LIBRARY_PATH
in your environment.  If your libca has a different (or no) SONAME then
Set LIBCA_NAMES to a colon seperated list of SONAMEs.
"""%(', '.join(libnames)))

libca, libca_name = findca()

if __name__=='__main__':
    print("Found libca as: '%s'"%libca_name)
