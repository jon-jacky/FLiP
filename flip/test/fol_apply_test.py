from fol_session import *
from command_wrapper import *

# This way prints Apply(), not generated formula

ex917 = \
  [(Text('From example 9.17'), comment),
   (Not(R(a)), given),
   (Equal(a,x), given),
   (Apply(),sub,2,1)]

print check_proof(ex917)
print

# This way prints generated formula at prapply step

def ex917a():
  pcheckp(Text('From example 9.17'), comment)
  pcheckp(Not(R(a)), given)
  pcheckp(Equal(a,x), given)
  prapply(sub,2,1)

clear()
ex917a()
print

def ex917a():
  pcheckp(Text('Like ex, 9.17 but substitution term is more complex'), comment)
  pcheckp(Not(R(a)), given)
  pcheckp(Equal(a,f(x,(g(x,y)))), given)
  prapply(sub,2,1)

clear()
ex917a()
print

def ex917x():
  pcheckp(Text('like ex. 9.17, but eqn does not match premise, so no substitution'), comment)
  pcheckp(Not(R(a)), given)
  pcheckp(Equal(b,x), given)
  prapply(sub,2,1)

clear()
ex917x()
print

def ex914():
  checkp(Text('Valid E-elim, Kaye ex. 9.14, Ax.~P(x) |- ~Ex.P(x)'), comment)
  checkp(A(x, Not(P(x))), given)
  checkp(E(x, P(x)), assume)
  checkp(Let(a,P(a)), let)
  prapply(Ae, 1, a) # for Ae must provide only replacement term t1 for{v1:t1}
  prapply(contra, 3,4)
  prapply(Ee, 2,3,5) # for Ee we needn't provide anything
  prapply(raa, 2,6)

clear()
ex914()
print

def ex914x1():
  checkp(Text('Erroneous ex. 9.14, fail at A-elim, omit term'), comment)
  checkp(A(x, Not(P(x))), given)
  checkp(E(x, P(x)), assume)
  checkp(Let(a,P(a)), let)
  prapply(Ae, 1) # missing otherdata, term a
  prapply(contra, 3,4)
  prapply(Ee, 2,3,5) # for Ee we needn't provide anything
  prapply(raa, 2,6)

clear()
ex914x1()
print


def ex914x2():
  checkp(Text('Erroneous 9.14, wrong term in Ae, fail at contra'), comment)
  checkp(A(x, Not(P(x))), given)
  checkp(E(x, P(x)), assume)
  checkp(Let(a,P(a)), let)
  prapply(Ae, 1, b) # for Ae must provide only replacement term t1 for{v1:t1}
  prapply(contra, 3,4)
  prapply(Ee, 2,3,5) # for Ee we needn't provide anything
  prapply(raa, 2,6)

clear()
ex914x2()
print

def ex91Ae():
  pcheckp(Text('A-elim from Kaye ex 9.10'), comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1, w) # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91Ae()
print

def ex91AeX1():
  pcheckp(Text('A-elim like Kaye ex 9.10, but same term'), comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1, x) # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91AeX1()
print

def ex91AeX2():
  pcheckp(Text('A-elim like Kaye ex 9.10, but more complicated term'), comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1, f(x,g(x,y))) # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91AeX2()
print

def ex91AeX3():
  pcheckp(Text('A-elim like Kaye ex 9.10, but missing term'), comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1) # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91AeX3()
print

def ex91AeX4():
  pcheckp(Text('A-elim like Kaye ex 9.10, but number instead of term'),comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1, 2) # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91AeX4()
print

def ex91AeX4():
  pcheckp(Text('A-elim like Kaye ex 9.10, but string instead of term'),comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1, "w") # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91AeX4()
print


def ex91AeX5():
  pcheckp(Text('A-elim like Kaye ex 9.10, but dictionary instead of term'),comment)
  pcheckp(A(x,E(v,Equal(v,x))), given)
  prapply(Ae, 1, {x:v}) # for Ae must provide only replacement term t1 for {v1:t1}

clear()
ex91AeX5()
print

def p111Ae():
  pcheckp(Text('P(t), Ax.(P(x) -> ~Q(x)) |- ~Q(t) using Ae from H&R p. 111'),comment)
  pcheckp(P(t), given)
  pcheckp(A(x,Impl(P(x),Not(Q(x)))), given)
  prapply(Ae, 2, t) # for Ae must provide only replacement term t1 for {v1:t1}
  prapply(imple, 3,1)

