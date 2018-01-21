import tkinter as tk
from word_functions import wordfunctions

class App:

    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.wordLabel = tk.Label(frame, text='Enter a word or words.')
        self.wordLabel.pack(side='left')
        self.txtEntry = tk.Entry(frame)
        self.txtEntry.pack(side='left')
        self.okButton = tk.Button(frame, text='Go', command=self.goButton)
        self.okButton.pack(side='left')
        self.clearButton = tk.Button(frame, text='Clear', command=self.clearText)
        self.clearButton.pack(side='left')
    def clearText(self):
        print('clear text clicked')

    def goButton(self):
        print('go button clicked')
# root = tk.Tk()
# root.minsize(width=640, height=480)
# app = App(root)
#
# root.mainloop()
# #root.destroy() # optional; see description below