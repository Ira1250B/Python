import numpy as np
import matplotlib.pyplot as plt

fs = 1000     
f = 10    
t = np.linspace(0, 1, fs, endpoint=False)
sine_wave = np.sin(2 * np.pi * f * t)
sine_wave_scaled = 3*sine_wave

plt.subplot(2,1,1)
plt.stem(t,sine_wave)
plt.title('Original signal')
plt.xlabel('Time ')
plt.ylabel('Amplitude')
plt.subplot(2,1,2)
plt.xlabel('Time ')
plt.ylabel('Amplitude')
plt.title(' Amplitude-Scaled  Sine Wave')
plt.stem(t,sine_wave_scaled)
plt.legend()
plt.show()
