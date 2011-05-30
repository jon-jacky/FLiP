"""
Natural deduction proof checker for forward proofs, in Kaye's format.
This module manages proof state, provides proof commands, print/display, save.
The formula module provides formula representation, matching, and substitution.
The various logic modules define the logic languages and inference rules.
The config modules configure this checker with various logics.
The session modules are preludes for interactive sessions with various logics.
The test modules are self contained, configure the checker for test case logic.
"""

import common as logic  # minimal core, import more logic in config modules
from formula import Formula, Term, Apply, ppfdict, ppflist, ar, ac, dr, xr, xx
from pprint import pprint
from operator import concat

# proof state is a list proof steps, represented as tuples, where
# assumptions is a stack of step numbers, premises is a seq. of step numbers:
#  (rule_type, assumptions, freevars, formula, rule, premises)

steps = []       # list of tuples, one for each step in proof
assumptions = [] # stack of step numbers for currently undischarged assumptions
freevars = [[]]  # stack of lists of free variables in main proof and assumps.
formula = Apply() # current formula, may be rebound by Apply in check_rule

# core functions: check_proof, check, check_rule

def check_proof(script=[]):
    """
    Check steps in proof script (not a file but an expression).
    Pretty-print each step as it is checked.
    If invalid step found, print error message and return False.
    If no invalid steps, after last step print nothing more and return True.
    """
    # if we want default script=[] can't do it arg list, must use script=None
    global steps           # proof state, not in param list to simplify UI
    global assumptions     # ditto
    global freevars        # ditto
    global formula         # ditto
    steps = []             # rebind to empty proof
    assumptions = []       # ditto
    freevars = [[]]        # ditto
    error = ''             # empty proof is valid
    for line, step in enumerate(script):
      error = check(*step)      # *step unpacks step tuple to check args
      if isinstance(step[0],Formula):        # otherwise pps crashes
        print pps(line, assumptions, *step)  # print after check updates state
      if error:
        print error
        break
    # if script and not error:  # Omit - noisy
    #   print 'QED'             # in script, print check_proof(p) to see True
    return not error

