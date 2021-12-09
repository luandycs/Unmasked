import urllib

import os
from PIL import Image
from facerecognizer import FaceRecognizer
import cv2 as cv
import TakePicture
import Detector
import time

fr = FaceRecognizer()
# ctrl + C to quit program
fr.startDetect()
