""" 
First-order logic from Kaye ch 9, rules from defn. 9.1, p. 122
This logic is to be used with the propositional logic defined in
prop_common and (optionally) other prop modules.
"""

from copy import copy  # needed to copy bound variable list

from formula import Letter, Variable, Function, Relation, InfixRelation, Quantifier, New, Let, Subst, SubstAll, NotIn, FormulaPlaceholder, TermPlaceholder, VariablePlaceholder

# Kaye's functions, defs 9.1, 9.2

class f(Function):
  """
  Example of Function, used in ex 9.18, ex 9.28
  """
  def __init__(self, *args):  # seq of args 
    Function.__init__(self, *args)

class g(Function):
  """
  Another function, stand-in for arithmetic expressions in Kaye etc.
  """
  def __init__(self, *args):  # seq of args 
    Function.__init__(self, *args)

class h(Function):
  """
  One more function
  """
  def __init__(self, *args):  # seq of args 
    Function.__init__(self, *args)

# Kaye's relations, defs 9.1, 9.4

class P(Relation):
  """
  Example of relation, used in Kaye ex 9.16, 9.17 , Huth and Ryan sect. 2.3
  """
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

class Q(Relation):
  """
  Example of relation, not used by Kaye, but used by Huth and Ryan sect. 2.3
  """
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

class R(Relation):
  """
  Example of relation, used in Kaye def 9.4, ex 9.16, 9.17
  """
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

class S(Relation):
  """
  Example of relation, used in Kaye def 9.18
  """
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

# Kaye also uses relations theta, psi, phi, sigma
#  but never more than two different relations in a proof so R and P will do

# Special relations, occur in inference rules

class Equal(InfixRelation):
  """
  Kaye's equality relation = , defs 9.1, 9.4, ex 9.16 - 9.20
  """
  def __init__(self, *args):
    InfixRelation.__init__(self, *args)
    self.symbol = '='

# Quantifiers

class A(Quantifier):
  """
  Universal quantifier, Kaye's defs 9.1, 9.4
  """
  def __init__(self, *args):
    Quantifier.__init__(self, *args)

class E(Quantifier):
  """
  Existential quantifier, Kaye's defs 9.1, 9.4
  """
  def __init__(self, *args):
    Quantifier.__init__(self, *args)

# Placeholder patterns used in rules
# use each key S1 etc. in subformulas dictionary for all instances of its class

s1key, p1key, q1key = map(FormulaPlaceholder, ['S1','P1','Q1'])

class S1(Subst):
  def __init__(self, arg):
    self.pattern = s1key
    Subst.__init__(self, arg)

class P1(SubstAll):
  def __init__(self, arg):
    self.pattern = p1key
    Subst.__init__(self, arg)

class Q1(NotIn):
  def __init__(self, arg):
    self.pattern = q1key
    NotIn.__init__(self, arg)

# Define symbol for each rule, short for easy typing at Python interpreter
# Rule symbols are self-evaluating, used to write proof in save file format

refl,sym,trans,sub,new,let,Ee,Ei,Ae,Ai = \
  'refl','sym','trans','sub','new','let','Ee','Ei','Ae','Ai'

# Pretty-print names for rules.
# Note _ prefix on _rule_names here makes it private

_rule_names = { refl : 'Reflexivity',
                sym : 'Symmetry',
                trans : 'Transitivity',
                sub : 'Substitution' ,
                Ae : 'A-Elimination',
                Ei : 'E-Introduction', 
                new : 'New variable for subproof',
                Ai : 'A-Introduction',
                let : 'Assumption, with new variable',
                Ee : 'E-Elimination', 
             }
# Inference rules, dictionary of rule symbol and list of formulas:
#  list of premises, then conclusion last
# Subproofs in inference rules are nested lists

# Placeholders used in rules
t1,t2,s1  = map(TermPlaceholder, ('t1','t2','s1'))
v1,v2     = map(VariablePlaceholder, ('v1','v2'))

_rules = { refl:  [ Equal(t1,t1) ],
           sym:   [ Equal(t1,s1), Equal(s1,t1) ],
           trans: [ Equal(t1,s1), Equal(s1,t2), Equal(t1,t2) ],    
           sub :  [ Equal(t1,s1), S1(t1), S1({t1:s1}) ],
           Ae  :  [ A(v1,P1(v1)), P1({v1:t1}) ],
           Ei  :  [ S1(t1), E(v1, S1({t1:v1})) ],
           new :  [[ New(v1) ]],
           Ai  :  [[ New(v1), P1(v1) ], A(v1, P1(v1)) ],
           let :  [[ Let(v1,P1(v1)) ]],
           Ee  :  [ E(v1, P1(v1)), [Let(v2,P1({v1:v2})), Q1({v2:None})], Q1({v2:None}) ]
         }

# Variables, letters used in proofs
# recall a,b,c,d,f, t are propositional Letters in prop_session, but that's ok 
a,b,c,d,t,u,v,w,x,y,z = map(Variable, 'abcdtuvwxyz')  # u.name = 'u' etc
e,p,q,r = map(Letter, 'epqr')

# Import statement to write to save file, so it in turn can be imported 

_imports = 'from fol import *'
