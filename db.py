import psycopg2
import passwordEncrypt

class DB():
    def __init__(self):
        # Create your own database and add config here
        self.con = psycopg2.connect(
            host = "localhost",
            database = "PasswordManagerDB",
            user = "postgres",
            password = "******"
            )
        self.cur = self.con.cursor()

        self.key = None
        self.username = None


    def insertUser(self, username, password):
        try:
            hashPassword, salt, key = passwordEncrypt.hashPassword(password)
            salt = salt.decode('utf-8')
            # Store salt in db as well
            self.cur.execute(f"insert into users (username, hashedpassword, salt) values ('{username}', '{hashPassword}', '{salt}')")
            self.con.commit()
            self.key = key
            self.username = username
            return True
        except:
            return False
        
    def deleteWebsite(self, website):
        # try:
        #     #self.cur.execute(f"insert into users (username, hashedpassword, salt) values ('{username}', '{hashPassword}', '{salt}')")
        #     self.cur.execute(f"delete from websites where website = '{website}")
        #     self.con.commit()
        #     return True
        # except:
        #     return False
        
        self.cur.execute(f"delete from websites where website = '{website}'")
        self.con.commit()
        return True

        
    # check that password given is correct of user
    def checkPassword(self, username, password):
        self.cur.execute(f"select * from users where username = '{username}'")
        user = self.cur.fetchall()
        if user:
            hashedPassword = user[0][1]
            salt = user[0][2].encode('utf-8')
            isAuthenticated, key = passwordEncrypt.checkPassword(password, hashedPassword, salt)
            self.key = key
            self.username = username
            return isAuthenticated
        return False
    
    def storePassword(self, website, password):
        try:
            encryptedPassword = passwordEncrypt.encryptPassword(password, self.key)
            self.cur.execute(f"insert into websites (website, encryptedpassword, usersusername) values ('{website}', '{encryptedPassword}', (SELECT username from users WHERE username='{self.username}'))")
            self.con.commit()
            return True
        except:
            return False

    # Get all the websites and their passwords of a user
    def getAllPasswords(self, username):
        webList = []
        try:
            self.cur.execute(f"select * from websites where usersusername = '{username}'")
            websites = self.cur.fetchall()
            for website in websites:
                websiteName = website[0]
                encryptedPassword = website[2]
                password = passwordEncrypt.decryptPassword(encryptedPassword, self.key)
                webList.append((websiteName, password))
            return webList
        except:
            return webList
