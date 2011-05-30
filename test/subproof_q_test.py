from fol_session import *

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

ex912_var_used = \
  [(Text('Erroneous A-intro, ex. 9.12, New variable already in use'), comment),
    (Equal(x,b),given),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 5),
    (F, contra, 6,3),
    (Not(Not(P(x))), raa, 5,7),
    (P(x), ne, 8),
    (A(x, P(x)), Ai, 4,9),
    (F, contra, 10,2),
    (Not(Not(E(x, Not(P(x))))), raa, 3,11),
    (E(x, Not(P(x))), ne, 12)]

print check_proof(ex912_var_used)

ex912_other_var = \
  [(Text('Erroneous A-intro, ex. 9.12, New variable not used in conclusion'), comment),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 4),
    (F, contra, 5,2),
    (Not(Not(P(x))), raa, 4,6),
    (P(x), ne, 7),
    (A(y, P(y)), Ai, 3,8),
    (F, contra, 9,1),
    (Not(Not(E(x, Not(P(x))))), raa, 2,10),
    (E(x, Not(P(x))), ne, 11)]

print check_proof(ex912_other_var)

ex912_new_not_used = \
  [(Text('Erroenous A-intro, ex. 9.12, New variable not used in subproof'), comment),
    (Equal(x,b),given),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(y), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 5),
    (F, contra, 6,3),
    (Not(Not(P(x))), raa, 5,7),
    (P(x), ne, 8),
    (A(x, P(x)), Ai, 4,9),
    (F, contra, 10,2),
    (Not(Not(E(x, Not(P(x))))), raa, 3,11),
    (E(x, Not(P(x))), ne, 12)]

print check_proof(ex912_new_not_used)

ex912_no_new = \
  [(Text('Erroneous A-intro, ex. 9.12, subproof assumption is not New'), comment),
    (Equal(x,b),given),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (Equal(x,x), assume),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 5),
    (F, contra, 6,3),
    (Not(Not(P(x))), raa, 5,7),
    (P(x), ne, 8),
    (A(x, P(x)), Ai, 4,9),
    (F, contra, 10,2),
    (Not(Not(E(x, Not(P(x))))), raa, 3,11),
    (E(x, Not(P(x))), ne, 12)]

print check_proof(ex912_no_new)

ex912_wrong_pred = \
  [(Text('Erroneous A-intro, ex. 9.12, wrong predicate in conclusion'), comment),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 4),
    (F, contra, 5,2),
    (Not(Not(P(x))), raa, 4,6),
    (P(x), ne, 7),
    (A(x, Q(x)), Ai, 3,8),
    (F, contra, 9,1),
    (Not(Not(E(x, Not(P(x))))), raa, 2,10),
    (E(x, Not(P(x))), ne, 11)]

print check_proof(ex912_wrong_pred)

ex912_wrong_bound = \
  [(Text('Erroneous A-intro, ex. 9.12, wrong bound variable in conclusion after quantifier'), comment),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 4),
    (F, contra, 5,2),
    (Not(Not(P(x))), raa, 4,6),
    (P(x), ne, 7),
    (A(y, P(x)), Ai, 3,8),
    (F, contra, 9,1),
    (Not(Not(E(x, Not(P(x))))), raa, 2,10),
    (E(x, Not(P(x))), ne, 11)]

print check_proof(ex912_wrong_bound)

ex912_wrong_body = \
  [(Text('Erroneous A-intro, ex. 9.12, wrong bound variable in conclusion body'), comment),
    (Not(A(x, P(x))), given),
    (Not(E(x, Not(P(x)))), assume),
    (New(x), new),
    (Not(P(x)), assume),
    (E(x, Not(P(x))), Ei, 4),
    (F, contra, 5,2),
    (Not(Not(P(x))), raa, 4,6),
    (P(x), ne, 7),
    (A(x, P(y)), Ai, 3,8),
    (F, contra, 9,1),
    (Not(Not(E(x, Not(P(x))))), raa, 2,10),
    (E(x, Not(P(x))), ne, 11)]

print check_proof(ex912_wrong_body)

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

