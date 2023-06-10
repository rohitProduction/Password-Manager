import tkinter as tk
from db import DB

"""
Potential TODO'S:
Error pop up page
disconnect db when you sign out
when you sign up, check for tables. If none then create tables.
"""

class GUI():
    def __init__(self):
        self.db = DB()
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.title("Password Manager")
        # Starting page:
        self.logInPage()
        
        self.root.mainloop()
        

    def logInPage(self):
        self.logInFrame = tk.Frame(self.root)
        self.homepageTitle = tk.Label(self.logInFrame, text="Password Manager", font= ('',20))
        self.homepageTitle.pack(pady = 20)

        self.logInTitle = tk.Label(self.logInFrame, text="Log In", font= ('',15))
        self.logInTitle.pack(pady = (0, 20))

        self.usernameText = tk.Label(self.logInFrame, text="Username: ")
        self.usernameText.pack() 

        self.usernameEntry = tk.Entry(self.logInFrame)
        self.usernameEntry.pack(pady = (0, 20))

        self.passwordText = tk.Label(self.logInFrame, text="Password: ")
        self.passwordText.pack() 

        self.passwordEntry = tk.Entry(self.logInFrame, show="*")
        self.passwordEntry.pack(pady = (0, 30))

        self.logInButton = tk.Button(self.logInFrame, text="Log In", command= self.logIn)
        self.logInButton.pack(pady = (0, 20))

        self.signUpText = tk.Label(self.logInFrame, text="Don't have an account? Sign up now: ")
        self.signUpText.pack() 

        self.goSignUpButton = tk.Button(self.logInFrame, text="Sign Up", command= self.goSignUp)
        self.goSignUpButton.pack()

        self.logInFrame.pack()

    def signUpPage(self):
        self.signUpFrame = tk.Frame(self.root)
        self.homepageTitle = tk.Label(self.signUpFrame, text="Password Manager", font= ('',20))
        self.homepageTitle.pack(pady = 20)

        self.logInTitle = tk.Label(self.signUpFrame, text="Sign Up", font= ('',15))
        self.logInTitle.pack(pady = (0, 20))

        self.usernameText = tk.Label(self.signUpFrame, text="Username: ")
        self.usernameText.pack() 

        self.usernameEntry = tk.Entry(self.signUpFrame)
        self.usernameEntry.pack(pady = (0, 20))

        self.passwordText = tk.Label(self.signUpFrame, text="Password: ")
        self.passwordText.pack() 

        self.passwordEntry = tk.Entry(self.signUpFrame, show="*")
        self.passwordEntry.pack(pady = (0, 30))

        self.signUpButton = tk.Button(self.signUpFrame, text="Sign Up", command= self.signUp)
        self.signUpButton.pack(pady = (0, 20))

        self.logInText = tk.Label(self.signUpFrame, text="Already have an account? Log in now: ")
        self.logInText.pack() 

        self.goLogInButton = tk.Button(self.signUpFrame, text="Log in", command= self.goLogIn)
        self.goLogInButton.pack()

        self.signUpFrame.pack()

    # Page for list of websites and their passwords.
    def websiteListPage(self, websites):
        self.websiteListFrame = tk.Frame(self.root)
        self.webTitle = tk.Label(self.websiteListFrame, text="List Of Websites And Their Passwords", font= ('',12))
        self.webTitle.grid(row = 0, column = 1, pady = 2)

        self.signOutButton = tk.Button(self.websiteListFrame, text="Sign Out", command= self.signOut)
        self.signOutButton.grid(row = 2, column = 1, pady = 2)

        self.newEntryText = tk.Label(self.websiteListFrame, text="Add a new entry to the password manager: ")
        self.newEntryText.grid(row = 3, column = 1, pady = 2)

        self.newEntryTextButton = tk.Button(self.websiteListFrame, text="New entry", command= self.goNewEntry)
        self.newEntryTextButton.grid(row = 4, column = 1, pady = 2)

        self.websiteHeader = tk.Label(self.websiteListFrame, text="Websites: ", font= ('',12))
        self.websiteHeader.grid(row = 5, column = 0, pady = 2)

        self.passwordHeader = tk.Label(self.websiteListFrame, text="Passwords: ", font= ('',12))
        self.passwordHeader.grid(row = 5, column = 1, pady = 2)

        for x, website in enumerate(websites):
            self.webLabel = tk.Label(self.websiteListFrame, text=website[0])
            self.webLabel.grid(row = 6 + x, column = 0, pady = 2)
            self.passLabel = tk.Label(self.websiteListFrame, text=website[1])
            self.passLabel.grid(row = 6 + x, column = 1, pady = 2)
            # self.deleteButton = tk.Button(self.websiteListFrame, text="Delete", command= self.deleteEntry)
            self.deleteButton = tk.Button(self.websiteListFrame, text="Delete", command=lambda site=website[0]: self.deleteEntry(site))
            self.deleteButton.grid(row = 6 + x, column = 2, pady = 2)

        self.websiteListFrame.pack()

    # Page to add a new website and password entry to database
    def newEntryPage(self):
        self.newEntryFrame = tk.Frame(self.root)
        self.newEntryTitle = tk.Label(self.newEntryFrame, text="New Entry", font= ('',20))
        self.newEntryTitle.pack(pady = 20)

        self.websiteText = tk.Label(self.newEntryFrame, text="Website: ")
        self.websiteText.pack() 

        self.websiteEntry = tk.Entry(self.newEntryFrame)
        self.websiteEntry.pack(pady = (0, 20))

        self.websitePasswordText = tk.Label(self.newEntryFrame, text="Password: ")
        self.websitePasswordText.pack() 

        self.websitePasswordEntry = tk.Entry(self.newEntryFrame, show="*")
        self.websitePasswordEntry.pack(pady = (0, 30))

        self.newEntryButton = tk.Button(self.newEntryFrame, text="Add New Entry", command= self.checkEntry)
        self.newEntryButton.pack(pady = (0, 20))

        self.cancelButton = tk.Button(self.newEntryFrame, text="Go Back", command= self.cancelEntry)
        self.cancelButton.pack(pady = (0, 20))

        self.newEntryFrame.pack()


    def logIn(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if self.db.checkPassword(username, password):
            self.logInFrame.destroy()
            websites = self.getAllWebsite(username)
            self.websiteListPage(websites)


    def goSignUp(self):
        self.logInFrame.destroy()
        self.signUpPage()

    def signUp(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if (username and password) and self.db.insertUser(username, password):
            self.signUpFrame.destroy()
            websites = self.getAllWebsite(username)
            self.websiteListPage(websites)

    def goLogIn(self):
        self.signUpFrame.destroy()
        self.logInPage()

    def signOut(self):
        self.db.key = None
        self.db.username = None
        self.websiteListFrame.destroy()
        self.logInPage()

    def goNewEntry(self):
        self.websiteListFrame.destroy()
        self.newEntryPage() 
    
    def deleteEntry(self, website):
        if self.db.deleteWebsite(website):
            self.websiteListFrame.destroy()
            websites = self.getAllWebsite(self.db.username)
            self.websiteListPage(websites)

    def checkEntry(self):
        website = self.websiteEntry.get()
        password = self.websitePasswordEntry.get()
        if (website and password) and self.db.storePassword(website, password):
            self.newEntryFrame.destroy()
            websites = self.getAllWebsite(self.db.username)
            self.websiteListPage(websites)

    def cancelEntry(self):
        self.newEntryFrame.destroy()
        websites = self.getAllWebsite(self.db.username)
        self.websiteListPage(websites)


    def getAllWebsite(self, username):
        return self.db.getAllPasswords(username)


if __name__ == "__main__":
    gui = GUI()