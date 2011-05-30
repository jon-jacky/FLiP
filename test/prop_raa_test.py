from prop_session import *

ok = \
  [(Text('Reductio Ad Absurdum (RAA) from inner subproof of ex 6.9'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa, 2,3)]

print check_proof(ok)

err0 = \
  [(Text('RAA, Consequent is not F'), comment),
   (a, given),
   (Not(a),assume),
   (T, top),
   (Not(Not(a)), raa, 2,3)]

print check_proof(err0)

err1 = \
  [(Text('RAA, conclusion is not negation of assumption'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(a), raa, 2,3)]

print check_proof(err1)

err2 = \
  [(Text('RAA, conclusion argument is not assumption argument'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(b)), raa, 2,3)]

print check_proof(err2)

err3 = \
  [(Text('RAA, premise indices reversed'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa, 3,2)]

print check_proof(err3)

err4 = \
  [(Text('RAA, conclusion argument wrong BUT premises missing'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(b)), raa, 2,3)]

print check_proof(err4)

err5 = \
  [(Text('RAA: steps correct except RAA step premises missing'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa)]

print check_proof(err5)
