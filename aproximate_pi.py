import math
def aproximate_pi(n):
    theta = math.radians(360/n)
    height = ((math.cos((theta/2))))
    half_apothem = (math.sin((theta/2)))
    
    
    
    area = (n * height * half_apothem)
   
    print(area)
     
