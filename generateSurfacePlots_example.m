% add relevant paths 
addpath ('/usr/local/freesurfer/6.0/matlab');
addpath('~/kg98/Ashlea/code/cbrewer/cbrewer/cbrewer');
addpath('/fs03/kg98/Honours_2021/code/functions');


% Inputs for the function

% Working directory where the data is you want to plot
wdir = '/scratch/kg98/Honours_2021/Nathan/data/norm_model/MDD/real_model/run_1/';

% Data file to plot (1 x NROIs in size)
data_filename =  [wdir,'percent_tot_extrema_overlap_pos.txt'];

% Annot files which tells the function where each ROI is on the brain
atlas_annot_filename_lh = '/scratch/kg98/Honours_2021/data/fsaverage/lh_Schaefer2018_500Parcels_7Networks_order_annot.txt'
atlas_annot_filename_rh = '/scratch/kg98/Honours_2021/data/fsaverage/rh_Schaefer2018_500Parcels_7Networks_order_annot.txt'

% filename of output
outfile_string = [wdir, 'percent_tot_extrema_overlap_neg']; 

% Threshold range
thr = [0 10]

% Which colourmap you want to use
colourmap = cbrewer('seq', 'Reds', 256);
colourmap = cbrewer('seq', 'Blues', 256);
%colourmap = cbrewer('div', 'RdBu', 256);


% Run function to generate plot
thr = [0 6]
data_filename =  [wdir,'percent_tot_extrema_overlap_neg_cv.txt'];
CreateSurfacePlot(outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data_filename,thr,colourmap)