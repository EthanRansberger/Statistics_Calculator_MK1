import math
from SciPy import stats
#includes logic for different distrubtions
#I think it will loop until the function for results is reached.
#use try function, and keep trying through things to see if can get anywhere
#class normalDist(self,)
#popmean
mu=None
sd=None
#sample sd
s_sd=None
#sample mean
sx=None
popmean=None
popvar=None
var=None
covar=None
cor=None
#confidence interval 
ci=None
n_x=1
n_y=None
if n_y==None:
    n=n_x
if n:
    df=n-1

cv_l=None
cv_h=None
p=None

#probability with line on top and probability for hypothesis tests
ps=None
pp=None

#type 1 and 2 error probability
alpha=None
beta=None
power=None
#bernoulli, random, normal
typevar="str"

#hypothesis p value
hyp=None
hyptype="greater"
#tail test (right, left, two)
#tails="right"

small=True
normal=True
popmean=True
success_probability=False
population_variance=False
if sd:
    popvar=True


#zu is Ci z value f.e. 90% ci == 1.645
zu=1
#when do you use t test
tu=1
#chi-squared
chi_u=1
chi_l=1


#TESTS formulas

Ztst=1
tn_i=1
Zlim_tn_i=1
special=None
Z_CLT=1
binomial=1
bootstrapping=None
chin_i=1


"""
if Ztst:
    Pmean=(sx-mu)/(sd/math.sqrt(n))
    Cint_l= sx-(zu*sd)/math.sqrt(n)
    Cint_u= sx+(zu*sd)/math.sqrt(n)
"""

def getPower():
    if beta:
        return (1-beta)
def getBeta():
    if power:
        return(1-power):
    else:
        return
def getAlpha():
    return

def Ztst():
    Pmean=(sx-mu)/(sd/math.sqrt(n))
    Cint_l= sx-(zu*sd)/math.sqrt(n)
    Cint_u= sx+(zu*sd)/math.sqrt(n)
def tn_i(sx=None,mu=None,,s_sd=None,n=None,tu=None):
    Pmean=(sx-mu)/(s_sd/math.sqrt(n))
    Cint_l= sx-(tu*s_sd)/math.sqrt(n)
    Cint_u= sx+(tu*s_sd)/math.sqrt(n)
def Zlim_tn_i(sx=None,mu=None,,s_sd=None,n=None,zu=None):
    Pmean=(sx-mu)/(s_sd/math.sqrt(n))
    Cint_l= sx-(zu*s_sd)/math.sqrt(n)
    Cint_u= sx+(zu*s_sd)/math.sqrt(n)
def chin_i(sd=None,s_sd=None,n=None,zu=None):
    Pmean= ((n-1)((s_sd)^2))/(sd^2)
    Cint_l= ((n-1)((s_sd)^2))/(chi_u^2)
    Cint_u= ((n-1)((s_sd)^2))/(chi_l^2)
#get from sample exams
def Z_CLT(sx=None,mu=None,sd=None,s_sd=None,n=None,zu=None):
    if popvar:
        Pmean= (sx-mu)/(sd/math.sqrt(n))
        Cint_l= sx-(zu*sd)/math.sqrt(n)
        Cint_u= sx+(zu*sd)/math.sqrt(n)
    else:
        Pmean= (sx-mu)/(s_sd/math.sqrt(n))
        Cint_l= sx-(zu*s_sd)/math.sqrt(n)
        Cint_u= sx+(zu*s_sd)/math.sqrt(n)
def Z_CLT_prp(ps=None,pp=None,zu=None):
    Pmean= (ps-pp)/math.sqrt((ps(1-ps))
    Cint_l=ps-zu*math.sqrt((ps(1-ps))
    Cint_u=ps+zu*math.sqrt((ps(1-ps))

def getCriticalValue(n=None,hyp=None,hypp=None,hyptype=None,sd=None):
    try:
    except:
        
    
#given any amount of information it finds everything else is the goal
def combinations(r,n):
    return
def permutations(r,n):
    return
def getZ():
    return
def getT():
    return
def getF(x,n_x,n_y==None):
    if n_y!=None:
        return
    else:
        return

def getPopSD(vari=None):
    if popvar:
        return math.sqrt(var)
def getPopVar():
    if sd:
        return 
    else:
        return

def getTest():
    #see flow chart
    if popmean:
        if normal:
            if popvar:
                #z
                return(Ztst)
            else:
                if small:
                    return(tn_i)
                else:
                    return(Zlim_tn_i)
        else:
            if small:
                return(special)
            else:
                return(Z_CLT)
    elif success_probability:
        # bernoulli
        if small:
            return(binomial)
        else:
            return(Z_CLT_prp)
    elif population_variance:
        if normal:
            return(chin_i)
            #chi-squared
        else:
            return(bootstrapping)
            #non-normal
            #bootstrapping
