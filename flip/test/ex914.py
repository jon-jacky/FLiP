from flip.logic.common import *
from flip.logic.prop_common import *
from flip.logic.prop_classic import *
from flip.logic.fol import *

ex914 = \
  [(Text('Valid E-elim, Kaye ex. 9.14, Ax.~P(x) |- ~Ex.P(x)'), comment),
    (A(x, Not(P(x))), given),
    (E(x, P(x)), assume),
    (Let(a,P(a)), let),
    (Not(P(a)), Ae, 1),
    (F, contra, 3,4),
    (F, Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]
