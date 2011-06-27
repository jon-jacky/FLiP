from fol_session import *

ex91Ei = \
  [(Text('E-intro from Kaye ex 9.10, not all occurrences of bound variable substituted'), comment),
   (Equal(x,x), refl),
   (E(v,Equal(v,x)), Ei, 1)]

print check_proof(ex91Ei)

ex91EiX = \
  [(Text('Erroneous E-intro from Kaye ex 9.10, bound variable does not match'), comment),
   (Equal(x,x), refl),
   (E(v,Equal(w,x)), Ei, 1)]

print check_proof(ex91EiX)

ex91Ae = \
  [(Text('A-elim from Kaye ex 9.10'), comment),
   (A(x,E(v,Equal(v,x))), given),
   (E(v,Equal(v,w)), Ae, 1)]

print check_proof(ex91Ae)

ex91AeX = \
  [(Text('Erroneous A-elim from Kaye ex 9.10, bound variable does not match'), comment),
   (A(x,E(v,Equal(v,x))), given),
   (E(v,Equal(w,x)), Ae, 1)]

print check_proof(ex91AeX)

p111Ae = \
  [(Text('P(t), Ax.(P(x) -> ~Q(x)) |- ~Q(t) using Ae from H&R p. 111'),comment),
   (P(t), given),
   (A(x,Impl(P(x),Not(Q(x)))), given),
   (Impl(P(t),Not(Q(t))), Ae, 2),
   (Not(Q(t)), imple, 3,1)]

print check_proof(p111Ae)

p114AeEi = \
  [(Text('Ax.P(x) -> Ex.P(x) using Ae, Ei from H&R p. 114'), comment),
   (A(x,P(x)), given),
   (P(x), Ae, 1),
   (E(x,P(x)), Ei, 2)]

print check_proof(p114AeEi)

ex99c = \
  [(Text('Valid subst. of *free* var into quantified formula, Kay ex 9.9'),comment),
   (Equal(t,g(y,z)),given),
   (E(x,Equal(x,f(t))),given),
   (E(x,Equal(x,f(g(y,z)))),sub,1,2)]

print check_proof(ex99c)

ex99v = \
  [(Text('Valid subst. of *free* var into *some* occurences in quantified formula, Kay ex 9.9'),comment),
   (Equal(x,y),given),
   (E(z,Equal(x,f(x,z))),given),
   (E(z,Equal(x,f(y,z))),sub,1,2)]

print check_proof(ex99v)

ex99a = \
  [(Text('Erroneous subst. of bound var into quantified formula, Kay ex 9.9'),comment),
   (Equal(t,x),given),
   (E(x,Equal(x,f(t))),given),
   (E(x,Equal(x,f(x))),sub,1,2)]

print check_proof(ex99a)

ex99b = \
  [(Text('Erroneous subst. of bound var into quantified formula, Kay ex 9.9'),comment),
   (Equal(t,g(x,y)),given),
   (E(x,Equal(x,f(t))),given),
   (E(x,Equal(x,f(g(x,y)))),sub,1,2)]

print check_proof(ex99b)

ex99d = \
  [(Text('Erroneous use of bound var as source of subst. into quant. form'),comment),
   (Equal(x,y),given),
   (E(x,Equal(x,f(x,z))),given),
   (E(x,Equal(y,f(y,z))),sub,1,2)]

print check_proof(ex99d)

ex99e = \
  [(Text('Erroneous appearance of bound var in source of subst. into quant. form'),comment),
   (Equal(f(x,z),g(y,z)),given),
   (E(x,Equal(x,f(x,z))),given),
   (E(x,Equal(x,g(y,z))),sub,1,2)]

print check_proof(ex99e)

ex211a = \
  [(Text('Correct A-elim similar to erroneous example H&R ex 2.11, R(x,y) is x < y'), comment),
   (A(x,(E(y, R(x,y)))), given),
   (E(y, R(z,y)), Ae, 1)]
   
print check_proof(ex211a)

ex211b = \
  [(Text('Erroneous A-elim similar to H&R ex 2.11, R(x,y), wrong variable substituted'), comment),
   (A(x,(E(y, R(x,y)))), given),
   (E(y, R(x,z)), Ae, 1)]
   
print check_proof(ex211b)

ex211c = \
  [(Text('Erroneous A-elim similar to H&R ex 2.11, R(x,y), variable order reversed'), comment),
   (A(x,(E(y, R(x,y)))), given),
   (E(y, R(y,z)), Ae, 1)]
   
print check_proof(ex211c)

