"""
Propositional logic tests from Huth & Ryan.
Self contained, can execute standalone: python prop_derived_test.py.
Alternatively, can execute in another session: import prop_derived_test.
"""

from prop_derived_session import *

ex111 = \
  [(Text('Ex. 1.11: |- (q -> r) -> ((~q -> ~p) -> (p -> r))'), comment),
    (Impl(q,r), assume),
    (Impl(Not(q),Not(p)), assume),
    (p, assume),
    (Not(Not(p)), nni, 3),
    (Not(Not(q)), mt, 2,4),
    (q, nne, 5),
    (r, imple, 1,6),
    (Impl(p,r), impli, 3,7),
    (Impl(Impl(Not(q),Not(p)),Impl(p,r)), impli, 2,8),
    (Impl(Impl(q,r),Impl(Impl(Not(q),Not(p)),Impl(p,r))), impli, 1,9)]

print check_proof(ex111)

ex118 = \
  [(Text('Ex. 1.18: p & (q v r) |- (p & q) v (p & r) using Or-elim'), comment),
    (And(p,Or(q,r)), given),
    (p, aer, 1),
    (Or(q,r), ael, 1),
    (q, assume),
    (And(p,q), ai, 2,4),
    (Or(And(p,q),And(p,r)), oir, 5),
    (r, assume_case),
    (And(p,r), ai, 2,7),
    (Or(And(p,q),And(p,r)), oil, 8),
    (Or(And(p,q),And(p,r)), ore, 3,4,6,7,9)]

print check_proof(ex118)

ex124 = \
  [(Text('Ex 1.24 p -> q |- ~p v q using Law of Excluded Middle'), comment),
    (Impl(p,q), given),
    (Or(p,Not(p)), lem),
    (p, assume),
    (q, imple, 1,3),
    (Or(Not(p),q), oil, 4),
    (Not(p), assume_case),
    (Or(Not(p),q), oir, 6),
    (Or(Not(p),q), ore, 2,3,5,6,7)]

print check_proof(ex124)

p20 = \
  [(Text('p. 20 |- p -> (q -> p) using copy'), comment),
    (p, assume),
    (q, assume),
    (p, copy, 1),
    (Impl(q,p), impli, 2,3),
    (Impl(p,Impl(q,p)), impli, 1,4)]

print check_proof(p20)


p20n = \
  [(Text('Attempt like p. 20 |- p -> (q -> p) *without* using copy'), comment),
    (p, assume),
    (q, assume),
    (Impl(q,p), impli, 2,1),
    (Impl(p,Impl(q,p)), impli, 1,3)]

print check_proof(p20n)

pbc_case = \
  [(Text('|- ~(p & F) using Proof By Contradiction'), comment),
    (Not(Not(And(p,F))), assume),
    (And(p,F), nne, 1),
    (F, ael, 2),
    (Not(And(p,F)), pbc, 1,3)]

print check_proof(pbc_case)
