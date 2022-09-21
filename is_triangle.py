#Question 1.1
def is_triangle():
    print ("Is there a triangle with side lengths a, b and c?")
    a = float (input ("Enter side a: "))
    b = float (input ("Enter side b: "))
    c = float (input ("Enter side c: "))
    if a > 0 and b > 0 and c > 0 and (a + b) >= c  and (a + c) >= b and (b + c) >= a:
        print ("Yes, there is a triangle with side lengths a, b and c!")
    else:
        print ("No, there isn't a triangle with side lengths a, b and c!") 
    
