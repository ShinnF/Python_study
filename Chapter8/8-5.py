from exception3_module import exception3
def exception9(a):
    x = a[0] + a[1] + a[2]
    y = a[3] + a[4] + a[5]
    z = a[6] + a[7] + a[8]
    if x==y:
        return exception3(a[6], a[7], a[8])
    elif x==z:
        return exception3(a[3], a[4], a[5])
    else:
        return exception3(a[0], a[1], a[2])
    
print(exception9([1,2,2,2,2,2,2,2,2]))
print(exception9([4,4,4,4,4,2,4,4,4]))
print(exception9([9,9,9,9,9,9,9,9,3]))