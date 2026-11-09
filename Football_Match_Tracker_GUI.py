import tkinter as tk
from matchLib import *
from datetime import datetime

#--------------------------------------------------------------------------------------

class Application(tk.Frame):
  
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.welcome()

#--------------------------------------------------------------------------------------

    def welcome(self):
    
        for widget in self.winfo_children():
          widget.destroy()
        
        self.lblWelcome = tk.Label(self, text="WELCOME TO THE FOOTBALL MATCH TRACKER APP!")
        self.lblWelcome.pack()

        self.lblTeam = tk.Label(self, text="Please Enter Your Favourite Team: \n(The team you wish to input details for...)")
        self.lblTeam.pack()

        self.enterTeam = tk.Entry(self)
        self.enterTeam.pack()
      
        self.btnBegin = tk.Button(self, text="Begin", command=self.start_app)
        self.btnBegin.pack()
    
        self.EXIT = tk.Button(self, text="EXIT", fg="blue", command=root.destroy)
        self.EXIT.pack(side="bottom")

#--------------------------------------------------------------------------------------

    def start_app(self):
        self.fav_team = self.enterTeam.get()
        if not self.fav_team:
          return
        self.main_menu()
#--------------------------------------------------------------------------------------

    def text_area(self):
        self.scrollbar = tk.Scrollbar(self)
        self.output_text = tk.Text(self, width = 60, height = 30, yscrollcommand=self.scrollbar.set)
    
        self.scrollbar.config(command=self.output_text.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.output_text.pack(fill="both",expand=True)
        
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
    
        self.btnSort = tk.Button(self, text="Sort Matches", command=self.sort_menu)
        self.btnSort.pack()
    
        self.btnSearch = tk.Button(self, text="Search Matches")
        self.btnSearch.pack()
    
        self.btnStats = tk.Button(self, text="View Statistics", command=self.stats_menu)
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
        homeS = int(self.enterHomeS.get())
        awayS = int(self.enterAwayS.get())
        stadium = self.enterStad.get()
        distance = float(self.enterDist.get())
        result = self.enterResult.get().lower()
        rating = float(self.enterRating.get())
    
        match = Match(date,homeT,awayT,homeS,awayS,stadium,distance,result,rating)
        
        with open("matches_Tracker.txt", "a") as f:
            f.write(
                f"{match.date}|{match.homeTeam}|{match.awayTeam}|"
                f"{match.homeScore}|{match.awayScore}|"
                f"{match.stadium}|{match.distance}|"
                f"{match.result}|{match.rating}\n"
            )
    
        self.lblSaved = tk.Label(self, text="Match saved successfully!")
        self.lblSaved.pack()        
    
#--------------------------------------------------------------------------------------
    
    def view_match(self):
        
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()
    
        for match in matches:
            self.output_text.insert("end", display_match(match) + "\n")
    
        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.main_menu)
        self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------
    def sort_menu(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.lblSortMenu = tk.Label(self, text="Please select an option:\n\n Sort by:")
        self.lblSortMenu.pack()
    
        self.btnDateAsc = tk.Button(self, text="Date Ascending", command = lambda: self.show_sort_date(False))
        self.btnDateAsc.pack()
    
        self.btnDateDesc = tk.Button(self, text="Date Descending", command = lambda: self.show_sort_date(True))
        self.btnDateDesc.pack()
    
        self.btnRatingAsc = tk.Button(self, text="Rating Ascending", command = lambda: self.show_sort_rating(False))
        self.btnRatingAsc.pack()
    
        self.btnRatingDesc = tk.Button(self, text="Rating Descending", command = lambda: self.show_sort_rating(True))
        self.btnRatingDesc.pack()
    
        self.btnDistAsc = tk.Button(self, text="Distance Ascending", command = lambda: self.show_sort_distance(False))
        self.btnDistAsc.pack()
    
        self.btnDistDesc = tk.Button(self, text="Distance Descending", command = lambda: self.show_sort_distance(True))
        self.btnDistDesc.pack()

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.main_menu)
        self.btnReturn.pack(side="bottom")
#--------------------------------------------------------------------------------------
    def show_sort_date(self, reverse_order):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = sort_date(reverse_order)
        
        for match in matches:
            self.output_text.insert("end", simple_display(match) + "\n")
            
        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.sort_menu)
        self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------

    def show_sort_rating(self, reverse_order):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = sort_rating(reverse_order)
        
        for match in matches:
            self.output_text.insert("end", display_match(match) + "\n")
            
        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.sort_menu)
        self.btnReturn.pack(side="bottom")
      
