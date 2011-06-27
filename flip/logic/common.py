"""
Classes and rules common to all logics: Text class, comment and given rules.
"""

from formula import Formula, FormulaPlaceholder, check_count

class Text(Formula):
  """
  Text, used for comments in proofs, also base class for formulas in tree logic
  """

  def __init__(self, *args):
    check_count(self, 1, *args)
    if not isinstance(args[0], str):
      raise TypeError, 'argument %s is not a string' % text
    self.text = args[0]

  def pform(self):
    return "Text('%s')" % self.text

  def ppf(self):
    return self.text

  def free(self):  # for compatibility, comment text appears in formula place
    return []  # Text is a constant not a variable

# Define a symbol for each rule.
# Rule symbols are self-evaluating, used to write proof in save file format.
 
(comment, given) = ('comment', 'given')

# Pretty-print names for rules.

rule_names = { comment: 'Comment', given : 'Given' }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
m1 = FormulaPlaceholder('m1')

rules = { 
           comment: [ m1 ],   # match any formula
           given:   [ m1 ]
        }
          
# Import statement to write to save file, so it in turn can be imported 

imports = 'from common import *' 
