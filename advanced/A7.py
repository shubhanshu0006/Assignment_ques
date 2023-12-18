#using for loops
students = ["Shubhanshu", "Bhupender", "prakhar"]
subjects = ["Math", "English", "Science"]
student_subject_dict = {}
for i in range(len(students)):
    student_subject_dict[students[i]] = subjects[i]
print(student_subject_dict)
#using dictionary comprehension
students = ["Shubhanshu", "Bhupender", "prakhar"]
subjects = ["Math", "English", "Science"]

student_subject_dict = {students[i]: subjects[i] for i in range(len(students))}

print(student_subject_dict)
