import sqlite3
import time
import os
from datetime import datetime #Fixes (module 'datetime' has no attribute 'now')

#Global Varibles
user_cred = {} 

#main method
def main():
    print("Program running...")
    time.sleep(1) #tends to give the user the feeling that its doing something 

    #Call to get credidentails
    #load_usrs()

    dashboard() #TEMP!!!!!

def load_usrs():
    print("Loading users....")
    time.sleep(1) #tends to give the user the feeling that its doing something 

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
    time.sleep(1) #tends to give the user the feeling that its doing something 

    #Bring in the dictionary
    global user_cred

    checker = 0 #Will be set to 1 if login successful to break loop
    
    while(checker != 1):
        os.system('cls') #Clears terminal
        usrName = input("Enter your username and press enter ")
        usrPass = input("Enter you password and press enter ")

        #Check user input against dictionary
        if user_cred.get(usrName) == usrPass:
            print("Success, Thank you")
            checker = 1
            os.system('cls') #Clears terminal
            dashboard() #Run the dashbaord
        else:
            print("Invalid Credentails")
            #checker remains 0

def dashboard():
    print("Dashboard Running...")
    time.sleep(1) #tends to give the user the feeling that its doing something 

    #Start drawing up the dash
    print("=====================================")
    print("VIDEO STORE DASHBOARD")
    print("=====================================")
    print("1. Add new client")
    print("2. Add new movie")
    print("3. Hire out movie")
    print("4. Return movie")
    print("=====================================")
    print("5. Log-Out")
    print("X Close")
    print("=====================================")
    usrChoice = input("Choice: ")

    if usrChoice == "1":
        add_client()

    elif usrChoice == "2":
        add_movie()

    elif usrChoice == "3":
        hire_movie()

    elif usrChoice == "4":
        return_movie()

    elif usrChoice == "5":
        print("Byeeeeee")
        time.sleep(1)
        main()

    elif usrChoice.upper() == "X": #.uppercase to ensure that "x" and "X" result in the program closing
        print("Byeeeeee")
        time.sleep(1)
        exit()

    else:
        print("Invalid input!")
        dashboard()
    
def add_client():
    os.system('cls') #Clears terminal
    print("Lets add a new client")
    
    #Collect all data
    fName = input("First Name: ")
    sName = input("Surname: ")
    phone = input("Phone: ")
    address1 = input("Address Line 1: ")
    city = input("City/town: ")
    province = input("Province: ")
    postcode = input("PostalCode: ")

    #Chuck it into the database
    conn = sqlite3.connect("video_store.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO tblCustomers (fName, sName, phone, address1, city, province, postcode)
        VALUES ('{fName}', '{sName}', '{phone}', '{address1}', '{city}', '{province}', '{postcode}')
    """)

    conn.commit()
    conn.close()

    print("Client has been added")
    time.sleep(1)
    os.system('cls')
    dashboard()

def add_movie():
    os.system('cls')
    print("Lets add a new movie")

    videoVer = input("Video Vertion: ")
    vname = input("Video Name: ")
    typ = input("Type: ") #Vairible named typ due to type being reserved
    
    #Date (Formatted Year, Month, Day)
    print("Getting date....")
    time.sleep(0.4)
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d") #Convert to string before insert

    #Chuck it into the database
    conn = sqlite3.connect("video_store.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO tblVideos (videoVer, vname, type, dateAdded)
        VALUES ('{videoVer}', '{vname}', '{typ}', '{date_string}')
    """)

    conn.commit()
    conn.close()

    print("Done")
    dashboard()
    os.system('cls') 

def hire_movie():
    print("Hire out a movie")

    videoID = input("VideoID: ") 
    custID = input("Customer ID: ")
    
    #Date stuff
    print("Getting date....")
    time.sleep(0.4)
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d") #Convert to string before insert

    #Insert
    conn = sqlite3.connect("video_store.db")
    cursor = conn.cursor()

    cursor.execute(f"""
        INSERT INTO tblHire (custID, videoID, dateHired)
        VALUES ('{custID}', '{videoID}', '{date_string}')
    """)

    conn.commit()
    conn.close()

    print("Done")
    time.sleep(0.5)
    dashboard()

def return_movie():
    os.system('cls')
    print("Return Movie")

#Main method runner
if __name__ == "__main__":
    main()

