"""
Prelude for interactive proof session with poset logic from Kaye ch 4
Open session with: python -i poset_session.py
"""

# logic module for poset logic from Kaye ch 4

import poset

# Put logics etc. in checker nd

import nd

nd.add_rule_names(poset._rule_names)

nd.add_rules(poset._rules)

# used by save function
nd.add_imports(poset._imports)

# Import all the identifiers that might be used in the interactive session

from common import * 
from poset import *

from nd import *      # prover commands

from pprint import pprint
