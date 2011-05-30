"""
Or-elimination scope tests. 
"""

from prop_constructive_session import *

ex51a_scramble_subproofs = \
  [(Text('Fig. 5.1(a), but scramble subproof premises, should fail'),comment),
   (Or(e,f),given),
   (Not(f),given),
   (e, assume),
   (f, assume_case),
   (F, contra, 4,2),
   (e, contra_con, 5),
   (e, ore, 1,3,6,4,3)]

print check_proof(ex51a_scramble_subproofs)

failed_ore = \
  [(Text('Failed attempt at a v b |- a, does not match rule'),comment),
   (Or(a,b),given),
   (a, assume),
   (b, assume_case),
   (a, ore, 1,2,2,3,3)]

print check_proof(failed_ore)

invalid_subproofs = \
  [(Text('Invalid a v b |- a, using invalid premise/subproof citations'),comment),
   (Or(a,b),given),
   (a, assume),
   (b, assume_case),
   (a, ore, 1,2,2,3,2)]

print check_proof(invalid_subproofs)

ore_scope_invalid = \
  [(Text('Invalid a v b |- a, discharge ore from wrong scope'), comment),
    (Or(a,b), given),
    (a, assume),
    (a, assume_case),
    (b, assume),
    (And(b,a), ai, 4,3),
    (a, ael, 5),
    (a, ore, 1,2,2,4,6)]

print check_proof(ore_scope_invalid)

ore_scope_invalid1 = \
  [(Text('Invalid a v b |- a, discharge ore cites wrong scope'), comment),
    (Or(a,b), given),
    (a, assume),
    (a, assume_case),
    (b, assume),
    (And(b,a), ai, 4,3),
    (a, ael, 5),
    (Impl(b,a), impli, 4,6),
    (a, ore, 1,2,2,4,6)]

print check_proof(ore_scope_invalid1)
