print("why")
import scipy
#from scipy import stats

#sample observation     
#a=1

#'normal', 'uniform'
poptype='normal'
n=50
popmean=1
#propagate,raise, omit
nanpo='propagate'
#two-sided, greater, less
alt='two-sided'
ci=.95


def tTest(a,popmean,nanpo,alt,ci):
    res=scipy.stats.ttest_1samp(a, popmean, axis=0, nan_policy=nanpo, alternative=alt, keepdims=False)
    res.confidence_interval(confidence_level=ci)
    return(res)

def getTestType(n,poptype):
    if poptype=='normal':
        #return stats.norm.rvs(size=n)
    elif poptype=='uniform':
        #return stats.uniform.rvs(size=n)

a=getTestType(n,poptype)

tTestRes = tTest(a,popmean,nanpo,alt,ci)
print(tTestRes)

