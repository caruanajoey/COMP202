#group 11D
import math

def open_door():
    '''
    NoneType -> str
    This function returns the word friend
    
    >>> open_door()
    'friend'
    
    '''
    return "friend"

#In observatory using the telescope
def make_constellation_in_sky(sky):
    '''
    (list<list<str>>)->list<list<str>>
    Takes a sky map nested list and returns the same sky map nested list
    with the stars ('*') characters connected using '-' character horizontally
    and the '|' character vertically.
    
    >>> make_constellation_in_sky([['*', '*', '*'], ['.', '.', '.'], ['.', '*', '*']])
    [['*', '*', '*'], ['.', '|', '|'], ['.', '*', '*']]
    >>> make_constellation_in_sky([['.', '.', '*', '.', '.', '*', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['*', '.', '*', '.', '.', '.', '.', '*']])
    [['.', '.', '*', '-', '-', '*', '.', '.'], ['.', '.', '|', '.', '.', '.', '.', '.'], ['*', '-', '*', '-', '-', '-', '-', '*']]
    >>> make_constellation_in_sky([['*', '.', '*'], ['.', '.', '.'], ['*', '.', '*']])
    [['*', '-', '*'], ['|', '.', '|'], ['*', '-', '*']]
    '''
    
    start=""
    for row in range(len(sky)):
        for column in range (len(sky[row])):
            if sky[row][column] == "*" and start !="":
                mylist=[]
                for i in range (column-start-1):
                    mylist.append('-')
                sky[row][start+1:column]=mylist
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
    """(str) -> float
    Takes a quadratic or linear equation as a string, and returns the solution as a float.
    If two solutions exist, the larger is returned.
    
    >>>solve_equation("-83x-25=-16791")
    202.0
    
    >>>solve_equation("-80x^2+32320x-3264320=0")
    202.0
    
    >>>solve_equation("-60x^2+23880x-2376060=0")
    199.0
    
    """
    
    equation_copy = equation.replace("=", " ")
    equation_copy = equation_copy.replace("x^2", " ")
    equation_copy = equation_copy.replace("x", " ")
    equation_copy_list = equation_copy.split()
    
    a = int(equation_copy_list[0])
    b = int(equation_copy_list[1])
    c = int(equation_copy_list[2])
    
    if "x^2" in equation:
        
        d = int(equation_copy_list[3])
        
        solution_list = []
        solution_list.append((-b + math.sqrt(math.pow(b, 2) -4*a*(c-d)))/(2*a))
        solution_list.append((-b - math.sqrt(math.pow(b, 2) -4*a*(c-d)))/(2*a))
        solution = max(solution_list)
        
    else:
        solution = (c - b)/a
    
    return solution
