
import numpy as np

def problem1():
    array1 = [0, 10, 20, 40, 60, 80]
    array2 = [10, 30, 40, 50, 70]
    union = np.union1d(np.array(array1),np.array(array2))
    print(union)

def problem2():
    array1 = [1,2]
    array2 = [4,5]
    print("a > b\n",np.greater(array1,array2))
    print("a >= b\n",np.greater_equal(array1,array2))
    print("a < b\n",np.less(array1,array2))
    print("a <= b\n",np.less_equal(array1,array2))

def problem3():
    x = np.array([[2, 4, 6], [6, 8, 10]])
    print(type(x))
    print(x.shape)
    print(x.dtype)

def problem4():
    array_filled_0 = np.full((3, 5), 0)
    array_filled_12 = np.full((3, 5), 12)
    print("With Zero: \n",array_filled_0)
    print("Filled with 12 \n",array_filled_12)

def problem5():
    n = int(input("Enter the Number: "))
    for i in range(1,11):
        print(n,"*",i," = ",n*i)

def problem7():
    matrix1 = np.array([[2, 4, 6], [6, 8, 10], [2, 4, 6]])
    matrix2 = np.array([[1, 7, 4], [3, 9, 1], [5, 3, 2]])
    sum_matrix = matrix1 + matrix2
    sub_matrix = matrix1 - matrix2
    print("Matrix Sum: \n",sum_matrix,end='\n\n')
    print("Matrix Sub: \n",sub_matrix,end='\n\n')


problem1()
