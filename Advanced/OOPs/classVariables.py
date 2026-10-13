"""
================================================================================
TOPIC: Class Variables vs Instance Variables
================================================================================
SHORT THEORY:
- Instance Variables: Variables tied to a specific instance (`self.var`). 
  Each object maintains its own distinct copy in memory.
- Class Variables: Variables shared by all instances of the class. Defined directly 
  in the class body, outside any method.
- Namespace Resolution: When accessing `obj.attr`, Python first checks the instance 
  dictionary (`obj.__dict__`). If absent, it searches the class dictionary (`Class.__dict__`).

SYNTAX REFERENCE:
    class MyClass:
        class_var = "shared across all"   # Class variable

        def __init__(self, val):
            self.instance_var = val        # Instance variable

    MyClass.class_var = "new shared"       # Modifies for all instances
    obj1.class_var = "shadowed"            # CREATES NEW INSTANCE VAR on obj1 (shadowing!)

KEY TAKEAWAYS / PITFALLS:
- SHADOWING TRAP: Assigning `instance.class_variable = value` does NOT change the 
  class variable for all objects! It creates a new instance variable that shadows 
  the class variable for that specific instance only.
- Always modify class variables via the Class name: `ClassName.class_variable = ...`.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

class Employee:
    # Class Variables (Shared by all employees)
    company_name = "TechCorp Global"
    total_employee_count = 0

    def __init__(self, name: str, salary: float) -> None:
        # Instance Variables (Unique to each employee)
        self.name = name
        self.salary = salary
        
        # Increment class-level tracking counter
        Employee.total_employee_count += 1

    def display(self) -> None:
        print(f"Employee: {self.name} | Salary: ${self.salary:,} | Company: {self.company_name}")


emp1 = Employee("Rahul Sharma", 85000)
emp2 = Employee("Priya Patel", 95000)

print(f"Total employees hired: {Employee.total_employee_count}")  # 2
emp1.display()
emp2.display()

# Example 1: Updating Class Variable via Class Name (Affects all)
Employee.company_name = "TechCorp AI Labs"
print(f"\nAfter company rebrand:")
print(f"emp1 company: {emp1.company_name}")  # TechCorp AI Labs
print(f"emp2 company: {emp2.company_name}")  # TechCorp AI Labs

# Example 2: Demonstrating the Shadowing Trap
# Assigning through instance creates an instance-level attribute on emp1
emp1.company_name = "Independent Contractor"

print(f"\nAfter shadowing via emp1.company_name:")
print(f"emp1 company (instance attribute): {emp1.company_name}") # Independent Contractor
print(f"emp2 company (class attribute):    {emp2.company_name}") # TechCorp AI Labs
print(f"Employee class company:            {Employee.company_name}") # TechCorp AI Labs
