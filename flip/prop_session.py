"""
Prelude for interactive proof session with prop logic from Kaye ch 6
Open session with: python -i prop_session.py
"""

# logic modules

from common import * 
from prop_common import *
from prop_classic import *

# checker

import prop_config   # configure checker with logic modules
from nd import *     # prover commands

# other useful items

from pprint import pprint
