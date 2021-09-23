#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:57:03 2020

@author: asegal
"""
import numpy as np
import nibabel as nb

surf_labels_lh = nb.freesurfer.read_annot('/home/npham/kg98_scratch/Honours_2021/data/fsaverage/lh.Schaefer2018_100Parcels_7Networks_order.annot')[0]
fileame = '/home/npham/kg98_scratch/Honours_2021/data/fsaverage/lh_Schaefer2018_100Parcels_7Networks_order_annot.txt'
np.savetxt(fileame, surf_labels_lh)


surf_labels_rh = nb.freesurfer.read_annot('/home/npham/kg98_scratch/Honours_2021/data/fsaverage/rh.Schaefer2018_100Parcels_7Networks_order.annot')[0]
fileame = '/home/npham/kg98_scratch/Honours_2021/data/fsaverage/rh_Schaefer2018_100Parcels_7Networks_order_annot.txt'
np.savetxt(fileame, surf_labels_rh)
