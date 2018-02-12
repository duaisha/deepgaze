#!/usr/bin/env python

#The MIT License (MIT)
#Copyright (c) 2016 Massimiliano Patacchiola
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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


for j=1..3:
filename = 'trip4.txt'
f=open(filename,'w')


f.write("Frame Roll Pitch Yaw\n")
i=1
while (i<1382):

    if(i>=1 and i<=9):
	file_name = "trip4/frame_det_00000"+str(i) + ".bmp"
    elif(i>=10 and i<=99):
	file_name = "trip4/frame_det_0000"+str(i) + ".bmp"
    elif(i>=100 and i<=999):
	file_name = "trip4/frame_det_000"+str(i) + ".bmp"
    elif(i>=1000 and i<=9999):
	file_name = "trip4/frame_det_00"+str(i) + ".bmp"
    elif(i>=1000 and i<=9999):
	file_name = "trip4/frame_det_00"+str(i) + ".bmp"
    else:
	file_name = "trip4/frame_det_0"+str(i) + ".bmp"

    print("Processing image ..... " + file_name)
    image = cv2.imread(file_name) #Read the image with OpenCV
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
