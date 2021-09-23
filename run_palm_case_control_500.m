
% add palm to path 
addpath ('/home/npham/kg98/Ashlea/code/PALM-master');

wdir = ('/home/npham/kg98_scratch/Honours_2021/Nathan/code/case-control/PALM_500')
% path to your working directory where the output is saved
cd(wdir)

% inputs for palm
design_matrix = 'design_matrix.mat';
design_contrast = 'design_contrasts.con';
inputs = 'subj_x_roi_inputs.csv' ;
outfilename = 'palm';

% run palm command 
palmCommand = ['palm -i ',inputs,' -d ',design_matrix,' -o ',outfilename, ' -t ',design_contrast, ' -corrcon -fdr -n 10000'];
eval(palmCommand);

% ONCE FINISHED
%can load in palm outputs to look at results 
pvals_fwe_c2 = load('palm_dat_tstat_cfwep_c2.csv');
pvals_fdr_c2 = load('palm_dat_tstat_cfdrp_c2.csv');
pvals_unc_c2 = load('palm_dat_tstat_uncp_c2.csv');

plot(pvals_fwe_c2)
plot(pvals_fdr_c2)
plot(pvals_unc_c2)