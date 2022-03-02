import cv2
import numpy as np

def save_matrix(name: str, matrix: np.ndarray) -> None:
    with open(f'{name}.txt', 'w') as f:
        for i in range(h):
            for j in range(w):
                f.write(str(matrix[i][j]))
                f.write("\n")

#kordinat Crop
x = 350
y = 40
w = 300
h = 300

#Letak Gambar
img = cv2.imread("C:\\Users\\danim\\Downloads\\putin.jpg")

#Crop Gambar
crop_image = img[y:y+h, x:x+w]

#Convert warna gambar
crop_gray_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
crop_green_image = cv2.cvtColor(crop_image, cv2.COLOR_BGR2HSV )

#Cetak Matrix Array
save_matrix("Gambar Crop", crop_image)
save_matrix("Gambar Abu Abu", crop_gray_image)

#Tampil Gambar
cv2.imshow("Gambar Crop", crop_image)
cv2.imshow("Gambar Abu Abu", crop_gray_image)
cv2.imshow("Gambar Hijau", crop_green_image)
cv2.imshow("gambar original", img)
cv2.waitKey(0)