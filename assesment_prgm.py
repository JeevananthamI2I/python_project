students = {
    "S001": {
        "name": "Alice",
        "marks": {
            "Math": 88,
            "Science": 92,
            "English": 85
        }
    },
    "S002": {
        "name": "Bob",
        "marks": {
            "Math": 75,
            "Science": 78,
            "English": 80
        }
    },
    "S003": {
        "name": "Charlie",
        "marks": {
            "Math": 10,
            "Science": 35,
            "English": 90
        }
    },
    "S004": {
        "name": "Diana",
        "marks": {
            "Math": 95,
            "Science": 36,
            "English": 36
        }
    }
}
new_student={}
for key, value in students.items():
    # print(all(list(value["marks"].values())))
    if "marks" in value and all(i >=35 for i in value["marks"].values()):
            new_student[key]=value
# print(new_student)

average_marks={student_detail["name"]:(sum(student_detail["marks"].values()) / len(student_detail["marks"])) for student_detail in new_student.values() }
print(average_marks)
ranked_students=sorted(average_marks.items(),key=lambda x:x[1], reverse=True)
print(ranked_students)
student_ranking={}
rank = 1
previous_average = None

for index, (student_name, average) in enumerate(ranked_students):
    student_ranking[student_name] = rank
    previous_average = average
    # print(ranked_students[index][1])
    # print(len(ranked_students))
    if index < len(ranked_students) - 1 and ranked_students[index][1] != ranked_students[index + 1][1]:
        rank = index + 2
print(student_ranking) 