def check(formula_arg, rule, *premises_etc):
    """
    Check proof step, update proof state, return error string, None means ok
    """
    # Use global to make argument list shorter, easier to use at command prompt
    global steps
    global assumptions
    global freevars
    global formula  # might be reassigned by Apply in call to check_rule
    formula = formula_arg
    if not isinstance(formula, Formula):
      return 'Fail: %s is %s, must be Formula' % (formula, type(formula))
    premises = []
    premise_lines = []
    # classify rule
    frule = logic.frules[rule] # flot form of inference rule
    premise_indices = filter(lambda i: isinstance(i, int), premises_etc)
    otherdata = filter(lambda i: not isinstance(i, int), premises_etc)
    nrule, npremises = len(frule) - 1, len(premise_indices)
    if not nrule == npremises:
      return 'Fail: requires %d premises, found %d' %(nrule,npremises)
    rule_type = xr             # other, neither assumer nor discharger
    if assumer(frule):
      rule_type = ar
    if assumer_case(frule):
      rule_type = ac
    if discharger(frule):
      rule_type = dr
    # collect and check premises
    subproofs = {} # map to check that premises are in right subproof
    for index, line in enumerate(premise_indices):
      if not (0 <= line < len(steps)):
        return 'Fail: no line %d for premise at index %d' % (line, index)
      # unpack step tuple into named variables
      #  (...) = steps[line] doesn't work, must have stuple[5:] at the end
      stuple = steps[line]
      (prem_rule_type,prem_assump_tup,freevars_tup,prem_formula,prem_rule,
         prem_premises) = \
         (stuple[0], stuple[1], stuple[2], stuple[3], stuple[4], stuple[5:])
      prem_assump = list(prem_assump_tup) # make mutable copy, update below
      (subproof, frule_type, pattern) = frule[index] # unpack flot tuple
      # Check assump. is in valid subproof scope,not nested in another subproof
      # Discharger might have multiple subproofs (like Or-elim), special case:
      # Must use  frule_type from rule, not prem_rule_type from step in proof 
      if rule_type == dr and frule_type == ar \
          and ((not assumptions) or (prem_assump[1:] != assumptions[1:])):
        return 'Fail: assumption at index %d, line %d not in scope for discharging rule'%(index,line)
      # Premise assumption stack must be suffix of conclusion assumption stack 
      # Scope is OK if premise is at top level (its assumption stack is empty)
      # Slice with -0 first index means whole list, not empty suffix
      if rule_type != dr and \
           prem_assump and prem_assump != assumptions[-len(prem_assump):]:
        return 'Fail: premise at index %d, line %d not in scope'%(index,line)
      # Check that premise is assumption, if that is required
      if frule_type == ar and not (prem_rule_type == ar or prem_rule_type == ac):
        return 'Fail: premise at index %d, line %d not an assumption'%(index,line)
      # Check that premises that should be in the same subproof, are indeed.
      if subproof > 0: # 0 is top level, not a subproof
        if subproof in subproofs:
          if not prem_assump_tup == subproofs[subproof]:
            return 'Fail: premise at index %d, line %d not in same scope as assumption'%(index,line)
        else:
          subproofs.update({ subproof: prem_assump_tup })
      premises += [ prem_formula ]
      premise_lines += [ line ]
    # check premises and conclusion formulae against inference rule 
    error = check_rule(rule, premises, rule_type, otherdata) #formula is global
    if error:
      return error
    # Step succeeded, update proof state
    # maintain subproof stacks
    if rule_type == ar:                   # assumer:
      assumptions[0:0] = [len(steps)]     #  push assumption on stack
      # push list of new free vars on stack, tuple makes immutable copy
      freevars[0:0] = [[ v for v in formula.free() 
                             if v not in reduce(concat, freevars) ]]
    elif rule_type == ac:                 # assumer_case:
      assumptions[0] = len(steps)         #  replace assumption on top of stack
      freevars[0] = formula.free()        #  replace free variables
    elif rule_type == dr:                 # discharger:
      del assumptions[0]                  #  pop discharged assumption
      del freevars[0]                     #  pop free variables
    else:
      # do not add variables that appear in any of the preceding levels
      freevars[0] += [ v for v in formula.free() 
                          if v not in reduce(concat, freevars) ]
    # Add step tuple to state, use .. + premise_indices to concatenate them all
    # Use tuple(...) to make immutable copies of lists, can't share struture
    steps += [(rule_type, tuple(assumptions),
               tuple([ tuple(vs) for vs in freevars ]), formula, rule)
              + premises_etc ]
    return None # indicates success, prints nothing

def check_rule(rule, premises, rule_type, otherdata):  # formula is global
  """
  Check formula and premises against rule, return error string, '' means ok
  Also handle Apply rule if present: generate formula from rule and premises
  """
  global formula # Apply might rebind it
  inference_rule = logic.frules[rule]  
  formula_etc = premises + [formula]   # same order as in inference_rule
  subformulas = {} # each call to match uses/updates, start w/ empty dict.
  for (form, (subproof,frule_type,pattern)) in zip(formula_etc,inference_rule):
    other_errors = [] # list of error messages (strings)
    boundvars = [] # list of bound variables at entry to mismatch
    if isinstance(form, Apply): # can only occur when checking rule conclusion
      if subformulas == {}: #generate needs premises (subformulas) to work with
        return 'Fail: cannot apply %s rule, must provide formula' % prn(rule)
      # generate formula from rule (pattern) and premises (subformulas)
      form = pattern.generate(subformulas, otherdata, other_errors)
      if other_errors:
        return other_errors[0] # for now there is just one string in list
      formula = form # prepare to check that the generated formula is valid
    if pattern.mismatch(form, subformulas, boundvars, reduce(concat, freevars),
                        other_errors, rule_type): 
      return 'Fail: %s does not match %s with %s' % \
                 (form.ppf(),pattern.ppf(), ppfdict(subformulas))
    elif other_errors:
      return other_errors[0] # for now there is just one string in list
  return '' # success


# Utilities for proof state, rule representation

def flotten(nested_rule):  # flotulize?
 """
 Convert rule from nested list of patterns to flat list of tuples (flot),
 Return flot where each pattern is paired with its rule type and subproof label
 Rules have one level of nesting, no need for recursion, just concat and append
 """
 flot = []  # flat list of tuples
 label = 0  # subproof label
 for pattern in nested_rule:
   if isinstance(pattern, list):  # subproof
     label = label + 1 
     if pattern:   # assumer_case uses empty pattern
       flot.append((label, ar, pattern[0])) # first pattern in subp. is assumer
       flot = flot + [(label, xx, p) for p in pattern[1:] ] # concatenate
   else:
     flot.append((0, xx, pattern)) # not a subproof, label always zero
 return flot

