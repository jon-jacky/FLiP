"""
Propositional rules used in all sources: Kaye, Huth&Ryan, and Bornat
Supplement this module with more rules from prop_classic (Kaye), 
 prop_derived (H&R), or prop_constructive (Bornat)
Rules here based on Kaye ch 6, defn. 6.3, p. 65, impl. from defn. 6.22, p. 76
See also Bornat, table 3.10, p. 43 and Huth&Ryan, Fig. 1.2, p. 27
"""

from formula import Letter, PrefixLogical, InfixLogical, FormulaPlaceholder

# T, F are just propositional letters that appear in inference rules

T,F = map(Letter, 'TF')

class Not(PrefixLogical):
  """
  Not(a) means ~a in Kaye.  Capitalize Not to distinguish from Python keyword
  """
  def __init__(self, *args):
    PrefixLogical.__init__(self, *args)
    self.symbol = '~'

class And(InfixLogical):
  """
  And(a,b) means a & b in Kaye. Capitalize And, distinguish from Python keyword
  """
  def __init__(self, *args):
    InfixLogical.__init__(self, *args)
    self.symbol = '&'

class Or(InfixLogical):
  """
  Or(a,b) means a v b in Kaye.  Capitalize Or, distinguish from Python keyword
  """
  def __init__(self, *args):
    InfixLogical.__init__(self, *args)
    self.symbol = 'v'

class Impl(InfixLogical):
  """
  Impl(a,b) means a -> b in Kaye
  """
  def __init__(self, *args):
    InfixLogical.__init__(self, *args)
    self.symbol = '->'

# Define symbol for each rule, short for easy typing at Python interpreter
# Rule symbols are self-evaluating, used to write proof in save file format

# Rules for core propositional logic from Kaye
# Use Kaye's nomenclature: raa and contra are Bornat's not-intro and not-elim.
# All the rules here are constructive so they can be used with Bornat.
# Kaye's Not-elim (double negation elim) is not included, it's not constructive
# Or-elim is not included here; Kaye uses different forms than Bornat or H&R

assume, top, ai, ael, aer, oil, oir, contra, raa, impli, imple = \
  'assume','top','ai','ael','aer','oil','oir','contra','raa','impli','imple'

# Pretty-print names for rules.
# Each logic module merges its own rule_names with checker.rule_names
# Note _ prefix on _rule_names here makes it private

_rule_names = { assume: 'Assumption', 
               top: 'Top rule', 
               ai: 'And-Introduction', 
               ael: 'And-Elimination (Left)', 
               aer: 'And-Elimination (Right)', 
               oil: 'Or-Introduction (Left)', 
               oir: 'Or-Introduction (Right)', 
               contra : 'Contradiction', 
               raa: 'Reductio Ad Absurdum',
               impli: 'Implication-Introduction',
               imple: 'Implication-Elimination (Modus Ponens)'
              }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1, m2 = map(FormulaPlaceholder, ('m1','m2'))

_rules = { assume: [[ m1 ]],  # subproof, assumer
           top:    [ T ],
           ai:     [ m1, m2, And(m1,m2) ],
           ael:    [ And(m1,m2), m2 ],
           aer:    [ And(m1,m2), m1 ],
           oil:    [ m2, Or(m1,m2) ],
           oir:    [ m1, Or(m1,m2) ],
           contra: [ m1, Not(m1), F ], 
           raa:    [[ m1, F ], Not(m1) ],      # subproof, discharger
           impli:  [[ m1, m2], Impl(m1,m2) ],  # ditto
           imple:  [ Impl(m1,m2), m1, m2 ] 
         }

# Propositional letters used in proofs
# Use a,b,p,t for Kaye's alpha, beta, psi, theta
a,b,c,d,e,f,p,q,r,t = map(Letter, 'abcdefpqrt')    # a.name = 'a' etc.

# Import statement to write to save file, so it in turn can be imported 
_imports = 'from prop_common import *'
