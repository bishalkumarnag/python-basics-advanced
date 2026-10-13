"""
================================================================================
TOPIC: Sorting Nested Dictionaries (Dictionary Inside Dictionary)
================================================================================
SHORT THEORY:
- In real-world data structures, dictionaries often hold inner dictionaries (e.g., records).
- Sorting by an inner property requires accessing the inner dictionary inside 
  the `lambda` sort key: `lambda item: item[1]["inner_key"]`.

SYNTAX REFERENCE:
    sorted(nested_dict.items(), key=lambda item: item[1]["target_metric"])

KEY TAKEAWAYS / PITFALLS:
- Ensure the target inner key exists on all nested entries, or provide a safe `.get()`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

students = {
    "student_1": {"name": "Alice", "gpa": 3.8, "attendance": 95},
    "student_2": {"name": "Bob", "gpa": 3.2, "attendance": 88},
    "student_3": {"name": "Charlie", "gpa": 3.9, "attendance": 91},
    "student_4": {"name": "Diana", "gpa": 3.5, "attendance": 99}
}

# Example 1: Sort Students by GPA Descending
by_gpa = dict(sorted(students.items(), key=lambda item: item[1]["gpa"], reverse=True))
print("Students sorted by GPA (Descending):")
for s_id, data in by_gpa.items():
    print(f"  {data['name']:<8} (ID: {s_id}) -> GPA: {data['gpa']}")

# Example 2: Sort Students by Attendance Ascending
by_attendance = dict(sorted(students.items(), key=lambda item: item[1]["attendance"]))
print("\nStudents sorted by Attendance (Ascending):")
for s_id, data in by_attendance.items():
    print(f"  {data['name']:<8} -> Attendance: {data['attendance']}%")