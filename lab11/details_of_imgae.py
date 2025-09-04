from PIL import Image
import numpy as np
img=Image.open(r'C:\Users\bhoga\Downloads\flower.jpg')

img_array=np.array(img)
width ,length =img.size
print(f"Dimentions :{width}x{length} ")

print("Shape: {img_array.shape}")
blue=img_array[:,:,2].min()
print(f"Minimum blue part in image:{blue}")