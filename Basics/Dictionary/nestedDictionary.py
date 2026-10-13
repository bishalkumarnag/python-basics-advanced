"""
================================================================================
TOPIC: Nested Dictionaries in Python
================================================================================
SHORT THEORY:
- A nested dictionary is a dictionary that contains other dictionaries as values.
- Used extensively when working with JSON data, database records, and configuration trees.
- Accessing inner elements uses chained indexing: `dict[outer_key][inner_key]`.
- For safe traversal without KeyError, chain `.get()` or use `functools.reduce()`.

SYNTAX REFERENCE:
    users = {
        "user1": {"name": "Alice", "role": "Admin"},
        "user2": {"name": "Bob", "role": "Viewer"}
    }
    users["user1"]["role"]               # Chained key access
    users.get("user1", {}).get("role")   # Safe nested lookup

KEY TAKEAWAYS / PITFALLS:
- Chaining `d["outer"]["inner"]` crashes if `"outer"` does not exist. 
  `d.get("outer", {}).get("inner", fallback)` prevents crashes.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

organization = {
    "emp_101": {
        "name": "Bishal",
        "department": "Engineering",
        "skills": ["Python", "Algorithms", "System Design"],
        "compensation": {"base": 120000, "bonus": 15000}
    },
    "emp_102": {
        "name": "Sarah",
        "department": "Product",
        "skills": ["Roadmapping", "Analytics"],
        "compensation": {"base": 110000, "bonus": 12000}
    }
}

# Example 1: Accessing Nested Elements
print("Employee 101 Name:", organization["emp_101"]["name"])
print("Employee 101 Base Salary:", organization["emp_101"]["compensation"]["base"])
print("Employee 101 First Skill:", organization["emp_101"]["skills"][0])

# Example 2: Safe Deep Lookup
emp_id = "emp_999"
bonus = organization.get(emp_id, {}).get("compensation", {}).get("bonus", 0)
print(f"Safe bonus lookup for {emp_id}: ${bonus}")

# Example 3: Modifying Nested Data
organization["emp_101"]["skills"].append("Docker")
organization["emp_101"]["compensation"]["base"] += 10000
print(f"\nUpdated Emp 101: {organization['emp_101']}")

# Example 4: Iterating Nested Dictionaries
print("\nStaff Directory:")
for eid, details in organization.items():
    print(f"ID: {eid} | Name: {details['name']} | Dept: {details['department']}")