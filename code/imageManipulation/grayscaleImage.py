import cv2

# read the image from a file
image = cv2.imread('IMAGE_FILEPATH')

# grayscale the image
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# write the image to a file
cv2.imwrite('GRAYSCALE_IMAGE_FILEPATH', grayscaleImage)