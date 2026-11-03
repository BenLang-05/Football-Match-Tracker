import tkinter as tk

class Application(tk.Frame):
  
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack()
    self.Welcome()


  def Welcome(self):
    
    for widget in self.winfo_children():
      widget.destroy()
    
    self.lblWelcome = tk.Label(self, text="WELCOME TO THE FOOTBALL MATCH TRACKER APP!")
    self.lblWelcome.pack()

    self.btnBegin = tk.Button(self, text="Begin", command=self.Main_menu)
    self.btnBegin.pack()

    
  
  def Main_menu(self):

    for widget in self.winfo_children():
      widget.destroy()
    
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


    self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.Welcome)
    self.btnReturn.pack(side="bottom")

    
root = tk.Tk()
root.title('Football Match Tracker')
root.geometry("800x600")

app = Application(master=root)
app.mainloop()
