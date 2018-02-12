#!/bin/bash
clear

for i in {1..200}
do 
echo $i
START_TIME=$SECONDS
python data_10s.py -v  "../../../driver_assistance_project/ordered_dataset/training_ordered/trip$i"".mp4" -p  "../../../driver_assistance_project/tiny_faces_output/trained_tinyfaces/trip$i"".txt" -o "../../../driver_assistance_project/headpose/tiny_face/trip$i"".txt"


done
echo All 
