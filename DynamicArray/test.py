import numpy as np

a=lambda x:1+x
arr=np.array([[1,2,3,4,5],[2,3,4,5,6]])
veca=np.vectorize(a)

print(veca(arr))