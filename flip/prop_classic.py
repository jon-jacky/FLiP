"""
Additional propositional logic rules from Kaye, ch 6, defn. 6.3, p. 65.
Supplements rules in prop_common.
This module is an alternative to prop_derived or prop_constructive.
"""

from formula import FormulaPlaceholder
from prop_common import Not, Or

# Additional rules for propositional logic from Kaye
# Or-elim. rules here are allowed in both classic and constructive logics,
#  but both Bornat and H&R use a different form.
# Also Not-elim is here, only classical, not allowed in constructive.

# Define symbol for each rule, short for easy typing at Python interpreter
# Rule symbols are self-evaluating, used to write proof in save file format

oel, oer, ne = 'oel', 'oer', 'ne'

# Pretty-print names for rules.
# Each logic module merges its own rule_names with checker.rule_names
# Note _ prefix on _rule_names here makes it private

_rule_names = { oel: 'Or-Elimination (Left)', 
                oer: 'Or-Elimination (Right)',
                ne: 'Not-Elimination',
              }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1, m2 = map(FormulaPlaceholder, ('m1','m2'))

_rules = { oel:    [ Or(m1,m2), Not(m1), m2 ],
           oer:    [ Or(m1,m2), Not(m2), m1 ],
           ne:     [ Not(Not(m1)), m1 ]
         }

# Import statement to write to save file, so it in turn can be imported 

_imports = 'from prop_classic import *'