ex914_var_used = \
  [(Text('Erroneous E-elim, ex. 9.14, Let variable already in use'), comment),
    (Equal(x,a),given),
    (A(x, Not(P(x))), given),
    (E(x, P(x)), assume),
    (Let(a,P(a)), let),
    (Not(P(a)), Ae, 2),
    (F, contra, 4,5),
    (F, Ee, 3,4,6),
    (Not(E(x, P(x))), raa, 3,7)]

print check_proof(ex914_var_used)

# Does this even make sense?  No, can only check its appearance in Let itself
#ex914_let_not_used = \
 # [(Text('Erroenous E-elim, ex. 9.14, Let variable not used in subproof'), comment),
  # ]
#print check_proof(ex914_let_not_used)

# Fails at  requires different proof
ex914_wrong_pred = \
  [(Text('Erroneous E-elim, ex. 9.14, wrong predicate in Let statement'), comment),
    (A(x, Not(Q(x))), given),
    (E(x, P(x)), assume),
    (Let(a,Q(a)), let),
    (Not(Q(a)), Ae, 1),
    (F,contra,3,4),
    (F, Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]

print check_proof(ex914_wrong_pred)

# v1 in P1,{v1:v2} does not match  E(v1,P1) in premise 
# must add another arg to P to check this
ex914_wrong_bound = \
  [(Text('Erroneous E-elim, ex. 9.14, wrong source variable in Let statement body'), comment),
    (A(y, Not(P(x,y))), given),
    (E(x, P(x,y)), assume),
    (Let(a,P(x,a)), let),
    (Not(P(x,a)), Ae, 1),
    (F,contra,3,4),
    (F, Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]

print check_proof(ex914_wrong_bound)

# v2 in P1,{v1:v2} does not match  Let(v2,...) in same formula
ex914_wrong_body = \
  [(Text('Erroneous E-elim, ex. 9.14, wrong replacement variable in Let statement body'), comment),
    (A(x, Not(P(x))), given),
    (E(x, P(x)), assume),
    (Let(a,P(b)), let),
    (Not(P(b)), Ae, 1),
    (F, contra, 3,4),
    (F, Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]

print check_proof(ex914_wrong_body)

# Just use assume not let
ex914_no_let = \
  [(Text('Erroneous E-elim, ex. 9.14, subproof assumption is not Let'), comment),
    (A(x, Not(P(x))), given),
    (E(x, P(x)), assume),
    (P(a), assume),
    (Not(P(a)), Ae, 1),
    (F, contra, 3,4),
    (F, Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]

print check_proof(ex914_no_let)

ex914_different_concl = \
  [(Text('Erroneous E-elim, ex. 9.14, Rule conclusion is not subproof conclusion'), comment),
    (A(x, Not(P(x))), given),
    (E(x, P(x)), assume),
    (Let(a,P(a)), let),
    (Not(P(a)), Ae, 1),
    (F, contra, 3,4),
    (Not(q), Ee, 2,3,5),
    (Not(E(x, P(x))), raa, 2,6)]

print check_proof(ex914_different_concl)

# To test this requires a different proof, because here concl has no vars
let_used_concl = \
  [(Text('Erroneous E-elim, Let variable is used in conclusion'), comment),
    (E(x,And(P(x),Impl(P(x),Q(x)))), given),
    (Let(a,And(P(a),Impl(P(a),Q(a)))), let),
    (P(a),aer,2),
    (Impl(P(a),Q(a)),ael,2),
    (Q(a),imple,4,3),
    (Q(a),Ee,1,2,5)]

print check_proof(let_used_concl)

ai_wrongvar = \
  [(Text('Erroneous A-intro, new variable a not used in subproof'), comment),
    (And(Equal(x,y),Equal(x,z)), given),
    (New(a), new),
    (Equal(x,y), aer, 1),
    (A(x, Equal(x,y)), Ai, 2,3)]

print check_proof(ai_wrongvar)

ai_vac = \
  [(Text('Vacuous A-intro, new variable a does not occur in conclusion body'), comment),
    (And(Equal(x,y),Equal(x,z)), given),
    (New(a), new),
    (Equal(x,y), aer, 1),
    (A(a, Equal(x,y)), Ai, 2,3)]

print check_proof(ai_vac)