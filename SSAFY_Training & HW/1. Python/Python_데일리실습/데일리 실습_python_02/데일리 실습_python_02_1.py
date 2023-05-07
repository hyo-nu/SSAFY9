a = 3
b = 6
c = - 5

def root (a,b,c):
    result = ()
    root_p = round((-b + ((b**2)-(4*a*c))**(1/2)) / 2 / a,4)
    root_m = round((-b - ((b**2)-(4*a*c))**(1/2)) / 2 / a,4)

    result = root_p,root_m
    return result

print(root(a,b,c))
