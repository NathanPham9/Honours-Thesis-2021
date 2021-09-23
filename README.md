# Honours-Thesis-2021
As a commitment to open source science I present the code used in my honour's thesis. This includes Python, MATLAB and Bash scripts. Massive thanks to Ash and Sid for teaching me how to code throughout my honours year and providing the structure of much of my code.

My thesis uses normative modelling (https://github.com/amarquand/PCNtoolkit) to map the heterogeneous cortical structure of depression at the level of the individual. Along with this I performed a permutation test using Permutation Analysis of Linear Models (https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM) to assess regional group differences. Regions were defined by the Schaefer Atlas 500 Regions (https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal).

Additional scripts are used to:
1. Reconstruct the cortical surface and calculate Euler numbers in FreeSurfer (https://surfer.nmr.mgh.harvard.edu/). 
2. Perform a Principal Components Analysis on output produced by MRIQC (https://mriqc.readthedocs.io/en/stable/).
