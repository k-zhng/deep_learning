from PIL import Image
from sklearn.datasets import load_sample_images
import numpy as np

china = load_sample_images().images[0]
flower = load_sample_images().images[1]

# print((china.shape, china.dtype))
# print((flower.shape, flower.dtype))

imChina = Image.fromarray(china)
imFlower = Image.fromarray(flower)
# imChina.show()
# imFlower.show()
# imChina.save("china.png")
# imFlower.save("flower.png")

im = Image.open("china.png")
# im.show()
img = np.array(im)
print((img.shape, img.dtype))
gray = im.convert("L")
gray.show()
g = np.array(gray)
print((g.shape, g.dtype))