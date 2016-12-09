'''
Goals for this project:

1) For a configuration of buildings, figure out optimal shock
   placement.
2) Determine margin of error (difference between radius of
   shock and radius of smallest possible shock that would work
   which is equivalent to how much you could be off on either
   side of the correct placement.)

Solving number 1 basically gives us number 2, so really it's
just one part.
'''

'''
Method:

1) Determine closest point on each building for resulting 
   shock circle to hit.
2) Figure out equation of circle that would exactly hit
   these points for the optimal shock location (center)
   and the margin of error (radius)
'''

import numpy as np
from math import sqrt

def sphere_tho(r1, r2, r3):
	"""
	Returns the radius and center of a circle, given three
	points on the circumference. Uses determinants! It's neat.
	
	Shout-outs to Wolfram :)
	"""

	x1, y1 = r1
	x2, y2 = r2
	x3, y3 = r3

	a_array = np.array([[x1, y1, 1], 
					    [x2, y2, 1],
					    [x3, y3, 1]])
	d_array = np.array([[x1**2 + y1**2, y1, 1],
						[x2**2 + y2**2, y2, 1],
						[x3**2 + y3**2, y3, 1]])
	e_array = np.array([[x1**2 + y1**2, x1, 1],
						[x2**2 + y2**2, x2, 1],
						[x3**2 + y3**2, x3, 1]])
	f_array = np.array([[x1**2 + y1**2, x1, y1],
						[x2**2 + y2**2, x2, y2],
						[x3**2 + y3**2, x3, y3]])

	a = np.linalg.det(a_array)
	d = -np.linalg.det(d_array)
	e = np.linalg.det(e_array)
	f = -np.linalg.det(f_array)	

	x_coord = -d/(2*a)
	y_coord = -e/(2*a)

	r = sqrt((d**2 + e**2)/(4*a**2) - f/a)

	return r, (x_coord, y_coord)

	



