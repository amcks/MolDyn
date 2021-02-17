"""
Created on Wed Feb 17 10:49:48 2021

Python code to illustrate the usage of the Euler algorithm
to solve the 1-dimensional harmonic oscillator system.

@author: adhika.n.suryatin@gmail.com
"""

## Import Relevant Packages
import sys

## Define Functions & Initialization Errors

# Functions
def force(k, x):                    # Calculates restoring force
	f = -k * x
	return f

def energy(k, x, m, v):             # Calculates system energy
	e = 0.5*k*x**2 + 0.5*m*v**2
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
nsteps = int(sys.argv[1])   # Number of steps
dt = float(sys.argv[2])     # Size of time-step
nprint = int(sys.argv[3])   # Print frequency

# Hard-coded Constants
k=1.0                       # Spring constant
m=1.0                       # Mass of oscillator
x0 = 0.0                    # initial position
v0 = 1.0                    # initial velocity

#x0 = np.random.random()    # Alternative for random starting position

# Assign Variables
x = x0                      # Position initialization
v = v0                      # Velocity initialization
f = force(k, x)             # Force initialization

# Prepare Formatted Print Output
print('{0:^8s}  {1:^8s}    {2:^8s}  {3:^8s}'.\
          format('Time', 'Position', 'Velocity', 'Energy'))
print("==========================================")
print('{0:^8.2f}  {1:+8.2e}  {2:+8.2e}  {3:^8s}'.\
              format(0, x, v, '-'))

# Main Loop
for i in range(nsteps):
	nx = x + v*dt + (0.5*f/m)*(dt**2)   # Position at next time step
	nf = force(k, nx)                   # Force at next time step
	nv = v + dt*f/m                     # Velocity at next time step
	E = energy(k, nx, m, nv)            # Energy at next time step

	# Print Formatted Output
	if (i+1)%nprint == 0:
		print('{0:^8.2f}  {1:+8.2e}  {2:+8.2e}  {3:8.2e}'.\
			format((i+1)*dt, nx, nv, E))

	# Update Variables
	x = nx
	v = nv
	f = nf
