"""
First uncaught exception will crash the script, code that follows will not run.
Therefore all but last test case is wrapped in try: ...
Remove 'try:' from any test case to see its traceback
"""

from fol_session import *

print 'Relation, correct argument types'
print P(x,y,z).pform()
print

print 'Relation, wrong argument 1 type, Letter not Variable'
print 'P(x,p,z)'
try: P(x,p,z)
except: print '... caught exception ...'
print


print 'Function, correct argument types'
print f(x,y,z).pform()
print

print 'Function, wrong argument 1 type, Letter not Variable'
print 'f(x,p,z)'
try: f(x,p,z)
except: print '... caught exception ...'
print

print 'InfixRelation, correct argument types'
print Equal(f(a,b,c),g(x,y,z)).pform()
print

print 'InfixRelation, wrong argument 0 and 1 types, Formulas not Terms'
print 'Equal(Impl(p,q),Or(Not(p),q))'
try: Equal(Impl(p,q),Or(Not(p),q))
except: print '... caught exception ...'
print

print 'PrefixLogical, correct argument types'
print Not(q).pform()
print

print 'PrefixLogical, wrong argument type, a is Term not Formula'
print 'Not(a)'
try: Not(a)
except: print '... caught exception ...'
print

print 'InfixLogical, correct argument types'
print And(p,q).pform()
print

print 'InfixLogical, wrong argument 1 type, a is Term not Formula'
print 'And(p,a)'
try: And(p,a)
except: print '... caught exception ...'
print

print 'Quantifer, correct argument types'
print A(x,P(x)).pform()
print

print 'Quantifier, argument 0 is Letter not Variable'
print 'A(q,P(q))'
try: A(q,P(q))
except: print '... caught exception ...'
print

print 'Quantifier, argument 0 is Function not Variable'
print 'A(f(x),P(x))'
try: A(f(x),P(x))
except: print '... caught exception ...'
print

print 'Quantifier, argument 0 is Relation not Variable'
print 'A(Q(x),P(x))'
try: A(Q(x),P(x))
except: print '... caught exception ...'
print

print 'Quantifier, argument 1 is Term not Formula'
print 'A(x,f(x))'
try: A(x,f(x))
except: print '... caught exception ...'
print

print 'New, correct argument type'
print New(x).pform()
print

print 'New, wrong argument type, Letter not Variable'
print 'New(p)'
try: New(p)
except: print '... caught exception ...'
print

print 'New, wrong argument type, Function not Variable'
print 'New(f(x))'
try: New(f(x))
except: print '... caught exception ...'
print

print 'Let, correct argument types'
print Let(x,P(x)).pform()
print

print 'Let, wrong arg 0 type, Letter not Variable'
print 'Let(q,P(q))'
try: Let(q,P(q))
except: print '... caught exception ...'
print

print 'Let, wrong arg 0 type, Letter not Variable'
print 'Let(q,P(q))'
try: Let(q,P(q))
except: print '... caught exception ...'
print

print 'From subst_test, InfixLogical fails because fol_session defines a,b,c,d as vars not letters'
print 'aanb = And(a,Not(b))'
try: aanb = And(a,Not(b))
except: print '... caught exception ...'
print

print 'From equal_sub_test, uses x,z as variables and letters in same proof'
print """one_occur_ok = 
  [(Text('Valid substitution into one of multiple occurences'),comment),
   (Equal(x,z), given),
   (And(Or(x,y),Impl(x,y)), given),
   (And(Or(x,y),Impl(z,y)), sub, 1,2)]"""
try:
 one_occur_ok = \
  [(Text('Valid substitution into one of multiple occurences'),comment),
   (Equal(x,z), given),
   (And(Or(x,y),Impl(x,y)), given),
   (And(Or(x,y),Impl(z,y)), sub, 1,2)]
except: print '... caught exception ...'
print

print 'From simple_q_test, uses x as letter and variable in same proof'
print """ex_src_scope_ok = \
  [(Text('Valid substitution, source variable whose name is bound in inner scope'),comment),
   (Equal(x,z),given),
   (And(Not(x),A(x,R(x,y))),given),
   (And(Not(z),A(x,R(x,y))),sub,1,2)]"""
try: 
 ex_src_scope_ok = \
  [(Text('Valid substitution, source variable whose name is bound in inner scope'),comment),
   (Equal(x,z),given),
   (And(Not(x),A(x,R(x,y))),given),
   (And(Not(z),A(x,R(x,y))),sub,1,2)]
except: print '... caught exception ...'
print

print 'From free_test, uses same symbols as bound variables and letters'
print 'q3l3so = A(c,A(b,A(a,Or(And(a,Not(b)),Or(c,Not(d))))))'
try: q3l3so = A(c,A(b,A(a,Or(And(a,Not(b)),Or(c,Not(d))))))
except: print '... caught exception ...'
print

# Uncomment to see traceback
#print 'From free_test, uses same symbols as bound variables and letters, uncaught'
#q3l3so = A(c,A(b,A(a,Or(And(a,Not(b)),Or(c,Not(d))))))
