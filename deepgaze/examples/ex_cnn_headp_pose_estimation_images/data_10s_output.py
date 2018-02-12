import os
import tensorflow as tf
import cv2
from deepgaze.head_pose_estimation import CnnHeadPoseEstimator

sess = tf.Session() #Launch the graph in a session.
my_head_pose_estimator = CnnHeadPoseEstimator(sess) #Head pose estimation object

# Load the weights from the configuration folders
my_head_pose_estimator.load_roll_variables(os.path.realpath("../../etc/tensorflow/head_pose/roll/cnn_cccdd_30k.tf"))
my_head_pose_estimator.load_pitch_variables(os.path.realpath("../../etc/tensorflow/head_pose/pitch/cnn_cccdd_30k.tf"))
my_head_pose_estimator.load_yaw_variables(os.path.realpath("../../etc/tensorflow/head_pose/yaw/cnn_cccdd_30k"))

from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, default="",
	help="path to input video file")
ap.add_argument("-o", "--output", type=str, default="",
	help="path to output video file")
args = vars(ap.parse_args())


img_folder_path = args["video"]
dirListing = os.listdir(img_folder_path)
l=len(dirListing)
print(len(dirListing))



filename = args["output"]+".txt"
print filename
f=open(filename,'w')





f.write("Frame Roll Pitch Yaw\n")
i=1
while (i<l):

    if(i>=1 and i<=9):
	image = args["video"]+"/frame_det_00000"+str(i) + ".bmp"
    elif(i>=10 and i<=99):
	image = args["video"]+"/frame_det_0000"+str(i) + ".bmp"
    elif(i>=100 and i<=999):
	image = args["video"]+"/frame_det_000"+str(i) + ".bmp"
    elif(i>=1000 and i<=9999):
	image = args["video"]+"/frame_det_00"+str(i) + ".bmp"
    elif(i>=1000 and i<=9999):
	image = args["video"]+"/frame_det_00"+str(i) + ".bmp"
    else:
	image = args["video"]+"/frame_det_0"+str(i) + ".bmp"

    #print image
    #i=i+1
    print("Processing image ..... " + image)
    
    image = cv2.imread(image) #Read the image with OpenCV
    
    image = cv2.resize(image,(200,200))
    # Get the angles for roll, pitch and yaw
    roll = my_head_pose_estimator.return_roll(image)  # Evaluate the roll angle using a CNN
    pitch = my_head_pose_estimator.return_pitch(image)  # Evaluate the pitch angle using a CNN
    yaw = my_head_pose_estimator.return_yaw(image)  # Evaluate the yaw angle using a CNN
    print("Estimated [roll, pitch, yaw] ..... [" + str(roll[0,0,0]) + "," + str(pitch[0,0,0]) + "," + str(yaw[0,0,0])  + "]")
    f.write(str(i) + " " + str(roll[0,0,0]) + " " + str(pitch[0,0,0]) + " " + str(yaw[0,0,0]) +"\n")
    i=i+1;


print "done"
f.close()

