#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 10:53:00 2021

@author: asegal
"""

import os
import pandas as pd
import numpy as np

Nrois = 500
datasets = ['GOC','KANMDD', 'RUSMDD','YMDD']
outdir = '/scratch/kg98/Honours_2021/Nathan/data/norm_model/MDD'
for d,dataset in zip(range(len(datasets)),datasets):
    
    data_dir = '/scratch/kg98/Honours_2021/data/'+dataset+'/stats_files'
    subjlist_dir = '/scratch/kg98/Honours_2021/Nathan/subjlist'
    os.chdir(data_dir)
     
    # load metadat file 
    metadata_filename = subjlist_dir + '/'+dataset+'_master_nath_under40s.csv'
    metadata_dataset = pd.read_table(metadata_filename,delimiter=',')
    
    # give unqiue size number
    metadata_dataset['site'] = d
    
     # Load stat files     
    lh_stats_file = 'aparc_lhstats_'+str(Nrois)+'.txt'
    rh_stats_file = 'aparc_rhstats_'+str(Nrois)+'.txt'


    if dataset =='GOC':
        lh_stats = pd.read_table(lh_stats_file)
        rh_stats = pd.read_table(rh_stats_file)
    else:
        lh_stats = pd.read_table(lh_stats_file,delimiter=',')
        rh_stats = pd.read_table(rh_stats_file,delimiter=',')
        
    
    # Get subject list from stat files 
    subj_ids_ct = lh_stats['lh.Schaefer2018_'+str(Nrois)+'Parcels_7Networks_order.thickness'].tolist() # get subject list
    subj_ids_ct = [s[:-3] for s in subj_ids_ct] # remove _fs in string
    
    # remove extra columns
    lh_stats = lh_stats.iloc[:,1:-2] # remove extra columns
    rh_stats = rh_stats.iloc[:,1:-2] # remove extra columns
    
    # concat lh and rh
    stats = pd.concat([lh_stats,rh_stats],axis=1)
    #convert to numpy 
    stats_numpy = stats.to_numpy()

    #numROIs = np.shape(stats)[1] # get number of ROI
    
    # get ct data in same oder as metadata 
    sub_x_ROIs_dataset = np.zeros((len(metadata_dataset['subj_id']),Nrois))
    for k in range(len(metadata_dataset['subj_id'])):

        print('Metadata subj: ',metadata_dataset['subj_id'].iloc[k])        
        idx = [i for i, j in enumerate(subj_ids_ct) if j == metadata_dataset['subj_id'].iloc[k]]  
        idx = int(idx[0]) # need to fix this line so index in a int to list
        print('CT subj: ',subj_ids_ct[idx])

        sub_x_ROIs_dataset[k,:] = stats_numpy[idx]
        
    if d == 0: 
        metadata_all = metadata_dataset
        sub_x_ROIs = sub_x_ROIs_dataset
    else: 
        metadata_all = pd.concat([metadata_all,metadata_dataset])
        sub_x_ROIs = np.concatenate([sub_x_ROIs, sub_x_ROIs_dataset])
        
idx = [i for i, j in enumerate(metadata_all['diagnosis_string']) if j == 'MDD']
metadata_all['diagnosis'].iloc[idx] = 2


outdir = '/scratch/kg98/Honours_2021/Nathan/data/norm_model/MDD'
os.chdir(outdir)

metadata_all.to_csv('metadata.csv', index=False)
anat_ct_filename = 'anat_ct_'+str(Nrois)+'Parcels.txt'
np.savetxt(anat_ct_filename,sub_x_ROIs)