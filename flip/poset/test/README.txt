README.txt for poset/test

This directory contains tests for the FLiP poset logic.  It
demonstrates the recommended way to organize tests for logic packages
in FLiP.

Put all the tests for a given logic package in their own separate
package (directory containing an __init__.py module).  In each test
module, import the session module for the logic package to be tested
using the form import <package>.<module>.  The modules here test the
modules in the poset package.  They contain: 
  import poset.session
Therefore, to run the tests in this directory, the directory that
contains the logic module to be tested (the poset module) must be on PYTHONPATH.

If this condition is satisfied, the test package can go anywhere.
It is recommended (but not necessary) that the test package go in the
logic package to be tested (in logic package directory).  For example,
this test directory is in the poset directory, it is poset/test.  This
is consistent with typical Python practice for unit tests.

Then, to run the tests in this directory:
  python exercises.py
From elsewhere, if the directory containing poset is on PYTHONPATH:
  python -m poset.test.exercises
From elsewhere, because the poset package is in the flip package, 
which is on PYTHONPATH:
  python -m flip.poset.test.exercises

To do regression testing using the plogdiff command (in the FLiP/bin
directory, described in FLiP/notes/test.txt) you must execute the
test modules from this directory, because the .ref files are here.
  plogdiff exercises

To execute several test modules with one command, invoke the all_test
shell script in this directory.
  ./all_test

(The flip/test directory contains tests for all the logic packages
under flip/logic.  That organization was used for logic modules and
tests created for FLiP version 1.0.  It is not recommended for new
logic packages and their tests. It is intended that no more tests or
logic modules be added to those directories.)

