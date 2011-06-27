"""
Prelude for interactive proof session with constructive propositional logic 
from Bornat.
Open session with: python -i prop_constructive_session.py
"""

# logic modules for constructive propositional logic from Bornat

import prop_common
import prop_constructive

# Combine logics etc. in checker nd

import nd

nd.add_rule_names(prop_common._rule_names, prop_constructive._rule_names)
nd.add_rules(prop_common._rules, prop_constructive._rules)

# used by save function
nd.add_imports(prop_common._imports, prop_constructive._imports)

# import all identifiers that might be used in interactive session

from common import * 
from prop_common import *
from prop_constructive import *

from nd import *     # prover commands

from pprint import pprint
