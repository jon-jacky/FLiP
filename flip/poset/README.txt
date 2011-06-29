README.txt for poset

This directory contains the logic for Partially Ordered Sets, or
"posets" from Kaye chapter 4.   It demonstrates the
recommended way to organize a new logic and its tests for FLiP.

The logic goes into a Python package (a directory containing an
__init__.py file along with the other files).  Here the package is named poset.

This package contains a logic module poset.py that defines the logic
and a session module poset_session.py that sets up an interactive
Python session for entering and checking proofs in the logic.  The
session module loads the logic module and all its dependencies and the
natural deduction proof checker module into a Python session.

To start an interactive proof session from within the poset directory:
 python poset_session.py

If the logic package is in a directory or package that is on
PYTHONPATH, invoke it from anywhere via that package using the python
-m option and the full path.  In the FLiP distribution, the poset
package is in the flip package and the flip package is in a directory
on PYTHONPATH, so we can start an interactive proof session anywhere this way: 
  python -m flip.poset.poset_session

The tests for this package are in the test package under this
package (poset/test directory containing an __init__.py module)

A logic package need not be in the flip package.  It can be
entirely outside the FLiP development directories.

(The flip/logic directory (the flip.logic package) contains several
logic modules and session modules.  Their tests are in the flip/test
directory (flip.test package). That organization was used for logic
modules and tests created for FLiP version 1.0 and is not recommended
for new logic packages and their tests. It is intended that no more
logic modules or tests be added to those directories.  The poset
modules and their tests are also present in those directories but this
package is provided to show how logic packages and their tests should
be organized from now on.)