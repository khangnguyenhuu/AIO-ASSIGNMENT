# Cau 1: Cau nao sau day la dung de tao mang 1 chieu tu 0 -> 9
import numpy as np
arr = np.arange(0, 10, 1)
print("Dap an cau 1\n", arr)
print("="*20)
# dap an a

# Cau 2: Cach tao mot mang boolean 3x3 voi tat ca gia tri la True
arr = np.ones((3, 3), dtype=bool)
print("Dap an cau 2\n", arr)
print("="*20)
# dap an b

# Cau 3: Ket qua cua doan code sau day
arr = np.arange(0, 10)
print("Dap an cau 3\n", arr[arr%2==1])
print("="*20)
# dap an a

# Cau 4: Ket qua cua doan code sau day
arr = np.arange(0, 10)
arr[arr%2==1] = -1
print("Dap an cau 4\n", arr)
print("="*20)
# dap an b

# Cau 5: Ket qua cua doan code sau day
arr = np.arange(10)
arr_2d = arr.reshape(2, -1)
print("Dap an cau 5\n", arr_2d)
print("="*20)
# dap an b

# Cau 6: Ket qua cua doan code sau day
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=0)
print("Dap an cua cau 6\n", c)
print("="*20)
# dap an a

# Cau 7: Ket qua cua doan code sau day
arr1 = np.arange(10).reshape(2, -1)
arr2 = np.repeat(1, 10).reshape(2, -1)
c = np.concatenate([arr1, arr2], axis=1)
print("Dap an cua cau 7\n", c)
print("="*20)
# dap an c

# Cau 8: Ket qua cua doan code sau day
arr = np.array([1, 2, 3])
print(np.repeat(arr, 3))
print(np.tile(arr, 3))
print("="*20)
# dap an a

# Cau 9: Ket qua cua doan code sau day
a = np.array([2, 6, 1, 9, 10, 3, 27])
index = np.where((a >= 5)&(a<=10))
print("Ket qua cau 9\n", a[index])
print("="*20)
# dap an c

# Cau 10: Ket qua cua doan code sau day
def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(maxx, otypes=[float])
print("Dap an cau 10 la\n", pair_max(a, b))
print("="*20)
# dap an d

# Cau 11: Ket qua cua doan code sau day
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print("Dap an cua cau 11 la\n", np.where(a < b, b, a))
print("="*20)
# dap an a