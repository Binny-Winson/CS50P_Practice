students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
# for student in students:
#     print(student)
# The print out both values and keys

# for student in students:
#     print(student, students[student], sep=", ")

for i, student in enumerate(students):
    print(i+1, student, students[student], sep=", ")