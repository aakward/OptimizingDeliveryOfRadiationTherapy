import math
from pulp import *
import numpy as np
import matplotlib.pyplot as plt

mid=[[[0,0] for j in range(140)]for i in range(120)]
for i in range(120):
    for j in range(140):
        mid[i][j]=[i+0.025,j+0.025]
delta=[[0 for j in range(140)]for i in range(120)]
for i in range(120):
    for j in range(140):
        if(math.sqrt((mid[i][j][0]-60)**2+(mid[i][j][1]-70)**2)<=80):
            delta[i][j]=4
for i in range(120):
    for j in range(140):
        if(mid[i][j][0]>=40.025 and mid[i][j][0]<=99.975 and mid[i][j][1]>=20.025 and mid[i][j][1]<=39.975):
            delta[i][j]=10
        if(mid[i][j][0]>=40.025 and mid[i][j][0]<=99.975 and mid[i][j][1]>=80.025 and mid[i][j][1]<=99.975):
            delta[i][j]=10
        if(mid[i][j][0]>=60.025 and mid[i][j][0]<=79.975 and mid[i][j][1]>=40.025 and mid[i][j][1]<=79.975):
            delta[i][j]=10

G1=[0]
G2=[j for j in range(140)]
G3=[120]
G4=[i for i in range(120)]
G5=[140]

T_i=[]
T_j=[]
for i in range(120):
    for j in range(140):
        if(i>=40 and i<=99 and j>=20 and j<=39):
            T_i.append(i)
            T_j.append(j)
        if(i>=40 and i<=99 and j>=80 and j<=99):
            T_i.append(i)
            T_j.append(j)
        if(i>=60 and i<=79 and j>=40 and j<=79):
            T_i.append(i)
            T_j.append(j)





prob=LpProblem("Problem1",LpMinimize)
#D=LpVariable.dicts("D",([i for i in range(120)],[j for j in range(140)]), 0, None, LpContinuous)
w1=LpVariable.dicts("w1",(G1,G2),0, None, LpContinuous)
w2=LpVariable.dicts("w2",(G3,G2),0, None, LpContinuous)
w3=LpVariable.dicts("w3",(G4,G1),0, None, LpContinuous)
w4=LpVariable.dicts("w4",(G4,G5),0, None, LpContinuous)
prob+= lpSum([[w1[0][j]+w2[120][j]+w3[i][0]+w4[i][140] for j in range(140)] for i in range(120)])
for i in range(120):
        for j in range(140):
            if(i<=80 and j <=80 and (120-i)<=80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]+w3[i][0]+w4[i][140]>=10

            if(i>80 and j <=80 and (120-i)<=80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]+w3[i][0]+w4[i][140]>=10

            if(i<=80 and j >80 and (120-i)<=80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]/2.0+w3[i][0]+w4[i][140]>=10

            if(i<=80 and j <=80 and (120-i)>80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]+w3[i][0]/2.0+w4[i][140]>=10
            if(i<=80 and j <=80 and (120-i)<=80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]+w3[i][0]+w4[i][140]/2.0>=10

            if(i>80 and j >80 and (120-i)<=80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]/2.0+w3[i][0]+w4[i][140]>=10

            if(i>80 and j <=80 and (120-i)>80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]+w3[i][0]/2.0+w4[i][140]>=10

            if(i>80 and j <=80 and (120-i)<=80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]+w3[i][0]+w4[i][140]/2.0>=10

            if(i<=80 and j >80 and (120-i)>80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]/2.0+w3[i][0]/2.0+w4[i][140]>=10

            if(i<=80 and j >80 and (120-i)<=80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]/2.0+w3[i][0]+w4[i][140]/2.0>=10

            if(i<=80 and j <=80 and (120-i)>80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]+w3[i][0]/2.0+w4[i][140]/2.0>=10
            if(i>80 and j >80 and (120-i)>80 and (140-j)<=80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]/2.0+w3[i][0]/2.0+w4[i][140]>=10

            if(i>80 and j >80 and (120-i)<=80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]/2.0+w3[i][0]+w4[i][140]/2.0>=10

            if(i>80 and j <=80 and (120-i)>80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]+w3[i][0]/2.0+w4[i][140]/2.0>=10

            if(i<=80 and j >80 and (120-i)>80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]+w2[120][j]/2.0+w3[i][0]/2.0+w4[i][140]/2.0>=10

            if(i>80 and j >80 and (120-i)>80 and (140-j)>80 and (i in T_i) and (j in T_j)):
                prob+= w1[0][j]/2.0+w2[120][j]/2.0+w3[i][0]/2.0+w4[i+0.025][140]/2.0>=10
prob.solve(PULP_CBC_CMD(fracGap=0.00001,maxSeconds=500,threads=None))
print LpStatus[prob.status]

for v in prob.variables():
        print "{}={}".format(v.name, v.varValue)
