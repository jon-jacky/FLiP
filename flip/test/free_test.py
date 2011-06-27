from fol_session import *

print 'No duplicates'
l3so = Or(And(P(a),Not(Q(b))),Or(R(c),Not(S(d))))
print l3so.pform()
print ppflist(l3so.free())
print

print 'Duplicates, at different levels'
l3mod = Or(And(P(a),Not(Q(b))),Or(R(c),Not(P(a))))
print l3mod.pform()
print ppflist(l3mod.free())
print

print 'Duplicates, at the same level'
l3mos = Or(And(P(a),Not(Q(b))),Or(R(c),R(c)))
print l3mos.pform()
print ppflist(l3mos.free())
print

print 'Quantify one of four variables'
q1l3so = A(a,Or(And(P(a),Not(Q(b))),Or(R(c),Not(S(d)))))
print q1l3so.pform()
print ppflist(q1l3so.free())
print

print 'Quantify two of four variables'
q2l3so = A(b,A(a,Or(And(P(a),Not(Q(b))),Or(R(c),Not(S(d))))))
print q2l3so.pform()
print ppflist(q2l3so.free())
print

print 'Quantify three of four variables'
q3l3so = A(c,A(b,A(a,Or(And(P(a),Not(Q(b))),Or(R(c),Not(S(d)))))))
print q3l3so.pform()
print ppflist(q3l3so.free())
print

print 'Quantify four of four variables'
q4l3so = A(d,A(c,A(b,A(a,Or(And(P(a),Not(Q(b))),Or(R(c),Not(S(d))))))))
print q4l3so.pform()
print ppflist(q4l3so.free())
print

print 'Nested quantifier'
q1nl3so = Or(And(P(a),Not(Q(b))),E(c,Or(R(c),Not(P(a)))))
print q1nl3so.pform()
print ppflist(q1nl3so.free())
print

print 'Nested quantifier, bound var. same name as free var. in outer scope'
q1n2l3so = Or(And(P(a),Not(Q(b))),A(a,E(c,Or(R(c),Not(P(a))))))
print q1n2l3so.pform()
print ppflist(q1n2l3so.free())
print

print 'Nested quantifier, inner scope'
q1n2il3so = Or(And(P(a),E(b,Not(Q(b)))),Or(R(c),Not(P(a))))
print q1n2il3so.pform()
print ppflist(q1n2il3so.free())
print
