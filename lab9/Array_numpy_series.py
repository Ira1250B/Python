import pandas as pd
import numpy as np

list = [1, 2, 3, 4]
s_list = pd.Series(list)
print("Series from List:\n")
print(s_list)

array = np.array([10, 20, 30, 40, 50])
s_array = pd.Series(array)
print("Series from NumPy Array:\n")
print(s_array)

# From dictionary
dict = {'x': 100, 'y': 200, 'z': 300}
s_dict = pd.Series(dict)
print("Series from Dictionary:\n")
print(s_dict)