# Group exercise 1
# Gr. 11D
# Authors: Joey Caruana, Jerry Gao, Laurence Perreault, Philippe Aprahamian, Zachary Quirion-Haddine

import math
# Question 1.1
def is_triangle():
    a = float(input ("Enter side a: "))
    b = float(input ("Enter side b: "))
    c = float(input ("Enter side c: "))
    if ((a + b) >= c ) and ((a + c) >= b) and ((b + c) >= a):
        print ("Yes, there is a triangle with side lengths a, b and c!")
    else:
        print ("No, there isn't a triangle with side lengths a, b and c!") 

# Question 1.2
def is_special_triangle():
    side_1 = float(input ("Enter side 1 length"))
    side_2 = float(input ("Enter side 2 length"))
    side_3 = float(input ("Enter side 3 length"))
    if side_1==side_2==side_3 :
        print("The triangle is equilateral")
    if (side_1==side_2) or (side_2==side_3) or (side_1==side_3):
        print ("The triangle is isosceles")
    is_side1_hypotenuse = side_1 == math.sqrt(side_2**2+side_3**2)
    is_side2_hypotenuse = side_2 == math.sqrt(side_1**2+side_3**2)
    is_side3_hypotenuse = side_3 == math.sqrt(side_2**2+side_1**2)
    if is_side1_hypotenuse or is_side2_hypotenuse or is_side3_hypotenuse:
        print ("The triangle is right-angle")

# Question 1.3        
def perimeter_of_triangle():
    a = float(input("side a: "))
    b = float(input("side b: "))
    c = float(input("side c: "))
    print(a+b+c)

# Question 1.4    
def area_of_triangle():
    a = float(input("side a: "))
    b = float(input("side b: "))
    c = float(input("side c: "))
    per = float((a + b + c)/2)
    area = (math.sqrt((per * (per-a) * (per-b) * (per-c))))
    print(area)

# Question 1.5    
def angles_of_triangle():
    a = float(input ("Enter side 1 length: "))
    b = float(input ("Enter side 2 length: "))
    c = float(input ("Enter side 3 length: "))
    alpha = math.acos((math.pow(b,2)+math.pow(c,2)-math.pow(a,2))/(2*b*c))
    beta = math.acos((math.pow(a,2)+math.pow(c,2)-math.pow(b,2))/(2*a*c))
    gamma = math.acos((math.pow(a,2)+math.pow(b,2)-math.pow(c,2))/(2*a*b))
    print(alpha*180/math.pi)
    print(beta*180/math.pi)
    print(gamma*180/math.pi)

# Question 2.1    
def circumscribed_circle(a, b, c): #takes three side lengths as arguments, corresponding to local parameters a, b, and c
    angle_a = math.acos((b**2+c**2-a**2)/(2*b*c)) #cosine law to solve for angle alpha
    radius = a/(math.sin(angle_a))/2 #uses given formula to solve for the circumscribed circle's radius
    print (radius)

# Question 2.2    
def inscribed_circle(a, b, c): #takes three side lengths as arguments, corresponding to local parameters a, b, and c
    angle_a = math.acos((b**2+c**2-a**2)/(2*b*c)) #cosine law to solve for angle alpha
    half_perimeter = (a+b+c)/2
    radius = (half_perimeter-a)*math.tan(angle_a/2) #uses given formula to solve for the inscribed circle's radius
    print (radius)

# Question 3
def approximate_pi(n):
    theta = math.radians(360/n)
    height = ((math.cos((theta/2))))
    half_apothem = (math.sin((theta/2)))
    area = (n * height * half_apothem)
    print(area)
