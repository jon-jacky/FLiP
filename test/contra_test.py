from poset_session import *  


contra_ok1 = \
 [(Text("Contradiction rule"), comment),
  (lt(a,b), given),
  (nlt(a,b), given),
  (F, contra, 1,2)]

print check_proof(contra_ok1)

contra_ok2 = \
 [(Text("Contradiction rule, reversed premise order, indices also"), comment),
  (nlt(a,b), given),
  (lt(a,b), given),
  (F, contra, 2,1)]

print check_proof(contra_ok2)

# reverse premise order, but don't reverse index order 

contra_err0 = \
 [(Text("Contradiction rule, reversed premise order, but not indices"), comment),
  (nlt(a,b), given),
  (lt(a,b), given),
  (F, contra, 1,2)]

print check_proof(contra_err0)

# Separate test case for each conjunct in rule

contra_err1 = \
 [(Text("Contradiction, first premise not <"), comment),
  (nlt(a,b), given),
  (nlt(a,b), given),
  (F, contra, 1,2)]

print check_proof(contra_err1)

contra_err2 = \
 [(Text("Contradiction, second premise not /<"), comment),
  (lt(a,b), given),
  (lt(a,b), given),
  (F, contra, 1,2)]

print check_proof(contra_err2)

contra_err3 = \
 [(Text("Contradiction, conclusion not F"), comment),
  (lt(a,b), given),
  (nlt(a,b), given),
  (lt(c,d), contra, 1,2)]

print check_proof(contra_err3)

contra_err4 = \
 [(Text("Contradiction, left arguments don't match"), comment),
  (lt(a,b), given),
  (nlt(c,b), given),
  (F, contra, 1,2)]

print check_proof(contra_err4)

contra_err4 = \
 [(Text("Contradiction, right  arguments don't match"), comment),
  (lt(a,b), given),
  (nlt(a,c), given),
  (F, contra, 1,2)]

print check_proof(contra_err4)
