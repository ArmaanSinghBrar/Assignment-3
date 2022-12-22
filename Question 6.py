#Student records
student_records = {}                  #Empty dictionary

more_students = 'Y'

while more_students == 'Y':
  name = input("Enter the name of a student: ")
  sid = input("Enter the SID of the student: ")

  student_records[sid] = name   #Add to dictionary

  more_students = input("Do you want to enter more students? (Y/N) ")

print("Student records:")
for sid, name in student_records.items():
  print(f"{sid}: {name}")

sorted_by_name = sorted(student_records.items(), key=lambda x: x[1])
print("\nStudent records sorted by name:")                            #Sorted by name
for sid, name in sorted_by_name:
  print(f"{sid}: {name}")

sorted_by_sid = sorted(student_records.items())
print("\nStudent records sorted by SID:")                            #Sorted by SID
for sid, name in sorted_by_sid:
  print(f"{sid}: {name}")

search_sid = input("\nEnter a SID to search: ")
if search_sid in student_records:
  print(f"Name: {student_records[search_sid]}")
else:
  print("No student found with that SID.")
