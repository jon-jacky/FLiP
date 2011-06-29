README.txt for grail

This directory contains a case study inspired by the "She's a witch!"
scene from Monty Python and the Holy Grail.  It demonstrates the
recommended way to organize a case study that uses FLiP.

The case study goes into a Python package (a directory containing an
__init__.py file along with the other files).  Here the package is named grail.

The modules in the study import FLiP logic modules using their full
path in the flip package, for example:  from flip.logic.fol_session import *

To invoke a module in the case study from within the case study directory:
 python witch.py

If the case study package is in a directory or package that is on
PYTHONPATH, invoke it via that package using the python -m option and
the full path.  In the FLiP distribution, the grail package is in the
flip package and the flip package is in a directory on PYTHONPATH, so
we can invoke the witch module this way:
 python -m flip.grail.witch

A case study package need not be in the flip package.  It can be
entirely outside the FLiP development directories.

