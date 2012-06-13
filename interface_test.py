###################################################################
#
#         Test file for the Rigol Scope Python interface 
#
# Author          :   Marc-Olivier Schwartz
# E-Mail          :   marcolivier.schwartz@gmail.com
#
####################################################################

# Imports
import numpy
import pylab
import ScopeInterface
import time

# Interface creation
scopi = ScopeInterface.ScopeInterface()

start_time = time.time()

# Get data
t, voltage = scopi.getScopeValue(1)

# Get max 
print "Max :",scopi.getMean(1),"V"

# Get min 
print "Min :",scopi.getMin(1),"V"

# Get mean 
print "Mean :",scopi.getMean(1),"V"

print "Acquisition done in",time.time() - start_time,"s"

# Plot
pylab.plot(t,voltage)
pylab.show()