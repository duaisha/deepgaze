
#!/bin/bash
clear

for i in {1..500}
do
echo $i

python test.py -v "../../../trip3/trip$value""_front-$i""crop.avi" -o "../../../output/poses/trip$value""_front-$i""_poses"

done
fi

#done
echo All done


