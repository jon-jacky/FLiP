F L i P : Logical Framework in Python

Flip is a logical framework written in Python.  A logical framework is
a library for defining logics and writing applications such as theorem
provers.  One Flip application is a proof checker for entering and
editing proofs in natural deduction style.  Here is some output from
the checker, generated from a Python proof script:

Kaye ex. 9.12, ~Ax.P(x) |- Ex.~P(x)  (0)  Comment
~Ax.P(x)                  (1)  Given
|~Ex.~P(x)                (2)  Assumption
||Let x be arbitrary      (3)  New variable for subproof
|||~P(x)                  (4)  Assumption
|||Ex.~P(x)               (5)  E-Introduction (4)
|||F                      (6)  Contradiction (5) (2)
||~~P(x)                  (7)  Reductio Ad Absurdum (4) (6)
||P(x)                    (8)  Not-Elimination (7)
|Ax.P(x)                  (9)  A-Introduction (3) (8)
|F                       (10)  Contradiction (9) (1)
~~Ex.~P(x)               (11)  Reductio Ad Absurdum (2) (10)
Ex.~P(x)                 (12)  Not-Elimination (11)

The checker can use different logics; Flip comes with several.  You
can add another logic, or add axioms and derived rules, by writing a
module in Python.  Python is both the object language and the
metalanguage.  Formulas, inference rules, and entire proofs are Python
expressions.  Prover commands are Python functions.  The Python
interpreter itself is the only user interface to the proof checker
application.  (It is not necessary to know much Python to use the
checker.)

Flip was undertaken as a Python programming exercise.  It is not
intended to compete with industrial-strength theorem provers such as HOL,
nor with nicely-designed educational provers such as Jape.
That said, the checker is quite capable of working the examples and
exercises in university-level textbooks on logic for computer science or
mathematics, such as Kaye, Huth and Ryan, and Bornat.
