"""
Created on Wed Feb 17 15:15:10 2021

Python code to illustrate the performances of the Euler and Verlet algorithms
relative to the analytical solution for a 1-dimensional undamped
harmonic oscillator system. 

@author: adhika.n.suryatin@gmail.com
"""

## Import Relevant Packages
import math
import numpy as np
import matplotlib.pyplot as plt                  # Comparison plots
import matplotlib.animation as anim              # Animation tools

## Define Functions & Set-up Auxiliary Features
# Functions
def force(k, x):                    # Calculates restoring force
	f = -k * x
	return f

def energy(k, x, m, v):             # Calculates system energy
	e = 0.5*k*(x**2) + 0.5*m*(v**2)
	return e

def animation_frame(i):                          # Function for animation
	x_A_anim.append(x_A[i])                  # Analytical position
	p_A_anim.append(p_A[i])                  # Analytical momentum
	
	line_A.set_data(x_A_anim, p_A_anim)      # Update analytical line
	
	x_E_anim.append(x_E[i])                  # Euler position
	p_E_anim.append(p_E[i])                  # Euler momentum
	
	line_E.set_data(x_E_anim, p_E_anim)      # Update euler line

	x_V_anim.append(x_V[i])                  # Verlet position
	p_V_anim.append(p_V[i])                  # Verlet momentum
	
	line_V.set_data(x_V_anim, p_V_anim)      # Update verlet line
	
	return line_A, line_E, line_V,

# Set-up Movie Writer Format
writer = anim.ImageMagickWriter(fps=15)



## Main Code

## Simulation Loop
# Parse Input
nsteps = 100                              # Number of steps
dt = 0.25                                 # Size of time-step

# Hard-coded Constants
k=1.0                                    # Spring constant
m=1.0                                    # Mass of oscillator
x0 = 0.0                                 # initial position
v0 = 1.0                                 # initial velocity

# Assign Variables
w = math.sqrt(k/m)                       # Angular frequency
A = x0**2 + (v0/w)**2                    # Amplitude
ph = math.atan(x0*w/v0)                  # Phase shift
t = [i*dt for i in range(0, nsteps+1)]   # Time intervals



## Part I: Analytical Solution 
# Initialize Position, Velocity, Momentum, and Energy Arrays
x_A, v_A, p_A, E_A = ([] for j in range(4))

# Calculate & Update Arrays
for l in range(len(t)):
	x_A.append(A*math.sin(w*t[l]+ph))          # Position
	v_A.append(A*w*math.cos(w*t[l]+ph))        # Velocity
	p_A.append(m*v_A[l])                       # Momentum
	E_A.append(energy(k, x_A[l], m, v_A[l]))   # System total energy
	


## Part II: Numerical Algorithms
# Initialize Euler Variables
x_E = [x0]
v_E = [v0]
p_E = [m*v0]
f_E = [force(k, x0)]
E_E = [energy(k, x_E[0], m, v_E[0])]

# Main Euler Loop
for i in range(nsteps):
	x_E.append(x_E[i] + v_E[i]*dt + (0.5*f_E[i]/m)*(dt**2))   # Position
	v_E.append(v_E[i] + dt*f_E[i]/m)                          # Velocity
	p_E.append(m*v_E[-1])                                     # Momentum
	f_E.append(force(k, x_E[-1]))                             # Force
	E_E.append(energy(k, x_E[-1], m, v_E[-1]))                # Energy

# Initialize Verlet Variables
x_V = x_E[0:2]
v_V = v_E[0:2]
p_V = p_E[0:2]
f_V = f_E[0:2]
E_V = E_E[0:2]

# Main Verlet Loop
for i in range(nsteps-1):
	x_V.append(x_V[i+1] + v_V[i]*dt + f_V[i+1]/(2*m)*(dt**2))   # Position
	f_V.append(force(k, x_V[-1]))                               # Force
	v_V.append(v_V[i+1] + dt/(2*m)*(f_V[i+1] + f_V[-1]))        # Velocity
	p_V.append(m*v_V[-1])                                       # Momentum
	E_V.append(energy(k, x_V[-1], m, v_V[-1]))                  # Energy



## Visualization
# Initialize Plot Area & Variables
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid("True", which='both')
ax.set_ylabel('Particle Momentum $p$')
ax.set_xlabel('Particle Position $x$')
plt.title('Phase Space Evolution of Numerical & Analytical Solutions')

# Initialize Plot Variables
line_A, = ax.plot(x0, m*v0, 'b-', mfc="None", label="Analytical")
line_E, = ax.plot(x0, m*v0, 'r-', mfc="None", label="Euler")
line_V, = ax.plot(x0, m*v0, 'g^', mfc="None", linestyle="None", label="Verlet")
fig.legend(loc=[0.15, 0.705])

# Initialize Data Sets to be Updated
x_A_anim, p_A_anim = ([] for j in range(2))
x_E_anim, p_E_anim = ([] for j in range(2))
x_V_anim, p_V_anim = ([] for j in range(2))

# Animate Evolution
animation = anim.FuncAnimation(fig, func=animation_frame,
						   frames=np.arange(0,nsteps,1), interval=100)

# Show Plot
plt.show()

# Save Movie
# animation.save('Phase_Evol.gif', writer=writer)
