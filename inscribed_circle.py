import math #imports math module, namely for the purpose of math.acos(), math.sin(), and math.tan()

def inscribed_circle(a, b, c): #takes three side lengths as arguments, corresponding to local parameters a, b, and c
    angle_a = math.acos((b**2+c**2-a**2)/(2*b*c)) #cosine law to solve for angle alpha
    half_perimeter = (a+b+c)/2
    radius = (half_perimeter-a)*math.tan(angle_a/2) #uses given formula to solve for the inscribed circle's radius
    print (radius)
