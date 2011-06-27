"""
Logic module for simple formal system example from Kaye 3.1, rules on p. 24.
Formulas are strings of 0,1, can be interpreted as paths through a binary tree.
Rules here resemble Post system rules in def 3.26, p. 36.
This module seems awfully heavyweight for what little it does,
that's a consequence of working with strings in our class-based framework.
The real work here is done by the check methods in the classes x0,x1,y1,y.
"""

import re
from common import Text
from formula import Formula, FormulaPlaceholder

# for syntax check on Path
wff = re.compile(r'[01]*$') # define syntax using regular expression
                               # need $ to match the whole string
# or reduce(operator.and, [ c notin '01' for c in text ])

class Path(Text):
  """
  Path, only formula class in tree logic, just a string of 0,1
  """
  def __init__(self, text):
    Text.__init__(self, text)
    if not wff.match(text): 
      raise SyntaxError, 'path %s does not match [01]*$' % text

  def pform(self):
    return "Path('%s')" % self.text

# Patterns that only appear in rules

class TreeRule(Formula):
  """
  Base class for totree logic rules
  """
  def __init__(self, *args):
    self.pattern = args[0]  # expect placeholder bound to Path('...')

  def pform(self):
    return 'at %s' % self.__class__.__name__   # this is all we've got

  def ppf(self):
    return self.pform()

  def mismatch(self, formula, subformulas, bound, freevars, other_errors, rule_type):
    premise = subformulas[self.pattern].text
    conclusion = formula.text
    if self.check(premise, conclusion):
      return [] # match
    else:
      return [(formula, subformulas[self.pattern], [])] # mismatch

# Tree logic rule subclasses. 
# Messages from pform and ppf look better if class names are lowercase.
# The real work in this module is done by the check methods in these classes.

class x0(TreeRule):
  def __init__(self, *args): 
    TreeRule.__init__(self, *args) 
  def check(self, premise, conclusion):
    return conclusion == premise + '0'

class x1(TreeRule):
  def __init__(self, *args): 
    TreeRule.__init__(self, *args) 
  def check(self, premise, conclusion):
    return conclusion == premise + '1'

class y1(TreeRule):
  def __init__(self, *args): 
    TreeRule.__init__(self, *args)
  def check(self, premise, conclusion):
    return premise[-1] == '0' and conclusion == premise[:-1] + '1'

class y(TreeRule):
  def __init__(self, *args): 
    TreeRule.__init__(self, *args) 
  def check(self, premise, conclusion):
    return conclusion == premise[:-1]

# Define symbol for each rule, short for easy typing at Python interpreter
# Rule symbols are self-evaluating, used to write proof in save file format

lengthen0, lengthen1, shorten = 'lengthen0', 'lengthen1', 'shorten'

# Pretty-print names for rules.
# Each logic module merges its own rule_names with checker.rule_names
# Note _ prefix on _rule_names here makes it private

_rule_names = { lengthen0 : 'Lengthening, 0', lengthen1 : 'Lengthening, 1', 
                shorten: 'Shortening' }

# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
x,y0 = map(FormulaPlaceholder, ['x','y0'])

# Rules here resemble Post system inference rules in def 3.26, p. 36
# Placeholders are processed left to right, bare placeholder must appear first
# Placeholder must bind to whole formula (instance),can't bind to just a string

_rules = { lengthen0: [  x, x0(x) ],
           lengthen1: [  x, x1(x) ],
           shorten:   [ y0, y1(y0), y(y0) ],
         }

# Import statement to write to save file, so it in turn can be imported 

_imports = 'from tree import *'
