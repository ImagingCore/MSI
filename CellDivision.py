import os
import pandas as pd

# INPUTS
inputfile = '/Users/konstk/Desktop/MSI_testfile.txt'
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
    df.to_csv(outputfile)

getSelectCellReviewData(inputfile,GUI_phenotypeLabel)


# --------------------------
## This script pulls inForm cell_seg_data.txt for selected phenotypes
## INPUT:  outputfile from getSelectData
## OUTPUT:  CSV file with morphological information for phenotypes of interest

#def getSelectCellSegData
#




