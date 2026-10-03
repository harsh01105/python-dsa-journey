# Problem: Sort a list of student dictionaries by their "marks" value,
# using Insertion Sort (not Python's built-in sort).
# Approach: Build the sorted portion one student at a time, shifting
# larger elements right until the correct spot is found.
# Time: O(n^2)  |  Space: O(1)

def insertion_sort_by_marks(students):
    for i in range(1, len(students)):
        key_student = students[i]
        j = i - 1
        while j >= 0 and students[j]["marks"] > key_student["marks"]:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_student
    return students


students = [
    {"name": "Aman", "marks": 72},
    {"name": "Priya", "marks": 91},
    {"name": "Harsh", "marks": 85},
    {"name": "Rina", "marks": 60},
]

sorted_students = insertion_sort_by_marks(students)
for s in sorted_students:
    print(f"{s['name']}: {s['marks']}")