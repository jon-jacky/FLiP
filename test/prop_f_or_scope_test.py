from prop_session import *


f_scope_error = \
  [(Text('Erroneous proof of |- F using scope error'), comment),
    (And(T,F), assume),
    (F, ael, 1),
    (Not(And(T,F)), raa, 1,2),
    (F, ael, 1)]

print check_proof(f_scope_error)

or_scope_error = \
  [(Text('Erroneous proof of a v b |- b using scope error'), comment),
    (Or(a,b), given),
    (And(Not(a),Not(b)), assume),
    (Not(a), aer, 2),
    (b, oel, 1,3),
    (Not(b), ael, 2),
    (F, contra, 4,5),
    (Not(And(Not(a),Not(b))), raa, 2,6),
    (b, oel, 1,3)]

print check_proof(or_scope_error)
