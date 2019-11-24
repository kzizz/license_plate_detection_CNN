#!/usr/bin/env python

import cv2
import numpy as np
import sys
import time
import random


imgWidth = 95
imgHeight = 170

def augmentImage(image):
    distortedImage = 0
    # possible operations
    # color distortion, random blur, shear transform, decrease resolution
    possibleResolutions = [10,20,30,40,50,60]
    possibleBlurs = [5,11,19,21,31,35]
    possibleChannels = [cv2.COLOR_BGR2HSV,cv2.COLOR_BGR2GRAY,'BGR'] #or keep BGR
    possibleOperations = [possibleResolutions,possibleBlurs,possibleChannels]
    possibleFunctions = [lowerResolution,blur,changeColorChannel]
    for index,operation in enumerate(possibleOperations):
        numberOfOptions = len(operation)
        randomOperation = operation[random.randint(0,numberOfOptions-1)]
        distortedImage = possibleFunctions[index](image,randomOperation)
    cv2.imshow("distorted image", distortedImage)
def changeColorChannel(image,channel):
    if(channel != 'BGR'):
        newImage = cv2.cvtColor(image,channel)
    else:
        newImage = image
    return newImage
        
# lowers the resolution of the image
def blur(image,kernelVal):
    print(kernelVal)
    return cv2.GaussianBlur(image,(kernelVal,kernelVal),cv2.BORDER_DEFAULT)

def lowerResolution(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    resizedImage = cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
    lowResImage = cv2.resize(resizedImage,(imgWidth,imgHeight))
    return lowResImage


def main(args):
    image = cv2.imread('./cropped/croppedA/A2.png')
    print(image)
    cv2.imshow("image",image)
    cv2.waitKey(3)
    augmentImage(image)

if __name__ == '__main__':
    main(sys.argv)
