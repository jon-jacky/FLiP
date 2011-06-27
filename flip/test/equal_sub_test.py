from fol_session import *

ex917 = \
  [(Text('From example 9.17'), comment),
   (Not(R(a)), given),
   (Equal(a,x), given),
   (Not(R(x)),sub,2,1)]

print check_proof(ex917)

ex918 = \
  [(Text('From example 9.18'), comment),
   (S(f(a)), given),
   (Equal(f(a),a), given),
   (S(a),sub,2,1)]

print check_proof(ex918)

no_premise_match = \
  [(Text('Premise does not match equation'), comment),
   (S(f(b)), given),
   (Equal(f(a),a), given),
   (S(a),sub,2,1)]

print check_proof(no_premise_match)

no_conclusion_match = \
  [(Text('Conclusion does not match equation'), comment),
   (S(f(a)), given),
   (Equal(f(a),a), given),
   (S(b),sub,2,1)]

print check_proof(no_conclusion_match)

equation_reversed = \
  [(Text('Equation reversed'), comment),
   (S(f(a)), given),
   (Equal(a,f(a)), given),
   (S(a),sub,2,1)]

print check_proof(equation_reversed)

premises_reversed = \
  [(Text('Premises reversed'), comment),
   (S(f(a)), given),
   (Equal(f(a),a), given),
   (S(a),sub,1,2)]

print check_proof(premises_reversed)

no_eq_premise_number = \
  [(Text('No equation premise number'), comment),
   (S(f(a)), given),
   (Equal(f(a),a), given),
   (S(a),sub,1)]

print check_proof(no_eq_premise_number)

no_s1_premise_number = \
  [(Text('No premise formula number'), comment),
   (S(f(a)), given),
   (Equal(f(a),a), given),
   (S(a),sub,2)]

print check_proof(no_s1_premise_number)

one_occur_ok = \
  [(Text('Valid substitution into one of multiple occurences'),comment),
   (Equal(x,z), given),
   (And(P(x,y),Q(x,y)), given),
   (And(P(x,y),Q(z,y)), sub, 1,2)]

print check_proof(one_occur_ok)

mult_occur_ok = \
  [(Text('Valid substitution into all of multiple occurences'),comment),
   (Equal(x,z), given),
   (And(P(x,y),Q(x,y)), given),
   (And(P(z,y),Q(z,y)), sub, 1,2)]

print check_proof(mult_occur_ok)

mult_occur_err = \
  [(Text('Erroneous substitution into one of multiple occurences, other occurence ok'),comment),
   (Equal(x,z), given),
   (And(P(x,y),Q(x,y)), given),
   (And(P(z,y),Q(u,y)), sub, 1,2)]

print check_proof(mult_occur_err)

mult_occur_err_1 = \
  [(Text('Erroneous substitution into one of multiple occurences, other occurence ok, reverse order'),comment),
   (Equal(x,z), given),
   (And(P(x,y),Q(x,y)), given),
   (And(P(u,y),Q(z,y)), sub, 1,2)]

print check_proof(mult_occur_err_1)
