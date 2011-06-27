from poset_session import *  

'Test poset Assumption and Reductio Ad Absurdum rules with Kaye ex. 4.3, p. 40'


ex43 = \
 [(Text('Kaye ex. 4.3, p. 40'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (lt(c,a), assume),
  (lt(a,a), trans, 3,4),
  (F, irref, 5),
  (nlt(c,a), raa, 4,6)]

check_proof(ex43)

# Check each conjunct in raa rule

raa_err1 = \
 [(Text('Kaye ex. 4.3, p. 40 but discharge is not F'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (lt(c,a), assume),
  (lt(a,a), trans, 3,4),
  (nlt(a,a), given),
  (nlt(c,a), raa, 4,6)]

check_proof(raa_err1)

raa_err2 = \
 [(Text('Kaye ex. 4.3, p. 40, but raa is not negation of assumption'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (lt(c,a), assume),
  (lt(a,a), trans, 3,4),
  (F, irref, 5),
  (lt(c,a), raa, 4,6)]

check_proof(raa_err2)

raa_err3 = \
 [(Text('Kaye ex. 4.3, p. 40, but raa left arg does not match assumption'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (lt(c,a), assume),
  (lt(a,a), trans, 3,4),
  (F, irref, 5),
  (nlt(b,a), raa, 4,6)]

check_proof(raa_err3)

raa_err4 = \
 [(Text('Kaye ex. 4.3, p. 40, but raa right arg does not match assumption'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (lt(c,a), assume),
  (lt(a,a), trans, 3,4),
  (F, irref, 5),
  (nlt(c,d), raa, 4,6)]

check_proof(raa_err4)

# Check missing assumption, consequent

raa_err5 = \
 [(Text('Kaye ex. 4.3, p. 40, missing assumption'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (nlt(c,a), raa, 4,6)]

check_proof(raa_err5)

raa_err6 = \
 [(nlt(c,a), raa)]

print "One-line erroneous proof with no comment line"
check_proof(raa_err6)
