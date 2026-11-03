import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

  def createWidgets(self):
    self.btn = tk.Button(self)
    self.btn["text"] = "WELCOME TO THE FOOTBALL MATCH TRACKER APP\n(click here)"
    self.btn["command"] = self.welcome
    self.btn.pack(side="top")
    self.QUIT = tk.Button(self, text="QUIT", fg="blue", command=root.destroy)
    self.QUIT.pack(side="bottom")

  def welcome(self):
    print("Please select one of the following options:")

root = tk.Tk()
app = Application(master=root)
#app.master.title('Football Match Tracker')
app.mainloop()
