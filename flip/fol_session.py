"""
Prelude for interactive proof session with fol logic from Kaye ch 9
Open session with: python -i fol_session.py
"""

# logic modules

from common import * 
from prop_common import *
from prop_classic import *
from fol import *

# checker

import fol_config   # configure checker with logic modules
from nd import *     # prover commands

# other useful items

from pprint import pprint
