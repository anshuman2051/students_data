from sys import exit
import MySQLdb

def view():
    print "welcome here is your view"
    query = "select version()"
    print execute_query(query)[0]

def edit():
    print "here you can edit students data"

def execute_query(query):
    try:
        db = MySQLdb.connect("localhost", "defalt", "password", "students")
        cursor = db.cursor()
        cursor.execute(query) 
        db.commit()
        print "query executed"
        return cursor.fetchone()
    except:
        db.rollback()
        print "error occured"
    db.close()

def main():
    print """welcome user to this students database,
    :>for viewing info press 1
    :>for editing info press 2
    :> press enter to quit"""
    while True:
        input = raw_input('>')

        if not input :
            exit(1) 
        elif int(input) == 1:
            view()
        elif int(input) == 2:
            edit()
        else :
            print 'please enter a valid no.'
            continue
 

if __name__ == "__main__":
    main()