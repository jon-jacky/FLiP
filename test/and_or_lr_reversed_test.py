from prop_session import *
'Propositional logic tests from Kaye, chapter 6, pps. 65 - 69'


ex64 = \
  [(Text('Example 6.4  ~a v b |- ~(a & ~b)'), comment), # 0
   (And(a,Not(b)), assume),  # 1
   (a, ael, 1),              # 2
   (Not(a), assume),         # 3
   (F, contra, 2, 3),        # 4
   (Not(Not(a)),raa, 3, 4),  # 5
   (Not(b),aer, 1),          # 6
   (Or(Not(a),b),given),     # 7
   (b,oer, 7, 5),            # 8
   (F, contra, 8, 6),        # 9
   (Not(And(a,Not(b))), raa, 1, 9)]  # 10

print check_proof(ex64)  # 'print' prints True or False after all proof steps

ex65 = \
  [(Text('Example 6.5  |- ((a & ~b) v ~a) v b'), comment),
    (Not(Or(Or(And(a,Not(b)),Not(a)),b)), assume),
    (b, assume),
    (Or(Or(And(a,Not(b)),Not(a)),b), oir, 2),
    (F, contra, 3,1),
    (Not(b), raa, 2,4),
    (Not(a), assume),
    (Or(And(a,Not(b)),Not(a)), oir, 6),
    (Or(Or(And(a,Not(b)),Not(a)),b), oil, 7),
    (F, contra, 8,1),
    (Not(Not(a)), raa, 6,9),
    (a, ne, 10),
    (And(a,Not(b)), ai, 11,5),
    (Or(And(a,Not(b)),Not(a)), oil, 12),
    (Or(Or(And(a,Not(b)),Not(a)),b), oil, 13),
    (F, contra, 14,1),
    (Not(Not(Or(Or(And(a,Not(b)),Not(a)),b))), raa, 1,15),
    (Or(Or(And(a,Not(b)),Not(a)),b), ne, 16)]

print check_proof(ex65)

ex67 = \
  [(Text('Example 6.7  erroneous a v b |- b, undischarged assumption'), comment),
    (Or(a,b), given),
    (Not(b), assume),
    (Not(a), assume),
    (b, oer, 1,3),
    (F, contra, 4,2),
    (Not(Not(b)), raa, 2,5),
    (b, ne, 6)]

print check_proof(ex67)

ex67a = \
  [(Text("Example 6.7a  dead end a v b |- b, can't discharge assumption"), comment),
    (Or(a,b), given),
    (Not(b), assume),
    (Not(a), assume),
    (b, oer, 1,3),
    (F, contra, 4,2),
    (Not(Not(a)), raa, 3,5),
    (Text('...'), comment)]

print check_proof(ex67a)

ex68 = \
  [(Text('Example 6.8  erroneous a v b |- b, confusion about brackets'), comment),
    (Or(a,b), given),
    (Not(a), assume),
    (Or(Not(a),b), oil, 2),
    (F, contra, 1, 3),
    (Not(Not(a)), raa, 2, 4),
    (a, ne, 5)]

print check_proof(ex68)

ex69 = \
  [(Text('Example 6.9  a & b |- ~(~a v ~b)'), comment),
    (And(a,b), given),
    (a, ael, 1),
    (b, aer, 1),
    (Or(Not(a),Not(b)), assume),
    (Not(a), assume),
    (F, contra, 2,5),
    (Not(Not(a)), raa, 5,6),
    (Not(b), oer, 4,7),
    (F, contra, 3,8),
    (Not(Or(Not(a),Not(b))), raa, 4,9)]

print check_proof(ex69)
