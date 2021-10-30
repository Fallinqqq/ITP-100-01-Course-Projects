# Grace Foster
# ITP 100-01
# EXERCISE: 07
# courseinfo.py
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
    'CS102': 'Alvardo',
    'CS103': 'Rich',
    'NT110': 'Burkes',
    'CM241': 'Lee',
}
meeting_dict = {
    'CS101': '8:00 a.m.',
    'CS102': '9:00 a.m.',
    'CS103': '10:00 a.m.',
    'NT110': '11:00 a.m.',
    'CM241': '1:00 p.m.',
}

print("College Course Locator Program")
course_number = str(input("Enter a course number:  "))
print('---------------------------------------------------')

if course_number not in room_dict:
    print(f"{course_number} course number is invalid.")
else:
    print(f"The details for course {course_number} are: ")
    print(f'Room: {room_dict [course_number]}')
    print(f'Instructor: {instructors_dict [course_number]} ')
    print(f'meeting time: {meeting_dict [course_number]} ')

print('---------------------------------------------------')
print("program has terminated")
