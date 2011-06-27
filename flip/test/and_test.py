from prop_session import *

ai_ok = \
  [(Text("And-Introduction"), comment),
   (Not(a),given),
   (Not(b),given),
   (And(Not(a),Not(b)), ai, 1,2)]

print check_proof(ai_ok)

aer_ok = \
  [(Text("And-Elimination Right"),comment),
   (And(Not(a),Not(b)), given),
   (Not(a), aer, 1)]

print check_proof(aer_ok)

ael_ok = \
  [(Text("And-Elimination Left"),comment),
   (And(Not(a),Not(b)), given),
   (Not(b), ael, 1)]

print check_proof(ael_ok)

ai_err1 = \
  [(Text("And-Introduction, premise indices don't match"), comment),
   (Not(a),given),
   (Not(b),given),
   (And(Not(a),Not(b)), ai, 2,1)]

print check_proof(ai_err1)

ai_err2 = \
  [(Text("And-Introduction, left argument doesn't match"), comment),
   (Not(c),given),
   (Not(b),given),
   (And(Not(a),Not(b)), ai, 1,2)]

print check_proof(ai_err2)

ai_err3 = \
  [(Text("And-Introduction, right argument doesn't match"), comment),
   (Not(a),given),
   (Not(c),given),
   (And(Not(a),Not(b)), ai, 1,2)]

print check_proof(ai_err3)

ai_err4 = \
  [(Text("And-Introduction, conclusion is not And"), comment),
   (Not(a),given),
   (Not(c),given),
   (Or(Not(a),Not(b)), ai, 1,2)]

print check_proof(ai_err4)

aer_err1 = \
  [(Text("And-Elimination Right, argument doesn't match"),comment),
   (And(Not(c),Not(b)), given),
   (Not(a), aer, 1)]

print check_proof(aer_err1)

ael_err1 = \
  [(Text("And-Elimination Left, argument doesn't match"),comment),
   (And(Not(a),Not(c)), given),
   (Not(b), ael, 1)]

print check_proof(ael_err1)


ael_err2 = \
  [(Text("And-Elimination Left, premise is not And"),comment),
   (Or(Not(a),Not(b)), given),
   (Not(b), ael, 1)]

print check_proof(ael_err2)

ael_err3 = \
  [(Text("And-Elimination Left, premise index is for comment"),comment),
   (Or(Not(a),Not(c)), given),
   (Not(b), ael, 0)]

print check_proof(ael_err3)
