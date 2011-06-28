README.txt for grail

This directory contains a case study inspired by the "She's a
witch!"  scene from Monty Python and the Holy Grail.

This directory demonstrates the recommended way to organize a case
study for FLiP.  A case study is a collection of proofs (that is,
Python modules) and possibly other files (.txt files for documentation
etc.) that use logics already defined in FLiP.

The case study goes into a Python package (a directory containing an
__init__.py file along with the other files).  

The modules in the study import FLiP logic modules using their full
path in the flip package, for example: 
 from flip.logic.fol_session import *

To invoke a module in the case study from within the case study directory:
 python witch.py
If the case study package is in a directory or package that is on PYTHONPATH:
 python -m flip.grail.witch

To invoke a module in the case study, the directory containing the
flip package must by on the PYTHONPATH.  The case study package need
not be in the flip package.  It can be entirely outside the FLiP
development directories. 




