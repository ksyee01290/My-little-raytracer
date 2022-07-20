from math import sqrt


class vec3:
    def __init__(self, x, y, z):
        self.__e = [x,y,z]

    @staticmethod
    def new_from_zero():
        return vec3(0.0, 0.0, 0.0)

    def x(self):
        return self.__e[0]

    def y(self):
        return self.__e[1]

    def z(self):
        return self.__e[2]

    def length(self):
        return sqrt(self.length_squared())

    def length_squared(self):
        return self.__e[0] * self.__e[0] + self.__e[1] * self.__e[1] + self.__e[2] * self.__e[2]

    def normalize(self):
        return unit_vector(self)

    def __neg__(self):
        return vec3(-self.__e[0], -self.__e[1], -self.__e[2])

    def __imul__(self, other):
        self.__e[0] = self.__e[0] * other
        self.__e[1] = self.__e[1] * other
        self.__e[2] = self.__e[2] * other
        return self

    def __idiv__(self, other):
        self *= 1.0 / other
        return self

    def __iadd__(self, other):
        self.__e[0] += other.x()
        self.__e[1] += other.y()
        self.__e[2] += other.z()
        return self

    def __add__(self, other):
        return vec3(self.__e[0] + other.x(), self.__e[1] + other.y(), self.__e[2] + other.z())

    def __sub__(self, other):
        return vec3(self.__e[0] - other.x(), self.__e[1] - other.y(), self.__e[2] - other.z())

    def __mul__(self, other):
        if isinstance(other, vec3):
            return vec3(self.__e[0] * other.x(), self.__e[1] * other.y(), self.__e[2] * other.z())
        return vec3(self.__e[0] * other, self.__e[1] * other, self.__e[2] * other)

    def __rmul__(self, other):
        return vec3(self.__e[0] * other, self.__e[1] * other, self.__e[2] * other)

    def __truediv__(self, other):
        return self * (1.0 / other)

    def __getitem__(self, item):
        return self.__e[item]

def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]

def cross(u, v):
    return vec3(u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0])

def unit_vector(v):
    return v / v.length()


point = vec3
color = vec3