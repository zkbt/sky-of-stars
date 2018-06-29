'''
The Friendly Stars (tfs) is a toolkit for managing catalogs of stars,
including tools for querying popular astronomy archives.
'''

__version__ = '0.0'

# specify whether we're calling this from within setup.py
try:
    __SKYOFSTARSSETUP__
except NameError:
    __SKYOFSTARSSETUP__ = False

if not __SKYOFSTARSSETUP__:
    # (run this stuff if it's not form within setup.py)
    pass
