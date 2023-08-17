a,b,c = map(float, input("Enter the co-effcient x^2, x and constant term: ").split())
if a==0:
    print("Two roots are not possible")
else:
    D = (b**2- 4*a*c)
    if(D==0):
        root = -b/(2*a)
        print("The determinant is zero so\nthe roots are real and same\nRoots: ",root, root)
    elif D>0:
        root1 = (-b+D**0.5)/(2*a)
        root2 = (-b-D**0.5)/(2*a)
        print("The Determinant is +ve so the roots are real and distinct\nroot1 = ", root1,"\nroot2 = ", root2)
    else:
        print("The determinant is -ve so the roots are complex and conjugater\nroot1 = ",-b/(2*a), " + i(",-(-D)**0.5,")\nroot2 = ",-b/(2*a)," + i(",(-D)**0.5,")", sep= "")