clear()
p111Ae()
print


def p111AeX1():
  pcheckp(Text('P(x), Ax.(P(x) -> ~Q(x)) |- ~Q(x) same term'),comment)
  pcheckp(P(x), given)
  pcheckp(A(x,Impl(P(x),Not(Q(x)))), given)
  prapply(Ae, 2, x) # for Ae must provide only replacement term t1 for {v1:t1}
  prapply(imple, 3,1)

clear()
p111AeX1()
print


def p111AeX2():
  pcheckp(Text('P(...), Ax.(P(x) -> ~Q(x)) |- ~Q(...) more complex term'),comment)
  pcheckp(P(f(x,g(x,y))), given)
  pcheckp(A(x,Impl(P(x),Not(Q(x)))), given)
  prapply(Ae, 2, f(x,g(x,y))) # for Ae must provide only replacement term t1 for {v1:t1}
  prapply(imple, 3,1)

clear()
p111AeX2()
print

# This example suggests we could let otherdata t1 default to v1

def p114AeEi():
  pcheckp(Text('Ax.P(x) -> Ex.P(x) using Ae, Ei from H&R p. 114'), comment)
  pcheckp(A(x,P(x)), given)
  prapply(Ae, 1, x) # for Ae must provide only replacement term t1 for {v1:t1}
  prapply(Ei, 2, {x:x})  # for Ei must provide {t1:v1}, here just {x:x}

clear()
p114AeEi()
print


def p114AeEiX1():
  pcheckp(Text('Ax.P(x) -> Ey.P(y) but with more complicated intermediate term'), comment)
  pcheckp(A(x,P(x)), given)
  prapply(Ae, 1, f(x,g(x,y))) # for Ae must provide only replacement term t1 for {v1:t1}
  prapply(Ei, 2, {f(x,g(x,y)):y})  # for Ei must provide {t1:v1}, here just {x:x}

clear()
p114AeEiX1()
print

def ex91Ei():
  pcheckp(Text('E-intro, Kaye ex 9.10, except here substitute all occurrences of bound variable'), comment)
  pcheckp(Equal(x,x), refl)
  prapply(Ei, 1, {x:v}) # for Ei must provide {t1:v1}

clear()
ex91Ei()
print


def ex91EiXa():
  pcheckp(Text('E-intro, Kaye ex 9.10, except here substitute with more complicated term'), comment)
  pcheckp(Equal(f(x,g(x,y)),z), given)
  prapply(Ei, 1, {f(x,g(x,y)):v}) # for Ei must provide {t1:v1}

clear()
ex91EiXa()
print

def ex91EiX1():
  pcheckp(Text('Erroneous E-intro, like Kaye ex 9.10, term not dict given'), comment)
  pcheckp(Equal(x,x), refl)
  prapply(Ei, 1, x) # for Ei must provide {t1:v1}

clear()
ex91EiX1()
print

def ex91EiX2():
  pcheckp(Text('Erroneous E-intro, like Kaye ex 9.10, term and variable reversed'), comment)
  pcheckp(Equal(x,x), refl)
  pcheckp(Equal(f(x,g(x,y)),z), given)
  prapply(Ei, 1,  {v:f(x,g(x,y))}) # for Ei must provide {t1:v1}

clear()
ex91EiX2()
print

def ex91EiX3():
  pcheckp(Text('Erroneous E-intro, like Kaye ex 9.10, number not variable given'), comment)
  pcheckp(Equal(x,x), refl)
  pcheckp(Equal(f(x,g(x,y)),z), given)
  prapply(Ei, 1,  {f(x,g(x,y)):1}) # for Ei must provide {t1:v1}

clear()
ex91EiX3()
print

def ex91EiX4():
  pcheckp(Text('Erroneous E-intro, like Kaye ex 9.10, string not variable given'), comment)
  pcheckp(Equal(x,x), refl)
  pcheckp(Equal(f(x,g(x,y)),z), given)
  prapply(Ei, 1,  {f(x,g(x,y)):"v"}) # for Ei must provide {t1:v1}

clear()
ex91EiX4()
print

def ex912():
  checkp(Text('Valid A-intro, Kaye ex. 9.12, ~Ax.P(x) |- Ex.~P(x)'), comment)
  checkp(Not(A(x, P(x))), given)
  checkp(Not(E(x, Not(P(x)))), assume)
  checkp(New(x), new)
  checkp(Not(P(x)), assume)
  prapply(Ei, 4, {x:x}) # for Ei must provide {t1:v1}, here just {x:x}
  prapply(contra, 5,2)
  prapply(raa, 4,6)
  prapply(ne, 7)
