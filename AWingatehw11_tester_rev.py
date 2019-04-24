import sqlite3
import os.path
from prettytable import PrettyTable 

def query_instructors():
    """ Run Instructors Summary Table query """
 
    db_path = "C:/SQLite/810_hw11"
    db = sqlite3.connect(db_path)
    query = "select i.CWID, i.Name, i.Dept, g.Course, COUNT(*) as Students\
                FROM instructors i\
                    JOIN grades g\
                    ON i.CWID=g.Instructor_CWID\
                GROUP BY i.CWID, i.Name, i.Dept, g.Course"
 
    fields = ['CWID', 'Name', 'Dept', 'Course', 'Students']
    pt = PrettyTable(field_names=fields)
    print('Instructors Summary Table\n')
    for row in db.execute(query):
        pt.add_row(row)
    print(pt)
    
    return None

def main():
    """ Main program body """

    query_instructors()
   
if __name__ == "__main__":
    main()

