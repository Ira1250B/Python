import pandas as pd
s1=pd.Series([20,40,60,80,100])
s2=pd.Series([10,30,70,90,110])
#Vertically stacking
ver=pd.concat([s1,s2],axis=0)
print(ver,"\n")
#Horizontal stacking
hrl=pd.concat([s1,s2],axis=1)
print(hrl)