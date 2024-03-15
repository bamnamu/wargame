from PIL import Image
import numpy as np
from operator import xor

im1=Image.open('C:\\Users\\taotr\\Desktop\\wargame\\wargame\\cryptohack\\General\\XOR\\Lemur_xor\\flag.png').convert('RGB')
im2=Image.open('C:\\Users\\taotr\\Desktop\\wargame\\wargame\\cryptohack\\General\\XOR\\Lemur_xor\\lemur.png')



p1=np.array(im1)
p2=np.array(im2)

p=np.zeros_like(im1)

for i in range(len(p)):
    for j in range(len(p1[0])):
        p[i][j]=tuple(xor(a, b)for a, b in zip(p1[i][j], p2[i][j]))

ans=Image.fromarray(p)
ans.save("ans.png")
ans.show()