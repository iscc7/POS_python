from matplotlib import pyplot as plt
from numpy import exp,sin,cos, array, square,sqrt,var,mean,linspace
from random import random
from time import clock

def fun(x):
    x = array(x)
    return (sin(x+square(x*10)))/(sqrt(x+square(x)))


def initial(size,down,up):
    pops = []
    for item in range(size):
        a = down+random()*(up-down)
        pops.append(a)
    y_pops = fun(pops)
    his_individual = pops
    y_pops = y_pops.tolist()
    y_pops_index = y_pops.index(max(y_pops))
    his_social = pops[y_pops_index]
    return pops,his_individual,his_social
def pops_update(pops,w,v,c1,c2,his_individual,his_social,down,up):
    for i in range(len(pops)):
        v = w*v+c1*random()*(his_individual[i]-pops[i])+c2*random()*(his_social-pops[i])
        pops[i] = pops[i]+v
        if pops[i]>up:
            pops[i] = up
        if pops[i]<down:
            pops[i] = down
    return pops
def his_update(pops,his_ind):
    y_pops = fun(pops)
    y_his_ind = fun(his_ind)
    for i in range(len(pops)):
        if y_his_ind[i]<y_pops[i]:
            his_ind[i] = pops[i]

    y_pops = y_pops.tolist()
    y_pop_index = y_pops.index(max(y_pops))
    his_soc = pops[y_pop_index]
    return his_ind,his_soc

if __name__ == '__main__':
    bagin = clock()
    up =0.4
    down = 0.2
    pop_size = 10
    w = 0.1
    v = 1
    c1 = 2
    c2 = 2
    pops_0,his_individual,his_social = initial(pop_size,down,up)
    plt.plot(pops_0,fun(pops_0),'r*')
    pops_1 = pops_0
    while var(pops_1)/mean(pops_1)>0.0001:
        pops_1 = pops_update(pops_1,w,v,c1,c2,his_individual,his_social,down,up)
        his_individual,his_social = his_update(pops_1,his_individual)

    plt.plot(pops_1, fun(pops_1), 'k*')
    end = clock()
    print pops_1,'\n',var(pops_1),'\n',end-bagin

    x = linspace(down,up,1000)
    y =fun(x)
    plt.plot(x,y,'b--')
    plt.show()

