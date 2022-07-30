import cmath
from math import sqrt
from vector import unit_vector, vec3, color, point,dot
from Ray import Ray
from hittable import *
from utility import *
from hittable_list import *

def ray_color(Ray,world):
	#hit 된게 있을때
	rec = HitRecord()
	#sphere = Sphere(1.0,point(0.0,0.0,+2.0))
	if True == world.hit(Ray,0.0,INFINITY,rec):
		return 0.5*(rec.normal+color(1.0,1.0,1.0))
	#hit 된게 없을때
	unit_direction = unit_vector(Ray.direction)
	t= 0.5*(unit_direction.y()+1.0)
	sunset = color(247.0/255.9,147.0/255.9,27.0/255.9)
	bluesky = color(0.5,0.7,1.0)
	my_color = color(240.0/255.9,0.0/255.9,15.0/255.9)

	return (1.0-t)*color(1.0,1.0,1.0)+t*bluesky


def present(width,ratio,world):
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
			c=ray_color(r,world)

			arr.append(int(c[0]*255.999))
			arr.append(int(c[1]*255.999))
			arr.append(int(c[2]*255.999))
	return arr

width = 800
ratio = 16.0/9.0
height = int(width/ratio)
world = hittalbe_list()

#Sp = Sphere(point(0.0,0.0,-1.0),0.5)
#Tp = Sphere(point(0.0,-100.5,-1.0)100.0)
#world.add(Sp)
#world.add(Tp)

world.add(Sphere(0.5,point(0.0,0.0,-1.0)))
world.add(Sphere(100.0,point(0.0,-100.5,-1.0)))

ppm_header = "P3\n{} {}\n255".format(width,height)
output = present(width,ratio,world)

f= open("my.ppm", 'w')
#print(a,end='')
f.write(ppm_header)

for i in range(len(output)):

	if i%3==0:
		f.write("\n")
		#print()
	c= "{} ".format(output[i])
	f.write(c)
	#print("{} ".format(b[i]),end='')
f.close()