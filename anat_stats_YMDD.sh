#!/bin/env bash

#SBATCH --job-name=anat_stats_RUSMDD
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=npha0013@student.monash.edu
#SBATCH --mail-type=FAIL
# SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mem-per-cpu=4G
#SBATCH --time 20:00:00

module load freesurfer/6.0
SUBJECTS_DIR=/home/npham/kg98_scratch/Honours_2021/data/YMDD/YMDD_all_data

for i in `cat ${SUBJECTS_DIR}/subjlist_fs.txt` ; do
for h in lh rh ; do
for p in 100 300 1000 ; do
mris_anatomical_stats -a ${SUBJECTS_DIR}/${i}/label/${h}.Schaefer2018_${p}Parcels_7Networks_order.annot \
-f ${SUBJECTS_DIR}/${i}/stats/${h}.Schaefer2018_${p}Parcels_7Networks_order.stats ${i} ${h}
done ; done ; done
