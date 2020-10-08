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
G2=[j+0.025 for j in range(140)]
G3=[120]
G4=[i+0.025 for i in range(120)]
G5=[140]

prob=LpProblem("Problem1",LpMinimize)
D=LpVariable.dicts("D",([i for i in range(120)],[j for j in range(140)]), 0, None, LpContinuous)
w1=LpVariable.dicts("w1",(G1,G2),0, None, LpContinuous)
w2=LpVariable.dicts("w2",(G3,G2),0, None, LpContinuous)
w3=LpVariable.dicts("w3",(G4,G1),0, None, LpContinuous)
w4=LpVariable.dicts("w4",(G4,G5),0, None, LpContinuous)



#prob=LpProblem("Problem1",LpMinimize)
#    D=LpVariable.dicts("D",([i for i in range(120)],[j for j in range(140)]), 0, None, LpContinuous)
#    w1=LpVariable.dicts("w1",(0,[j+0.025 for j in range(140)]),0, None, LpContinuous)
#    w2=LpVariable.dicts("w2",(120,[j+0.025 for j in range(140)]),0, None, LpContinuous)
#    w3=LpVariable.dicts("w3",([i+0.025 for i in range(120)],0),0, None, LpContinuous)
#    w4=LpVariable.dicts("w4",([i+0.025 for i in range(120)],140),0, None, LpContinuous)
        
    prob+= lpSum([[D[i][j] for j in range(140)] for i in range(120)])
    for i in range(120):
        for j in range(140):
            if(i<=80 and j <=80 and (120-i)<=80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]
            if(i>80 and j <=80 and (120-i)<=80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]
            if(i<=80 and j >80 and (120-i)<=80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]
            if(i<=80 and j <=80 and (120-i)>80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]
            if(i<=80 and j <=80 and (120-i)<=80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]/2.0
            if(i>80 and j >80 and (120-i)<=80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]
            if(i>80 and j <=80 and (120-i)>80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]
            if(i>80 and j <=80 and (120-i)<=80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]+w4[i+0.025][140]/2.0
            if(i<=80 and j >80 and (120-i)>80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]
            if(i<=80 and j >80 and (120-i)<=80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]/2.0
            if(i<=80 and j <=80 and (120-i)>80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
            if(i>80 and j >80 and (120-i)>80 and (140-j)<=80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]
            if(i>80 and j >80 and (120-i)<=80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]+w4[i+0.025][140]/2.0
            if(i>80 and j <=80 and (120-i)>80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
            if(i<=80 and j >80 and (120-i)>80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
            if(i>80 and j >80 and (120-i)>80 and (140-j)>80):
                prob+= D[i][j]>=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
                prob+= D[i][j]<=w1[0][j+0.025]/2.0+w2[120][j+0.025]/2.0+w3[i+0.025][0]/2.0+w4[i+0.025][140]/2.0
        for i in range(120):
            for j in range(140):
                if(i>=40 and i<=99 and j>=20 and j<=39):
                    prob+= D[i][j]>=10
                if(i>=40 and i<=99 and j>=80 and j<=99):
                    prob+= D[i][j]>=10
                if(i>=60 and i<=79 and j>=40 and j<=79):
                    prob+= D[i][j]>=10
        for i in range(120):
            for j in range(140):
                if(math.sqrt((mid[i][j][0]-60)**2+(mid[i][j][1]-70)**2)<=80):
                    prob+= D[i][j]<=4
        
    prob.solve(PULP_CBC_CMD(fracGap=0.00001,maxSeconds=500,threads=None))
    print LpStatus[prob.status]  
    
    
    D=[[0 for j in range(140)]for i in range(120)]
    for v in prob.variables():
        x=str(v.name)
        k=x[1]
        if(k==1):
            m=int(x[5:])
            for i in range(120):
                if(i<=80):
                    D[i][m]=D[i][m]+v.varValue
                else:
                    D[i][m]=D[i][m]+(v.varValue)/2.0
        if(k==2):
            m=int(x[7:])
            for i in range(120):
                if(i<40):
                    D[i][m]=D[i][m]+v.varValue
                else:
                    D[i][m]=D[i][m]+(v.varValue)/2.0
        if(k==3):
            if(x[4]=='_'):
                m=int(x[3:4])
            if(x[5]=='_'):
                m=int(x[3:5])
            if(x[6]=='_'):
                m=int(x[3:6])
            for j in range(140):
                if(j<=80):
                    D[m][j]=D[m][j]+v.varValue
                else:
                    D[m][j]=D[m][j]+(v.varValue)/2.0
        if(k==4):
            if(x[4]=='_'):
                m=int(x[3:4])
            if(x[5]=='_'):
                m=int(x[3:5])
            if(x[6]=='_'):
                m=int(x[3:6])
            for j in range(140):
                if(j<=80):
                    D[m][j]=D[m][j]+v.varValue
                else:
                    D[m][j]=D[m][j]+(v.varValue)/2.0
                    
            
            
    
    A=D
    A=np.matrix(A)
    cmap = plt.get_cmap('RdBu', np.max(A)-np.min(A)+1)
    mat = plt.matshow(A,cmap=cmap,vmin = np.min(A)-.5, vmax = np.max(A)+.5)
    #tell the colorbar to tick at integers
    plt.colorbar(mat, ticks=np.arange(np.min(A),np.max(A)+1))
    plt.title("Distribution of coverage of EMS across the city")
    plt.show()