ex211 = \
  [(Text('Erroneous A-elim with subst of bound variable into nested quantified formula, H&R ex 2.11'), comment),
   (A(x,(E(y, R(x,y)))), given),
   (E(y, R(y,y)), Ae, 1)]
   
print check_proof(ex211)

ex211x = \
  [(Text('Erroneous E-intro with subst of bound variable into nested quantified formula, similar to H&R ex 2.11'), comment),
   (A(y, R(y,z)), given),
   (E(x, A(y, R(x,z))), Ei, 1)]
   
print check_proof(ex211x)

ex_src_scope_ok = \
  [(Text('Valid substitution, source variable whose name is bound in inner scope'),comment),
   (Equal(x,z),given),
   (And(Not(P(x)),A(x,R(x,y))),given),
   (And(Not(P(z)),A(x,R(x,y))),sub,1,2)]

print check_proof(ex_src_scope_ok)

ex_src_scope_err = \
  [(Text('Erroneous substitution, source variable whose name is bound in inner scope'),comment),
   (Equal(x,z),given),
   (And(Not(P(x)),A(x,R(x,y))),given),
   (And(Not(P(x)),A(x,R(z,y))),sub,1,2)]

print check_proof(ex_src_scope_err)

ex_tgt_scope_ok = \
  [(Text('Valid substitution, replacements variable whose name is bound in inner scope'),comment),
   (Equal(x,z),given),
   (And(Not(P(x)),A(z,R(x,z))),given),
   (And(Not(P(z)),A(z,R(x,z))),sub,1,2)]

print check_proof(ex_tgt_scope_ok)

ex_tgt_scope_err = \
  [(Text('Erroneous substitution, replacement variable whose name is bound in inner scope'),comment),
   (Equal(x,z),given),
   (And(Not(P(x)),A(z,R(x,z))),given),
   (And(Not(P(x)),A(z,R(z,z))),sub,1,2)]

print check_proof(ex_tgt_scope_err)

ei_bound_replace_err = \
  [(Text('Erroneous E-intro where replacement term includes bound variable'),comment),
   (E(y,E(x,R(x,y,z))), given),
   (E(x,E(y,E(x,R(x,y,x)))), Ei, 1)]

print check_proof(ei_bound_replace_err)

ae_bound_source_err = \
  [(Text('Erroneous A-elim where source term includes bound variable'),comment),
   (A(x,E(y,E(x,R(x,y)))), given),
   (E(y,E(x,R(t,y))), Ae, 1)]

print check_proof(ae_bound_source_err)

ae_all_occurrences_ok = \
  [(Text('Valid A-elim where all occurences of bound var are replaced with same term'),comment),
   (Equal(x,u),given),
   (Equal(t,v),given),
   (Not(Equal(u,v)),given),
   (A(x,Equal(x,x)),given),
   (Equal(t,t),Ae,4)]

print check_proof(ae_all_occurrences_ok)

ae_all_occurrences_ok = \
  [(Text('Valid A-elim where all occurences of bound var are replaced with bound var name'),comment),
   (Equal(x,u),given),
   (Equal(t,v),given),
   (Not(Equal(u,v)),given),
   (A(x,Equal(x,x)),given),
   (Equal(x,x),Ae,4)]

print check_proof(ae_all_occurrences_ok)

ae_overlooked_occurrences_err = \
  [(Text('Erroneous A-elim where not all occurences of bound var are replaced'),comment),
   (Equal(x,u),given),
   (Equal(t,v),given),
   (Not(Equal(u,v)),given),
   (A(x,Equal(x,x)),given),
   (Equal(x,t),Ae,4)]

print check_proof(ae_overlooked_occurrences_err)

ae_overlooked_occurrences_err = \
  [(Text('Erroneous A-elim where different occurences of bound var are replaced differently'),comment),
   (Equal(y,u),given),
   (Equal(t,v),given),
   (Not(Equal(u,v)),given),
   (A(x,Equal(x,x)),given),
   (Equal(y,t),Ae,4)]

print check_proof(ae_overlooked_occurrences_err)

ae_bound_no_body_ok = \
  [(Text('Valid A-elim where bound variable does not occur in body'),comment),
   (A(y,Equal(x,x)),given),
   (Equal(x,x),Ae,1)]

print check_proof(ae_bound_no_body_ok)

ei_bound_no_body_ok = \
  [(Text('Valid A-elim where bound variable does not occur in body'),comment),
   (Equal(x,x),given),
   (E(y,Equal(x,x)),Ei,1)]

print check_proof(ei_bound_no_body_ok)
