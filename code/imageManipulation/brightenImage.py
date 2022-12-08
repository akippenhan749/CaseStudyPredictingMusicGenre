import cv2

# function to increase the brightness of a given image by value amount
# taken from: https://stackoverflow.com/questions/32609098/how-to-fast-change-image-brightness-with-python-opencv
def increaseBrightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

# read the image from a file
image = cv2.imread('IMAGE_FILEPATH')

# choose the value for the VALUE variable below
brightenedImage = increaseBrightness(image, VALUE)

# write the image to a file
cv2.imwrite('BRIGHTENED_IMAGE_FILEPATH', brightenedImage)