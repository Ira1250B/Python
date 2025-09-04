import numpy as np
from PIL import Image


image_path = r"C:\Users\bhoga\Downloads\flower.jpg"   
image = Image.open(image_path)
image_np = np.array(image)


top, bottom, left, right = 50, 50, 100, 100


padded_image = np.pad(
    image_np,
    ((top, bottom), (left, right), (0, 0)),   
    constant_values=0  
)


padded_image_pil = Image.fromarray(padded_image)


padded_image_pil.show()
padded_image_pil.save("padded_image.jpg")