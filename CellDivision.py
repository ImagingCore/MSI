import os
import pandas as pd
import re

# INPUTS
inputfile = '/Volumes/ctc2-raw4/MSI_149/Vectra1/Images/CellDivision/60x_miniscan_revised/60x_miniscan_revised.HP.LTNtest.object_table.txt'
GUI_phenotypeLabel = 'Good'

# ------------------------
## This script removes unwanted phenotypes from large a CellReview object table
## INPUT:  CellReview HP object table, phenotype of interest
## OUTPUT:  CSV file that contains only phenotypes of interest

# pass input file path and phenotype label from GUI
def getSelectCellReviewData(inputfile, GUI_phentotypeLabel):
    # load object table as a data frame
    df = pd.read_csv(inputfile, delimiter='\t')

    # parse fullfilepath
    path, filename = os.path.split(inputfile)
    root, ext = os.path.splitext(filename)

    # create output filename with same root and path as input file, adding the suffix _GOOD
    outputfile = path + '/' + root + '_GOOD.csv'

    # sort Phenotype column (contains hand validated classes)
    df.sort_values(by='Phenotype (Reviewer)', axis=0, inplace=True)
    #print df.ix[:, ['LP ID', 'Phenotype (Reviewer)']].head(5)

    # keep rows that do not have desired phenotype
    df = df[df.ix[:,'Phenotype (Reviewer)']==GUI_phenotypeLabel]

    # write output to file
    df.to_csv(outputfile, index=False)

getSelectCellReviewData(inputfile,GUI_phenotypeLabel)


# --------------------------

## This script pulls inForm cell_seg_data.txt for selected phenotypes
## INPUT:  outputfile from getSelectData
## OUTPUT:  CSV file with morphological information for phenotypes of interest

# pass input file path and IPP folder location
def getSelectCellSegData(inputfile):

    # parse input fullfilepath
    path, filename = os.path.split(inputfile)
    root, ext = os.path.splitext(filename)

    # Object table with the selected phenotypes
    objectTable = os.path.join(path, root+'_GOOD.csv')

    # load object table as a data frame
    df = pd.read_csv(objectTable, delimiter=',')

    # create cell_seg output filename with same path as input file, adding the suffix _GOOD
    outputfile = os.path.join(path, 'cell_seg_data_GOOD.csv')

    IPP_path = os.path.join(path, 'IPP')

    data = pd.DataFrame() # don't know size of final dataframe, b/c can have multiple objects in a single FOV

    # create list of data
    for f in df.ix[:,'Sample Name']:

        rootname = re.split(']', f)[0]
        fname = os.path.join(IPP_path, rootname + ']_cell_seg_data.txt')

        dat = pd.read_csv(fname, delimiter='\t')


        data = pd.concat([data,dat], ignore_index=True)

    data.to_csv(outputfile, delimiter=',')
    print 'Done!'

getSelectCellSegData(inputfile)