#--------------------------------------------------------------------------------------
    
    def show_sort_distance(self, reverse_order):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = sort_distance(reverse_order)
        
        for match in matches:
            self.output_text.insert("end", display_match(match) + "\n")
            
        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.sort_menu)
        self.btnReturn.pack(side="bottom")
      
#--------------------------------------------------------------------------------------

    def stats_menu(self):
        for widget in self.winfo_children():
            widget.destroy()
        
        self.lblStatsMenu = tk.Label(self, text="Please select a statistics option to view:\n")
        self.lblStatsMenu.pack()
    
        self.btnHva = tk.Button(self, text="Home Vs Away Games", command = self.show_hva)
        self.btnHva.pack()
    
        self.btnWinPercent = tk.Button(self, text="Win Percentage", command = self.show_win_percent)
        self.btnWinPercent.pack()
    
        self.btnTotGoals = tk.Button(self, text="Total Goals", command = self.show_total_goals)
        self.btnTotGoals.pack()
    
        self.btnAvgRating = tk.Button(self, text="Average Rating", command = self.show_avg_rating)
        self.btnAvgRating.pack()
    
        self.btnStadVisited = tk.Button(self, text="Stadiums Visited", command = self.show_stad_visited)
        self.btnStadVisited.pack()
    
        self.btnTotMiles = tk.Button(self, text="Total Mileage", command = self.show_total_miles)
        self.btnTotMiles.pack()

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.main_menu)
        self.btnReturn.pack(side="bottom")
      
#--------------------------------------------------------------------------------------

    def show_hva(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()

        home_games, away_games = home_vs_away(matches, self.fav_team)

        self.output_text.insert("end", "Home Games: " + str(home_games) + "\n")
        self.output_text.insert("end", "Away Games: " + str(away_games) + "\n")

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.stats_menu)
        self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------
    
    def show_win_percent(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()

        percent, no_of_wins = win_percent(matches)

        self.output_text.insert("end", self.fav_team + " had a " + str(percent) + "% win rate\n")
        self.output_text.insert("end", "Winning " + str(no_of_wins) + " out of " + str(len(matches)) + " matches you visited\n")

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.stats_menu)
        self.btnReturn.pack(side="bottom")
     
#--------------------------------------------------------------------------------------

    def show_total_goals(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()

        tot_goals, tot_team_goals, average_goals = total_goals(matches, self.fav_team)

        self.output_text.insert("end", "You have seen " + str(tot_goals) + " goals in total across all games\n")
        self.output_text.insert("end", "With " + self.fav_team + " scoring " + str(tot_team_goals) + " of those goals\n")
        self.output_text.insert("end", "Averaging at " + str(average_goals) + "% of the total goals you've seen\n")

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.stats_menu)
        self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------

    def show_avg_rating(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()

        avg_rating = average_rating(matches)

        self.output_text.insert("end", "You gave " + self.fav_team + " an average rating of " + str(avg_rating) + "/10 across " + str(len(matches)) + " matches seen\n")

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.stats_menu)
        self.btnReturn.pack(side="bottom")

#--------------------------------------------------------------------------------------

    def show_stad_visited(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()

        stadiums = stadiums_visited(matches)
      
        self.output_text.insert("end", "You have visited the following stadiums:\n")
        for stadium, visits in stadiums:
            self.output_text.insert("end", stadium + ": " + str(visits) + " time(s)\n")

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.stats_menu)
        self.btnReturn.pack(side="bottom")
        
#--------------------------------------------------------------------------------------

    def show_total_miles(self):
        for widget in self.winfo_children():
            widget.destroy()
    
        self.text_area()
    
        matches = load_matches()

        total_miles, avg_miles = total_mileage(matches)
      
        self.output_text.insert("end", "You travelled " + str(total_miles) + " miles across " + str(len(matches)) + " matches\n")
        self.output_text.insert("end", "At an average of " + str(avg_miles) + " miles per game\n")

        self.btnReturn = tk.Button(self, text="Return", fg="blue", command=self.stats_menu)
        self.btnReturn.pack(side="bottom")
      
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------



root = tk.Tk()
root.title('Football Match Tracker')
root.geometry("475x600")

app = Application(master=root)
app.mainloop()
