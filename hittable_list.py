from hittable import *
from vector import *
from Ray import Ray


class hittalbe_list():
    def __init__(self):
        self.world = []

    def hit(self,ray,t_min,t_max,hit_record):
        temp_rec = HitRecord()
        t = t_max
        flag = False
        
        for obj in self.world:
            if obj.hit(ray,t_min,t_max,temp_rec):
                flag = True
                if t > temp_rec.t:
                    hit_record.point = temp_rec.point
                    hit_record.fromnt_face = temp_rec.front_face
                    hit_record.normal = temp_rec.normal
                    t = temp_rec.t
        return flag

    def add(self,obj):
        self.world.append(obj)
    
    def clear(self):
        self.world=[]