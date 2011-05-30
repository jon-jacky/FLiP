"""
Configure checker with logic modules for fol logic from Kaye ch 9
"""

# logic modules

import prop_common
import prop_classic
import fol

# checker

import nd

# combine logic modules in checker and preprocess rules to convenient format

nd.logic.rule_names.update(prop_common._rule_names)
nd.logic.rule_names.update(prop_classic._rule_names)
nd.logic.rule_names.update(fol._rule_names)
nd.logic.rules.update(prop_common._rules)
nd.logic.rules.update(prop_classic._rules)
nd.logic.rules.update(fol._rules)

nd.logic.frules = dict([(n,nd.flotten(r)) for (n,r) in nd.logic.rules.items()])

# used by save function

nd.logic.imports += "\n%s\n%s\n%s" % \
  (prop_common._imports, prop_classic._imports, fol._imports)
