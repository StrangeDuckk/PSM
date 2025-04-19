len = 1 #dlugosc
k = 0.1 #sprawdzic
dt = 0.1 #sprawidzic
m = 1

def deriv(y,n):
    dy = y-len
    a = -k*dy/n

    return v,a

def eulerStep(y,v,ky,kv,dt):
    y = y+k*dt
    v = v+ kv*dt
    return y,v

y = len + 0.3
v = 0

tt = []
yy = []

for i in range(10000):
    yy.append(i*dt)
    tt.append(y)

    k1y ,k1v = deriv(y,y)
    # y,v = eulerStep(y,v,k1y,k1v,dt)
    y_2, v_2 = eulerStep(y,v,k1y,k1v,dt/2)
    k2y, k2v = deriv(y_2,y)

    #dodtakowo tlumienie ale nie dla nas, my go nie potrzebujemy

