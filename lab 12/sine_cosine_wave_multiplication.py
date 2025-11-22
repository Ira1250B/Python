import numpy as np
import matplotlib.pyplot as plt
fs=500
f1=5
f2=10
t=np.linspace(0,2,fs,endpoint=False)
sine_wave=np.sin(2*np.pi*f1*t)
cosine_wave=np.cos(2*np.pi*f2*t)
result=sine_wave*cosine_wave
plt.plot(t,result)
plt.title('Resulted signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()