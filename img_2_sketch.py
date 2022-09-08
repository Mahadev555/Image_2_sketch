#import the libray 
import cv2

#img name
filename = 'img5.jpeg'

#Read the image
img = cv2.imread(filename)

#convert img to gray scale
gray_image = cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)

#invert the image
invt_gr_img = 255 - gray_image

#blur image by guassian function 
blurred_img = cv2.GaussianBlur(invt_gr_img,(21,21),0)

#invert the blur image
invt_blur_img = 255 - blurred_img

#Create the pencil sketch img
sketch_image = cv2.divide(gray_image,invt_blur_img,scale = 256.0)

#Show the image
cv2.imshow('original image',img)
cv2.imshow('pencil sketch',sketch_image )
cv2.waitKey(0)