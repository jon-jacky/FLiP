from fol_session import *

a,b,c,d,x = map(Letter, 'abcdx')  # Variable in fol_session, must rebind now

def differ(s,t):
  if not s.mismatch(t,{},[],[],[],''):
    return 'no difference'
  else:
    return 'substitution differs'

# Not(a) etc.

print "One occurence of a at level 1, substitute {a:b} should work"
na = Not(a)
subs = {a:b}
nb = na.subst(subs)
# print original formula na *after* substitute to confirm we didn't mutate it
print na.pform()
print ppfdict(subs)
print nb.pform()
print differ(na,nb)
print

print "Formula contains only a, substitute {x:b} should fail"
sxb = {x:b}
nax = na.subst(sxb)
print na.pform()
print ppfdict(sxb)
print nax.pform()
print differ(na,nax)
print

# And(a,Not(b)) etc.

print "One a at level 1, one b at level 2, subst {a:b}, {b:d} should  both work"
print

aanb = And(a,Not(b))

sac = {a:c}
aanb2c = aanb.subst(sac)
print aanb.pform()
print ppfdict(sac)
print  aanb2c.pform()
print differ(aanb,aanb2c)
print

sbd = {b:d}
aanb2d = aanb.subst(sbd)
print aanb.pform()
print ppfdict(sbd)
print aanb2d.pform()
print differ(aanb,aanb2d)
print

sxd = {x:d}
aanx2d = aanb.subst(sxd)
print aanb.pform()
print ppfdict(sxd)
print aanx2d.pform()
print differ(aanb,aanx2d)
print

print "Not just Symbol:Symbol, but  Symbol:Compound"
san = {a:Not(b)}
aanb2an = aanb.subst(san)
print aanb.pform()
print ppfdict(san)
print aanb2an.pform()
print differ(aanb,aanb2an)
print

print "Not just Symbol:Symbol, but Compound:Symbol"
snd = {Not(b):d}
aanb2nd = aanb.subst(snd)
print aanb.pform()
print ppfdict(snd)
print aanb2nd.pform()
print differ(aanb,aanb2nd)
print

print "Not just Symbol:Symbol, but Compound:Compound"
sno = {Not(b):Or(b,c)}
aanb2o = aanb.subst(sno)
print aanb.pform()
print ppfdict(sno)
print aanb2o.pform()
print differ(aanb,aanb2o)
print

print "Compound that doesn't match at its own level 1"
snxd = {Not(x):d}
aanb2nxd = aanb.subst(snxd)
print aanb.pform()
print ppfdict(snxd)
print aanb2nxd.pform()
print differ(aanb,aanb2nxd)
print



print "Level 3 with single occurrences"
print

l3so = Or(And(a,Not(b)),Or(c,Not(d)))

print "Symbol that matches, deep level"
# subs = {a:b}
l3soa2b = l3so.subst(subs)
print l3so.pform()
print ppfdict(subs)
print l3soa2b.pform()
print differ(l3so,l3soa2b)
print

print "Symbol that matches, deeper level"
# sbd = {b:d}
l3sob2d = l3so.subst(sbd)
print l3so.pform()
print ppfdict(sbd)
print l3sob2d.pform()
print differ(l3so,l3sob2d)
print

print "Compound that matches"
# sno = {Not(b):Or(b,c)}
l3son2o = l3so.subst(sno)
print l3so.pform()
print ppfdict(sno)
print l3son2o.pform()
print differ(l3so,l3son2o)
print

print "Compound that matches"
socnd = { Or(c,Not(d)) : Or(a,Not(b)) }
l3sosocnd = l3so.subst(socnd)
print l3so.pform()
print ppfdict(socnd)
print l3sosocnd.pform()
print differ(l3so,l3sosocnd)
print

print "Compound whose argument (deep) does not match"
socna = { Or(c,Not(a)) : Or(a,Not(b)) }
l3sosocna = l3so.subst(socna)
print l3so.pform()
print ppfdict(socna)
print l3sosocna.pform()
print differ(l3so,l3sosocna)
print

print "Compound whose constructor does not match, but whose arguments do"
sacnd = { And(c,Not(d)) : Or(a,Not(b)) }
l3sosacnd = l3so.subst(sacnd)
print l3so.pform()
print ppfdict(sacnd)
print l3sosacnd.pform()
print differ(l3so,l3sosacnd)
print

print "Compound that doesn't match at its own level 1"
# snxd = {Not(x):d}
l3sonxd = l3so.subst(snxd)
print l3so.pform()
print ppfdict(snxd)
print l3sonxd.pform()
print differ(l3so,l3sonxd)
print

print "Level 3 with multiple occurrences at different levels"
l3mod = Or(And(a,Not(b)),Or(c,Not(a)))
l3moda2b = l3mod.subst(subs)
print l3mod.pform()
print ppfdict(subs)
print l3moda2b.pform()
print differ(l3mod,l3moda2b)
print

print "Level 3 with multiple occurrences at the same level"
l3mos = Or(And(a,Not(b)),Or(c,c))
scd = {c:d}
l3mosc2d = l3mos.subst(scd)
print l3mos.pform()
print ppfdict(scd)
print l3mosc2d.pform()
print differ(l3mos,l3mosc2d)
print

a,b = map(Variable, 'ab') # a,b now Variable not Letter, rebind again

print "Test case no_premise_match from equal_sub_test"
npm_p1 = S(f(b))
print npm_p1.pform()
npm_matches = { f(a):a }
print ppfdict(npm_matches)
npm_sub = npm_p1.subst(npm_matches)
print npm_sub.pform()
print differ(npm_p1,npm_sub)
print

a,b = map(Letter, 'ab') # a,b now Letter again

print "Multiple substitution"
print aanb.pform()
sacno = {a:c,Not(b):Or(b,c)}
print ppfdict(sacno)
aanb2no = aanb.subst(sacno)
print aanb2no.pform()
print differ(aanb,aanb2no)
print

# rebind again
x = Variable('x')

print "Two single substitutions in sequence"
pxy = P(x,y)
print pxy.pform()
x2y = { x:y }
print ppfdict(x2y)
px2y = pxy.subst(x2y)
print px2y.pform()
y2x = { y:x }
print ppfdict(y2x)
px2y2x = px2y.subst(y2x)
print px2y2x.pform()
print
print "With multiple substitution, simultaneous substitution should swap x,y"
print " but sequential substitution would have the same result as above"
print pxy.pform()
xyswap = { x:y, y:x }
print ppfdict(xyswap)
pxyswap = pxy.subst(xyswap)
print pxyswap.pform()
print

print "Source keys appear in replacement formulas, check for runaway recursion"
andpq = And(p,q)
print andpq.pform()
pqsubs = { p:Not(p), q:Or(p,q) }
print ppfdict(pqsubs)
andno = andpq.subst(pqsubs)
print andno.pform()
print

print "Placeholders used as keys in substitutions work like any other symbols"
nm1 = Not(m1)
subsm1 = {m1:q}
nm1s = nm1.subst(subsm1)
print nm1.pform()
print ppfdict(subsm1)
print nm1s.pform()
print
andm12 = And(m1,m2)
subsm12 = { m1:p, m2:q }
andm12s = andm12.subst(subsm12)
print andm12.pform()
print ppfdict(subsm12)
print andm12s.pform()
print
