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

# construct the argument parse and parse the arguments
input_file='../../../../../shared/fusor/home/isha.d/data_10s/'
output_file='../../../../../shared/fusor/home/isha.d/output/deepgaze/'


#vs = FileVideoStream(args["video"]).start()

vs = cv2.VideoCapture(args["video"])
fileStream = True
time.sleep(1.0)
count = -1
vidcount = 1
filename = args["output"] + '.txt'
f=open(filename,'w')
width = vs.get(3)
height = vs.get(4)
#out = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc('H','2','6','4'), 24, (width,height))
# loop over frames from the video stream
print "\nFrame Roll Pitch Yaw\n"
f.write("Frame Roll Pitch Yaw\n")
while True:
        count = count + 1
	# if this is a file video stream, then we need to check if
	# there any more frames left in the buffer to process
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale
	# channels)
	ret,image = vs.read()
	if not ret:
		break
	image = cv2.resize(image,(200,200))
        roll = my_head_pose_estimator.return_roll(image)  # Evaluate the roll angle using a CNN
        pitch = my_head_pose_estimator.return_pitch(image)  # Evaluate the pitch angle using a CNN
        yaw = my_head_pose_estimator.return_yaw(image)  # Evaluate the yaw angle using a CNN
        print str(count) + " " + str(roll[0,0,0]) + " " + str(pitch[0,0,0]) + " " + str(yaw[0,0,0])
	f.write(str(count) + " " + str(roll[0,0,0]) + " " + str(pitch[0,0,0]) + " " + str(yaw[0,0,0]) +"\n")
        cv2.imshow("Frame", image)
    	key = cv2.waitKey(1) & 0xFF
            # count = count + 1
    	# if the `q` key was pressed, break from the loop
    	if key == ord("q"):
    		break
	# frame = imutils.resize(frame, width=450)
	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
f.close()
#out.release()
cv2.destroyAllWindows()
