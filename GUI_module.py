from Tkinter import *
import tkFileDialog
import pandas as pd
import CellDivision


class MainGuiClass(Frame):

    # all labels
    FILE = 'Object table file'
    EXIT_PROGRAM = ' Exit'
    PROCESS = 'Process!'
    PHENOTYPE = 'Phenotypes:'
    CLEAR = 'Clear'

    def updateListBox(self, phenotypesIn):
        self.ls.delete(0, END)  # clear list
        for item in phenotypesIn:
            self.ls.insert(END, item)
        self.ls.selection_set(first=0)

    # Operations
    def pickTheFile(self):
        # open the file selection window, read the the file into a dataframe,
        # pull out the column, drop NaN values and get the unique names of the
        # phenotypes
        self.filename = tkFileDialog.askopenfilename(filetypes=[("TXT", "*.txt")])
        if self.filename != '':
            df = pd.read_csv(self.filename, delimiter='\t')
            phenotypes = df['Phenotype (Reviewer)'].dropna().unique()
            self.updateListBox(phenotypes)

    def processIt(self):
        if self.filename != None and self.filename != '':
            selection = self.ls.get(ACTIVE)
            CellDivision.getSelectCellReviewData(self.filename, selection)
            CellDivision.getSelectCellSegData(self.filename, selection)
        else:
            print 'load the file first!'

    def clearIt(self):
        self.ls.delete(0, END)  # clear list
        self.filename = ''

    # Main window widgets and layout
    def createWidgets(self,masterIn):

        # Version label (top left)
        self.ver_label_str = "  v " + VERSION_NUMBER + ", last updated on " + VERSION_DATE
        self.ver_label = Label(masterIn, text=self.ver_label_str, font=("Arial", 10, "italic"), fg='gray')

        # Labels
        self.phen_label = Label(masterIn, text=self.PHENOTYPE, font=("Arial", 14), fg='black')

        # Buttons
        self.button1 = Button(masterIn, text=self.FILE, font=("Arial", 16), command=self.pickTheFile)
        self.button2 = Button(masterIn, text=self.PROCESS, font=("Arial", 16), command=self.processIt)
        self.button3 = Button(masterIn, text=self.EXIT_PROGRAM, font=("Arial", 16), command=self.quit)
        self.button4 = Button(masterIn, text=self.CLEAR, font=("Arial", 16), command=self.clearIt)

        # Listbox
        self.ls = Listbox(masterIn)

        # Place all object in the window
        self.ver_label.grid(row=0, column=0, sticky=W)
        self.phen_label.grid(row=1, column=1, sticky=S)
        self.button1.grid(row=2, column=0, sticky=NW)
        self.ls.grid(row=2, column=1, sticky=E)
        self.button2.grid(row=3, column=0, sticky=W)
        self.button3.grid(row=3, column=1, sticky=E)
        self.button4.grid(row=3, column=1, sticky=S)

    # Class initialization
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.filename = None
        self.grid()
        self.createWidgets(master)


def main():

    # Developer: remember to update these!
    global VERSION_DATE
    global VERSION_NUMBER
    VERSION_DATE = "4/27/16"
    VERSION_NUMBER = "0.0.2"

    # start main GUI window.
    # Instantiate a MainGuiClass object.
    # Developer: select GUI version (1 or 2)
    root = Tk()
    root.title("MSI Tools")
    mainWindow = MainGuiClass(master=root)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()
