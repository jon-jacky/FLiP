from prop_session import *           # for ex64
from prop_derived_session import *   # for ex111
from prop_constructive_session import * # for ex51
from command_wrapper import *

def ex64_apply():
  check_proof()
  pcheckp(Text('Ex 6.4, ~a v b |- ~(a & ~b)'),comment)
  pcheckp(And(a,Not(b)),assume)
  prapply(aer,1)
  pcheckp(Not(a),assume)
  prapply(contra,2,3)
  prapply(raa,3,4)
  prapply(ael,1)
  pcheckp(Or(Not(a),b),given)
  prapply(oel,7,5)
  prapply(contra,8,6)
  prapply(raa,1,9)

ex64_apply()
pstate()
print

def ex64_apply_aerxl():
  check_proof()
  pcheckp(Text('Erroneous Ex 6.4, use ael not aer in step 2 so apply contra fails in 4'),comment)
  pcheckp(And(a,Not(b)),assume)
  prapply(ael,1)
  pcheckp(Not(a),assume)
  prapply(contra,2,3)

ex64_apply_aerxl()
pstate()
print

# from prop_constructive_test

def ex51a():
  check_proof()
  pcheckp(Text('Fig. 5.1(a), Constructive e v f, ~f |- e'),comment)
  pcheckp(Or(e,f),given)
  pcheckp(Not(f),given)
  pcheckp(e, assume)
  pcheckp(f, assume_case)
  prapply(contra, 4,2)
  pcheckp(e, contra_con, 5)
  prapply(ore, 1,3,3,4,6)

ex51a()
print

def ex51a_noformula():
  check_proof()
  pcheckp(Text('Erroneous Fig. 5.1(a), attempt to use Apply with contra_con'),comment)
  pcheckp(Or(e,f),given)
  pcheckp(Not(f),given)
  pcheckp(e, assume)
  pcheckp(f, assume_case)
  prapply(contra, 4,2)
  prapply(contra_con, 5)
  prapply(ore, 1,3,3,4,6)

ex51a_noformula()
print

# error checks from prop_ore_scope_test

def ex51a_scramble_subproofs():
  check_proof()
  pcheckp(Text('Erroneous Fig. 5.1(a), scramble subproof premises'),comment)
  pcheckp(Or(e,f),given)
  pcheckp(Not(f),given)
  pcheckp(e, assume)
  pcheckp(f, assume_case)
  prapply(contra, 4,2)
  pcheckp(e, contra_con, 5)
  prapply(ore, 1,3,6,4,3)

ex51a_scramble_subproofs()
print

def failed_ore():
  clear() # calls check_proof()
  pcheckp(Text('Failed attempt at a v b |- a, does not match rule'),comment),
  pcheckp(Or(a,b),given)
  pcheckp(a, assume)
  pcheckp(b, assume_case)
  prapply(ore, 1,2,2,3,3)

failed_ore()
print

def invalid_subproofs():
  clear()
  pcheckp(Text('Invalid a v b |- a, using invalid premise/subproof citations'),comment)
  pcheckp(Or(a,b),given)
  pcheckp(a, assume)
  pcheckp(b, assume_case)
  prapply(ore, 1,2,2,3,2)

invalid_subproofs()
print

def ore_scope_invalid():
  clear()
  pcheckp(Text('Invalid a v b |- a, discharge ore from wrong scope'), comment)
  pcheckp(Or(a,b), given)
  pcheckp(a, assume)
  pcheckp(a, assume_case)
  pcheckp(b, assume)
  prapply(ai, 4,3)
  prapply(ael, 5)
  prapply(ore, 1,2,2,4,6)

ore_scope_invalid()
print

def ore_scope_invalid1():
  clear()
  pcheckp(Text('Invalid a v b |- a, discharge ore cites wrong scope'), comment)
  pcheckp(Or(a,b), given)
  pcheckp(a, assume)
  pcheckp(a, assume_case)
  pcheckp(b, assume)
  prapply(ai, 4,3)
  prapply(ael, 5)
  prapply(impli, 4,6)
  prapply(ore, 1,2,2,4,6)

ore_scope_invalid1()
print

# compare to ex111 in prop_derived_test, the formulas in impli steps are big

def ex111_apply():
  check_proof()
  pcheckp(Text('Ex. 1.11: |- (q -> r) -> ((~q -> ~p) -> (p -> r))'), comment)
  pcheckp(Impl(q,r), assume)
  pcheckp(Impl(Not(q),Not(p)), assume)
  pcheckp(p, assume)
  prapply(nni, 3)
  prapply(mt, 2,4)
  prapply(nne, 5)
  prapply(imple, 1,6)
  prapply(impli, 3,7)
  prapply(impli, 2,8)
  prapply(impli, 1,9)

ex111_apply()


