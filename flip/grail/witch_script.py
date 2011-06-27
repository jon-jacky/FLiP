""" 
"She's a witch!" from Monty Python and the Holy Grail
for the FLiP proof checker.
Film excerpt at http://www.youtube.com/watch?v=zrzMhU_4m-g
transcript at http://www.sacred-texts.com/neu/mphg/mphg.htm
"""

from flip.logic.fol_session import *
from villagers import *

# "There are ways of telling whether she's a witch."
 
witch_axioms = \
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
   (Equal(weight(duck),weight(girl)), given)]

check_proof(witch_axioms)
rapply(Ae,5,duck)
rapply(Ae,7,girl)
rapply(ai,4,6)
rapply(imple,8,9)
rapply(Ae,3,girl)
rapply(imple,11,10)
rapply(Ae,2,girl)
rapply(imple,13,12)
rapply(Ae,1,girl)
rapply(imple,15,14)

# "A witch!  A witch! Burn her!  Burn!"
