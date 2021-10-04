def task(n,k):
    c,p,q=1,0,1
    s=0
    while q<k+n:
        if q>=k:
            s+=c
        c,p=c+p,c
        q+=1
    return s    
        
n=int(input("n="))
k=int(input("k="))
 
print(task(n,k))
