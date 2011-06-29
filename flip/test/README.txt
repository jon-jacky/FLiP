README.txt for flip/test

This directory flip/test (the flip.test package) contains tests for the several
logics defined in the flip/logic directory (the flip.logic package).

To execute these tests, put the ../logic directory on the PYTHONPATH
by executing the cpath script in this directory.  Then execute a test
script like this: python prop_test.py.  Execute a regression test that
compares test script output to save output like this: source plogdiff
prop_test.  Execute a collection of regression tests like this:
source prop_all_test

This organization was used for logic modules and tests created for
FLiP version 1.0.  It is not recommended for new logic packages and
their tests. It is intended that no more logic modules or tests be
added to these directories.  The flip.poset package is a model for 
new logic packages and their tests, see its README.txt.
