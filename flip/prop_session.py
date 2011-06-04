"""
Prelude for interactive proof session with prop logic from Kaye ch 6
Open session with: python -i prop_session.py
"""

# logic modules for prop logic from Kaye ch 6

import prop_common
import prop_classic

# Combine logics etc. in checker nd

import nd

nd.add_rule_names(prop_common._rule_names, prop_classic._rule_names)
nd.add_rules(prop_common._rules, prop_classic._rules)

# used by save function
nd.add_imports(prop_common._imports, prop_classic._imports)

# import all identifiers that might be used in interactive session

from common import * 
from prop_common import *
from prop_classic import *

from nd import *     # prover commands

from pprint import pprint
