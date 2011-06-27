from prop_session import *

top_ok = \
  [(Text('Top rule'),comment),
   (T, top)]

print check_proof(top_ok)

top_err = \
  [(Text('Top rule, formula is not T'),comment),
   (F, top)]

print check_proof(top_err)

