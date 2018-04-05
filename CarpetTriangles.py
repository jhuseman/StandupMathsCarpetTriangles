#! /usr/bin/env python

def isosc_around(x,y,x_max,y_max):
	top = min([x,y,(x_max-x)])
	left = min([x,y,(y_max-y)])
	bottom = min([x,(y_max-y),(x_max-x)])
	right = min([y,(y_max-y),(x_max-x)])
	return sum([top, left, bottom, right])

def right_around(x,y,x_max,y_max):
	top_left = min([x,y])
	bottom_left = min([x,(y_max-y)])
	top_right = min([(x_max-x),y])
	bottom_right = min([(y_max-y),(x_max-x)])
	return sum([top_left, bottom_left, top_right, bottom_right])

def triangles_around(x,y,x_max,y_max):
	return right_around(x,y,x_max,y_max) + isosc_around(x,y,x_max,y_max)



def total_triangles(x_max, y_max, down_right):
	total = 0
	for x in xrange(0, x_max+1):
		for y in xrange(0, y_max+1):
			val = 0
			if x%2 ^ y%2 ^ down_right:
				val = triangles_around(x, y, x_max, y_max)
			total = total + val
	return total

if __name__=="__main__":
	print total_triangles(20, 18, True)  # Full-size carpet
	# print total_triangles(15, 13, False) # Carpet shown on store
	# print total_triangles(5, 2, True)    # small segment created by Matt Parker
