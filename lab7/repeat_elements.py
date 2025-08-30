import numpy  as np
arr=np.array([1,7,8,45,1,3,4,2,7])
values ,counts=np.unique(arr,return_counts=True)
repeated=values[counts>1]
print("Repeated elements in array: ",repeated)

