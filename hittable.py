from vector import *
from Ray import Ray


class HitRecord():
    def __init__(self,normal,point,t):
        self.normal = normal
        self.point = point
        self.t=t
    def set_face_normal(self,Ray,outward_normal):
        self.front_face = dot(Ray.direction(),outward_normal) < 0.0
        if self.front_face == True:
            self.normal = outward_normal
        else:
            self.normal = -outward_normal



class Hittable():
    def hit(self,Ray,t_min,t_max,hit_record):
        pass

class Sphere():
    def __init__(self,radius,position):
        self.radius = radius
        self.position = position
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

p=point
normal = vec3
front_face = bool