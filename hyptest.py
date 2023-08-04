import math

sampl=int(input("1 or 2 samples?: "))
modez=input("mean, prob, or var?:")
n = int(input('n?: '))
if sampl==2:
    n_y= int(input('n_y?: '))
if modez=='mean' or modez=='var':
    nrml=input("norm or no?: ")
    if modez=='var':
        if nrml=='norm':
            chi_u=float(input('chi_u'))
            chi_l=float(input('chi_l'))
            mod='chin_i'
        else:
            print('bootstrapping')
            mod='no'
    if modez=='mean':
        if nrml=='norm':
            mu=input('mu?: ')
            sx=input('x bar?: ')
            ukwn=input('var known or unknown?: ')
            if ukwn=='known':
                sd = float(input('sd?: '))
                vari= sd*sd
                mod='ztest'
                
            else:
                siz=input('small or large?')
                if siz=='small':
                    mod='tn_i'
                    tu=float(input('t score?: '))
                else:
                    mod='ztest'
                    sd = float(input('sample sd?: '))
                    vari=sd*sd
        else:
            siz=input('small or large?')
            if 'small':
                print('bootstrapping')
                mod='no'
            else:
                mod='z_clt'

if modez=='prob':
    siz=input('small or large?: ')
    if siz=='large':
        mod='z_clt_prb'

    else:
   #     print('bootstrapping')
        print('binomial')
    
if mod=='bern' or mod=='z_clt_prb':
    ps=float(input('ps'))
    pp=float(input('pp'))
if mod=='ztest' or mod=='zlim' or mod=='z_clt' or mod=='z_clt_prb':
    zu=float(input('z score?: '))
if mod=='tn_o' or mod=='zlim' or mod=='chin_i':
    s_sd=float(input('sample standard deviation?: '))
#if mod=='ztest' or mod=='tn_i' or mod=='zlim' or mod=='z_clt':
  #  sx=float(input('x bar?: '))
  #  mu=float(input('population mean?'))



if mod=='ztest':
    Pmean=(sx-mu)/(sd/math.sqrt(n))
    Cint_l= sx-(zu*sd)/math.sqrt(n)
    Cint_u= sx+(zu*sd)/math.sqrt(n)
    print("mean: ", Pmean, "\n interval low:", Cint_l, "\n interval high:", Cint_u)
    
#normal, unknown variance, small small
elif mod=='tn_i':
    Pmean=(sx-mu)/(s_sd/math.sqrt(n))
    Cint_l= sx-(tu*s_sd)/math.sqrt(n)
    Cint_u= sx+(tu*s_sd)/math.sqrt(n)
    print("mean: ", Pmean, "\n interval low:", Cint_l, "\n interval high:", Cint_u)
 
#
elif mod=='zlim':
    Pmean=(sx-mu)/(s_sd/math.sqrt(n))
    Cint_l= sx-(zu*s_sd)/math.sqrt(n)
    Cint_u= sx+(zu*s_sd)/math.sqrt(n)
    print("mean: ", Pmean, "\n interval low:", Cint_l, "\n interval high:", Cint_u)
  

elif mod=='chin_i':
    Pmean= ((n-1)((s_sd)^2))/(sd^2)
    Cint_l= ((n-1)((s_sd)^2))/(chi_u^2)
    Cint_u= ((n-1)((s_sd)^2))/(chi_l^2)
    print("mean: ", Pmean, "\n interval low:", Cint_l, "\n interval high:", Cint_u)
 
#get from sample exams
elif mod =='z_clt':
    if vari:
        Pmean= (sx-mu)/(sd/math.sqrt(n))
        Cint_l= sx-(zu*sd)/math.sqrt(n)
        Cint_u= sx+(zu*sd)/math.sqrt(n)
    else:
        Pmean= (sx-mu)/(s_sd/math.sqrt(n))
        Cint_l= sx-(zu*s_sd)/math.sqrt(n)
        Cint_u= sx+(zu*s_sd)/math.sqrt(n)
    print("mean: ", Pmean, "\n interval low:", Cint_l, "\n interval high:", Cint_u)

if mod=='z_clt_prb':
    Pmean = (ps-pp)/math.sqrt((ps*(1-ps))/n)
    Cint_l=ps-zu*math.sqrt((ps*(1-ps))/n)
    Cint_u=ps+zu*math.sqrt((ps*(1-ps))/n)
    print("mean: ", Pmean, "\n interval low:", Cint_l, "\n interval high:", Cint_u)
"""
if mod=='bern'
    Pmean = (ps-zu*math.sqrt((ps*(1-ps))/n))
    Cint_l=ps-zu*math.sqrt((ps(1-ps))
    Cint_u=ps+zu*math.sqrt((ps(1-ps))
    print("mean: none \n interval low:", Cint_l, "\n interval high:", Cint_u)
"""
                      