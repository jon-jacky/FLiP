from prop_session import *
from command_wrapper import *

def ex69_import_save_restore():
 print('import ex69ref')
 import ex69ref           # includes check_proof at the bottom
 pstate()
 print("save('ex69')")
 save('ex69')
 print('clear()')
 clear()
 print('from ex69 import ex69')
 from ex69 import ex69
 print ('check_proof(ex69)')
 check_proof(ex69)
 pstate()

ex69_import_save_restore()

from prop_derived_session import *

def ex111_apply_save_restore():
  clear()
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
  pstate()
  print("save('ex111')")
  save('ex111')
  print('clear()')
  clear()
  print('from ex111 import ex111')
  from ex111 import ex111
  print('check_proof(ex111)')
  check_proof(ex111)
  pstate()

ex111_apply_save_restore()
