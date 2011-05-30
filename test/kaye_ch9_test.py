from fol_session import *

ex910 = \
  [(Text('Kaye ex. 9.10, erroneous proof with quantifiers'), comment),
    (New(x), new),
    (Equal(x,x), refl),
    (E(v, Equal(v,x)), Ei, 2),
    (A(x, E(v, Equal(v,x))), Ai, 1,3),
    (New(w), new),
    (E(v, Equal(v,f(w))), Ae, 4),
    (Let(a,Equal(a,f(w))), let),
    (Equal(a,f(w)),Ee,6,7,7)]

print check_proof(ex910)


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

print check_proof(ex912)

ex914 = \
  [(Text('Valid E-elim, Kaye ex. 9.14, Ax.~P(x) |- ~Ex.P(x)'), comment),
    (A(x, Not(P(x))), given),
    (E(x, P(x)), assume),
    (Let(a,P(a)), let),
    (Not(P(a)), Ae, 1),
    (F, contra, 3,4),
    (F, Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]

print check_proof(ex914)

ex916 = \
  [(Text('Kaye ex. 9.16: Ex.Ey.(R(x) & R(y) & ~(x = y)), Ax.Ay.(P(x) & P(y) -> (x = y)) |- Ex.(R(x) & ~P(x))'), comment),
    (E(x, E(y, And(And(R(x),R(y)),Not(Equal(x,y))))), given),
    (A(x, A(y, Impl(And(P(x),P(y)),Equal(x,y)))), given),
    (Not(E(x, And(R(x),Not(P(x))))), assume),
    (Let(a,E(y, And(And(R(a),R(y)),Not(Equal(a,y))))), let),
    (Let(b,And(And(R(a),R(b)),Not(Equal(a,b)))), let),
    (And(R(a),R(b)), aer, 5),
    (R(a), aer, 6),
    (R(b), ael, 6),
    (Not(Equal(a,b)), ael, 5),
    (Not(P(a)), assume),
    (And(R(a),Not(P(a))), ai, 7,10),
    (E(x, And(R(x),Not(P(x)))), Ei, 11),
    (F, contra, 12,3),
    (Not(Not(P(a))), raa, 10,13),
    (P(a), ne, 14),
    (Not(P(b)), assume),
    (And(R(b),Not(P(b))), ai, 8,16),
    (E(x, And(R(x),Not(P(x)))), Ei, 17),
    (F, contra, 18,3),
    (Not(Not(P(b))), raa, 16,19),
    (P(b), ne, 20),
    (And(P(a),P(b)), ai, 15,21),
    (A(y, Impl(And(P(a),P(y)),Equal(a,y))), Ae, 2),
    (Impl(And(P(a),P(b)),Equal(a,b)), Ae, 23),
    (Equal(a,b), imple, 24,22),
    (F, contra, 25,9),
    (F, Ee, 4,5,26),
    (F, Ee, 1,4,27),
    (Not(Not(E(x, And(R(x),Not(P(x)))))), raa, 3,28),
    (E(x, And(R(x),Not(P(x)))), ne, 29)]

print check_proof(ex916)

ex917 = \
  [(Text('Kaye ex. 9.17: Ex.(P(x) & ~R(x)), Ax.Ay.(P(x) & P(y) -> (x = y) |- Ax.(R(x) -> ~P(x))'), comment),
    (A(x, A(y, Impl(And(P(x),P(y)),Equal(x,y)))), given),
    (E(x, And(P(x),Not(R(x)))), given),
    (New(x), new),
    (R(x), assume),
    (Let(a,And(P(a),Not(R(a)))), let),
    (P(a), aer, 5),
    (Not(R(a)), ael, 5),
    (P(x), assume),
    (And(P(a),P(x)), ai, 6,8),
    (A(y, Impl(And(P(a),P(y)),Equal(a,y))), Ae, 1),
    (Impl(And(P(a),P(x)),Equal(a,x)), Ae, 10),
    (Equal(a,x), imple, 11,9),
    (Not(R(x)), sub, 12,7),
    (F, contra, 4,13),
    (Not(P(x)), raa, 8,14),
    (Not(P(x)), Ee, 2,5,15),
    (Impl(R(x),Not(P(x))), impli, 4,16),
    (A(x, Impl(R(x),Not(P(x)))), Ai, 3,17)]

print check_proof(ex917)

print 

pp()

print

ptree()
