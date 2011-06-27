from fol_derived_session import *

p111Ae = \
  [(Text('P(t), Ax.(P(x) -> ~Q(x)) |- ~Q(t) using Ae from H&R p. 111'),comment),
   (P(t), given),
   (A(x,Impl(P(x),Not(Q(x)))), given),
   (Impl(P(t),Not(Q(t))), Ae, 2),
   (Not(Q(t)), imple, 3,1)]

print check_proof(p111Ae)

p111AeAi = \
  [(Text('H&R p. 111 Ae, Ai: Ax.(P(x) -> Q(x)), Ax.P(x) |- Ax.Q(x)'), comment),
    (A(x, Impl(P(x),Q(x))), given),
    (A(x, P(x)), given),
    (New(x), new),
    (Impl(P(x),Q(x)), Ae, 1),
    (P(x), Ae, 2),
    (Q(x), imple, 4,5),
    (A(x, Q(x)), Ai, 3,6)]

print check_proof(p111AeAi)

p114AeEi = \
  [(Text('Ax.P(x) -> Ex.P(x) using Ae, Ei from H&R p. 114'), comment),
   (A(x,P(x)), given),
   (P(x), Ae, 1),
   (E(x,P(x)), Ei, 2)]

print check_proof(p114AeEi)

p114AeEiEe = \
  [(Text('H&R p. 114, valid Ae,Ei,Ee: Ax.(P(x) -> Q(x)), Ex.P(x) |- Ex.Q(x)'), comment),
    (A(x, Impl(P(x),Q(x))), given),
    (E(x, P(x)), given),
    (Let(x,P(x)), let),
    (Impl(P(x),Q(x)), Ae, 1),
    (Q(x), imple, 4,3),
    (E(x, Q(x)), Ei, 5),
    (E(x, Q(x)), Ee, 2,3,6)]

print check_proof(p114AeEiEe)

p114AeEeEi_err = \
  [(Text('H&R p. 114, erroneous Ae,Ee,Ei: Ax.(P(x) -> Q(x)), Ex.P(x) |- Ex.Q(x)'), comment),
    (A(x, Impl(P(x),Q(x))), given),
    (E(x, P(x)), given),
    (Let(x,P(x)), let),
    (Impl(P(x),Q(x)), Ae, 1),
    (Q(x), imple, 4,3),
    (Q(x), Ee, 2,3,5)]

print check_proof(p114AeEeEi_err)

hr119 = \
  [(Text('H&R p.119: ~Ax.P(x) |- Ex.~P(x)'), comment),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 4),
    (F, contra, 5,2),
    (P(x), pbc, 4,6),
    (A(x, P(x)), Ai, 3,7),
    (F, contra, 8,1),
    (E(x, Not(P(x))), pbc, 2,9)]

print check_proof(hr119)

p121EiEeOre = \
  [(Text('H&R p. 121: Ex.p v Ex.q |- Ex.(p v q)'), comment),
    (Or(E(x, p),E(x, q)), given),
    (E(x, p), assume),
    (Let(x,p), let),
    (Or(p,q), oir, 3),
    (E(x, Or(p,q)), Ei, 4),
    (E(x, Or(p,q)), Ee, 2,3,5),
    (E(x, q), assume_case),
    (Let(x,q), let),
    (Or(p,q), oil, 8),
    (E(x, Or(p,q)), Ei, 9),
    (E(x, Or(p,q)), Ee, 7,8,10),
    (E(x, Or(p,q)), ore, 1,2,6,7,11)]

print check_proof(p121EiEeOre)

p121EiOreEe = \
  [(Text('H&R p. 121: Ex.(p v q) |- Ex.p v Ex.q'), comment),
    (E(x, Or(p,q)), given),
    (Let(x,Or(p,q)), let),
    (p, assume),
    (E(x, p), Ei, 3),
    (Or(E(x, p),E(x, q)), oir, 4),
    (q, assume_case),
    (E(x, q), Ei, 6),
    (Or(E(x, p),E(x, q)), oil, 7),
    (Or(E(x, p),E(x, q)), ore, 2,3,5,6,8),
    (Or(E(x, p),E(x, q)), Ee, 1,2,9)]

print check_proof(p121EiOreEe)

p122EiEe = \
  [(Text('H&R p. 122: Ex.Ey.p |- Ey.Ex.p'), comment),
    (E(x, E(y, p)), given),
    (Let(x,E(y, p)), let),
    (Let(y,p), let),
    (E(x, p), Ei, 3),
    (E(y, E(x, p)), Ei, 4),
    (E(y, E(x, p)), Ee, 2,3,5),
    (E(y, E(x, p)), Ee, 1,2,6)]

print check_proof(p122EiEe)
