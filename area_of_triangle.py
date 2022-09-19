import math

def area_of_triangle():
    a= float(input("side a: "))
    b= float(input("side b: "))
    c= float(input("side c: "))
    
    per = float((a + b + c)/2)
    
    area = round((math.sqrt((per * (per-a) * (per-b) * (per-c)))),2)
  
    print(area)
    
