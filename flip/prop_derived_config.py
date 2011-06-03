"""
Configure checker with logic modules for prop logic from Huth and Ryan, ch. 1
"""

# logic modules

import prop_common
import prop_derived

# checker

import nd

# combine logic modules in checker and preprocess rules to convenient format

nd.logic.rule_names.update(prop_common._rule_names)
nd.logic.rule_names.update(prop_derived._rule_names)
nd.logic.rules.update(prop_common._rules)
nd.logic.rules.update(prop_derived._rules)

nd.logic.frules = dict([(n,nd.flotten(r)) for (n,r) in nd.logic.rules.items()])

# used by save function

nd.logic.imports += "\n%s\n%s" % (prop_common._imports, prop_derived._imports)