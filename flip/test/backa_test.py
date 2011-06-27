from fol_session import *
from command_wrapper import *

from ex916ref import ex916 # put defn *without* check in its own file

def backa_test():
  print '-- check_proof ex. 9.16'
  check_proof(ex916)
  print

  print '-- backa to delete big subproof that occupies most of proof'
  pbacka()
  pback()
  pback()
  pbacka()
  pp()
  print

  print '-- New(a) to check whether a is free at this point in proof'
  pcheckp(New(a),new)
  print

  print '-- start over, check_proof 9.16 again'
  check_proof(ex916)
  print

  print '-- back to delete many lines, end up in most deeply nested part of proof'
  pback(12)
  pp()
  print

  print '-- New(a) to check whether a is free at this point in proof'
  pcheckp(New(a),new)
  print

  for i in range(3):

    print '-- backa to pop this subproof'
    pbacka()
    pp()
    print 

    print '-- New(a) to check whether a is free at this point in proof'
    pcheckp(New(a),new)
    print

backa_test()
