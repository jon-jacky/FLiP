from fol_session import *
from formula import ppfpairs

# a,b,c are variables in fol_session, rebind
a,b,c = map(Letter, 'abc')

print 'Mismatch example from formula.txt'
f1 = And(c,Or(b,c))
f2 = And(a,Not(b))
print 'f1  %s' % f1.ppf()
print 'f2  %s' % f2.ppf()
mismatches = f1.mismatch(f2,{},[],[],[],'') # never mind other arguments for now
print 'f1.mismatch(f2,...) %s' % ppfpairs([ (s,f) for (s,f,vs) in mismatches ])
print

print 'Substitution example from formula.txt, except f3 not f2'
print 'The mismatches and subst methods are inverses (sort of)'
substitutions = { c:a, Or(b,c):Not(b) }
f3 = f1.subst(substitutions)
print 'f1  %s' % f1.ppf()
print 'substitutions  %s' % ppfdict(substitutions)
print 'f3 = f1.subst(substitutions)  %s' % f3.ppf()
m_mismatches = f3.mismatch(f1,{},[],[],[],'')
f1_ = f3.subst(dict([(s,r) for (s,r,b) in m_mismatches]))
print 'm_mismatches = f3.mismatch(f1, ...)  %s' % ppfpairs([ (s,f) for (s,f,b) in m_mismatches ])
print 'Now the pairs in the m_mismatches list are '
print ' just the inverses of the pairs in the substitutions dictionary'
print 'This are just the pairs we need '
print ' to substitute into f3 to get the original f1 back'
print 'f1_ = f3.subst(... m_mismatches...)  %s' % f1_.ppf()
print 'f1_.mismatch(f1, ...)  %s' %  f1_.mismatch(f1,{},[],[],[],'')
print 'not f1_.mismatch(f1, ...)  %s' %  (not f1_.mismatch(f1,{},[],[],[],''))
