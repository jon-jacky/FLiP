from prop_session import *

oil_ok = \
  [(Text("Or-Introduction Left"), comment),
   (Not(a),given),
   (Or(Not(b),Not(a)), oil, 1)]

print check_proof(oil_ok)

oir_ok = \
  [(Text("Or-Introduction Right"), comment),
   (Not(a),given),
   (Or(Not(a),Not(b)), oir, 1)]

print check_proof(oir_ok)

oel_ok = \
  [(Text("Or-Elimination Left"),comment),
   (Or(Not(b),Not(a)), given),
   (Not(Not(b)), given),
   (Not(a), oel, 1, 2)]

print check_proof(oel_ok)

oer_ok = \
  [(Text("Or-Elimination Right"),comment),
   (Or(Not(a),Not(b)), given),
   (Not(Not(b)), given),
   (Not(a), oer, 1, 2)]

print check_proof(oer_ok)

oil_err0 = \
  [(Text("Or-Introduction Left, argument doesn't match premise"), comment),
   (Not(a),given),
   (Or(Not(c),Not(b)), oil, 1)]

print check_proof(oil_err0)

oir_err0 = \
  [(Text("Or-Introduction Right, conclusion is not Or"), comment),
   (Not(b),given),
   (And(Not(a),Not(b)), oir, 1)]

print check_proof(oir_err0)

oer_err1 = \
  [(Text("Or-Elimination Right, argument doesn't match"),comment),
   (Or(Not(a),Not(b)), given),
   (Not(Not(c)), given),
   (Not(a), oer, 1, 2)]

print check_proof(oer_err1)

oel_err1 = \
  [(Text("Or-Elimination Left, argument doesn't match"),comment),
   (Or(Not(c),Not(b)), given),
   (Not(Not(a)), given),
   (Not(b), oel, 1, 2)]

print check_proof(oel_err1)


oel_err2 = \
  [(Text("Or-Elimination Left, premise is not Or"),comment),
   (And(Not(a),Not(b)), given),
   (Not(Not(a)), given),
   (Not(b), oel, 1, 2)]

print check_proof(oel_err2)

oel_err3 = \
  [(Text("Or-Elimination Left, premise index is for comment"),comment),
   (Or(Not(a),Not(b)), given),
   (Not(Not(a)), given),
   (Not(b), oel, 0, 2)]

print check_proof(oel_err3)

