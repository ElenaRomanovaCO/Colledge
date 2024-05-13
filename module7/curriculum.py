"""
This is program that is amied to help student to get room, instructors and meeting time based on
the course number.
User have to enter course number, and program will display course's instructor, course room and meeting
times.
"""


# Dictionaries for course information
rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Get course number from user
course_number = input("Enter a course number: ")

# Check if the course number exists in the dictionaries
if course_number in rooms and course_number in instructors and course_number in meeting_times:
    room_number = rooms[course_number]
    instructor = instructors[course_number]
    meeting_time = meeting_times[course_number]

    print(f"Course: {course_number}")
    print(f"Room Number: {room_number}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")
else:
    print("Invalid course number.")