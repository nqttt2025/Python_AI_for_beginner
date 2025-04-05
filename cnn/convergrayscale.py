# import opencv
import cv2
import numpy as np

# Load the input image
image = cv2.imread('/home/eenitug/Python_AI_for_beginner/cnn/images_dataset/tomatoes.jpg')
image2 = cv2.imread('/home/eenitug/Python_AI_for_beginner/cnn/images_dataset/IMG20220813115020.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

cv2.imwrite('/home/eenitug/Python_AI_for_beginner/cnn/tomatoes_grayscale.jpg', gray_image)

kernal = np.array([[0, 1, 0],
                  [1, -4, 1],
                  [0, 1, 0]])

convoled_image = cv2.filter2D(gray_image, -1, kernal)
convoled_image2 = cv2.filter2D(gray_image2, -1, kernal)
# cv2.imwrite('/home/eenitug/Python_AI_for_beginner/cnn/tomatoes_convolved.jpg', convoled_image)
cv2.imwrite('/home/eenitug/Python_AI_for_beginner/cnn/IMG20220813115020_convolved.jpg', convoled_image2)
