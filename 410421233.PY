from PIL import Image
import numpy as np
import random
"""input the image"""
k1 = Image.open("C:/Users/USER/Desktop/Image_and_ImageData/key1.png")
k2 = Image.open("C:/Users/USER/Desktop/Image_and_ImageData/key2.png")
k3 = Image.open("C:/Users/USER/Desktop/Image_and_ImageData/I.png")
E = Image.open("C:/Users/USER/Desktop/Image_and_ImageData/E.png")
EP = Image.open("C:/Users/USER/Desktop/Image_and_ImageData/Eprime.png")
"""ramdomize the weights"""
w1=np.random.rand(1)
w2=np.random.rand(1)
w3=np.random.rand(1)

""""turn image into numpy array"""
k1=np.array(k1)
k2=np.array(k2)
k3=np.array(k3)
E=np.array(E)
EP=np.array(EP)
"""setting parameter of gradient descent"""
epoch = 1
lr = 0.00001
limit=10
a=np.zeros((300,400))
e=np.zeros((300,400))
"""trainging part"""
while(epoch==1 or epoch<limit):
    for w in range(0,299):
        for h in range(0,399):
         """a(k)=w1*k1+w2*k2+w3*I"""
         a[w,h]=(k1[w,h]*w1)+(k2[w,h]*w2)+(k3[w,h]*w3)
         """e(k)=E(k)-a(k)"""
         e[w,h]=E[w,h]-a[w,h]
         """w(epoch+1)=w(epoch)+lr*e(k)*x(k)"""
         w1+=lr*e[w,h]*k1[w,h]
         w2+=lr*e[w,h]*k2[w,h]
         w3+=lr*e[w,h]*k3[w,h]
    print("epoch :",epoch)
    print("weight:",w1,w2,w3)
    epoch+=1



new=np.zeros((300,400))
new=(EP-(w1*k1)-(w2*k2))/w3

"""save and print answer"""
new=Image.fromarray(new)
new=new.convert('RGB')
new.save("Iprime.jpg")
new.show()

