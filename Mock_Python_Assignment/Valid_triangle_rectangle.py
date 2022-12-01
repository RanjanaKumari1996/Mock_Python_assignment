def checkValidity(a, b, c):
     
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True       
 
def isRectangle(a, b, c, d):
 
    # check all sides of rectangle combinations
    if (a == b and d == c) or (a == c and b == d) or (a == d and b == c):
        return True
    else:
        return False

# driver code
a = 7
b = 10
c = 5
if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid")
    

 
 
# Driver code
a, b, c, d = 1, 2, 3, 4
if isRectangle(a, b, c, d):
    print("valid") 
else:
    print("Invalid")