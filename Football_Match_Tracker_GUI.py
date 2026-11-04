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

class Application(tk.Frame):
  
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.welcome()

#--------------------------------------------------------------------------------------
def text_area(self):
    self.scrollbar = tk.Scrollbar(self)
    self.output_text = tk.Text(self, width = 50, height = 20, yscrollcommand=self.scrollbar.set)

    self.scrollbar.config(command=self.output_text.yview)
    self.scrollbar.pack(side="right", fill="y")
    self.output_text.pack(fill="both",expand=True)
    
#--------------------------------------------------------------------------------------

def welcome(self):

    for widget in self.winfo_children():
      widget.destroy()
    
    self.lblWelcome = tk.Label(self, text="WELCOME TO THE FOOTBALL MATCH TRACKER APP!")
    self.lblWelcome.pack()

    self.btnBegin = tk.Button(self, text="Begin", command=self.main_menu)
    self.btnBegin.pack()

    self.EXIT = tk.Button(self, text="EXIT", fg="blue", command=root.destroy)
    self.EXIT.pack(side="bottom")

#--------------------------------------------------------------------------------------

def main_menu(self):

    for widget in self.winfo_children():
      widget.destroy()
    
    self.lblMenu = tk.Label(self, text="Please select an option:")
    self.lblMenu.pack()

    self.btnAdd = tk.Button(self, text="Add Match", command=self.add_match)
    self.btnAdd.pack()

    self.btnView = tk.Button(self, text="View Matches", command=self.view_match)
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


    self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.welcome)
    self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------

def add_match(self):

    for widget in self.winfo_children():
      widget.destroy()

    self.lblAdd = tk.Label(self, text="Add a new match!")
    self.lblAdd.pack()
      
    self.lblDate = tk.Label(self, text="Please enter the date in the form dd/mm/yyyy:")
    self.lblDate.pack()
    self.enterDate = tk.Entry(self)
    self.enterDate.pack()
    

    self.lblHomeT = tk.Label(self, text="Please enter the home team:")
    self.lblHomeT.pack()
    self.enterHomeT = tk.Entry(self)
    self.enterHomeT.pack()

    self.lblAwayT = tk.Label(self, text="Please enter the away team:")
    self.lblAwayT.pack()
    self.enterAwayT = tk.Entry(self)
    self.enterAwayT.pack()

    self.lblHomeS = tk.Label(self, text="Please enter the home score:")
    self.lblHomeS.pack()
    self.enterHomeS = tk.Entry(self)
    self.enterHomeS.pack()

    self.lblAwayS = tk.Label(self, text="Please enter the away score:")
    self.lblAwayS.pack()
    self.enterAwayS = tk.Entry(self)
    self.enterAwayS.pack()

    self.lblStad = tk.Label(self, text="Please enter the stadium visited:")
    self.lblStad.pack()
    self.enterStad = tk.Entry(self)
    self.enterStad.pack()

    self.lblDist = tk.Label(self, text="Please enter the distance travelled to the stadium in miles:")
    self.lblDist.pack()
    self.enterDist = tk.Entry(self)
    self.enterDist.pack()
      
    self.lblResult = tk.Label(self, text="Did your team win, lose or draw:")
    self.lblResult.pack()
    self.enterResult = tk.Entry(self)
    self.enterResult.pack()
      
    self.lblRating = tk.Label(self, text="Please rate your team's performance from 1 to 10:")
    self.lblRating.pack()
    self.enterRating = tk.Entry(self)
    self.enterRating.pack()

    self.btnSave = tk.Button(self, text="Save Match", command=self.save_match)
    self.btnSave.pack()
      
    self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.main_menu)
    self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------

def save_match(self):
    date = self.enterDate.get()
    homeT = self.enterHomeT.get()
    awayT = self.enterAwayT.get()
    homeS = self.enterHomeS.get()
    awayS = self.enterAwayS.get()
    stadium = self.enterStad.get()
    distance = self.enterDist.get()
    result = self.enterResult.get().lower()
    rating = self.enterRating.get()

    match = Match(date,homeT,awayT,homeS,awayS,stadium,distance,result,rating)
    
    with open("matches_Tracker_GUI.txt", "a") as f:
        f.write(
            f"{match.date}|{match.homeTeam}|{match.awayTeam}|"
            f"{match.homeScore}|{match.awayScore}|"
            f"{match.stadium}|{match.distance}|"
            f"{match.result}|{match.rating}\n"
        )

    self.lblSaved = tk.Label(self, text="Match saved successfully!")
    self.lblSaved.pack()        

#--------------------------------------------------------------------------------------

def display_match(self,match):
    data = match.strip().split("|")

    output = (f"Date: {data[0]}\n" 
    f"Match: {data[1]} {data[3]}-{data[4]} {data[2]}\n"
    f"Travel: {data[6]} miles to {data[5]} stadium\n"
    f"Team Rating: {data[8]}\n"
    f"\n----------------------------------------\n")

    self.output_text.insert("end",output)

#--------------------------------------------------------------------------------------
def simple_display(self, match):

    data = match.strip().split("|")

    output = (f"Match: {data[0]}: {data[1]} {data[3]}-{data[4]} {data[2]}\n"
    f"\n----------------------------------------\n")

    self.output_text.insert("end",output)

#--------------------------------------------------------------------------------------

def view_match(self):
    
    for widget in self.winfo_children():
        widget.destroy()

    self.text_area()

    with open("matches_Tracker_GUI.txt", "r") as f:
        matches = f.readlines()

    for match in matches:
        self.display_match(match)
        #self.simple_display(match)

    self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.main_menu)
    self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------

root = tk.Tk()
root.title('Football Match Tracker')
root.geometry("350x475")

app = Application(master=root)
app.mainloop()
