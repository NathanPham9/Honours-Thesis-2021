# This one seems to show the original topological problems, put into Euler.txt file
# Change to lh or rh as needed
module load freesurfer/6.0
for i in `cat subjlist_fs.txt` ; do 
echo ${i} >> Euler_rh.txt
mris_euler_number /home/npham/kg98_scratch/Honours_2021/data/YMDD/${i}/surf/rh.orig.nofix 2>> Euler_rh.txt ; done


#Full pipe
awk -F">" '{ print $NF; }' Euler_rh.txt | awk '/sub/+/holes/' >> defects_rh.txt
