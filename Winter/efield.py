from vpython import *

# Define Constants
oofpez = 9e9	# [Nm^2/C^2] OOFPEZ, one-over-four-pi-episilon-zero
qe = 1.5e-19	# [C] Electron charge
sf = 3e-16		# scale factor for electric field arrows

# Set up visualization

source = sphere(pos=vec(0,0,0), radius = 1e-9,
		     color = color.red)
source.q = qe

E_arrows = []

theta = 0
theta_max = 2*pi
dtheta = pi/6
R = 1e-8
i=0

while theta < theta_max:
	rate(500)

	r_obs = R*vec(cos(theta),cos(pi/2 - theta),0)
	r = r_obs - source.pos
	rhat = r/mag(r)

	E = ( oofpez*source.q / pow(mag(r),2) ) * rhat
	E_arrows.append( arrow(pos=r_obs, color = color.orange,
	 					   axis = E*sf, shaftwidth=source.radius) )

	print(E_arrows[i].axis)
	i += 1
	theta = theta + dtheta
