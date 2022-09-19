import math
def is_special_triangle():
    side_1 = float(input ("Enter side 1 length"))
    side_2 = float(input ("Enter side 2 length"))
    side_3 = float(input ("Enter side 3 length"))
    if side_1==side_2==side_3 :
        print("The triangle is equilateral")
    if (side_1==side_2) or (side_2==side_3) or (side_1==side_3):
        print ("The triangle is isosceles")
    is_side1_hypotenuse = side_1==math.sqrt(side_2**2+side_3**2)
    is_side2_hypotenuse = side_2==math.sqrt(side_1**2+side_3**2)
    is_side3_hypotenuse = side_3==math.sqrt(side_2**2+side_1**2)
    if is_side1_hypotenuse or is_side2_hypotenuse or is_side3_hypotenuse:
        print ("The triangle is right angle")
