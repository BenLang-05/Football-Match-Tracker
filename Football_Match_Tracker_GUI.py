import tkinter as tk

class Application(tk.Frame):
  
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack()
    self.Welcome()


  def Welcome(self):
    self.lblWelcome = tk.Label(self, text="WELCOME TO THE FOOTBALL MATCH TRACKER APP!")
    self.lblWelcome.pack()

    self.btnBegin = tk.Button(self, text="Begin", command=self.Main_menu)
    self.btnBegin.pack()

    
  
  def Main_menu(self):
    self.lblWelcome.destroy()
    self.btnBegin.destroy()
    
    self.lblMenu = tk.Label(self, text="Please select an option:")
    self.lblMenu.pack()

    self.btnAdd = tk.Button(self, text="Add Match")
    self.btnAdd.pack()

    self.btnView = tk.Button(self, text="View Matches")
    self.btnView.pack()

    self.btnSort = tk.Button(self, text="Sort Matches")
    self.btnSort.pack()

    self.btnSearch = tk.Button(self, text="Search Matches")
    self.btnSearch.pack()

    self.btnStats = tk.Button(self, text="View Statistics")
    self.btnStats.pack()

    self.btnEdit = tk.Button(self, text="Edit Match")
    self.btnEdit.pack()

    self.btnDel = tk.Button(self, text="Delete Match")
    self.btnDel.pack()


    self.QUIT = tk.Button(self, text="QUIT", fg="blue", command=root.destroy)
    self.QUIT.pack(side="bottom")

    
root = tk.Tk()
app.master.title('Football Match Tracker')
root.geometry("800x600")

app = Application(master=root)
app.mainloop()
