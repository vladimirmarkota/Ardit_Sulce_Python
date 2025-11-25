import math
def luiqvol(h,r):
    v = (4*math.pi*pow(r, 3))/3 - math.pi*pow(h, 2)*(3*r-h)/3
    return v
print(luiqvol(2,10))

def luiqidvol(h):
    r = 10
    v = (4*math.pi*r**3)/3 - (math.pi*h**2*(3*r-h))/3
    return v
print(luiqidvol(2))