def assumer(flot_rule):
  """
  True iff rule makes an assumption (starts a subproof).
  Rule must be in flot format.
  """
  (label, rule_type, conclusion) = flot_rule[-1] # conclusion is always last
  return label == 1               # conclusion is in the first subproof

def assumer_case(flot_rule):
  """
  True iff rule makes another assumption in a case analysis, 
  (starts another subproof at the same level as the preceding case).
  Used with Or-Elimination.  Rule must be in flot format.
  """
  (label, rule_type, conclusion) = flot_rule[-1] # conclusion is always last
  return label > 1                # conclusion is in subproof after the first

def discharger(flot_rule):
  """
  True iff rule discharges an assumption (closes a subproof).
  Rule must be in flot format.
  """
  subproof = max([ label for (label, rule_type, pattern) in flot_rule ])
  (label, rule_type, conclusion) = flot_rule[-1] # conclusion is always last
  return subproof > 0 and label == 0  # subproofs in rule but not conclusion


# interactive prover commands

def checkp(formula_arg, rule, *premises_etc):
  """
  Check step and update proof state, pretty-print step, print error
  """
  line = len(steps) # line number of *next* proof step, user's input here
  error = check(formula_arg, rule, *premises_etc) # updates proof state for pps
  # Note we pass in formula_arg, but check may update global formula
  if isinstance(formula, Formula):
    print pps(line, assumptions, formula, rule, *premises_etc)
  return error

def rapply(rule, *premises_etc):  # apply is a Python built-in, like in Lisp
  """
  Like checkp but no formula argument. Prover generates formula from rule, premises
  For Ae rule must also provide term or variable to substitute for bound variable:
   rapply(Ae, 1, f(x,g(x,y))) # for Ae must provide replacement term t1
  For Ei rule must also provide substitution of bound variable for term:
   rapply(Ei, 1, {f(x,g(x,y)):v}) # for Ei must provide {t1:v1}
  """
  return checkp(Apply(), rule, *premises_etc) # Apply metaformula does the work

def restore(istep):
  """
  Restore assumptions and freevars from step at index istep
  Negative istep index not allowed here
  If istep out of range (after all steps removed, for example), set both empty
  """
  global assumptions
  global freevars
  if 0 <= istep < len(steps): 
    step = steps[istep]
    # make copies with list(...), we can't share these structures
    rule_type, assumps, fvs = step[0], step[1], step[2] # extract from tuple
    assumptions = list(assumps) # make copy, mutable list not immutable tuple
    freevars = [ list(vs) for vs in fvs ] # ditto, need list of lists 
  else:
    assumptions = []
    freevars = [[]]

def back(n=1):
  """
  Back up: delete last n proof steps, just print warning if n bigger than proof
  """
  if 0 < n <= len(steps):
    del steps[-n:]  # global steps apparenty not needed
    restore(len(steps)-1)  # index -1 not allowed here
  else:
    print 'Proof has %d steps, none removed' % len(steps)

def backa():
  """
  Back up past assumption: delete proof steps back through latest assumption
  """
  if assumptions:
    del steps[assumptions[0]:]
    restore(len(steps)-1)
  else:
    print 'Already at top level'

def clear():
  """
  Start over, remove all proof steps
  """
  check_proof() # just reinitialize

# display and print functions, pretty or not

def prn(rule):       
  """
  Return rule name string
  """
  return logic.rule_names[rule];  # trivial

def pr(rule):
  """
  Return rule premises and conclusion, list of strings
  """
  # Quick & dirty: frules is just a flat list, doesn't show subproofs
  return map(lambda tuple: tuple[2].pform(), logic.frules[rule])

def rules():
  """
  Print all rules: short name, premises, and conclusion.
  Does not show subproof structure of rules.
  """
  pprint([(r, pr(r)) for r in logic.rules.keys()])

def apropos(op):
  """
  Print rules where op (operator) is main connective in premise or conclusion.
  Does not show subproof structure.
  """
  def rulehas(rule, op):
    # True iff op is main connective in any premise or conclusion of rule
    return bool(filter(lambda p: isinstance(p[2],op), logic.frules[rule]))
  pprint([(r,pr(r)) for r in filter(lambda r: rulehas(r,op),logic.rules.keys())])
