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

qq = input("z,t,f,chi")
if qq=='t'or qq=='f' or qq=='chi':
    n=int(input("n:"))
    if qq=='f':
        n_y=int(input("n_y:"))
pof = input("ppf (give probability) or cdf (return probability)")
if pof == 'ppf':
    p=float(input("probability:"))
elif pof=='cdf':
    
    
    if qq=='f':
        
        f=float(input("f value:"))
    elif qq=='t':
        t=float(input("t value"))
    elif qq=='chi':
        chi=float(input("chi value:"))
    elif qq=='z':
        z=float(input("z value:"))
            
        

if n:
    df=n-1
if n_y:
    df_y=n-1

if p:
    if sd:
       pvalz=st.chi2.ppf(p,df)
       print("1-p \n", st.chi2.ppf((1-p),df) , "\n p")
    elif n:
        if n_y:
            pvalz=st.f.ppf(p,df,df_y) 
            print("1-p \n", st.f.ppf((1-p),df,df_y) , "\n p")
        else:
            pvalz=st.t.ppf(p,df) 
            print("1-p \n", st.t.ppf((1-p),df) , "\n p")
          
    else:
        pvalz=st.norm.ppf(p)
        print("1-p \n", st.norm.ppf((1-p)) , "\n p")
if z:
    pvalz=st.norm.cdf(z)
    print("greater than probability \n", 1-pvalz, "\n less than probability")
if t:
    pvalz=st.t.cdf(t,df)
    print("greater than probability\n", 1-pvalz, "\n less than probability")
if f:
    pvalz=st.f.cdf(f,df,df_y,loc=locc)
if chisq:
    pvalz=st.chi2.cdf(chisq,df)
    print("greater than probability \n", 1-pvalz, "\n less than probability")
    
 

print(pvalz)




