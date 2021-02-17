"""
Created on Wed Feb 17 13:14:03 2021

Python code to illustrate the analytical solution for the 
undamped 1-dimensional harmonic oscillator system.

@author: adhika.n.suryatin@gmail.com
"""

## Import Relevant Packages
import sys, math

## Define Functions & Initialization Errors

# ObjectsFunctions
def energy(k, x, m, v):             # Calculates system energy
	e = 0.5*k*(x**2) + 0.5*m*(v**2)
	return e

# Error Exit Message
if len(sys.argv) != 4:
	print("Invalid number of arguments.")
	print("Usage: %s nsteps dt nprint" %(sys.argv[0]))
	print("==============================================")
	print("nsteps: Number of simulation steps desired")
	print("dt    : Size of time-step")
	print("nprint: Frequency of printed step information")
	sys.exit(0)


## Main Code

# Parse Input
nsteps = int(sys.argv[1])                # Number of steps
dt = float(sys.argv[2])                  # Size of time-step
nprint = int(sys.argv[3])                # Print frequency

# Hard-coded Constants
k=1.0                                    # Spring constant
m=1.0                                    # Mass of oscillator
x0 = 0.0                                 # initial position
v0 = 1.0                                 # initial velocity

# Assign Variables
w = math.sqrt(k/m)                       # Angular frequency
A = x0**2 + (v0/w)**2                    # Amplitude
ph = math.atan(x0*w/v0)                  # Phase shift

# Prepare Formatted Print Output
print('{0:^8s}  {1:^8s}    {2:^8s}  {3:^8s}'.\
          format('Time', 'Position', 'Velocity', 'Energy'))
print("==========================================")

# Calculate & Update Arrays
for l in range(nsteps+1):
	x = A*math.sin(w*l*dt+ph)      # Position
	v = A*w*math.cos(w*l*dt+ph)    # Velocity
	E = energy(k, x, m, v)   # System total energy
	
	# Print Formatted Output
	if (l)%nprint == 0:
		print('{0:^8.2f}  {1:+8.2e}  {2:+8.2e}  {3:^8.2e}'.\
              format(l*dt, x, v, E))
