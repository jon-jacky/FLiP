""" 
"She's a witch!" from Monty Python and the Holy Grail
for the FLiP proof checker
Film excerpt at http://www.youtube.com/watch?v=zrzMhU_4m-g
transcript at http://www.sacred-texts.com/neu/mphg/mphg.htm
"""

from fol_session import *
from villagers import *

# "There are ways of telling whether she's a witch."
 
witch = \
  [(Text("She's a witch!"), comment),
   # "What do you do with witches?"  "Burn them!"   
   (A(x, Impl(Witch(x),Burn(x))), given),
   # "Why do witches burn?"  "'Cause they're made of wood!"
   (A(x, Impl(Wood(x),Witch(x))), given),
   # "How do we tell if she's made of wood?"
   # "Does wood sink in water?"  "It floats!"
   (A(x, Impl(Floats(x),Wood(x))), given),
   # "What also floats in water?" "A duck!"  
   (Floats(duck), given),
   # "Exactly!  So, logically ..."
   # "If she weights the same as a duck, she's made of wood!"
   (A(x, A(y, Impl(And(Floats(x),Equal(weight(x),weight(y))),Floats(y)))), given),
   # "We shall use my largest scales. ... Remove the supports!"
   (Equal(weight(duck),weight(girl)), given),
   (A(y, Impl(And(Floats(duck),Equal(weight(duck),weight(y))),Floats(y))), Ae, 5),
   (Impl(And(Floats(duck),Equal(weight(duck),weight(girl))),Floats(girl)), Ae, 7),
   (And(Floats(duck),Equal(weight(duck),weight(girl))), ai, 4,6),
   (Floats(girl), imple, 8,9),
   (Impl(Floats(girl),Wood(girl)), Ae, 3),
   (Wood(girl), imple, 11,10),

   # "A witch!  A witch!"
   (Impl(Wood(girl),Witch(girl)), Ae, 2),
   (Witch(girl), imple, 13,12),

   # "Burn her!  Burn!"
   (Impl(Witch(girl),Burn(girl)), Ae, 1),
   (Burn(girl), imple, 15,14)]

check_proof(witch)
