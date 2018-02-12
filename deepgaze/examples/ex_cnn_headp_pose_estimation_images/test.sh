#!/bin/bash
clear


#for value in {1..22}
#do
value=3
echo $value

if [ $value -ne 5 ]
then
for i in {0..45}
do
echo $i
#i=1
#echo $i
x="../../../trip3/trip$value""_front-$i""crop.avi"
echo "$x"
y="../../../output/poses/trip$value""_front-$i""_poses.txt"
echo "$y"
python test.py -v "../../../trip3/trip$value""_front-$i""crop.avi" -o "../../../output/poses/trip$value""_front-$i""_poses"

done
fi

#done
echo All done


