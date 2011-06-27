"""
Prelude for interactive proof session with tree logic from Kaye ch 3
Open session with: python -i tree_session.py
"""

# Logic module for tree logic from Kaye ch 3

import tree

# Put logics etc. in checker nd

import nd

nd.add_rule_names(tree._rule_names)

nd.add_rules(tree._rules)

# used by save function
nd.add_imports(tree._imports)

# Import all the identifiers that might be used in the interactive session

from common import *
from tree import *

from nd import *  # prover commands

from pprint import pprint
