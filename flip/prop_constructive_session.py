"""
Prelude for interactive proof session with constructive propositional logic 
from Bornat.
Open session with: python -i prop_constructive_session.py
"""

# logic modules

from common import * 
from prop_common import *
from prop_constructive import *

# checker

import prop_constructive_config   # configure checker with logic modules
from nd import *     # prover commands

# other useful items

from pprint import pprint
