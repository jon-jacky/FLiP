from prop_session import *

not_ok = \
  [(Text('Not-Elimination'),comment),
   (Not(Not(Or(a,b))), given),
   (Or(a,b), ne, 1)]

print check_proof(not_ok)

not_err1 = \
  [(Text('Not-Elimination, outer operator not Not'),comment),
   (Or(Not(Not(a)),b), given),
   (Not(a), ne, 1)]

print check_proof(not_err1)

not_err2 = \
  [(Text('Not-Elimination, inner operator not Not'),comment),
   (Not(Or(Not(a),b)), given),
   (Not(a), ne, 1)]

print check_proof(not_err2)

not_err3 = \
  [(Text('Not-Elimination, conclusion is not formula in premise'),comment),
   (Not(Not(Or(a,b))), given),
   (And(a,b), ne, 1)]

print check_proof(not_err3)
