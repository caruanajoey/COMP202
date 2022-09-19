import math
def circumscribed_circle(a, b, c):
    beta=math.acos((math.pow(a,2)+math.pow(c,2)-math.pow(b,2))/(2*a*c))
    radius=b/(2*math.sin(beta))
    print ("radius of the circumscribed triangle =",radius)