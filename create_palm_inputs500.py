#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 11:11:43 2021

@author: npham
"""

import os
import pandas as pd
import numpy as np

datasets = ['KANMDD','RUSMDD','YMDD']
outdir = '/home/npham/kg98_scratch/Honours_2021/Nathan/code/case-control/PALM_500/'
for d,dataset in zip(range(len(datasets)),datasets):


    data_dir = '/scratch/kg98/Honours_2021/data/'+dataset+'/stats_files'
    subjlist_dir = '/scratch/kg98/Honours_2021/Nathan/subjlist/subjlist_excluded'
    os.chdir(data_dir)
    
    # load metadat file 
    metadata_filename = subjlist_dir + '/'+dataset+'_master_ex.csv'
    metadata = pd.read_table(metadata_filename,delimiter=',')
    # Load stat files 
    lh_stats_file = 'xaparc_lhstats_500.txt'
    lh_stats = pd.read_table(lh_stats_file,delimiter=',')
    
    rh_stats_file = 'xaparc_rhstats_500.txt'
    rh_stats = pd.read_table(rh_stats_file,delimiter=',')
    
    # Get subject list from stat files 
    subj_ids = lh_stats['lh.Schaefer2018_500Parcels_7Networks_order.thickness'].tolist() # get subject list
    subj_ids = [s[:-3] for s in subj_ids] # remove _fs in string
    
    # remove extra columns
    lh_stats = lh_stats.iloc[:,1:-2] # remove extra co
    rh_stats = rh_stats.iloc[:,1:-2] # remove extra co
    
    # concat lh and rh
    stats = pd.concat([lh_stats,rh_stats],axis=1)
    #convert to numpy 
    stats_numpy = stats.to_numpy()
    
    # get the age and sex of participants 
    dataset_covs = np.zeros((len(subj_ids),4))
    for i,subj in zip(range(len(subj_ids)),subj_ids):
        
        idx = [i for i, j in enumerate(metadata['subj_id']) if j == subj]   
        dataset_covs[i,0] = metadata['diagnosis'].iloc[idx]   
        dataset_covs[i,1] = metadata['age'].iloc[idx]
        dataset_covs[i,2] = metadata['sex'].iloc[idx]
        dataset_covs[i,3] = d

    if d is 0:
        allStats = stats_numpy  
        allCovs = dataset_covs
    else:
        allStats = np.concatenate([allStats, stats_numpy])    
        allCovs = np.concatenate([allCovs, dataset_covs])
        
idx = np.where(allCovs[:,0]!=1)[0]
allCovs[idx,0] = -1
        
# create design contrast
design_contrast = np.zeros((2, 4))
design_contrast[0,0] = 1
design_contrast[1,0] = -1

# Save output as txt files
os.chdir(outdir)

np.savetxt('design_matrix.txt', allCovs)
np.savetxt('design_contrasts.txt', design_contrast)
np.savetxt('subj_x_roi_inputs.csv', allStats)

#Convert txt files to correct format for 
command = 'module load fsl; Text2Vest design_contrasts.txt design_contrasts.con ; Text2Vest design_matrix.txt design_matrix.mat' 
os.system(command)
