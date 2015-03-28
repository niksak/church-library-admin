#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author: Nikos Sakellariou
#Date started: 11/15/2014
#Summary:  A client for a library database administration. It admins its books
#users etc

import MySQLdb as mdb
import sys
con = ''
message = 'Βιβλιοθήκη \n'
print (message).decode('utf-8')


def init_con():
    global con
    con = mdb.connect(host="localhost", use_unicode = True, charset = "utf8", user='userpass', passwd='databasepass', db='test')

def create_church_table(con):
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS churchlib")
        cur.execute("CREATE TABLE churchlib(Id INT PRIMARY KEY AUTO_INCREMENT, TITLE VARCHAR(30), AUTHOR VARCHAR(30), SECONDAUTHOR VARCHAR(30),\
                    PROTOTYPE_TITLE VARCHAR(30), PUBLICATION_PLACE VARCHAR(30), PUBLISHER VARCHAR(30), PUBLISHING_TIME VARCHAR(30), \
                    EDITION VARCHAR(30), PAGES VARCHAR(20),cm VARCHAR(20), VISUAL VARCHAR(20), SERIES VARCHAR(30), NOTES VARCHAR(100), \
                    BOOK_STAMP VARCHAR(30),KEY_WORDS VARCHAR(100), ISBN VARCHAR(20), USHER_NUM VARCHAR(20), CLASSIFIER_NUM VARCHAR(20))")

def update_book(con):
    with con:
        name = ''
        user_id = ''

        cur = con.cursor()
        user_id = raw_input("Enter the id of the book you want to update \n")
        name = raw_input("Enter the title to be update \n")

        author = raw_input("Enter the author \n")
        second_author = raw_input("Enter the second author \n")
        prototype_title = raw_input("Enter the prototype title \n")
        publication_place = raw_input("Enter the publication place \n")
        publisher = raw_input("Enter the publisher \n")
        publishing_time = raw_input("Enter the publishing time \n")
        edition = raw_input("Enter the edition \n")
        pages = raw_input("Enter the number of pages \n")
        cm = raw_input("Enter the centimeters \n")
        visual = raw_input("Enter the if it is visual (You have to enter values 'TRUE' or 'FALSE') \n")
        series = raw_input("Enter the series\n")
        notes = raw_input("Here You may enter some notes max 100 characters \n")
        book_stamp = raw_input("Enter the book stamp \n")
        key_words = raw_input("Enter the key words \n")
        isbn = raw_input("Enter the ISBN \n")
        usher_num = raw_input("Enter the USHER number \n")
        classifier_num = raw_input("Enter the CLASSIFIER number \n")
        
        cur.execute("UPDATE churchlib SET TITLE = %s, AUTHOR = %s , SECONDAUTHOR = %s, PROTOTYPE_TITLE = %s, PUBLICATION_PLACE = %s, PUBLISHER = %s, PUBLISHING_TIME = %s\
, EDITION = %s, PAGES = %s, cm = %s, VISUAL = %s, SERIES = %s, NOTES = %s, BOOK_STAMP = %s, KEY_WORDS = %s, ISBN = %s, USHER_NUM = %s, CLASSIFIER_NUM = %s WHERE Id = %s", 
        (name,author,second_author,prototype_title,publication_place,publisher,publishing_time,edition,pages,cm,visual,series,notes,book_stamp,key_words,isbn\
         ,usher_num,classifier_num, user_id))        
    
        print "Number of rows updated:",  cur.rowcount
def delete(con):
    with con:
        cur =con.cursor()
        user_id = raw_input(" Enter the id of the book entry to be deleted\n")
        cur.execute("DELETE FROM churchlib WHERE Id= %s",user_id)
                    
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
        names = '|Primary key|Τίτλος|Συγγραφέας|Δευτερεύον Συγ|Τίτλος Προτοτύπου|Τόπος έκδοσης|Εκδότης|Ημερομηνία έκδοσης|Έκδοση|Σελίδες|εκατοστά|Εικονογραφιμένο\
|σειρά|σημειώσεις|Σφραγίδα Βιβλίου|Λέξεις κλειδιά|ISBN|αριθμός USHER|Classifier αριθμός|'
        
        cur = con.cursor()
        cur.execute("SELECT * FROM churchlib")
        print "This is the Church books Table : "
        rows = cur.fetchall()
        print names
        print_data(con, rows)

def load_from_file(con):
    with con:
        cursor = con.cursor()
        #add the path to load from file. It has to be in the right format. Currently is disabled.
        cursor.execute("LOAD DATA LOCAL INFILE 'C:/Documents and Settings/user/Desktop/libraryProject/books.txt' INTO TABLE churchlib ;")

def insert_new(con):
    with con:
        title = ''
        cur = con.cursor()
  
        print "Inserting new book. Currently we support only insertion of its' title :P \n"
        title = raw_input("Enter the title \n")
        author = raw_input("Enter the author \n")
        second_author = raw_input("Enter the second author \n")
        prototype_title = raw_input("Enter the prototype title \n")
        publication_place = raw_input("Enter the publication place \n")
        publisher = raw_input("Enter the publisher \n")
        publishing_time = raw_input("Enter the publishing time \n")
        edition = raw_input("Enter the edition \n")
        pages = raw_input("Enter the number of pages \n")
        cm = raw_input("Enter the centimeters \n")
        visual = raw_input("Enter the if it is visual (You have to enter values 'TRUE' or 'FALSE') \n")
        series = raw_input("Enter the series\n")
        notes = raw_input("Here You may enter some notes max 100 characters \n")
        book_stamp = raw_input("Enter the book stamp \n")
        key_words = raw_input("Enter the key words \n")
        isbn = raw_input("Enter the ISBN \n")
        usher_num = raw_input("Enter the USHER number \n")
        classifier_num = raw_input("Enter the CLASSIFIER number \n")
        
        
        cur.execute("INSERT INTO churchlib(TITLE,AUTHOR,SECONDAUTHOR,PROTOTYPE_TITLE,PUBLICATION_PLACE,PUBLISHER,PUBLISHING_TIME,\
EDITION,PAGES,cm,VISUAL,SERIES,NOTES,BOOK_STAMP,KEY_WORDS,ISBN,USHER_NUM,CLASSIFIER_NUM) \
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(title,author,second_author,prototype_title,publication_place,publisher,\
                                                                publishing_time,edition,pages,cm,visual,series,notes,book_stamp,key_words,\
                                                                isbn,usher_num,classifier_num))
                
def search_book(con):
    with con:
        cur = con.cursor()
        title = ''
        book_id = ''
        author = ''
        publisher = ''
        title = raw_input("Enter title(if exists) to search for \n")
        author = raw_input("Enter author(if exists) to search for \n")
        publisher = raw_input("Enter publisher(if exists) to search for \n")
        cur.execute("SELECT * FROM churchlib WHERE title = %s", title)
        rows = cur.fetchall()

        print_data(con,rows)
        
def main():
    global con
    init_con()
    with con:
        #The function bellow is only for initialization
        #create_church_table(con)
        show_books(con)

        while(1):  
            to_do = raw_input('1: show church books table \n2: insert new book \n3: Update Book\n4: Search book \n5: insert into database books from file\n6:Delete book entry or type "exit" \n > ')
            if to_do == '1':
                show_books(con)
            elif to_do == '2':
                insert_new(con)
            elif to_do == '3':
                update_book(con)
            elif to_do == '4':
                search_book(con)
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
