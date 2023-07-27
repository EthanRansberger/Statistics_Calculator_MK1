import scipy.stats as st

t=None
z=None
f=None
chisq=None
p=None
n=None
sd=None
n_y=None
locc=0

if n:
    df=n-1
if n_y:
    df_y=n-1

if p:
    if sd:
        pvalz=st.chisquare.pdf(p,df)
    elif n:
        if n_y:
            pvalz=st.f.ppf(p,df,df_y) 
        else:
            pvalz=st.t.ppf(p,df) 
    else:
        pvalz=st.norm.ppf(p)
   
if z:
    pvalz=st.norm.cdf(z)
    print(1-pvalz)
if t:
    pvalz=st.t.cdf(t,df)
if f:
    pvalz=st.f.cdf(f,df,df_y,loc=locc)
if chisq:
    pvalz=st.chisquare.cdf(chisq,df)
 

print(pvalz)




