#!/bin/env bash

#SBATCH --job-name=loop_for_stats
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=npha0013@student.monash.edu
#SBATCH --mail-type=FAIL
# SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mem-per-cpu=4G
#SBATCH --time 20:00:00

module load freesurfer/6.0
SUBJECTS_DIR=/home/npham/kg98_scratch/Honours_2021/data/KANMDD

for h in lh rh ; do
for p in 100 200 300 400 500 600 700 800 900 1000 ; do
aparcstats2table --subjectsfile=${SUBJECTS_DIR}/subjlist_fs.txt --meas thickness --hemi ${h} --parc Schaefer2018_${p}Parcels_7Networks_order --skip --tablefile ${SUBJECTS_DIR}/stats_2/aparc_${h}stats_${p}.txt 
done ; done


