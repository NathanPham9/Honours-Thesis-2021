function CreateSurfacePlot(outfile_string,atlas_annot_filename_lh,atlas_annot_filename_rh, data_filename,thr,colourmap)

% Data to plot
data = load(data_filename);
Nrois = length(data);
% Load Stu's Template
codeDir = '~/kg98/Ashlea/code/plotSurfaceROIBoundary-master';
% codeDir = '/home/npham/kg98_scratch/Honours_2021/Nathan/code/brain_maps/ROI' ;
addpath(codeDir);

load([codeDir,'/fsaverage_surface_data.mat'])
%,'lh_inflated_verts','lh_verts','lh_faces','lh_HCPMMP1','lh_aparc','lh_rand200','lh_sulc')


colors = colourmap % cbrewer('div', 'RdBu', 256);
%%
t = tiledlayout(1,4,'Padding','tight');
t.TileSpacing = 'tight';
%figure('Position',[1 27 2560 1237])
%t.InnerPosition = [100 100 540 400];

%t.Units = 'inches';
%t.OuterPosition = [0.25 0.25 3 3];

for h=1:2
    
    if h==1
        hemisphere = 'lh';
        atlas_annot = load(atlas_annot_filename_lh);
        surface.vertices = lh_inflated_verts;
        surface.faces = lh_faces;
        data_tmp = data(1:Nrois/2); % cortical data only
    elseif h==2
        hemisphere = 'rh';
        atlas_annot = load(atlas_annot_filename_rh);
        surface.vertices = rh_inflated_verts;
        surface.faces = rh_faces;
        data_tmp = data((Nrois/2+1):500); % cortical data only
    end
    
    data_tmp(data_tmp==0) = NaN;
    
    for v=1:2
        nexttile([1 1])       
        % This just plots the ROI ID number for each ROI
        
        [fig] = plotSurfaceROIBoundary(surface,atlas_annot,data_tmp,'midpoint',colors,1,.5,thr);
        
        % The following options set up the patch object to look pretty. This works
        % well for the left hemisphere (medial and lateral). Change the inputs to
        % 'view' to see the brain from different angles ([-90 0] for left and [90 0]
        % for right I find works well)
        
        camlight(80,-10);
        camlight(-80,-10);
        
        if strcmp(hemisphere,'lh') && (v==1)
            angle = 'lateral';
            view([-90 0])
        elseif strcmp(hemisphere,'lh') && (v==2)
            angle = 'medial';
            view([90 0])
        elseif strcmp(hemisphere,'rh') && (v==1)
            angle = 'lateral';
            view([90 0])
        elseif strcmp(hemisphere,'rh') && (v==2)
            angle = 'medial';
            view([-90 0])
        end
        
        %view([90 0]) % -90 lateral, 90 medial
        %view([-90 0]) % -90 lateral, 90 medial (inside)
        
        axis off
        axis tight
        axis equal
    end
end
    outfile = [outfile_string,'.png'];
    %t.Units = 'inches';
    %saveas(t,outfile)
    %shg    
    exportgraphics(t,outfile,'Resolution','1000')

    %clf('reset')
    %clear fig
end
