README.txt for poset/test

This directory contains tests for the FLiP poset logic.  It
demonstrates the recommended way to organize tests for logic packages
in FLiP.

Put all the tests for a given logic package in their own separate
package (directory containing an __init__.py module).  In each test
module, import the session module for the logic package to be tested
using the form import <package>.<module>.  The modules here test the
modules in the poset package.  They contain: 
  import poset.poset_session

Then, to run the tests, put the directory containing the package to be
tested on PYTHONPATH.  To run the tests in this directory, put the
directory containing the poset package on PYTHONPATH.

If these conditions are satisfied, the test package can go anywhere.
It is recommended (but not necessary) that the test package go in the
logic package to be tested (in logic package directory).  For example,
this test directory is in the poset directory, it is poset/test.  This
is consistent with typical Python practice for unit tests.

To execute test modules from within this directory: python poset_test.py.  
To execute test modules from elsewhere, use the Python -m option and
the test package name, as long as the test package is in a directory
on PYTHONPATH.  For example, if the test package is in the poset
package (as it is here), in the poset package directory:
 python -m test.poset_test

To do regression testing using the plogdiff command (in the FLiP/bin
directory, described in FLiP/notes/test.txt) you must execute the
test modules from this directory, because the .ref files are here.

To execute several test modules with one command, invoke the all_test
shell script in this directory.

(The flip/test directory contains tests for all the logic packages
under flip/logic.  That organization was used for logic modules and
tests created for FLiP version 1.0.  It is not recommended for new
logic packages and their tests. It is intended that no more tests or
logic modules be added to those directories.)
