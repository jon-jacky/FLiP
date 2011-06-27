"""
Propositional logic tests from Bornat.  Most of these are classical, actually.
Self contained, can execute standalone: python prop_constructive_test.py.
Alternatively, can execute in another session: import prop_constructive_test.
"""

from prop_constructive_session import *

ex51a = \
  [(Text('Fig. 5.1(a), Constructive e v f, ~f |- e'),comment),
   (Or(e,f),given),
   (Not(f),given),
   (e, assume),
   (f, assume_case),
   (F, contra, 4,2),
   (e, contra_con, 5),
   (e, ore, 1,3,3,4,6)]

print check_proof(ex51a)

ex51b = \
  [(Text('Fig. 5.1(b), Classical e v f, ~f |- e'),comment),
   (Or(e,f),given),
   (Not(f),given),
   (e, assume),
   (f, assume_case),
   (Not(e), assume),
   (F, contra, 4,2),
   (e, contra_classic, 5,6),
   (e, ore, 1,3,3,4,7)]

print check_proof(ex51b)

fig510 = \
  [(Text('Fig. 5.10, classical proof of ~(~e & ~f) |- e v f'), comment),
    (Not(And(Not(e),Not(f))), given),
    (Not(Or(e,f)), assume),
    (e, assume),
    (Or(e,f), oir, 3),
    (F, contra, 4,2),
    (Not(e), raa, 3,5),
    (f, assume),
    (Or(e,f), oil, 7),
    (F, contra, 8,2),
    (Not(f), raa, 7,9),
    (And(Not(e),Not(f)), ai, 6,10),
    (F, contra, 11,1),
    (Or(e,f), contra_classic, 2,12)]

print check_proof(fig510)

fig511 = \
  [(Text('Fig. 5.11, classical proof of e v ~e'), comment),
    (Not(Or(e,Not(e))), assume),
    (e, assume),
    (Or(e,Not(e)), oir, 2),
    (F, contra, 3,1),
    (Not(e), raa, 2,4),
    (Or(e,Not(e)), oil, 5),
    (F, contra, 6,1),
    (Or(e,Not(e)), contra_classic, 1,7)]

print check_proof(fig511)
