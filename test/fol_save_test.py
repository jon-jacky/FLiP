from fol_session import *
from command_wrapper import *
  
def ex914_import_save_restore():
 print('import ex914ref')
 import ex914ref           # includes check_proof at the bottom
 print("save('ex914')")
 save('ex914')
 print('clear()')
 clear()
 print('from ex914 import ex914')
 from ex914 import ex914
 print ('check_proof(ex914)')
 check_proof(ex914)

ex914_import_save_restore() 
print

def ex912_apply_save_restore():
  clear()
  pcheckp(Text('Valid A-intro, Kaye ex. 9.12, ~Ax.P(x) |- Ex.~P(x)'), comment)
  pcheckp(Not(A(x, P(x))), given)
  pcheckp(Not(E(x, Not(P(x)))), assume)
  pcheckp(New(x), new)
  pcheckp(Not(P(x)), assume)
  prapply(Ei, 4, {x:x}) # for Ei must provide {t1:v1}, here just {x:x}
  prapply(contra, 5,2)
  prapply(raa, 4,6)
  prapply(ne, 7)
  prapply(Ai, 3,8, x) # for Ae must provide only replacement term t1 for{v1:t1}
  prapply(contra, 9,1)
  prapply(raa, 2,10)
  prapply(ne, 11)

  print("save('ex912')")
  save('ex912')
  print('clear()')
  clear()
  print('from ex912 import ex912')
  from ex912 import ex912
  print('check_proof(ex912)')
  check_proof(ex912)

ex912_apply_save_restore()
