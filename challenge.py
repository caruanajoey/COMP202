def generate_list(length,c):
    mylist=[]
    for i in range (length):
        mylist.append(c)
    return mylist

def make_constellation_in_sky(sky):
    start=""
    for row in range(len(sky)):
        for column in range (len(sky[row])):
            if sky[row][column] == "*" and start !="":
                sky[row][start+1:column]=generate_list(column-start-1,'-')
                
                start=column
            elif sky[row][column] == "*":
                start = column
        start =""
    
    for column in range(len(sky[row])):
        for row in range (len(sky)):
            if sky[row][column] == "*" and start !="":
                for q in range (start+1,row):
                    sky[q][column] = "|"
                start=row
            elif sky[row][column] == "*":
                start = row
        start =""
    
    return sky

def solve_equation(equation):
    
    #extract a, b and c...
    
    if "x^2" in str(equation):
        solution_list = []
        solution_list.append((-b + math.sqrt(math.pow(b, 2) -2*a*c))/2*a)
        solution_list.append((-b - math.sqrt(math.pow(b, 2) -2*a*c))/2*a)
        solution = max(solution_list)
        
    else:
        solution = (c - b)/a
    
    return solution


  
