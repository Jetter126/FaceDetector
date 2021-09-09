'''
Face Detection Program by Ved Prasad, 2021
Prerequisites for usage:
    - haarcascade_frontalface_default.xml stored in the same
      directory as the program, downloaded from GitHub at
      https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
    - Images to detect faces in
    - Text file "paths.txt" stored in the same directory as
      the program, containing the paths with filenames of
      each image on a new line
'''

import cv2
import sys

# Load the Haar cascade frontal face pre-trained data
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read image paths and store them in a list
file = open("paths.txt", "r")
paths = file.readlines()

# Loop through each path
for path in paths:

    # Read image from path
    image = cv2.imread(path.strip())

    # Convert image to grayscale
    bw_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect face
    face_coordinates = trained_face_data.detectMultiScale(bw_image)

    # Draw rectangle
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display window with image
    cv2.imshow("Face Detector", image)
    key = cv2.waitKey()

    # Display the number of faces in each picture
    print(str(len(face_coordinates)) + " face(s) in " + path)

    # Quit if 'q' or 'Q' is pressed
    if key == 81 or key == 113:
        sys.exit()