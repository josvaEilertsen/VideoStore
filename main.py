import sqlite3

#Global Varibles
user_cred = {} 

#main method
def main():
    print("Program running...")

    #Call to get credidentails
    load_usrs()

def load_usrs():
    print("Loading users....")

    #SQLite connection & read in
    conn = sqlite3.connect("video_store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT usrname, passw FROM tblUsers")
    rows = cursor.fetchall()

    global user_cred
    user_cred = dict(rows)

    #print(user_dict) 
    conn.close()

    #Run the login method
    usr_login()

#Start usr login
def usr_login():
    print("Running login...")

    #Bring in the dictionary
    global user_cred

    checker = 0 #Will be set to 1 if login successful to break loop
    
    while(checker != 1):
        usrName = input("Enter your username and press enter ")
        usrPass = input("Enter you password and press enter ")

        #Check user input against dictionary
        if user_cred.get(usrName) == usrPass:
            print("Success, Thank you")
            checker = 1
        else:
            print("Invalid Credentails")
            #checker remains 0


#Main method runner
if __name__ == "__main__":
    main()

