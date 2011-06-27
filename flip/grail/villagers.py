"""
Vocabulary used by villagers 
in "She's a witch!" from Monty Pyton and the Holy Grail
"""

from flip.logic.formula import Variable, Function, Relation

# variables

duck = Variable('duck')
girl = Variable('girl')

# functions

class weight(Function):
  def __init__(self, *args):  # seq of args 
    Function.__init__(self, *args)

# relations

class Witch(Relation):
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

class Burn(Relation):
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

class Wood(Relation):
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)

class Floats(Relation):
  def __init__(self, *args):  # seq of args 
    Relation.__init__(self, *args)
