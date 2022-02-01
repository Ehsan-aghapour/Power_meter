import pandas as pd
import matplotlib.pyplot as pt
import sys


f=open("test.csv")
lines=f.readlines()
print(len(lines))
powers=[]
pin_last=0
c=0
for l in lines:
    c=c+1
    values=l.split(',')
    v=float(values[0])
    if v>1:
        pin_last=v
        continue
    if v!=pin_last:
        powers.append([float(values[3])])
        #print(f'appending {float(values[3])} in row {c}')
        
    else:
        powers[-1].append(float(values[3]))
    pin_last=v

print(len(powers))
run_power=powers[1::2]
print(len(run_power))

pwr_avg=[(sum(p[10:-10])/len(p[10:-10])) for p in run_power]
components=['L','B','G']
freqs={'G':[2208000],
    'B':[500000, 667000, 1000000, 1200000, 1398000, 1512000, 1608000, 1704000, 1800000, 1908000, 2016000, 2100000, 2208000],
    'L':[500000, 667000, 1000000, 1200000, 1398000, 1512000, 1608000, 1704000, 1800000]
}
Layers=8
pwr_data={}
k=0
for c in components:
    pwr_data[c]={}
    for i in range(Layers):
        pwr_data[c][i]={}
        for f in freqs[c]:
            pwr_data[c][i][f]=pwr_avg[k]
            k=k+1


print(pwr_avg)
print(pwr_data)

#pt.plot(run_power[0])
#pt.show()


########### read performance data

f=open("timing.csv")
lines=f.readlines
data={'G':[],'B':[],'L':[]}
i=0
step={'G':13,'B':13,'L':9}
for l in lines:
    values=l.split(',')
    if values[0]=='G' and values[1]!='2208000':
        continue
    data[values[1]].append(values[2])
    data[values[1]].append(values[3])
    data[values[1]].append(values[4])
    data[values[1]].append(pwr_data[values[1]][int(values[3])][int(values[2])])

print(data['L'])


