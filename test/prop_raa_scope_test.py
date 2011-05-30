from prop_session import *

# Use and abuse of assumptions, raa, scope

ok = \
  [(Text('Valid a |- ~~a from inner subproof of ex 6.9'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa, 2,3)]

print check_proof(ok)

assume_raa_invalid_2 = \
  [(Text('Invalid |- ~~a with subproof too deeply nested'), comment),
    (a, assume),
    (Not(a), assume),
    (F, contra, 1,2),
    (Not(Not(a)), raa, 2,3),  # valid
    (Not(Not(a)), raa, 2,3)]  # invalid, now subproof too deeply nested.

print check_proof(assume_raa_invalid_2)

ex67_err = \
  [(Text('From example 6.7 invalid a v b |- b, subproof too deeply nested'), comment),
    (Or(a,b), given),
    (Not(b), assume),
    (Not(a), assume),
    (b, oel, 1,3),
    (F, contra, 4,2),
    (Not(Not(b)), raa, 2,5),
    (Not(Not(b)), raa, 2,5),
    (b, ne, 7)]


print check_proof(ex67_err)

assume_raa_derive_not_f = \
  [(Text('Valid |- ~F using assumption, raa'), comment),
    (F, assume),
    (Not(F), raa, 1,1)]

print check_proof(assume_raa_derive_not_f)

assume_raa_derive_valid = \
  [(Text('Valid |- ~(a & F) using assumption, raa'), comment),
    (And(a,F), assume),
    (F, ael, 1),
    (Not(And(a,F)), raa, 1,2)]

print check_proof(assume_raa_derive_valid)

# duplicate subproofs

dup_ok = \
  [(Text('Reductio Ad Absurdum (RAA), duplicate subproofs, cite premises in correct scope'), comment),
   (a, given),           # 1
   (Not(a),assume),      # 2
   (F, contra, 1,2),     # 3
   (Not(Not(a)), raa, 2,3),  # 4
   (Not(a),assume),      # 5
   (F, contra, 1,5),     # 6
   (Not(Not(a)), raa, 5,6)] # 7

print check_proof(dup_ok)

dup_err = \
  [(Text('Reductio Ad Absurdum (RAA), duplicate subproofs, cite premises in wrong scope'), comment),
   (a, given),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa, 2,3),
   (Not(a),assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa, 2,3)]

print check_proof(dup_err)


# Without scope check, crashes after raa when try to pop empty assump. stack

raa_scope_err_1 = \
  [(Text('Erroneous a |- ~a  using scope error'), comment),
   (a, given),
   (Not(a), assume),
   (F, contra, 1,2),
   (Not(Not(a)), raa, 2,3),
   (Not(a), raa, 1,3)]

print check_proof(raa_scope_err_1)

assume_raa_invalid = \
  [(Text('Invalid a |- ~~a with subproof too deeply nested'), comment),
    (a, given),
    (Not(a), assume),
    (F, contra, 1,2),
    (Not(Not(a)), raa, 2,3),  # valid
    (Not(Not(a)), raa, 2,3)]  # invalid, now subproof too deeply nested.

print check_proof(assume_raa_invalid)

assume_raa_derive_invalid = \
  [(Text('Invalid |- ~a using assumption, raa, should fail'), comment),
    (And(a,F), assume),
    (a, aer, 1),
    (F, ael, 1),
    (Not(a), raa, 2,3)] # invalid, premise at line 2 is not an assumption 

print check_proof(assume_raa_derive_invalid)

# This should pass

dup_discharge_ok = \
  [(Text('Valid Reductio Ad Absurdum (RAA), duplicate subproofs, discharge non-adjacent subproof, should pass'), comment),
   (a, given),           # 1
   (Not(a),assume),      # 2
   (F, contra, 1,2),     # 3
   (Not(Not(a)), raa, 2,3),  # 4
   (Not(a),assume),      # 5
   (F, contra, 1,5),     # 6
   (Not(Not(a)), raa, 2,3)] # 7  # not adjacent subproof, but valid anyway

print check_proof(dup_discharge_ok)

# This should fail

