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
ap.add_argument("-p", "--input_text", type=str, default="",
	help="path to input_text file")
ap.add_argument("-o", "--output", type=str, default="",
	help="path to output text file")
args = vars(ap.parse_args())


f1=open(args["input_text"]);
lines1=f1.read().splitlines()

filename = args["output"]
print filename
f=open(filename,'w')

f.write("Frame Roll Pitch Yaw\n")

cap = cv2.VideoCapture(args["video"]);
ret,frame=cap.read()
s=frame.shape

end=len(filename)
video_filename=filename[:end-3]+"mp4"

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter(video_filename,fourcc, 10.0, (s[1],s[0]))
count=0
for x in lines1 :
	count=count+1

	print("Processing image ..... " + str(count))
	ret,frame=cap.read()
	if (ret==True):
		a1=x.split(',')[2]
		a2=x.split(',')[3]
		a3=x.split(',')[4]
		a4=x.split(',')[5]

		a1=int(a1)+90
		a2=int(a2)+110
		a3=int(a3)-40
		a4=int(a4)-40
		w= a4-a2
		h=a3-a1
		
		#print type(w)
		#print type(h)
		#print abs(int(a1))
		#print frame.shape
		if(w>10 and h>10):
			
			if(int(a1)<0):
				a1=0;
			print a1,a2,a3,a4
			cv2.rectangle(frame, (int(a1),int(a2)), (int(a3),int(a4)), (0, 255, 0), 2)
			cv2.imshow('frame',frame)
			#cv2.rectangle(frame, (100,200), (300,400), (0, 255, 0), 2)

			crop_frame=frame[a2:a2+w,a1:a1+h]
			#print crop_frame
			#print crop_frame
			#cv2.imshow('frame',crop_frame)
			#name1 = "trip5/frame%d.jpg"%count
       			#cv2.imwrite(name1, crop_frame)
			s=crop_frame.shape
			image = cv2.resize(crop_frame,(s[1]/2,s[0]/2))
    			# Get the angles for roll, pitch and yaw
    			name1 = "trip5/frame%d.jpg"%count
       			cv2.imwrite(name1,image)
			if cv2.waitKey(1) & 0xFF == ord('q'):
            			break
	else:
		break
		

print "done"	
out.close()
f1.close()
