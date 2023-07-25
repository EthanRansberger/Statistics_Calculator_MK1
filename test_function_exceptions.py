a=1
b=None
c=3




def getB():
    
    return a+c
def getD(b=None):
    if b:
        return(b+a)
    else:
        try:
            b = getB()
            return getD(b)
        except:
            return
        
d=getD()
print(d)