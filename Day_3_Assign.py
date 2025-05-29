# You're building a system to manage student data for a university. 
# Each student is identified by a unique student ID and has the following details:
        # - Name
        # - Major
        # - Enrolled Courses (each course has a course name and a dictionary of assessment scores like midterm, final, and project)
#  Sample Data (Nested Dictionary):
university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}
# Q1: Print all student names and their majors
# Q2: Average score per course per student
# Q3: Find students who scored >90 in final of Python101
# Q4: Add new course AI101 for student S101
# Q5: Print average for each course

# Question 1
for student in university_data.values():
    print(f'Name : {student['name']}, major : {student['major']}')
# Output : Name : Alice Johnson, major : Computer Science
         # Name : Bob Smith, major : Mathematics
         # Name : Clara Lopez, major : Physics

# Question 2
for student in university_data.values():
    print(f'Student Name : {student['name']}')
    for course,score in student['courses'].items():
        avg = sum(score.values()) / len(score)
        print(f'Course Name : {course} , Average = {avg:.2f}')
# Output : Student Name : Alice Johnson
         # Course Name : Python101 , Average = 91.33
         # Course Name : Math201 , Average = 81.00
         # Student Name : Bob Smith
         # Course Name : Math201 , Average = 90.33
         # Course Name : Stats101 , Average = 83.00
         # Student Name : Clara Lopez
         # Course Name : Physics101 , Average = 78.33
         # Course Name : Math201 , Average = 70.00

# Question 3 
for student in university_data.values():
    if 'Python101' in student['courses']:
        if student['courses']['Python101']['final'] > 90:
            print(f'Student Name : {student['name']}')
# Output : Student Name : Alice Johnson

# Question 4
university_data['S101']['courses']['AI101'] = {"midterm": 75, "final": 82, "project": 78}
print(university_data["S101"])
# Output : {'name': 'Alice Johnson', 
            # 'major': 'Computer Science', 
            # 'courses': {
                            # 'Python101': {'midterm': 88, 'final': 92, 'project': 94}, 
                            # 'Math201': {'midterm': 78, 'final': 85, 'project': 80}, 
                            # 'AI101': {'midterm': 75, 'final': 82, 'project': 78}}}

# Question 5
course_total = {}
for student in university_data.values():
    for course,score in student['courses'].items():
        total = sum(score.values())
        count = len(score)
    if course in course_total :
        course_total[course]['total'] += total
        course_total[course]['count'] += count
    else :
        course_total[course] = {'total' : total, 'count' : count}

for course,data in course_total.items():
    avg = data['total'] / data['count']
    print(f'Course : {course} , Average : {avg:.2f} ')
# Output : Course : AI101 , Average : 78.33
         # Course : Stats101 , Average : 83.00
         # Course : Math201 , Average : 70.00