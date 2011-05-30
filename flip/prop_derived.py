"""
Additional propositional logic rules from Huth and Ryan, Fig 1.2, p. 27.
Also copy rule on top p. 20.  Supplements rules in prop_common.
This module is an alternative to prop_classic or prop_constructive.
"""

from formula import FormulaPlaceholder
from prop_common import Not, Or, F, Impl

# Additional rules for propositional logic from Huth and Ryan.
# Not a minimal collection of rules.  Some of these are derived rules.
# H&R not-intro, not-elim already appear in prop_common as raa, contra.
# assume_case,ore rules here also appeaer in prop_constructive with same names.
# pbc, fe rules here appear as contra_classic, contra_con in prop_constructive

# Define symbol for each rule, short for easy typing at Python interpreter
# Rule symbols are self-evaluating, used to write proof in save file format

assume_case, ore, fe, nne, mt, nni, pbc, lem, copy = \
  'assume_case', 'ore', 'fe', 'nne', 'mt', 'nni', 'pbc', 'lem', 'copy'

# Pretty-print names for rules.
# Each logic module merges its own rule_names with checker.rule_names
# Note _ prefix on _rule_name here makes it private

_rule_names = { assume_case: 'Assumption (next case)',
                ore: 'Or-Elimination',
                fe:  'False-Elimination',
                nne: 'Double-negation Elimination',
                mt:  'Modus Tollens',
                nni: 'Double-negation Introduction',
                pbc: 'Proof By Contradiction',
                lem: 'Excluded Middle',
                copy:'Copy'
              }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1, m2, m3 = map(FormulaPlaceholder, ('m1','m2','m3'))

_rules = { assume_case:  [[],[ m1 ]],  # subproof, replace top assumption
           ore: [ Or(m1,m2), [ m1,m3 ], [ m2,m3 ], m3 ], #subproofs, discharger
           fe:  [ F, m1 ],             # from False, infer anything!
           nne: [ Not(Not(m1)), m1 ],
           mt:  [ Impl(m1,m2), Not(m2), Not(m1) ],
           nni: [ m1, Not(Not(m1)) ],
           pbc: [[ Not(m1), F ], m1 ], # subproof, discharger
           lem: [ Or(m1, Not(m1)) ],
           copy:[ m1, m1 ]
         }

# Import statement to write to save file, so it in turn can be imported 

_imports = 'from prop_derived import *'
