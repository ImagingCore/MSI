import os
import pandas as pd

# INPUTS
inputfile = '/Users/lindanieman/Documents/WORK/PythonScripts/Data/CellDivision/60x_miniscan_revised.HP.LTNtest.object_table.txt'
GUI_phenotypeLabel = 'Good'

## this script removes unwanted phenotypes from large a CellReview object table
## INPUT:  CellReview HP object table, phenotype of interest
## OUTPUT:  CSV file that contains only phenotypes of interest

# pass input file path and phenotype label from GUI
def getSelectData(inputfile, GUI_phentotypeLabel):
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

getSelectData(inputfile,'EVENTS')


# NEW STUFF
# # #
# TEST TEST TEST
#