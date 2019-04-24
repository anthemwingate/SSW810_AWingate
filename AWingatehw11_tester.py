import sqlite3
import os.path
from prettytable import PrettyTable 


def connect_to():
    """ create a database connection to the SQLite  """

    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "810_hw11.db")
        with sqlite3.connect(db_path) as conn:
            return conn
    except IOError as err:
        print(err)
 
    return None

def query_instructors(conn):
    """ Run Instructors Summary Table query """

    c = conn.cursor()
    c.execute("SELECT i.CWID, i.Name, i.Dept, g.Course, COUNT(*) as Students\
         FROM instructors i\
             JOIN grades g\
                 ON i.CWID=g.Instructor_CWID\
                     GROUP BY g.Course")
 
    rows = c.fetchall()
    fields = ['CWID', 'Name', 'Dept', 'Course', 'Students']
    pt = PrettyTable(field_names=fields)
    print('Instructors Summary Table\n')
    for each in rows:
        pt.add_row(each)
    print(pt)
    
    return None

def main():
    """ Main program body """

    query_instructors(connect_to())
   
if __name__ == "__main__":
    main()