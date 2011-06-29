README.txt for poset/test

This directory demonstrates the recommended way to organize tests for
new logic packages in FLiP: put the tests in a package (subdirectory
with an __init__.py file) under the logic package to be tested.

The python modules in this directory are for testing the poset
package.  They belong to the test package, which belongs to the poset
package.  

Here are two ways to execute the test scripts in this directory:

The simplest way is from the poset directory (the directory above this
one, that contains the test package): python -m test.poset_test

Alternatively, to execute tests from this test directory, put the
parent directory .. on PYTHONPATH (for example by executing the
parent_path command, it's in FLiP/bin).  Then: python poset_test.py.
Also: with .. on the PYTHONPATH, python -m test.poset_test works here
too.

To do regression testing using the plogdiff or the all_test commands
(in the FLiP/bin directory, described in FLiP/notes/test.txt) you must
execute the commands from this directory, and the parent directory
.. must be on the PYTHONPATH.

(The flip/test directory contains tests for all the logic packages
under flip/logic.  That organization was used for logic modules and
tests created for FLiP version 1.0 and is not recommended for new
logic packages and their tests. It is intended that no more tests or
logic modules be added to those directories.)
