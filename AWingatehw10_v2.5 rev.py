#Project           : Course Tracker
#Program name      : AWingatehw10_v2.5 rev.py
#Author            : Anthem Rukiya J. Wingate
#Creation Date     : 4.10.19
#Purpose           : Data repository of courses, students, and instructors.  
# The system will be used to help students track their required courses, the courses they have successfully completed, their grades,  GPA, etc.  
# The system will also be used by faculty advisors to help students to create study plans.
#Revision History  : Version 3
#Notes  : Additional revision made for interview submission.

import os
from prettytable import PrettyTable 
from collections import defaultdict


class Student:
    """ Represent a single student """
    
    def __init__(self, cwid, name, major):
        self.cwid = cwid
        self.name = name
        self.major = major
        self.course_grades = defaultdict(str) # key: course  value: grade
 

    def add_grade(self, course, grade):
        """ assigns grades as values for course keys in default dictionary """

        if grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-']:  
            self.course_grades[course] = grade


    def info(self, major):
        """ returns field names for repository table """

        rem_req = major.req_courses - set(self.course_grades.keys()) # compute the set difference of courses and required
        if set(self.course_grades.keys()) & major.elec_courses:  # if any courses in common, then electives are met
            rem_elec = None  # empty set
        else:
            rem_elec = sorted(major.elec_courses)
        
        return [self.cwid, self.name, self.major, sorted(self.course_grades.keys()), sorted(rem_req), rem_elec ]
  
    @staticmethod
    def fields():
        """ returns field names for student class """
        
        return ["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives"]
        

class Instructor:
    """ Creates instructor class """
    
    def __init__(self, cwid, name, dept):
        self.cwid = cwid
        self.name = name
        self.dept = dept
        self.course_enrollment = defaultdict(int) # key: course  value: number of students enrolled in class

    def add_course(self, course):
        """ assigns enrollment iteration to values for course keys """
        self.course_enrollment[course] += 1

    def info(self):
        """ yields contents of instructor class default dictionary as rows for repository table """
        for course, students in self.course_enrollment.items():
            yield [self.cwid, self.name, self.dept, course, students]
    
    @staticmethod
    def fields():
        """ returns field names for instructor class """
        return ["CWID", "Name", "Dept", "Course", "Enrollment"]

class Major:
    """ Creates Major class """
    
    def __init__(self, dept):
        self.dept = dept
        self.req_courses = set() # Key: set of required courses
        self.elec_courses = set() # Key: set of elective courses

    def add_major_course(self, flag, course):
        """ assigns courses to values for department keys """

        if flag == 'R':
            self.req_courses.add(course)
        elif flag == 'E':
            self.elec_courses.add(course)
        else:
            print("Invalid flag '{flag} for {course} in {self.dept}")                     

             
    def info(self):
        """ returns contents of major class default dictionary as rows for repository table """

        return [self.dept, sorted(self.req_courses), sorted(self.elec_courses)]  # each major has only one row
    
    @staticmethod
    def fields():
        """ returns field names for major class """
        
        return ["Department", "Required", "Electives"]

class Repository:
    """ Creates dict of student, instructor and grades files """
    
    def __init__(self, path):
        # Repository variable assignments
        self.path = path  # directory where the students.txt, grades.txt, instructors.txt, and majors.txt are kept
        self.students = dict()  # key: student CWID value: instance of class Student
        self.instructors = dict()  # key: instructor CWID value: instance of class Instructor
        self.majors = dict() # key: dept value: instance of class Major

        # File access
        # Note: read majors first so you can tell Students electives and required when the student is created
        self.read_majors(os.path.join(path, "majors.txt"))
        self.read_students(os.path.join(path, "students.txt"))
        self.read_instructors(os.path.join(path, "instructors.txt"))
        self.read_grades(os.path.join(path, "grades.txt"))
        # Note: read majors first: self.read_majors(os.path.join(path, "majors.txt"))

        # Table Creation
        self.student_prettytable()
        self.instructor_prettytable()
        self.major_prettytable()

    def read_majors(self, filepath):
        """ Read major information from the specified path and create instances of class Major """

        # Note: get all Majors from self.major: #tot_dept = list()
        for dept, flag, course in self.file_reader(filepath, 3): 
            if dept not in self.majors:  # Note: create a new major if this is the first time we see the major
                self.majors[dept] = Major(dept)

            self.majors[dept].add_major_course(flag, course)

    def read_students(self, filepath):
        """ Read students from the specified path and create instances of class Student """
        for cwid, name, major in self.file_reader(filepath, 3):
            self.students[cwid] = Student(cwid, name, major)  # Note: updated

    def read_instructors(self, filepath):
        """ Read instructors from the specified path and create instances of class Instructor """
        
        for cwid, name, dept in self.file_reader(filepath, 3):
            self.instructors[cwid] = Instructor(cwid, name, dept)

    def read_grades(self, filepath):
        """ Read grades from the specified path and add to instances of class Instructor and class Student """
        
        for stu_cwid, course, grade, inst_cwid in self.file_reader(filepath, 4):
            self.students[stu_cwid].add_grade(course, grade)
            self.instructors[inst_cwid].add_course(course)

    def student_prettytable(self):
        """ creates table of student information """

        pt = PrettyTable(field_names=Student.fields())
        for student in self.students.values():
            pt.add_row(student.info(self.majors[student.major]))
        print(pt)

    def instructor_prettytable(self):
        """ creates table of instructor information """
        
        pt = PrettyTable(field_names=Instructor.fields())
        for instructor in self.instructors.values():
            for course in instructor.info():
                pt.add_row(course)
        print(pt)
    
    def major_prettytable(self):
        """ creates table of major information """

        pt = PrettyTable(field_names=Major.fields())
        for major in self.majors.values():
            pt.add_row(major.info())
        print(pt)
        
    def file_reader(self, filepath, numfields, sep='\t', header=False):  
        """ Retrieves lines from a file """
        
        current = 0

        try: 
            fp = open(filepath, 'r') 
        except FileNotFoundError: 
            raise FileNotFoundError("Can't open file")
        else:
            with fp:
                for line in fp:
                    current += 1
                    tokens = line.strip('\r\n').split(sep)
                    if tokens == ['']:
                        continue
                    elif numfields == len(tokens):
                        if header and current == 1:
                            continue
                        else:
                            yield tokens
                    else:
                        raise  ValueError("{} fields on line {} but expected {}".format(len(tokens), current, numfields))
                     
        return None

 
def main():
    """ Main program body """
    
    dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
    directory_path = f"{dir_abs_path}/SSW810/AWingatehw10_v2.5%20rev.py"
    Repository(directory_path)
    
if __name__ == "__main__":
    main()
        