#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 17:35:52 2021

@author: npham
"""


def find_excluded_subjs_pca(datadir,brain_input,numparc,dataset,thr):
    
    import os
    import numpy as np
    from scipy import stats
    import pandas as pd
    from sklearn import decomposition
    import matplotlib.pyplot as plt
    
    pca_outdir = datadir + '/' + dataset + '/derivatives/pca_results'
    if not os.path.exists(pca_outdir): # make directory if doesn't exist
        os.makedirs(pca_outdir)
    
    print('Data directory: ',datadir)
    print('Brain Input: ',brain_input)
    print('Number of parcellations: ',numparc)
    print('Dataset: ',dataset)
    print('Threshold: ',thr)
    
    if brain_input == 'ct':

        hemispheres = ['lh', 'rh']

        # Load in your data (or use random data)
        data_matrix = dict()
    
        # for each hemisphere
        for hemisphere in hemispheres:
            
            filename = datadir + '/' + dataset + '/stats_files/aparc_'+ hemisphere + 'stats_'+numparc+'.txt' #Filename for hemisphere
            df = pd.read_table(filename) # load hemisphere txt file
        
            IDs = df.iloc[:,0].tolist() # Extract subj ids 
            df_tmp = df.iloc[:,1:51] # remove two wextra columns that we are not interested in
            data_matrix[hemisphere] = df_tmp.values # convert cort thicks measures to matrix (ignores subj ids)
            
        data = np.concatenate((data_matrix['lh'],data_matrix['rh']),axis=1) # combines lh and rh together
            
    elif brain_input =='mriqc':
        
        filename = datadir + '/' + dataset + '/derivatives/mriqc/T1w_cleaned_nath_v2.csv' #Filename for hemisphere
        df = pd.read_table(filename,delimiter=',') # load hemisphere txt file
        
        IDs = df.iloc[:,0].tolist() # Extract subj ids 
        df_tmp = df.iloc[:,1:] # remove two wextra columns that we are not interested in
        data = df_tmp.values # convert cort thicks measures to matrix (ignores subj ids)
    
    # Run PCA and plot
    pca = decomposition.PCA(svd_solver='full')
    PCA_OUTPUT = pca.fit_transform(data)

    # Visualise eigens and variance explained
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance')
    figName = pca_outdir + '/' + brain_input + '_' +numparc+ '_' + 'pca_screeplot.png'
    plt.savefig(figName, dpi=150)
    plt.clf()   # Clear figure
    
    # run PCA for only 80% of the variance
    PCA_OUTPUT = pca.fit_transform(data)
    pca = decomposition.PCA(n_components = 0.8, svd_solver='full')

    # pca.explained_variance_ratio_ contains the eigenvalues of the covariance matrix for each component
    # Summing this provides the cumulative variance for all components up until the nth component
    # e.g. the amount of variance of your original data that can be explained by using the first n components alone
    
    # z-scores for outliers
    z_PCA = stats.zscore(PCA_OUTPUT)
    
    # Add IDs because I never made that on my random data
    rows, cols = z_PCA.shape
    
    # Create pretty column names
    PC_labels = np.arange(cols)
    PC_labels = [x+1 for x in PC_labels]
    PC_labels = [str(x) for x in PC_labels]
    PC_labels = ['PC' + x for x in PC_labels]
    
    # Turn it into a dataframe because we're learning about pandas now
    z_PCA_df = pd.DataFrame(z_PCA, columns=PC_labels)
    z_PCA_df.index = IDs # change index to subject ids
    
    
    #Remove outliers with z-score greater than threshold (4)
    THRESHOLD=thr
    z_PCA_df_clean = z_PCA_df[(z_PCA_df[PC_labels] < THRESHOLD) & (z_PCA_df[PC_labels] > THRESHOLD*-1)]
    z_PCA_df_clean = z_PCA_df_clean.dropna(how='any')
    z_PCA_df_outliers = z_PCA_df[(z_PCA_df[PC_labels] >= THRESHOLD) | (z_PCA_df[PC_labels] <= THRESHOLD*-1)]
    z_PCA_df_outliers = z_PCA_df_outliers.dropna(how='all')
    
    print('Number of excluded subjs:',len(z_PCA_df_outliers))
    if len(z_PCA_df_outliers) > 0:
        subjs_excluded = z_PCA_df_outliers.index.values.tolist() 
        print('Which subjects are excluded:\n',subjs_excluded)
