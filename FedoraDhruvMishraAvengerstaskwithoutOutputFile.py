import math
f=open('input.txt','r')
x=f.readlines()
n=1
while (n<=int(x[0])):
    P=int(x[n])
    winner=0
    xi=(2*P)**0.5
    xi=math.floor(xi)
    if(xi**2+xi==2*P):    
        if(xi%2==0):
            winner=2            
        else:
            winner=1
    else:        
        nmax=math.ceil(((((8*P)+1)**0.5)-1)/2)
        if((nmax-1)%2==0):
            pd=(nmax-1)//2
            winner=2
        else:
            pd=((nmax-1)//2)+1
            winner=1
        nmax2=math.ceil(((((8*(P-pd))+1)**0.5)-1)/2)
        if(nmax-nmax2>=1):
            winner=winner
        else:
            winner=winner+1
    if(winner%2==0):
        print('CAPTAIN AMERICA')
    else:
        print('IRON MAN')
    n=n+1    