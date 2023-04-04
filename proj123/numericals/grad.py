def dif1(f,x0,dx,args=()):
    f1=f(x0,*args)
    f2=f(x0+dx,*args)
    df=(f2-f1)/dx
    return df
