"""
Tree tests, check arguments
"""

from tree_session import *

# syntax checks

print 'Path, wrong argument count'
print "Path('1001','0101')"
try: Path('1001','0101')
except: print '... caught exception ...'
print

print 'Path, argument not string'
print 'Path(x)'
try: Path(x)
except: print '... caught exception ...'
print

print 'Path, argument not just 0,1'
print "Path('1010102')"
try: Path('1010102')
except: print '... caught exception ...'
print

print 'Proof step contains string, not formula'
print "check_proof([('101010',given)])"
print check_proof([('101010',given)])

