import numpy as np
array1=np.array([8,12,3,6,5,11])
array2=np.array([11,12,6,15,8,9])
l1=array1.size
l2=array2.size
a1=array1[:l1]
a2=array2[:l2]
for i in range(l1):
    for j in range(l2):
        if(a1[i]==a2[j]):
            print("Common elements are: ",a2[j])