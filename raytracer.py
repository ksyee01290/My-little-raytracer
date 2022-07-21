import cmath
from math import sqrt
from vector import unit_vector, vec3, color, point,dot
from Ray import Ray

def ppm_header(width,height):
	a = "P3\n{} {}\n255".format(width,height)
	return a;
    
def hit_sphere(Ray,s,r):
	DD = dot(Ray.direction, Ray.direction)
	DO = dot(Ray.direction,Ray.origin)
	PP = dot(s,s)
	PD = dot(s,Ray.direction)
	OO = dot(Ray.origin,Ray.origin)
	OP = dot(Ray.origin,s)
	RR = r*r

	b=(2.0*DO - 2.0*PD)
	disc = b*b -4.0*(DD)*(-2.0*OP+OO+PP-RR)

	if disc < 0.0:
		return -1
	else:
		return (-b -sqrt(disc))/(2.0*DD)

def ray_color(Ray):
	unit_direction = unit_vector(Ray.direction)
	t= 0.5*(unit_direction.y()+1.0)
	sunset = color(247.0/255.9,147.0/255.9,27.0/255.9)
	bluesky = color(0.5,0.7,1.0)
	my_color = color(240.0/255.9,0.0/255.9,15.0/255.9)

	m=t*0.5
	return (1.0-t)*color(1.0,1.0,1.0)+t*bluesky


def present(width,ratio):
	#그림 사이즈
	aspect_ratio = ratio
	image_width = width
	image_height = image_width/aspect_ratio

	#바라보는시점
	viewport_height = 2.0
	viewport_width = aspect_ratio*viewport_height
	focal_length = 1.0

	origin = point(0.0,0.0,0.0)
	horizontal = vec3(viewport_width,0.0,0.0)
	vertical = vec3(0.0,viewport_height,0.0)
	lower_left_corner = origin-horizontal/2.0-vertical/2.0-vec3(0.0,0.0,focal_length)

	arr = []
	for j in reversed(range(int(image_height))):
		for i in range(image_width):
			u=i/(image_width-1)
			v=j/(image_height-1)
			r=Ray(origin,(lower_left_corner+u*horizontal+v*vertical-origin))

			c= color(0.0,0.0,0.0)
			#c= ray_color(r)

			sphere = point(0.0,0.0,-2.0)
			t=hit_sphere(r,sphere,1.0)

			if t >= 0.0:
				P = (Ray.at(r,t))
				normal = unit_vector(P - sphere)
				c=color((normal.x()+1.0)*0.5,(normal.y()+1.0)*0.5,(normal.z()+1.0)*0.5)
				#c=color(1.0,0.0,0.0)
			else:
				c=ray_color(r)

			arr.append(int(c[0]*255.999))
			arr.append(int(c[1]*255.999))
			arr.append(int(c[2]*255.999))
	return arr;

width = 800
ratio = 16.0/9.0
height = int(width/ratio)

a=ppm_header(width,height)
b=present(width,ratio)

f= open("my.ppm", 'w')
#print(a,end='')
f.write(a)

for i in range(len(b)):

	if i%3==0:
		f.write("\n")
		#print()
	c= "{} ".format(b[i])
	f.write(c)
	#print("{} ".format(b[i]),end='')
f.close()