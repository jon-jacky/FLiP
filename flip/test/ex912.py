from flip.logic.common import *
from flip.logic.prop_common import *
from flip.logic.prop_classic import *
from flip.logic.fol import *

ex912 = \
  [(Text('Valid A-intro, Kaye ex. 9.12, ~Ax.P(x) |- Ex.~P(x)'), comment),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 4),
    (F, contra, 5,2),
    (Not(Not(P(x))), raa, 4,6),
    (P(x), ne, 7),
    (A(x, P(x)), Ai, 3,8),
    (F, contra, 9,1),
    (Not(Not(E(x, Not(P(x))))), raa, 2,10),
    (E(x, Not(P(x))), ne, 11)]
