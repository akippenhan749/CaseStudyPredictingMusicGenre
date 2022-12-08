import cv2

# function to flip a given image along either its x-axis, y-axis or both axes
def flipImage(image, method):
    match method: # choose which flipCode argument to provide to cv2.flip()
        case 'horizontal':
            flipCode = 1
        case 'vertical':
            flipCode = 0
        case 'both':
            flipCode = -1
        case _: # default case
            return 'Choose one of: \'horizontal\', \'vertical\', \'both\''
    return cv2.flip(image, flipCode)

# read the image from a file
image = cv2.imread('IMAGE_FILEPATH')

# choose the value for METHOD variable below
flippedImage = flipImage(image, METHOD)

# don't write to a file if flippedImage is a str
if not isinstance(flippedImage, str):
    cv2.imwrite('FLIPPED_IMAGE_FILEPATH', flippedImage)