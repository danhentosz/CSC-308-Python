#CSC308 Python Assignment 8
#Daniel Hentosz, Casey Crowley
#hen3883@calu.edu, cro8478@calu.edu
#Created: 3/19/21
#Last revised: 3/23/21
# Our main function.
def main():
    k1, k2, k3 = fill()
    course_num=str(input('Enter the course number for the class: '))
    course_num=course_num.upper()
    if course_num in k1:
        print('Course Number:', course_num)
        print('Room Number: ', k1.get(course_num, 'Not found.'))
        print('Instructor: ', k2.get(course_num, 'Not found.'))
        print('Meeting Time: ', k3.get(course_num, 'Not found.'))
    else:
        print('Invalid course number.')
        main()


# Creates the directories with the information provided in the text book.
# RECIVES: Nothing.
# RETURNES: Three directories.
# REQUIRES: Nothing.
def fill():
    k1 = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
    k2 = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
    k3 = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.',
          'CM241': '1:00 p.m.'}
    return k1, k2, k3


main()
