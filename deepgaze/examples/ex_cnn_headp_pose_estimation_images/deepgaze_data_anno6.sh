#!/bin/bash
clear


for i in {401..500}
do
echo $i
 
x="../../../driver_assistance_project/openface_outputs/output_openface_testing/output_openface_faces/trip$i"
echo "$x"
y="../../../driver_assistance_project/openface_poses/testing_openface_poses/trip$i"
echo "$y"
time python data_10s_output.py -v "../../../driver_assistance_project/openface_outputs/output_openface_testing/output_openface_faces/trip$i" -o "../../../driver_assistance_project/openface_poses/testing_openface_poses/trip$i"
done

echo All done


