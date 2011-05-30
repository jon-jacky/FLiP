"""
Import this module to configure checker with poset logic from Kay ch 4
"""

# logic modules

import poset

# checker

import nd

# combine logic modules in checker and preprocess rules to convenient format

nd.logic.rule_names.update(poset._rule_names)
nd.logic.rules.update(poset._rules)

nd.logic.frules = dict([(n,nd.flotten(r)) for (n,r) in nd.logic.rules.items()])

# used by save function

nd.logic.imports += "\n%s" % poset._imports
