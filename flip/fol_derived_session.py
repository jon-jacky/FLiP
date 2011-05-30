"""
Prelude for interactive proof session with fol logic from H&R ch 2
Open session with: python -i fol_derived_session.py
"""

# logic modules

from common import * 
from prop_common import *
from prop_derived import *
from fol import *

# checker

import fol_derived_config   # configure checker with logic modules
from nd import *     # prover commands

# other useful items

from pprint import pprint