# prapply(Ai, 3,8, x) # for Ae must provide only replacement term t1 for{v1:t1} NOT!
  prapply(Ai, 3,8)    # replacement term no longer needed for Ai rule
  prapply(contra, 9,1)
  prapply(raa, 2,10)
  prapply(ne, 11)

clear()
ex912()
print


def ex912X1():
  checkp(Text('Erroneous Kaye ex. 9.12, replace contra rule with ai, fail at following raa'), comment)
  checkp(Not(A(x, P(x))), given)
  checkp(Not(E(x, Not(P(x)))), assume)
  checkp(New(x), new)
  checkp(Not(P(x)), assume)
  prapply(Ei, 4, {x:x}) # for Ei must provide {t1:v1}, here just {x:x}
  prapply(ai, 5,2)  # BUG should be (contra, 5,2)
  prapply(raa, 4,6)
  prapply(ne, 7)
# prapply(Ai, 3,8, x) # for Ae must provide only replacement term t1 for{v1:t1} NOT!
  prapply(Ai, 3,8)    # replacement term no longer needed for Ai rule
  prapply(contra, 9,1)
  prapply(raa, 2,10)
  prapply(ne, 11)

clear()
ex912X1()
print

def ex912X2():
  checkp(Text('Erroneous Kaye ex. 9.12, replace contra rule with ael, takes 1 not 2 premises'), comment)
  checkp(Not(A(x, P(x))), given)
  checkp(Not(E(x, Not(P(x)))), assume)
  checkp(New(x), new)
  checkp(Not(P(x)), assume)
  prapply(Ei, 4, {x:x}) # for Ei must provide {t1:v1}, here just {x:x}
  prapply(ael, 5,2) # BUG was contra, ael only takes one premise
  prapply(raa, 4,6)
  prapply(ne, 7)
# prapply(Ai, 3,8, x) # for Ae must provide only replacement term t1 for{v1:t1} NOT!
  prapply(Ai, 3,8)    # replacement term no longer needed for Ai rule
  prapply(contra, 9,1)
  prapply(raa, 2,10)
  prapply(ne, 11)

clear()
ex912X2()
print

def ex912X3():
  checkp(Text('Erroneous Kaye ex. 9.12, replace Ai rule with Ae, change to 1 not 2 premises'), comment)
  checkp(Not(A(x, P(x))), given)
  checkp(Not(E(x, Not(P(x)))), assume)
  checkp(New(x), new)
  checkp(Not(P(x)), assume)
  prapply(Ei, 4, {x:x}) # for Ei must provide {t1:v1}, here just {x:x}
  prapply(contra, 5,2)
  prapply(raa, 4,6)
  prapply(ne, 7)
# prapply(Ai, 3, x) # for Ae must provide only replacement term t1 for{v1:t1} NOT!
  prapply(Ae, 3) # BUG, was (Ai 3,8)
  prapply(contra, 9,1)
  prapply(raa, 2,10)
  prapply(ne, 11)

clear()
ex912X3()
print


def ex912X0():
  checkp(Text('Kaye ex. 9.12 but with unnecessary otherdata x in Ai step'), comment)
  checkp(Not(A(x, P(x))), given)
  checkp(Not(E(x, Not(P(x)))), assume)
  checkp(New(x), new)
  checkp(Not(P(x)), assume)
  prapply(Ei, 4, {x:x}) # for Ei must provide {t1:v1}, here just {x:x}
  prapply(contra, 5,2)
  prapply(raa, 4,6)
  prapply(ne, 7)
  prapply(Ai, 3,8, x) # for Ae must provide only replacement term t1 for{v1:t1} NOT! But in this test case include it anyway
  # prapply(Ai, 3,8)    # replacement term no longer needed for Ai rule
  prapply(contra, 9,1)
  prapply(raa, 2,10)
  prapply(ne, 11)

clear()
ex912X0()
print

def ex91EiX5():
  pcheckp(Text('Erroneous E-intro, like Kaye ex 9.10, missing {t1:v1}'), comment)
  pcheckp(Equal(x,x), refl)
  pcheckp(Equal(f(x,g(x,y)),z), given)
  prapply(Ei, 1) # for Ei must provide {t1:v1}

clear()
ex91EiX5()
print
