#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author: Nikos Sakellariou
#Date started: 11/15/2014
#Summary:  A client for a library database administration. It admins its books
#users etc

import MySQLdb as mdb
import sys


#---------------------------------globals----------------------------------------
user_id = '1'
name = ''
last_name = ''
adress = ''
phone_num = 0
identification = ''
proffesion = ''
e_mail = ''
to_do = '0'

k=" Αρχείο χρηστών \n"


print (k).decode('utf-8')
#--------------------------end of global variables-------------------------------

#------------------------------functions-----------------------------------------
def search_user(con, name):
    with con:
        cur = con.cursor()
        name = ''
        user_id = 0
         
        name = raw_input("Enter name(if exists) to search for \n")
        user_id = raw_input("Enter id(if exists) to search for \n")
        
        cur.execute("SELECT * FROM Users WHERE Name = %s OR Id = %s", (name, user_id))
        rows = cur.fetchall()

        for row in rows:
            for element in row:
                print element
                
def initialize_db(con):

    with con:
            cur = con.cursor()
            cur.execute("set character_set_database = utf8;")
            cur.execute("set character_set_server = utf8;")
            cur.execute("set character_set_system = utf8;")
            cur.execute("set collation_database = utf8_general_ci;")
            cur.execute("set collation_server = utf8_general_ci;")
            cur.execute("set names utf8;")    
def delete(con):
    with con:
        cur =con.cursor()
        user_id = raw_input(" Enter the id of the user to be deleted\n")
        cur.execute("DELETE FROM USERS WHERE Id= %s",user_id)
            
def show_users(con):
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Users")
        print "This is the Users Table : "
        rows = cur.fetchall()
        print'----------------------------------------------------'
        for row in rows:
            print 
            for element in row:
                print element,
        print
        print'----------------------------------------------------'
def update_user(con, name):
    with con:
        cur = con.cursor()
        user_id = raw_input("Enter the id of the user you want to update \n")
        name = raw_input("Enter the updated name \n")
        last_name = raw_input("Enter the last name \n")
        adress = raw_input("Enter the adress \n")
        phone = raw_input("Enter the phone number \n")
        identification = raw_input("Vale arithmo tatutotitas(Identification) \n")
        proffesion = raw_input("Epagelma \n")
        email = raw_input("Email \n")
        cur.execute("UPDATE Users SET Name = %s, LastName = %s, Adress = %s, Phone = %s, Identification = %s, Proffesion = %s, Email = %s WHERE Id = %s", 
        (name,last_name, adress, phone, identification, proffesion, email, user_id))        
    
        print "Number of rows updated:",  cur.rowcount


    
def insert_new(con):
    with con:
        name = ''
        cur = con.cursor()
        user_id = raw_input("Enter the user id\n")
        print "Inserting new user. Currently we support only insertion of his name :P \n"

        name = raw_input("Enter the name \n")
        last_name = raw_input("Enter the last name \n")
        adress = raw_input("Enter the adress \n")
        phone = raw_input("Enter the phone number \n")
        identification = raw_input("Vale arithmo tatutotitas(Identification) \n")
        proffesion = raw_input("Epagelma \n")
        email = raw_input("Email \n")
        
        cur.execute("INSERT INTO Users(IDNUM, Name, LastName, Adress, Phone, Identification, Proffesion, Email) \
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(user_id, name, last_name, adress, phone, identification, proffesion, email))

       
def main():
    #---------------------------------CONNECTION--------------------------------------------------- 
    
    con = mdb.connect(host="localhost", use_unicode = True, charset = "utf8", user='user', passwd='pass', db='test')
    

    with con:
        
        cur = con.cursor()
        #cur.execute("DROP TABLE IF EXISTS Users")
        #cur.execute("CREATE TABLE Users(Id INT PRIMARY KEY AUTO_INCREMENT,IDNUM VARCHAR(20), Name VARCHAR(25), LastName VARCHAR(25),\
    #Adress VARCHAR(30), Phone VARCHAR(20), Identification VARCHAR(30), Proffesion VARCHAR(30), Email VARCHAR(30))")
       
    #----------------------------------------Main Menu--------------------------------------------------
        while(1):  
            to_do = raw_input('1: show Users table, 2: insert new user, 3 Update User, 4: Search User 5:Delete User or type "exit" \n > ')
            if to_do == '1':
                show_users(con)
            elif to_do == '2':
                insert_new(con)
            elif to_do == '3':
                update_user(con, name)
            elif to_do == '4':
                search_user(con, name)
            elif to_do == '5':
                delete(con)
            elif to_do == 'exit':
                print 'bye bye :) \n'
                break
            else:
                to_do = raw_input("You entered wrong Value. Try again. \n 1: show Users table, 2: insert new user, 3 Update User, 4: Search User or type 'exit' \n >") 

    con.close()



if __name__ == "__main__":
    main()


