import cv2
import numpy as np

# Load image
img = cv2.imread("C:\\Users\\deepika\\Downloads\\hi.jpg")

# Define the mapping function
xp, fp = [0, 64, 128, 192, 255], [0, 16, 128, 240, 255]
table = np.interp(np.arange(256), xp, fp).astype('uint8')

# Apply the mapping function
img = cv2.LUT(img, table)

# Resize both original and output images to fit within the window
max_height = 500
max_width = 700
scale = min(max_height / img.shape[0], max_width / img.shape[1])
output_resized = cv2.resize(img, None, fx=scale, fy=scale)
original_resized = cv2.resize(img, None, fx=scale, fy=scale)

# Display original and output images
cv2.imshow("Original", original_resized)
cv2.imshow("Output", output_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
