import cv2

image = cv2.imread("C:\\Users\\deepika\\Downloads\\rabbit.webp")

image = cv2.imread("C:\\Users\\deepika\\Downloads\\rabbit.webp")

# converting BGR to RGB

image_rgbb= cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

image_rgbg = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

image_rgbh = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

image_rgby = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

cv2.imshow('image1', image_rgbb)

cv2.imshow('image2', image_rgbg)

cv2.imshow('image3', image_rgbh)

cv2.imshow('image4', image_rgby)

cv2.waitKey(0)

cv2.destroyAllWindows()
