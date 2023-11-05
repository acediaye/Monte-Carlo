import numpy as np
import matplotlib.pyplot as plt

num_sim = 10000
num_circle = 0
num_square = 0

x_arr = np.zeros((1, num_sim))
y_arr = np.zeros((1, num_sim))
pi_arr = np.zeros((1, num_sim))
idx_arr = np.zeros((1, num_sim))
# print(np.size(x_arr))
# print(x_arr[0,0])

for i in range(0, num_sim):
    # random generate points
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    x_arr[0,i] = x
    y_arr[0,i] = y
    
    # compare points in area
    r = x**2 + y**2
    if r <= 1:
        num_circle += 1
    num_square += 1
    
    # converge to pi
    pi = 4*num_circle/num_square
    pi_arr[0,i] = pi
    idx_arr[0,i] = i
    # print(i)
    
plt.figure(1)
plt.plot(x_arr, y_arr, 'o')
# square limits
plt.plot([-1, -1], [-1, 1], 'r')
plt.plot([1, 1], [-1, 1], 'r')
plt.plot([-1, 1], [1, 1], 'r')
plt.plot([-1, 1], [-1, -1], 'r')
# circle limits
theta = np.arange(0, 2*np.pi, 0.01)
radius = 1
xp = 0 + radius*np.cos(theta)
yp = 0 + radius*np.sin(theta)
plt.plot(xp, yp, 'b')

plt.figure(2)
plt.plot(idx_arr[0,:], pi_arr[0,:], '-')  # [1,x] to [,x] dimension
print(f'expected   pi: {np.pi}')
print(f'calculated pi: {pi}')
plt.show()

print('done')

# circle = r^2*pi
# square = (2r)^2
# circle/square = r^2*pi/(2r)^2 = pi/4
# pi = 4*circle/square