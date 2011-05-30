from poset_session import *  

'Test poset Assumption and Reductio Ad Absurdum rules with Kaye ex. 4.3, p. 40'


ex43 = \
 [(Text('Kaye ex. 4.3, p. 40'), comment),
  (lt(a,b), given),        # 1
  (lt(b,c), given),        # 2
  (lt(a,c), trans, 1,2),   # 3
  (lt(c,a), assume),       # 4
  (lt(a,a), trans, 3,4),   # 5
  (F, irref, 5),           # 6
  (nlt(c,a), raa, 4,6)]    # 7

print check_proof(ex43)

dup_ok = \
 [(Text('Kaye ex. 4.3, p. 40, duplicate subproofs, cite premises in correct scope'), comment),
  (lt(a,b), given),        # 1
  (lt(b,c), given),        # 2
  (lt(a,c), trans, 1,2),   # 3
  (lt(c,a), assume),       # 4
  (lt(a,a), trans, 3,4),   # 5
  (F, irref, 5),           # 6
  (nlt(c,a), raa, 4,6),    # 7
  (lt(c,a), assume),       # 8
  (lt(a,a), trans, 3,8),   # 9  cites 8, same subproof
  (F, irref, 9),           # 10 cites 9, same subproof
  (nlt(c,a), raa, 8,10)]   # 11 explicit premises

print check_proof(dup_ok)

dup_err = \
 [(Text('Kaye ex. 4.3, p. 40, duplicate subproofs, cite premises in wrong scope'), comment),
  (lt(a,b), given),        # 1
  (lt(b,c), given),        # 2
  (lt(a,c), trans, 1,2),   # 3
  (lt(c,a), assume),       # 4
  (lt(a,a), trans, 3,4),   # 5
  (F, irref, 5),           # 6
  (nlt(c,a), raa, 4,6),    # 7
  (lt(c,a), assume),       # 8
  (lt(a,a), trans, 3,4),   # 9  cites 4, wrong subproof, should not be allowed
  (F, irref, 5),           # 10 cites 5, wrong subproof
  (nlt(c,a), raa, 4,6)]    # 11 explicit premises, wrong subproof

print check_proof(dup_err)

