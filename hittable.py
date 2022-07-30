from vector import *
from Ray import Ray


class HitRecord():
    def __init__(self):
        self.normal = None
        self.point = None
        
    def set_face_normal(self,ray,outward_normal):
        self.front_face = dot(ray.direction,outward_normal) < 0.0
        if self.front_face == True:
            self.normal = outward_normal
        else:
            self.normal = -outward_normal

class Hittable():
    def hit(self,ray,t_min,t_max,hit_record):
        pass

class Sphere():
    def __init__(self,radius,position):
        self.radius = radius
        self.position = position
        
    def hit(self,ray,t_min,t_max,hit_record):
        t=Sphere.hit_sphere(ray,self.position,self.radius)
        if t is None:
            return False
        else:
            near,far=t
            if near*far<0.0:
                t=far
            else:
                t=near
    
        if t<t_min and t>t_max:
            return False
        else:
            if t >= 0.0:
                P= ray.at(t)
                normal = unit_vector(P - self.position)
                
                hit_record.set_face_normal(ray,normal)
                hit_record.point = P
                hit_record.t = t
                return True
                
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

        if disc >= 0.0:
            return (-b -sqrt(disc))/(2.0*DD),(-b +sqrt(disc))/(2.0*DD)
        else:
            return None

p=point
normal = vec3
front_face = bool