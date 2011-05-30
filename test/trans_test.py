from poset_session import *  


trans_ok = \
 [(Text("Transitive rule"), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2)]

check_proof(trans_ok)

# Separate test case for each conjunct in rule

trans_err1 = \
  [(Text("Transitive rule, premise 0 isn't lt"), comment),
  (nlt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2)]

check_proof(trans_err1)

trans_err2 = \
  [(Text("Transitive rule, premise 2 isn't lt"), comment),
  (lt(a,b), given),
  (nlt(b,c), given),
  (lt(a,c), trans, 1,2)]

check_proof(trans_err2)

trans_err3 = \
  [(Text("Transitive rule, formula isn't lt"), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (nlt(a,c), trans, 1,2)]

check_proof(trans_err3)

trans_err4 = \
  [(Text("Transitive rule, variables in premises don't match"), comment),
  (lt(a,b), given),
  (lt(d,c), given),
  (lt(a,c), trans, 1,2)]

check_proof(trans_err4)

trans_err5 = \
  [(Text("Transitive rule, formula variable doesn't match premise 0"), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(d,c), trans, 1,2)]

check_proof(trans_err5)

trans_err6 = \
  [(Text("Transitive rule, formula variable doesn't match premise 1"), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,d), trans, 1,2)]

check_proof(trans_err6)

# Syntax error, checked before rule

#trans_err7 = \
# [(Text("Transitive rule, syntax error"), comment),
#  (lt(a,b), given),
#  (lt(b,c), given),
#  (binrel(a,c), trans, 1,2)]

# check_proof(trans_err7)

# Premise index, checked before rule

trans_err8 = \
 [(Text("Transitive rule, premise out of range"), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,3)]

check_proof(trans_err8)
