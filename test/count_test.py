from fol_session import *

print 'Relation, no count check'
print P().pform()
print P(x).pform()
print P(x,y).pform()
print P(x,y,z).pform()
print

print 'Function, no count check'
print f().pform()
print f(x).pform()
print f(x,y).pform()
print f(x,y,z).pform()
print

print 'InfixRelation, correct count 2'
print Equal(x,y).pform()
print

print 'InfixRelation, wrong count, 3 not 2'
print 'Equal(x,y,z)'
try: Equal(x,y,z)
except: print '... caught exception ...'
print

print 'InfixRelation, wrong count, 1 not 2'
print 'Equal(x)'
try: Equal(x)
except: print '... caught exception ...'
print

print 'InfixRelation, wrong count, 0 not 2'
print 'Equal()'
try: Equal()
except: print '... caught exception ...'
print

print 'PrefixLogical, correct count 1'
print Not(p).pform()
print

print 'PrefixLogical, wrong count 0 not 1'
print 'Not()'
try: Not()
except: print '... caught exception ...'
print

print 'PrefixLogical, wrong count 2 not 1'
print 'Not(p,q)'
try: Not(p,q)
except: print '... caught exception ...'
print

print 'InfixLogical, correct count 2'
print And(p,q).pform()
print

print 'InfixLogical, wrong count, 3 not 2'
print 'And(p,q,r)'
try: And(p,q,r)
except: print '... caught exception ...'
print

print 'InfixLogical, wrong count, 1 not 2'
print 'And(p)'
try: And(p)
except: print '... caught exception ...'
print

print 'InfixLogical, wrong count, 0 not 2'
print 'And()'
try: And()
except: print '... caught exception ...'
print

print 'Quantifer, correct count 2'
print A(x,P(x)).pform()
print

print 'Quantifier, wrong count, 3 not 2'
print 'A(x,y,P(x,y))'
try: A(x,y,P(x,y))
except: print '... caught exception ...'
print

print 'Quantifier, wrong count, 1 not 2'
print 'A(x)'
try: A(x)
except: print '... caught exception ...'
print


print 'New, correct count 1'
print New(x).pform()
print

print 'New, wrong count 2 not 1'
print 'New(x,y)'
try: New(x,y)
except: print '... caught exception ...'
print

print 'Let, correct count 2'
print Let(x,P(x)).pform()
print

print 'Let, wrong count, 3 not 2'
print 'Let(x,y,P(x,y))'
try: Let(x,y,P(x,y))
except: print '... caught exception ...'
print


# Uncomment to see traceback
# print 'InfixLogical, wrong count, 3 not 2, uncaught exception'
# And(p,q,r)


