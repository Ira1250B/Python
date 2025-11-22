import numpy as np
import matplotlib.pyplot as plt
fs = 1000  
f1 = 5  
f2=10 
t = np.linspace(0, 1, fs, endpoint=False)  
sine_wave1 = np.sin(2 * np.pi * f1 * t)
sine_wave2 = np.sin(2 * np.pi * f2 * t)
sine_wave=sine_wave1+sine_wave2
plt.plot(t,sine_wave)
plt.title('Resulted signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()