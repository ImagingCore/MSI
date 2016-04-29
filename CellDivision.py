import os
import pandas as pd
import re

# INPUTS
#inputfile = '/Volumes/ctc2-raw4-1/MSI_149/Vectra1/Images/CellDivision/60x_miniscan_revised/60x_miniscan_revised.HP-scored.object_table copy.txt'
#GUI_phenotypeLabel = 'EVENTS'

# ------------------------
## This script removes unwanted phenotypes from large a CellReview object table
## INPUT:  CellReview HP object table, phenotype of interest
## OUTPUT:  CSV file that contains only phenotypes of interest

# pass input file path and phenotype label from GUI
def getSelectCellReviewData(inputfile, GUI_phenotypeLabel):
    # load object table as a data frame
    df = pd.read_csv(inputfile, delimiter='\t')

    # parse fullfilepath
    path, filename = os.path.split(inputfile)
    root, ext = os.path.splitext(filename)

    # create output filename with same root and path as input file, adding the suffix _GOOD
    outputfile = path + '/' + root + '_' + GUI_phenotypeLabel + '.csv'

    # sort Phenotype column (contains hand validated classes)
    df.sort_values(by='Phenotype (Reviewer)', axis=0, inplace=True)
    #print df.ix[:, ['LP ID', 'Phenotype (Reviewer)']].head(5)

    # keep rows that do not have desired phenotype
    df = df[df.ix[:,'Phenotype (Reviewer)'] == GUI_phenotypeLabel]

    # write output to file
    df.to_csv(outputfile, index=False)

#getSelectCellReviewData(inputfile,GUI_phenotypeLabel)

# --------------------------

## This script pulls inForm cell_seg_data.txt for selected phenotypes
## INPUT:  outputfile from getSelectData
## OUTPUT:  CSV file with morphological information for phenotype of interest

# pass input file path and IPP folder location

def getSelectCellSegData(inputfile, GUI_phenotypeLabel):

    # parse input fullfilepath
    path, filename = os.path.split(inputfile)
    root, ext = os.path.splitext(filename)

    # Object table with the selected phenotypes
    objectTable = os.path.join(path, root + '_' + GUI_phenotypeLabel + '.csv')

    # load object table as a data frame
    df = pd.read_csv(objectTable, delimiter=',')

    # note:  cell_seg_data files are in IPP folder
    IPP_path = os.path.join(path, 'IPP')

    # initialize data frame that will contain data for phenotype of interest
    data = pd.DataFrame() # don't know size of final dataframe, b/c can have multiple objects in a single FOV
    f = pd.DataFrame()

    # populate dataframe that contains data for phenotype of interest
    # find unique FOV / image name (NOTE:  there can be multiple objects in a single FOV)
    imageName = df.ix[:,'Sample Name'].unique()

    for i in range(len(imageName)):

        f = imageName[i]
        rootname = re.split(']', f)[0]
        fname = os.path.join(IPP_path, rootname + ']_cell_seg_data.txt')

        dat = pd.read_csv(fname, delimiter='\t')

        data = pd.concat([data,dat], ignore_index=True)

    # create cell_seg output filename with same path as input file, adding the suffix _GOOD
    outputfile = os.path.join(path, 'cell_seg_data_GOOD.csv')

    # write output to csv file
    data.to_csv(outputfile, delimiter=',', index=False)

    statusOut = ' Done! '
    statusColor = 'darkgreen'
    return statusOut, statusColor

#getSelectCellSegData(inputfile)
