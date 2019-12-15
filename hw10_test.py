#Project           : Course Tracker
#Program name      : AWingatehw10_v2.5 rev.py
#Author            : Anthem Rukiya J. Wingate
#Creation Date     : 4.10.19
#Purpose           : AWingatehw10_v2.5 rev.py - Automated Test File
#Revision History  : Version 2.0
#Notes  : 

""" automated tests for AWingatehw10_v2.5 rev.py """

import os 
""" imports OS module """

import unittest
""" imports unit test module """

from AWingatehw10 import Repository, Student, Instructor, Major
""" imports program file for testing """

class Student_Prettytable_Test(unittest.TestCase):
    """ Test class for Student Pretty Table Function """

    def test_student_prettytable(self):
        """ Test function for Student Pretty Table  """
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/SSW810/AWingatehw10_v2.5%20rev.py"
        repo = Repository(directory_path)

        expected =  [[10103,'Baldwin, C','SFEN',['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'],['SSW 540','SSW 555'], None],
            [10115,'Wyatt, X','SFEN',['CS 5,45', 'SSW 564', 'SSW 567', 'SSW 687'],['SSW 540','SSW 555'], None],
            [10172,'Forbes, I','SFEN',['SSW 555', 'SSW 567'],['SSW 540','SSW 564'],['CS 501','CS 513','CS 545']],
            [10175,'Erickson, D','SFEN',['SSW 564','SSW 567','SSW 687'],['SSW 540','SSW 555'],['CS 501','CS 513','CS 545']],
            [10183,'Chapman, O','SFEN',['SSW 689'],['SSW 540','SSW 555','SSW 564','SSW 567'],['CS 501','CS 513','CS 545']],
            [11399,'Cordova, I','SYEN',['SSW 540'],['SYS 612','SYS 671','SYS 800'],None],
            [11461,'Wright, U','SYEN',['SYS 611', 'SYS 750', 'SYS 800'],['SYS 612','SYS 671'],['SSW 540','SSW 565','SSW 810']],
            [11658,'Kelly, P','SYEN',['SSW 540'],['SYS 612','SYS 671','SYS 800'],['SSW 540','SSW 565','SSW 810']],
            [11714,'Morton, A','SYEN',['SYS 611', 'SYS 645'],['SYS 612','SYS 671','SYS 800'],['SSW 540','SSW 565','SSW 810']],
            [11788,'Fuller, E','SYEN',['SSW 540'],['SYS 612','SYS 671','SYS 800'],None]]

        actual = [student.info() for student in repo.students.values()]
        self.assertEqual(actual, expected)
        
        return None

class Instructor_Prettytable_Test(unittest.TestCase):
    """ Test class for Instructor Pretty Table Function """

    def test_student_prettytable(self):
        """ Test function for Instructor Pretty Table  """
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/SSW810/AWingatehw10_v2.5%20rev.py"
        repo = Repository(directory_path)

        expected = [['98765','Einstein, A','SFEN','SSW 567',4],
            ['98765','Einstein, A','SFEN','SSW 540',3],
            ['98764','Feynman, R','SFEN','SSW 564',3],
            ['98764','Feynman, R','SFEN','SSW 687',3],
            ['98764','Feynman, R','SFEN','CS 501',1],
            ['98764','Feynman, R','SFEN','CS 545',1],
            ['98763','Newton, I','SFEN','SSW 555',1],
            ['98763','Newton, I','SFEN','SSW 689',1],
            ['98760','Darwin, C','SYEN','SYS 800',1],
            ['98760','Darwin, C','SYEN','SYS 750',1],
            ['98760','Darwin, C','SYEN','SYS 611',2],
            ['98760','Darwin, C','SYEN','SYS 645',1]] 

        actual = [course for instructor in repo.instructors.values() for course in instructor.info()]
        self.assertEqual(actual, expected)

        return None

class Major_Prettytable_Test(unittest.TestCase):
    """ Test class for Major Pretty Table Function """

    def test_major_prettytable(self):
        """ Test function for Major Pretty Table  """
        dir_abs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))
        directory_path = f"{dir_abs_path}/SSW810/AWingatehw10_v2.5%20rev.py"
        repo = Repository(directory_path)

        expected = [['SFEN', ['CS 501','CS 545','SSW 540','SSW 555','SSW 564','SSW 567','SSW 687','SSW 689']],
            ['SYEN', ['SYS 611','SYS 645','SYS 750']]]

        actual = [major.info() for major in repo.majors.values()]
        self.assertEqual(actual, expected)

        return None
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
        

    