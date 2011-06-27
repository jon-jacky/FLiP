from prop_session import *

contra_ok1 = \
 [(Text("Contradiction rule"), comment),
  (And(a,b), given),
  (Not(And(a,b)), given),
  (F, contra, 1,2)]

print check_proof(contra_ok1)

contra_ok2 = \
 [(Text("Contradiction rule, reversed premise order, indices also"), comment),
  (Not(And(a,b)), given),
  (And(a,b), given),
  (F, contra, 2,1)]

print check_proof(contra_ok2)

# reverse premise order, but don't reverse index order 

contra_err0 = \
  [(Text("Contradiction rule, reverse premise order but not indices"), comment),
   (Not(And(a,b)), given),
   (And(a,b), given),
   (F, contra, 1,2)]

print check_proof(contra_err0)

# Separate test case for each conjunct in rule

contra_err1 = \
 [(Text("Contradiction, first premise not negation of second"), comment),
  (And(a,b), given),
  (Not(Or(a,b)), given),
  (F, contra, 1,2)]

print check_proof(contra_err1)

contra_err2 = \
 [(Text("Contradiction, second premise not Not"), comment),
  (And(a,b), given),
  (Or(a,b), given),
  (F, contra, 1,2)]

print check_proof(contra_err2)

contra_err3 = \
 [(Text("Contradiction, conclusion not F"), comment),
  (And(a,b), given),
  (Not(And(a,b)), given),
  (T, contra, 1,2)]

print check_proof(contra_err3)

contra_err4 = \
 [(Text("Contradiction, left arguments don't match"), comment),
  (And(a,b), given),
  (Not(And(c,b)), given),
  (F, contra, 1,2)]

print check_proof(contra_err4)

contra_err4 = \
 [(Text("Contradiction, right  arguments don't match"), comment),
  (And(a,b), given),
  (Not(And(a,c)), given),
  (F, contra, 1,2)]

print check_proof(contra_err4)
