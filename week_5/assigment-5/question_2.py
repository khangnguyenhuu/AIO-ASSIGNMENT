import numpy as np
import matplotlib.image as mpimg

# cau 12: Hoan thanh doan code sau day de chuyen anh mau sang anh xam dua vao phuong phap lightness
def calculate_ligthness(image):
    max_values = np.max(image, axis=-1)
    min_values = np.min(image, axis=-1)
    lightness = (max_values + min_values) / 2
    return lightness
img = mpimg.imread("dog.jpeg")
gray_img_01 = calculate_ligthness(img)
print("dap an cua cau 14 la: ", gray_img_01[0, 0])
print("="*20)
# dap an a

# cau 13: Hoan thanh doan code sau day de chuyen anh mau sang anh xam dua vao phuong phap average
def calculate_average(image):
    image = np.average(image, axis=-1)
    return image
img = mpimg.imread("dog.jpeg")
gray_img_02 =  np.average(img, axis=-1)
print("dap an cua cau 13 la:", gray_img_02[0, 0])
print("="*20)
# dap an a

# Cau 14: Hoan thanh doan code sau day de chuyen anh mau sang anh xam dua vao phuong Luminosity
img = mpimg.imread("dog.jpeg")
gray_img_03 = 0.21*img[:, :, 0] + 0.72*img[:, :, 1] + 0.07*img[:, :, 2]
print("dap an cau 14 la:", gray_img_03[0, 0])
print("="*20)
# dap an c