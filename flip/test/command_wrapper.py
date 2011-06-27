from nd import back, backa, checkp, rapply, state

# for test scripts, print more output

def pback(n=1):
  print 'back(%s)' % n
  back(n) # back usually prints nothing

def pbacka():
  print 'backa()'
  backa() # backa usually prints nothing

def pcheckp(*args):
  error = checkp(*args) # checkp echoes step but does not print error message
  if error: 
    print error

def prapply(*args):
  error = rapply(*args) # calls checkp, echoes step but does not print error
  if error: 
    print error

def pstate():
  print 'state()'
  state() # state usually prints nothing
