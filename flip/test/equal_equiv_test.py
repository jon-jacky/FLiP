from fol_session import *


# Reflexivity

eq_refl_ok = \
  [(Text('Equal, Reflexivity'), comment),
   (Equal(a,a), refl)]

print check_proof(eq_refl_ok)

eq_refl1_ok = \
  [(Text('Equal, Reflexivity'), comment),
   (Equal(f(a),f(a)), refl)]

print check_proof(eq_refl1_ok)

eq_refl2_ok = \
  [(Text('Equal, Reflexivity'), comment),
   (Equal(g(x,f(a,b)),g(x,f(a,b))), refl)]

print check_proof(eq_refl2_ok)

eq_refl_err = \
  [(Text('Equal, Reflexivity, but arguments do not match'), comment),
   (Equal(a,b), refl)]

print check_proof(eq_refl_err)

eq_refl1_err = \
  [(Text('Equal, Reflexivity, but arguments do not match'), comment),
   (Equal(f(a),f(b)), refl)]

print check_proof(eq_refl1_err)

eq_refl2_err = \
  [(Text('Equal, Reflexivity, but arguments do not match'), comment),
   (Equal(g(x,f(a,b)),g(x,f(a,c))), refl)]

print check_proof(eq_refl2_err)

# Symmetry

eq_sym_ok = \
  [(Text('Equal, Symmetry'), comment),
   (Equal(a,b), given),
   (Equal(b,a), sym, 1)]

print check_proof(eq_sym_ok)

eq_sym1_ok = \
  [(Text('Equal, Symmetry'), comment),
   (Equal(f(a),f(b)), given),
   (Equal(f(b),f(a)), sym, 1)]

print check_proof(eq_sym1_ok)

eq_sym2_ok = \
  [(Text('Equal, Symmetry'), comment),
   (Equal(g(x,f(a,b)),g(x,f(b,c))), given),
   (Equal(g(x,f(b,c)),g(x,f(a,b))), sym, 1)]

print check_proof(eq_sym2_ok)

eq_sym_err = \
  [(Text('Equal, Symmetry'), comment),
   (Equal(a,b), given),
   (Equal(b,c), sym, 1)]

print check_proof(eq_sym_err)

eq_sym1_err = \
  [(Text('Equal, Symmetry, but arguments do not match'), comment),
   (Equal(f(a),f(b)), given),
   (Equal(f(b),f(c)), sym, 1)]

print check_proof(eq_sym1_err)

eq_sym2_err = \
  [(Text('Equal, Symmetry, but arguments do not match'), comment),
   (Equal(g(x,f(a,b)),g(x,f(b,c))), given),
   (Equal(g(x,f(b,c)),g(x,f(b,a))), sym, 1)]

print check_proof(eq_sym2_err)

# Transitivity

# Based on trans_test.py for poset logic, change lt -> Equal, nlt -> R

trans_ok = \
 [(Text('Transitive rule'), comment),
  (Equal(a,b), given),
  (Equal(b,c), given),
  (Equal(a,c), trans, 1,2)]

check_proof(trans_ok)

trans_err1 = \
  [(Text('Transitive rule, premise 0 is not Equal'), comment),
  (P(a,b), given),
  (Equal(b,c), given),
  (Equal(a,c), trans, 1,2)]

check_proof(trans_err1)

trans_err2 = \
  [(Text('Transitive rule, premise 2 is not Equal'), comment),
  (Equal(a,b), given),
  (P(b,c), given),
  (Equal(a,c), trans, 1,2)]

check_proof(trans_err2)

trans_err3 = \
  [(Text('Transitive rule, formula is not Equal'), comment),
  (Equal(a,b), given),
  (Equal(b,c), given),
  (P(a,c), trans, 1,2)]

check_proof(trans_err3)

trans_err4 = \
  [(Text('Transitive rule, variables in premises do not match'), comment),
  (Equal(a,b), given),
  (Equal(x,c), given),
  (Equal(a,c), trans, 1,2)]

check_proof(trans_err4)

trans_err5 = \
  [(Text('Transitive rule, formula variable does not match premise 0'),comment),
  (Equal(a,b), given),
  (Equal(b,c), given),
  (Equal(x,c), trans, 1,2)]

check_proof(trans_err5)

trans_err6 = \
  [(Text('Transitive rule, formula variable does not match premise 1'),comment),
  (Equal(a,b), given),
  (Equal(b,c), given),
  (Equal(a,x), trans, 1,2)]

check_proof(trans_err6)
