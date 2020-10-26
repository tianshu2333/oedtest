import numpy as np
from matplotlib import pyplot as plt
data = np.random.randn(2, 3)
print(data)
#generate some random data
print(data.shape)
print(data.dtype)
#data types for ndarrays
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.shape)
#change the type of array
float_arr = arr1.astype(np.float64)
#calculate as matrix
arr2 = np.random.randn(2,3)
arr3 = np.random.randn(3,2)
arr4 = np.dot(arr2, arr3)   #mul
arr5 = np.arange(16).reshape((2,2,4))
arr5.swapaxes(1,2)
print(arr5)
m, n = (5, 3)
x = np.linspace(0, 1, m)
y = np.linspace(0, 1, n)
X, Y = np.meshgrid(x, y)
#heat map
points = np.linspace(-5, 5, 1000)
xs, ys = np.meshgrid(points, points)
plt.style.use('ggplot')

plt.plot(X, Y, marker='.', color='blue', linestyle='none')
plt.show()
#print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()

square = [ 1, 4, 9, 16, 25 ]     #平方函数
plt.plot (square)                #plot（）画图
plt.show()                       #plt.show（）图片查看
#logic calculation for arrays
arr6 = np.random.randn(4, 4)
arr7 = arr6 > 0
arr8 = np.where(arr7, 2, -2)
print(arr6)
print(arr8)