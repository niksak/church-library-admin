#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author: Nikos Sakellariou
#Date started: 11/15/2014
#Summary:  A client for a library database administration. It admins its books
#users etc
#This is the user and books traffic table


import MySQLdb as mdb
import sys
con = ''
message = 'Αρχείο κίνησης βιβλίων \n'
print (message).decode('utf-8')


def init_con():
    global con
    con = mdb.connect(host="localhost", use_unicode = True, charset = "utf8", user='user', passwd='pass', db='test')

def create_traffic_table(con):
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS trafficTable")
        cur.execute("CREATE TABLE trafficTable(Id INT PRIMARY KEY AUTO_INCREMENT, USER_ID VARCHAR(20), NAME VARCHAR(30),\
DATE_OF_REGISTER VARCHAR(30), RETURN_DATE VARCHAR(30), INSERTION_NUMBER VARCHAR(30), RETURN_D VARCHAR(20), FINE VARCHAR(20), PAID VARCHAR(20), RENEW VARCHAR(30) )")

    
def update(con):
    with con:
        cur = con.cursor()
        id_ = raw_input("Enter the id of the raw you want to update\n")
        user_id = raw_input("Enter the user id \n")
        name = raw_input("Enter the name \n")
        date_of_reg = raw_input("Enter the date of register\n")
        return_date = raw_input("Enter the return date \n")
        insertion_num = raw_input("Enter the insertion number\n")
        return_k = raw_input("Enter the return(kati me epistrofh einai auto alla den... \n")
        fine = raw_input("Enter the prostimo\n")
        paid = raw_input("Enter if is paid \n")
        renew = raw_input("renewal ananewsh \n")
        
        
        cur.execute("UPDATE trafficTable SET USER_ID = %s, NAME = %s, DATE_OF_REGISTER = %s, RETURN_DATE = %s, INSERTION_NUMBER =%s, \
RETURN_D =%s, FINE =%s, PAID = %s, RENEW = %s  WHERE Id = %s", 
        (user_id,name,date_of_reg,return_date,insertion_num,return_k,fine,paid,renew, id_))        
    
        print "Number of rows updated:",  cur.rowcount
        
def print_data(con,rows):
    with con:
        print '--------------------------------------------------------------------------------'
        for row in rows:
            print 
            for element in row:
                    print element,"|",
        print
        print '--------------------------------------------------------------------------------'
def show_books(con):
    with con:
        names = '|Primary key|Κωδικός Χρήστη|Όνομα |Ημερομηνία δανειμου|Ημερομηνία επιστροφής|Αριθμός εισαγωγής|Επιστροφή|Πρόστιμο|Πληρωμή|Ανανέωση'
        #names = (names).decode('utf-8')
        cur = con.cursor()
        cur.execute("SELECT * FROM trafficTable")
        print "This is the traffic Table : "
        rows = cur.fetchall()
        print names
        print_data(con, rows)

def load_from_file(con):
    with con:
        cursor = con.cursor()
        #openfile = raw_input('Give the name of the file mapped. \n ex C:/Documents and Settings/user/Desktop/project/users.txt')
        cursor.execute("LOAD DATA LOCAL INFILE 'C:/Documents and Settings/user/Desktop/library project/books.txt' INTO TABLE churchlib ;")

def insert_new(con):
    with con:
        cur = con.cursor()
  
        print "Εισαγωγή νέου πεδίου \n".decode('utf-8')
       
        user_id = raw_input("Enter the user id \n")
        name = raw_input("Enter the name \n")
        date_of_reg = raw_input("Enter the date of register\n")
        return_date = raw_input("Enter the return date \n")
        insertion_num = raw_input("Enter the insertion number\n")
        return_k = raw_input("Enter the return(kati me epistrofh einai auto alla den... \n")
        fine = raw_input("Enter the prostimo\n")
        paid = raw_input("Enter if is paid \n")
        renew = raw_input("renewal ananewsh \n")
        
        #name = (name).decode('utf-8')
        cur.execute("INSERT INTO trafficTable( USER_ID, NAME ,DATE_OF_REGISTER, RETURN_DATE, INSERTION_NUMBER, RETURN_D, FINE, PAID, RENEW) \
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(user_id, name, date_of_reg, return_date, insertion_num, return_k, fine, paid, renew))
                
def search_user(con):
    with con:
        cur = con.cursor()
        name = ''
        id_ = ''
        user_id = raw_input("Search by user id \n")
        if user_id != '':
            pass
        id_ = raw_input("anazitisi me to id ths kataxwrishs\n")
        if id_ != '':
            cur.execute("SELECT * FROM trafficTable WHERE Id = %s", id_)
            rows = cur.fetchall()
            print_data(con,rows)
        name = raw_input("Search by the name of the user and show user information \n")
        if name != '':
            cur.execute("SELECT *,Users.Proffesion FROM trafficTable INNER JOIN USERS ON trafficTable.USER_ID = USERS.ID")
            rows = cur.fetchall()
            print_data(con,rows)
        #publisher = raw_input("Enter publisher(if exists) to search for \n")
        
        rows = cur.fetchall()
        print_data(con,rows)

def delete(con):
    with con:
        cur =con.cursor()
        user_id = raw_input(" Enter the id of the raw to be deleted\n")
        cur.execute("DELETE FROM trafficTable WHERE Id= %s",user_id)
              
def main():
    global con
    init_con()
    with con:
        #create_traffic_table(con)
        show_books(con)

        while(1):
            print (message).decode('utf-8')
            to_do = raw_input(' 1: show arxeio kinhshs table \n 2: insert new \n 3: Update \n 4: Search \n \
5: insert into database from file\n 6: Delete raw or type "exit" \n > ')
            if to_do == '1':
                show_books(con)
            elif to_do == '2':
                insert_new(con)
            elif to_do == '3':
                update(con)
            elif to_do == '4':
                search_user(con)
            elif to_do == '5':
                load_from_file(con)
            elif to_do == '6':
                delete(con)
            elif to_do == 'exit':
                print 'bye bye :) \n'
                break
            else:
                print 'You entered wrong Value. Try again or type "exit" to quit \n'
  
    con.close()
    


if __name__ == "__main__":
    main()
