"""
Configure checker with logic modules for tree logic from Kaye ch 3
"""

# logic modules
import tree

# checker
import nd

# combine logic modules in checker and preprocess rules to convenient format
nd.logic.rule_names.update(tree._rule_names)
nd.logic.rules.update(tree._rules)
nd.logic.frules = dict([(n,nd.flotten(r)) for (n,r) in nd.logic.rules.items()])

# used by save function
nd.logic.imports += "\n%s" % tree._imports