def assump():
  """
  Return current stack of assumptions (subproofs) in proof state
  """
  return assumptions # at Python prompt, >>> assumptions only shows initial []

def state(): 
  """
  Print entire proof state, list of steps as tuples
  """
  for line, step in enumerate(steps):
    rule_type, assumptions, freevars, formula, rule, premises_etc = \
      step[0], step[1], step[2], step[3], step[4], step[5:]    
    freevs = tuple([ tuple(ppflist(vlist)) for vlist in freevars ])
    print (line, rule_type,assumptions, freevs, formula.pform(), rule) + \
           premises_etc

def pps(line, assumptions, formula, rule, *premises_etc):
  """
  Return step (line in proof) as string in Kaye's format ("pretty-print")
  """
  indent = len(assumptions)
  bs = ''.join(['|']*indent)
  fs = formula.ppf()
  ls = '(%d)' % line
  rs = '%s %s  %s' % ((bs+fs).ljust(24), ls.rjust(4), prn(rule)) #10 for poset
  premise_indices = filter(lambda i: isinstance(i, int), premises_etc)
  ps = ''.join(map(lambda i: ' (%d)' % i, premise_indices))
  otherdata = filter(lambda i: not isinstance(i, int), premises_etc)
  # go to great lengths to make useful message, not crash
  if otherdata and isinstance(otherdata[0],Term):
    pd = ', with %s' % otherdata[0].pform()
  elif otherdata and isinstance(otherdata[0],dict):
    pair = (otherdata[0].items())[0]
    term = pair[0]
    bound = pair[1]
    if isinstance(bound,Term) and isinstance(term,Term):
      pd = ', with %s' % ppfdict(otherdata[0])
    else:
      pd = ', with %s' % otherdata
  elif otherdata: # must not be Term or dict:
    pd = ', with %s' % otherdata
  else:
    pd = ''
  return (rs + ps + pd)

def pp():
  """
  Print proof in Kaye's format ("pretty print")
  """
  for line, step in enumerate(steps):
    rule_type, assumptions, freevars, formula, rule, premises_etc = \
      step[0], step[1], step[2], step[3], step[4], step[5:]    
    print pps(line, assumptions, formula, rule, *premises_etc)

def ptree(index=len(steps)-1, indent=0):
  """
  Print proof steps as tree with conclusion at top, premises indented below.
  Root of tree is step at index, start with given indent (n of spaces)
  Default prints whole proof
  """
  step = steps[index]
  rule_type, assumptions, freevars, formula, rule, premises_etc = \
      step[0], step[1], step[2], step[3], step[4], step[5:]    
  # strip leading indent from string returned by pps
  print indent*' ' + \
    pps(index, assumptions, formula, rule, *premises_etc).lstrip('|')
  premise_indices = filter(lambda i: isinstance(i, int), premises_etc)
  for i in premise_indices:
    ptree(i, indent + 2)
  
# save functions

def pstep(step):
  """
  Return one proof step as string in save file format
  """
  (rule_type, assumptions, freevars, formula, rule, premises_etc) = \
     (step[0], step[1], step[2], step[3], step[4], step[5:])
  fs = formula.pform()
  premise_indices = filter(lambda i: isinstance(i, int), premises_etc)
  if premise_indices:
    ps = ', ' + ','.join(map(lambda i: '%d' % i, premise_indices))
  else:
    ps = ''
  otherdata = filter(lambda i: not isinstance(i, int), premises_etc)
  # Do not print otherdata, it is not useful once formula has been generated
  return '(%s, %s%s)' % (fs, rule, ps)

def psave(steps):
  """
  Return all proof steps as one string (with linebreaks) in save file format
  """
  return '  [' + ',\n    '.join(map(pstep, steps)) + ']'

def save_proof(name, steps):
  """
  Save proof steps in file, any proof. name is module name, not file name.
  """
  fname = '%s.py' % name
  f = open(fname, 'w')
  f.write('%s\n\n%s = \\\n%s\n' % \
    (logic.imports, name, psave(steps)))
  f.close()
  print 'Saved in %s' % fname

def save(name):
  """
  Save current proof state in file.  name is module name, not file name.
  """
  save_proof(name, steps)
