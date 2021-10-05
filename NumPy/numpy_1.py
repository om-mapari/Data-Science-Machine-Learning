import numpy as np
myarr = np.array([[3, 42, 5, 33, 1]], dtype=np.int64)

print(myarr[0][1])
# print(myarr.shape, myarr.dtype)
print(myarr.dtype)
print(myarr.shape)


# array creation
listarray = np.array([[3, 34, 5, 2], [3, 1, 5, 4], [3, 8, 2, 4]])
print("\n", listarray)
print("\n", listarray.shape, listarray.size, listarray.dtype)

print("take input")
x = 3.33
print("x  = ", np.floor(x))
print("x  = ", np.ceil(x))

# condition
if(x > 4):
    print("hello")
else:
    print("karna")
