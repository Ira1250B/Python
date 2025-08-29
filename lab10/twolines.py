import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,10,100)
#firstline
y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)
plt.plot(x,y1,label="Sin")
plt.plot(x,y2,label="Cos")
plt.plot(x,y3,label="Tan")
plt.title("Multiple Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()