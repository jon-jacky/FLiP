# Test cases for rule preprocessor, same shapes as kinds of rules
# For convenience, items are just integers not formulas

from nd import flotten, assumer, assumer_case, discharger

assume = [[0]]
discharge = [[0,1],2]
assume_case = [[],[0]]    # like assumption for constructive or-elimination
core = [0,[1,2],[3,4],5] # like constructive or-elimination

nota = [0,1,2]  # none of the above


print '%s --> %s' % (nota, flotten(nota))
print '%s --> %s' % (assume, flotten(assume))
print '%s --> %s' % (discharge, flotten(discharge))
print '%s --> %s' % (assume_case, flotten(assume_case))
print '%s --> %s' % (core, flotten(core))

rules = [ nota, assume, discharge, assume_case, core ]

flots = [ flotten(r) for r in rules ]  # each r becomes flat list of tuples

print
print 'assumer:      %s' % [ assumer(f) for f in flots ]
print 
print 'assumer_case: %s' % [ assumer_case(f) for f in flots ]
print 
print 'discharger:   %s' % [ discharger(f) for f in flots ]
