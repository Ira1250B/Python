from PIL import Image
img = Image.open(r"C:\Users\bhoga\Downloads\flower.jpg")
r,g,b = img.split()
red = Image.merge("RGB",(r,Image.new("L",r.size),Image.new("L",r.size)))
green = Image.merge("RGB",(Image.new("L",g.size),g,Image.new("L",g.size)))
blue = Image.merge("RGB",(Image.new("L",b.size),Image.new("L",b.size),b))

red.show(title = "Red highlighted")
green.show(title = "green highlighted")
blue.show(title = "blue highlighted")

merged_image = Image.merge("RGB",(r,g,b))
merged_image.show(title = "Merged Image")