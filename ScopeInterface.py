###################################################################
#
#         High-level Python interface for Rigol scopes
#
# Author          :   Marc-Olivier Schwartz
# E-Mail          :   marcolivier.schwartz@gmail.com
#
####################################################################

# Imports
import os
import sys
import instrument
import numpy as np
import time
import pylab
	
# Main class	
class ScopeInterface:

	# Init	
	def __init__(self):
		
		# Initialize our scope
		self.test = instrument.RigolScope("/dev/usbtmc0")
   
	# Get the whole scope trace
	def getScopeValue(self,channel):
		 
		# Grab the data from channel
		self.test.write(":WAV:POIN:MODE NOR")
		 
		self.test.write(":WAV:DATA? CHAN" + str(channel))
		rawdata = self.test.read(9000)

		data = np.frombuffer(rawdata, 'B')
		 
		# Get the voltage scale
		self.test.write(":CHAN" + str(channel) + ":SCAL?")
		voltscale = float(self.test.read(20))
		 
		# Get the voltage offset
		self.test.write(":CHAN" + str(channel)+ ":OFFS?")
		voltoffset = float(self.test.read(20))
		 
		# Invert data
		data = data * -1 + 255
		 
		# Scale to voltage
		data = (data - 130.0 - voltoffset/voltscale*25) / 25 * voltscale
		 
		# Get the timescale
		self.test.write(":TIM:SCAL?")
		timescale = float(self.test.read(20))
		 
		# Get the timescale offset
		self.test.write(":TIM:OFFS?")
		timeoffset = float(self.test.read(20))

		# Discard first 10 points of data
		if (data.size > 600):
			data = data[10:]
		 
		# Generate time axis
		time = np.arange(0, 600.0/50*timescale, timescale/50.0)
		 
		# If we generated too many points, crop the length of time.
		if (time.size > data.size):
		    time = time[0:600:1]

		return time, data
	        
	# Get mean value from the scope   
	def getMean(self,channel):
		
		# Grab the data
		self.test.write(":MEASure:VAVerage? CHAN" + str(channel))

		return self.test.read(20)
	
	# Get minimum value from the scope   
	def getMin(self,channel):

		# Grab the data
		self.test.write(":MEASure:VMIN? CHAN" + str(channel))

		return self.test.read(20)
	 
	# Get maximum value from the scope   
	def getMax(self,channel):
		 
		# Grab the data
		self.test.write(":MEASure:VMAX? CHAN" + str(channel))
		
		return self.test.read(20)

 
