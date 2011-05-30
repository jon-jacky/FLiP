from fol_session import *
from command_wrapper import *

def simple_back_test():
  check_proof()

  # range checks
  pcheckp(Text('Test0'),comment)
  pback(3)
  pback()
  pback()

  # freevars state restoration
  pcheckp(Text('Test1'),comment)
  pcheckp(Equal(x,x),given)
  pcheckp(Equal(y,y),given)
  pcheckp(New(y),new)        # should fail
  pback()
  pcheckp(New(y),new)        # should succeed

simple_back_test()
print

# from kaye_ch9_test import ex916  # NOT! This prints all the proofs!

from ex916ref import ex916 # put defn *without* check in its own file

# Printed indents, '... already appears free ...' confirm state is restored

def indents_back_test():
  check_proof(ex916)
  pback(1)
  pcheckp(New(a),new)
  pback(2)
  pcheckp(New(a),new)
  pback(2)
  pcheckp(New(a),new)
  pcheckp(New(b),new)
  pback(2)
  pcheckp(New(b),new)
  pback(9)
  pcheckp(New(b),new)

indents_back_test()

a,b = map(Letter, 'ab')  # rebind

def xr_back_test():
  check_proof()
  pcheckp(Text('Ex 6.4'),comment)
  pcheckp(And(a,Not(b)),assume)
  pcheckp(Not(b),ael,1)
  state()
  pback() 
  state()
  # takes else xr branch when save state
  pcheckp(a,aer,1)
  state()

xr_back_test()
print

  