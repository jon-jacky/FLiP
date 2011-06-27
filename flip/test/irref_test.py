from poset_session import *  


irref_ok = \
 [(Text("Irreflexivity rule"), comment),
  (lt(a,a), given),
  (F, irref, 1)]

check_proof(irref_ok)

# Separate test case for each conjunct in rule

irref_err1 = \
 [(Text("Irreflexivity rule, premise is not <"), comment),
  (nlt(a,a), given),
  (F, irref, 1)]

check_proof(irref_err1)

irref_err2 = \
 [(Text("Irreflexivity rule, premise arguments differ"), comment),
  (lt(a,b), given),
  (F, irref, 1)]

check_proof(irref_err2)

irref_err3 = \
 [(Text("Irreflexivity rule, conclusion is not F"), comment),
  (lt(a,a), given),
  (nlt(a,a), irref, 1)]

check_proof(irref_err3)

# Premise index, checked before rule

irref_err4 = \
 [(Text("Irreflexivity rule, premise out of range"), comment),
  (lt(a,b), given),
  (F, irref, 2)]

check_proof(irref_err4)
