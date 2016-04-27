from Tkinter import *
import tkFileDialog
import inspect


class MainGuiClass(Frame):


    # all labels
    FILE = 'Select the file'
    EXIT_PROGRAM = 'Exit'
    PROCESS = 'Process!'
    PHENOTYPE = 'Phenotypes:'

    def phenotypes(self):
        self.ls.insert(1, 'Red')
        self.ls.insert(2, 'Green')
        self.ls.insert(3, 'Blue')

    # Operations
    def pickTheFile(self):
        self.phenotypes()

    def processIt(self):
        print 'process it!'


    # Main window widgets and layout
    def createWidgets(self,masterIn):

        # Version label (top left)
        self.ver_label_str = "v " + VERSION_NUMBER + ", last updated on " + VERSION_DATE
        self.ver_label = Label(masterIn, text=self.ver_label_str, font=("Arial", 10, "italic"), fg='gray')

        # Labels
        self.phen_label = Label(masterIn, text=self.PHENOTYPE, font=("Arial", 14), fg='black')

        # Buttons
        self.button1 = Button(masterIn, text=self.FILE, font=("Arial", 16), command=self.pickTheFile)
        self.button2 = Button(masterIn, text=self.PROCESS, font=("Arial", 16), command=self.processIt)
        self.button3 = Button(masterIn, text=self.EXIT_PROGRAM, font=("Arial", 16), command=self.quit)

        # Listbox
        self.ls = Listbox(masterIn)

        # Place all object in the window
        self.ver_label.grid(row=0, column=0, sticky=W)
        self.phen_label.grid(row=1, column=1, sticky=S)
        self.button1.grid(row=2, column=0, sticky=NW)
        self.ls.grid(row=2, column=1, sticky=E)
        self.button2.grid(row=3, column=0, sticky=W)
        self.button3.grid(row=3, column=1, sticky=E)

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
    VERSION_NUMBER = "0.0.1"

    # start main GUI window.
    # Instantiate a MainGuiClass object.
    # Developer: select GUI version (1 or 2)
    root = Tk()
    root.title("MSI Tools")
    mainWindow = MainGuiClass(master=root)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()
