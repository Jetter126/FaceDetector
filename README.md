# FaceDetector
 FaceDetector uses OpenCV and a Haar Cascade to read a list of image paths, detect the faces in each image and return the number of faces.

### Prerequisites for usage

* haarcascade_frontalface_default.xml stored in the same
  directory as the program, downloaded from GitHub
  [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
* Images to detect faces in
* Text file "paths.txt" stored in the same directory as
  the program, containing the paths with filenames of
  each image on a new line

### Examples

This repository currently has 3 examples of images:

* Chelsea.jpg
* Golden State Warriors.jpg
* LM.png

The paths of these images are listed in paths.txt