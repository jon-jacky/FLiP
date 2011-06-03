"""
Prelude for interactive proof session with fol logic from Kaye ch 9
Open session with: python -i fol_session.py
"""

# First, configure checker nd with logic modules for fol logic from Kaye ch 9

import prop_common
import prop_classic
import fol

import nd

# combine logics etc. in checker

nd.add_rule_names(prop_common._rule_names, prop_classic._rule_names,
                  fol._rule_names)

nd.add_rules(prop_common._rules, prop_classic._rules, fol._rules)

# used by save function

nd.add_imports(prop_common._imports, prop_classic._imports, fol._imports)

# Next, import all the identifiers from logic modules and nd into session

from common import * 
from prop_common import *
from prop_classic import *
from fol import *

from nd import *     # prover commands

# import other useful identifiers

from pprint import pprint
