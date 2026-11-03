import tkinter as tk

class Match:
    def __init__(self, date, homeTeam, awayTeam, homeScore, awayScore, stadium, distance, result, rating):
        self.date = date
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.homeScore = homeScore
        self.awayScore = awayScore
        self.stadium = stadium
        self.distance = distance
        self.result = result
        self.rating = rating

#--------------------------------------------------------------------------------------

dateVar = tk.StringVar()
homeTVar = tk.StringVar()
awayTVar = tk.StringVar()
homeSVar = tk.IntVar()
awaySVar = tk.IntVar()
stadVar = tk.StringVar()
mileVar = tk.FloatVar()
resultVar = tk.StringVar()
ratingVar = tk.FloatVar()

#--------------------------------------------------------------------------------------

class Application(tk.Frame):
  
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack()
    self.Welcome()

#--------------------------------------------------------------------------------------

  def Welcome(self):
    
    for widget in self.winfo_children():
      widget.destroy()
    
    self.lblWelcome = tk.Label(self, text="WELCOME TO THE FOOTBALL MATCH TRACKER APP!")
    self.lblWelcome.pack()

    self.btnBegin = tk.Button(self, text="Begin", command=self.Main_menu)
    self.btnBegin.pack()

    self.EXIT = tk.Button(self, text="EXIT", fg="blue", command=root.destroy)
    self.EXIT.pack(side="bottom")

#--------------------------------------------------------------------------------------
  
  def Main_menu(self):

    for widget in self.winfo_children():
      widget.destroy()
    
    self.lblMenu = tk.Label(self, text="Please select an option:")
    self.lblMenu.pack()

    self.btnAdd = tk.Button(self, text="Add Match", command=self.Add_match)
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

#--------------------------------------------------------------------------------------

  def Add_match(self):
  
    for widget in self.winfo_children():
      widget.destroy()

    self.lblAdd = tk.Label(self, text="Add a new match!")
    self.lblAdd.pack()
      
    self.lblDate = tk.Label(self, text="Please enter the date in the form dd/mm/yyyy:")
    self.lblDate.pack()

    self.lblHomeT = tk.Label(self, text="Please enter the home team:")
    self.lblHomeT.pack()

    self.lblAwayT = tk.Label(self, text="Please enter the away team:")
    self.lblAwayT.pack()

    self.lblHomeS = tk.Label(self, text="Please enter the home score:")
    self.lblHomeS.pack()

    self.lblAwayS = tk.Label(self, text="Please enter the away score:")
    self.lblAwayS.pack()

    self.lblStad = tk.Label(self, text="Please enter the stadium visited:")
    self.lblStad.pack()

    self.lblDist = tk.Label(self, text="Please enter the distance travelled to the stadium in miles:")
    self.lblDist.pack()

    self.lblResult = tk.Label(self, text="Did your team win, lose or draw:")
    self.lblResult.pack()

    self.lblRating = tk.Label(self, text="Please rate your team's performance from 1 to 10:")
    self.lblRating.pack()

    self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.Welcome)
    self.btnReturn.pack(side="bottom")
    

   
    





#--------------------------------------------------------------------------------------
root = tk.Tk()
root.title('Football Match Tracker')
root.geometry("400x300")

app = Application(master=root)
app.mainloop()
