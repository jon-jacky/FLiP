"""
poset tests from Kaye ex. 4.2, 4.3 p. 40
Self contained, can execute standalone: python poset_test.py 
Alternatively, can execute in another session: import poset_test
"""

from poset_session import *

ex42 = \
  [(Text('Kaye ex. 4.2, p 40'), comment),
   (lt(a,b), given),
   (lt(b,c), given),
   (lt(a,c), trans, 1,2),
   (lt(c,a), given),
   (lt(a,a), trans, 3,4),
   (F, irref,5)]

print check_proof(ex42)

ex43 = \
 [(Text('Kaye ex. 4.3, p. 40'), comment),
  (lt(a,b), given),
  (lt(b,c), given),
  (lt(a,c), trans, 1,2),
  (lt(c,a), assume),
  (lt(a,a), trans, 3,4),
  (F, irref, 5),
  (nlt(c,a), raa, 4,6)]

print check_proof(ex43)

ex44 = \
 [(Text('Kaye ex. 4.4, p. 41'), comment),
  (lt(a,b),given),
  (lt(b,a),assume),
  (lt(a,a),trans,1,2),
  (F,irref,3),
  (nlt(b,a),raa, 2,4)]

print check_proof(ex44)

ex46 = \
[(Text('Kaye ex. 4.6, p. 41'), comment),
 (lt(c,b),given),
 (nlt(a,b),given),
 (lt(a,c),assume),
 (lt(a,b),trans,3,1),
 (F,contra,4,2),
 (nlt(a,c),raa,3,5)]

print check_proof(ex46)
