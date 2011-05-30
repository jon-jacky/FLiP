from common import *
from prop_common import *
from prop_classic import *
from prop_common import *
from prop_derived import *

ex111 = \
  [(Text('Ex. 1.11: |- (q -> r) -> ((~q -> ~p) -> (p -> r))'), comment),
    (Impl(q,r), assume),
    (Impl(Not(q),Not(p)), assume),
    (p, assume),
    (Not(Not(p)), nni, 3),
    (Not(Not(q)), mt, 2,4),
    (q, nne, 5),
    (r, imple, 1,6),
    (Impl(p,r), impli, 3,7),
    (Impl(Impl(Not(q),Not(p)),Impl(p,r)), impli, 2,8),
    (Impl(Impl(q,r),Impl(Impl(Not(q),Not(p)),Impl(p,r))), impli, 1,9)]
