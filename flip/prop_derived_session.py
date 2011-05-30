"""
Prelude for interactive proof session with prop logic from Huth and Ryan ch. 1
Open session with: python -i prop_derived_session.py
"""

# logic modules

from common import * 
from prop_common import *
from prop_derived import *

# checker

import prop_derived_config   # configure checker with logic modules
from nd import *     # prover commands

# other useful items

from pprint import pprint
