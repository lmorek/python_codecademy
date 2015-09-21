__author__ = 'morek'
import math

def degrees(rad):
    deg=rad*180/math.pi
    return  str(float(round(deg,2))) + "deg"

def radians(deg):
     if deg>0:
        rad = deg*math.pi/180
        return str((round(rad,2))) + "rad"
     else:
        rad = deg*math.pi/180
        return str(int(rad)) + "rad"

print degrees(29.8553884301)
print radians(0)

