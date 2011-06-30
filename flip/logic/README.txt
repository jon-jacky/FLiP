README.txt for flip/logic

This directory flip/logic (the flip.logic package) contains several
logic modules and session modules.  The logic modules define logics
and the session modules configure interactive Python sessions for
entering and checking proofs in the logics.  This package also
contains the natural deduction proof checker module, nd.py and some
other modules used by the others, for example formula.py Tests for all
the logics defined here are in the flip/test directory (flip.test
package).

To start an interactive proof session for a particular logic from
within the logic directory, invoke its session module.  Use the Python
-i option to get an interactive session that persists after the
session module is executed:
  python -i fol_session.py

In the FLiP distribution, the logic package is in the flip package and
the flip package is in a directory on PYTHONPATH, so we can start an
interactive proof session anywhere, using the Python -m option this way:
  python -i -m flip.logic.fol_session

This organization was used for logic modules and tests created for
FLiP version 1.0.  It is not recommended for new logic packages and
their tests. It is intended that no more logic modules or tests be
added to these directories.  The flip.poset package is a model for 
new logic packages and their tests, see its README.txt.
