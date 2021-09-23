#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 09:56:40 2021

@author: npham
"""

# Example usage:
import sys

# Load in function that lists all subjs excluded, depending on threshold set
function_path = '/scratch/kg98/Honours_2021/code/functions'
sys.path.append(function_path)
from qc_pca_functions import find_excluded_subjs_pca
    
# variable that we can vary
datadir = '/scratch/kg98/Honours_2021/data'
datasets = ['RUSMDD']
numparc_options = ['100','400','1000']
threshold_options = [3,3.5,4] # could also make a for loop so it loop through thresholds
brain_inputs = ['ct','mriqc','sa'] # could also make a for loop so it loops through brain inpts


#For each dataset, for each parcellation optn, run code. 
for dataset in datasets:
    for numparc in numparc_options:
        
        thr = 4
        brain_input = 'mriqc'
        find_excluded_subjs_pca(datadir,brain_input,numparc,dataset,thr)
        
        
