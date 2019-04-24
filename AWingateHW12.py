#Project          : Homework 12
#Program name      : AWingatehw12
#Author            : Anthem Rukiya J. Wingate
#Submission Date   : 04.24.2019
#Purpose           : Homework Submission 12 - University Repository with added functionality
#Revision History  : Version 1
#Notes  : 

import os.path
import sqlite3
from flask import Flask, render_template
import jinja2


app = Flask(__name__)

@app.route('/instructors')
def instructors_summary():
    """ Run Instructors Summary Table query """

    db_path = "C:/Users/Anthe/OneDrive/Documents/Stevens/SSW 810/Homework/AWingateHW12/810_hw11.db"
    
    query = """select i.CWID, i.Name, i.Dept, g.Course, COUNT(*) as Students
                FROM instructors i
                    JOIN grades g
                    ON i.CWID=g.Instructor_CWID
                GROUP BY i.CWID, i.Name, i.Dept, g.Course"""
    
    db = sqlite3.connect(db_path)
    rows = db.execute(query)
    data = [{'CWID':CWID, 'Name':Name, 'Dept':Dept, 'Course':Course, 'Students':Students} for CWID, Name, Dept, Course, Students in rows]
    db.close()

    return render_template('instructors_table.html', title = 'Stevens Repository', table_title = 'Number of Students by Course and Instuctor', instructors = data)

app.run(debug=True)
