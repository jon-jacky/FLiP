"""
Prelude for interactive proof session with fol logic from H&R ch 2
Open session with: python -i fol_derived_session.py
"""

# Logic modules for fol logic from H&R ch 2

import prop_common
import prop_derived
import fol

# Combine logics etc. in checker nd

import nd

nd.add_rule_names(prop_common._rule_names, prop_derived._rule_names,
                  fol._rule_names)

nd.add_rules(prop_common._rules, prop_derived._rules, fol._rules)

# used by save function
nd.add_imports(prop_common._imports, prop_derived._imports, fol._imports)

# Import all the identifiers that might be used in the interactive session

from common import * 
from prop_common import *
from prop_derived import *
from fol import *

from nd import *     # prover commands

from pprint import pprint
