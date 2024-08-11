import numpy as np
import time
import random

# #Time test for NumPy
# n = 10**6
# a = [random.random() for i in range(n)]
# b = [random.random() for i in range(n)]

# s = time.time()
# c = [a[i] * b[i] for i in range(n)]
# print("comprehension:", time.time() - s)

# s = time.time()
# c = []
# for i in range(n):
#     c.append(a[i] * b[i])
# print("for loop: ", time.time() - s)

# s = time.time()
# c = [0] * n
# for i in range(n):
#     c[i] = a[i] * b[i]
# print("existing list: ", time.time() - s)

# x = np.array(a)
# y = np.array(b)
# s = time.time()
# c = x * y
# print("NumPy time: ", time.time() - s)

# Reading files
a = np.loadtxt("abc.txt")

a = np.loadtxt("abc_tab.txt")

a = np.loadtxt("abc.csv", delimiter=",")

np.save("abc.npy", a)
b = np.load("abc.npy")
# np.savetxt("ABC.txt", b)
# np.savetxt("ABC.csv", b, delimiter=",")

np.savez_compressed("arrays.npz", a=a, b=b)
q = np.load("arrays.npz")
print(list(q.keys()))
print(q['a'])
print(q['b'])