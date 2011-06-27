"""
Tree tests based on Kaye 3.1, p. 25
"""

from tree_session import *

# valid proofs

shorten_ok = \
 [(Text('Kaye 3.1, p. 25'), comment), # 0
  (Path('00'), given), # 1
  (Path('01'), given), # 2
  (Path('0'), shorten, 1,2)] # 3

print check_proof(shorten_ok)

lengthen_ok = \
 [(Text('Kaye 3.1, p. 25'), comment), # 0
  (Path('00'), given), # 1
  (Path('01'), given), # 2
  (Path('0'), shorten, 1,2), # 3
  (Path('00'), lengthen0, 3), # 4
  (Path('001'), lengthen1, 4), # 5
  (Path('0010'), lengthen0, 5), # 6
  (Path('00100'), lengthen0, 6)] # 7

print check_proof(lengthen_ok)
  
# erroneous proofs

premise_oob = \
 [(Text('Premise out-of-bounds'), comment), # 0
  (Path('00'), given), # 1
  (Path('01'), given), # 2
  (Path('0'), shorten, 1,3)] # 3, second premise out-of-bounds

print check_proof(premise_oob)

premise_reversed = \
 [(Text('Shorten, premise indices reversed'), comment), # 0
  (Path('00'), given), # 1
  (Path('01'), given), # 2
  (Path('0'), shorten, 2,1)] # 3

print check_proof(premise_reversed)

shorten_0_err = \
 [(Text("Shorten, first premise doesn't match"), comment), # 0
  (Path('10'), given), # 1, formula 10 should be 00
  (Path('01'), given), # 2
  (Path('0'), shorten, 1,2)] # 3

print check_proof(shorten_0_err)

shorten_1_err = \
 [(Text("Shorten, second premise doesn't match"), comment), # 0
  (Path('00'), given), # 1
  (Path('11'), given), # 2, formula 11 should be 01
  (Path('0'), shorten, 1,2)] # 3

print check_proof(shorten_1_err)

lengthen_err = \
 [(Text("Lengthen, premise doesn't match"), comment), # 0
  (Path('00'), given), # 1
  (Path('01'), given), # 2
  (Path('0'), shorten, 1,2), # 3
  (Path('10'), lengthen0, 3), # 4, formula 10 here doesn't match premise 0 at 3
  (Path('101'), lengthen1, 4), # 5
  (Path('1010'), lengthen0, 5), # 6
  (Path('10100'), lengthen0, 6)] # 7

print check_proof(lengthen_err)
