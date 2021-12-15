# Grace Foster
# ITP 100-01
# EXERCISE: 07
# courseinfo.py
# ----------------------------------------------------------------
# You can also make a dictionary such as:
"""' rooms= {{'CS101':3004, 'CS102':4501, 'CS103':6755,
        'NT110':1244, 'CM241':1411}''"""
# ----------------------------------------------------------------

room_dict = {
    'CS101': '3004',
    'CS102': '4501',
    'CS103': '6755',
    'NT110': '1244',
    'CM241': '1411',
}
instructors_dict = {
    'CS101': 'Haynes',
    'CS102': ' Alvardo',
    'CS103': 'Rich',
    'NT110': 'Burkes',
    'CM241': 'Lee',
}
meeting_dict = {
    'CS101': '8:00 AM',
    'CS102': '9:00 AM',
    'CS103': '10:00 AM',
    'NT110': '11:00 AM',
    'CM241': '1:00 PM',
}

print("College Course Locator Program")
course_number = str(input("Enter a course number:  "))
print('---------------------------------------------------')

if course_number not in room_dict:
    print(f"The course {course_number} is an invalid course number. Please try again.")
else:
    print(f"The details for course {course_number} are: ")
    print(f'Room:\t\t\t{room_dict [course_number]}')
    print(f'Instructor:\t\t{instructors_dict [course_number]} ')
    print(f'Meeting time:\t{meeting_dict [course_number]} ')

print('---------------------------------------------------')
print("The Program has terminated properly")
