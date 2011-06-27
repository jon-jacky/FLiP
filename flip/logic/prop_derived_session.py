"""
Prelude for interactive proof session with prop logic from Huth and Ryan ch. 1
Open session with: python -i prop_derived_session.py
"""

# logic modules for prop logic from Huth and Ryan ch. 1

import prop_common
import prop_derived

# Combine logics etc. in checker nd

import nd

nd.add_rule_names(prop_common._rule_names, prop_derived._rule_names)
nd.add_rules(prop_common._rules, prop_derived._rules)

# used by save function
nd.add_imports(prop_common._imports, prop_derived._imports)

# import all identifiers that might be used in interactive session

from common import * 
from prop_common import *
from prop_derived import *

from nd import *     # prover commands

from pprint import pprint
