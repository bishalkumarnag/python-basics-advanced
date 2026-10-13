"""
================================================================================
TOPIC: Advanced File Handling (JSON, CSV, and pathlib.Path)
================================================================================
SHORT THEORY:
- In modern Python (3.4+), the `pathlib` module is the object-oriented standard 
  for managing filesystem paths across operating systems.
- JSON Handling (`json` module):
  - `json.dump(obj, f)`: Serializes Python dict/list directly into an open file.
  - `json.load(f)`: Deserializes JSON file into Python data structures.
  - `json.dumps(obj)` / `json.loads(str)`: In-memory string serialization.
- CSV Handling (`csv` module):
  - `csv.reader` / `csv.writer`: Positional row processing.
  - `csv.DictReader` / `csv.DictWriter`: Maps rows directly to Python dictionaries.

SYNTAX REFERENCE:
    from pathlib import Path
    p = Path("dir") / "file.txt"      # Cross-platform / path joining
    p.exists(), p.is_file(), p.read_text(), p.write_text()

    import json
    json.dump(data, file_obj, indent=2)
    data = json.load(file_obj)

    import csv
    reader = csv.DictReader(file_obj)

KEY TAKEAWAYS / PITFALLS:
- Never use string concatenation (`"path/" + "to/" + "file"`) to build paths. 
  Always use `pathlib.Path` or `os.path.join` for cross-platform portability.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

from pathlib import Path
import json
import csv

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "temp_config.json"
CSV_FILE = BASE_DIR / "temp_users.csv"

# Example 1: Object-Oriented Filesystem Operations via pathlib
print("--- 1. pathlib.Path Demonstration ---")
print(f"Current file:      {Path(__file__).name}")
print(f"Parent directory:  {BASE_DIR}")
print(f"File exists?       {Path(__file__).exists()}")

# Example 2: Structured JSON Serialization and Deserialization
print("\n--- 2. JSON File Handling ---")
database_config = {
    "host": "postgres.internal.net",
    "port": 5432,
    "credentials": {
        "user": "app_admin",
        "ssl_enabled": True
    },
    "pool_size": 20
}

# Writing JSON
with open(JSON_FILE, "w", encoding="utf-8") as jf:
    json.dump(database_config, jf, indent=4)
print(f"Config serialized to JSON: {JSON_FILE}")

# Reading JSON
with open(JSON_FILE, "r", encoding="utf-8") as jf:
    loaded_config = json.load(jf)
print(f"Loaded database host: {loaded_config['host']}")
print(f"SSL Status:          {loaded_config['credentials']['ssl_enabled']}")

# Example 3: Tabular CSV Operations with DictWriter and DictReader
print("\n--- 3. CSV File Handling (DictWriter / DictReader) ---")
user_records = [
    {"id": 1, "username": "bishal", "role": "Senior Engineer"},
    {"id": 2, "username": "ananya", "role": "Tech Lead"},
    {"id": 3, "username": "rahul",  "role": "Product Manager"}
]

# Writing CSV with headers
with open(CSV_FILE, "w", newline="", encoding="utf-8") as cf:
    fieldnames = ["id", "username", "role"]
    writer = csv.DictWriter(cf, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(user_records)

# Reading CSV
with open(CSV_FILE, "r", encoding="utf-8") as cf:
    reader = csv.DictReader(cf)
    for row in reader:
        print(f"User #{row['id']}: {row['username']:<8} ({row['role']})")

# Clean-up temporary files
if JSON_FILE.exists():
    JSON_FILE.unlink()
if CSV_FILE.exists():
    CSV_FILE.unlink()
print("\nTemporary demonstration files successfully removed.")
