README.txt for poset/test

The python modules in this directory belong to the test package, which
belongs to the poset package.  Therefore, there are two ways to
execute the test scripts in this directory.

The simplest way is from the poset directory (the directory above this
one, that contains the test package): python -m test.poset_test

Alternatively, to execute tests from this test directory, put ../poset
on PYTHONPATH by executing the parent_path command here. 
Then: python poset_test.py.  
With ../poset on PYTHONPATH, python -m test.poset_test works here also.

... must still explain .ref, plogdiff, poset_all_test ...
