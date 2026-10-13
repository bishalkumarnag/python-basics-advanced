"""
================================================================================
TOPIC: File Handling in Python (open, read, write, append, with statement)
================================================================================
SHORT THEORY:
- Python interacts with filesystem files using the built-in `open(filename, mode)` function.
- Core File Modes:
  - `'r'`: Read only (default). File must exist, otherwise raises `FileNotFoundError`.
  - `'w'`: Write only. Creates file if not present; TRUNCATES / OVERWRITES if it exists!
  - `'a'`: Append only. Writes data to the end of the file without overwriting.
  - `'r+'`: Read and write.
  - `'b'`: Binary mode (e.g., `'rb'`, `'wb'`) for images, PDFs, compiled files.
  - `'t'`: Text mode (default).
- Context Manager (`with open(...) as f:`):
  - Guarantees file stream closure automatically upon exiting the block, 
    even if an unhandled exception or crash occurs. Never rely on manual `f.close()`.

SYNTAX REFERENCE:
    with open("path/to/file.txt", "r", encoding="utf-8") as f:
        content = f.read()          # Read entire file as string
        line = f.readline()         # Read single line
        lines = f.readlines()       # Read all lines into list of strings
        for line in f: ...          # Memory-efficient line-by-line streaming

KEY TAKEAWAYS / PITFALLS:
- Always specify `encoding="utf-8"` when working with text files to prevent cross-platform 
  Unicode decoding errors on Windows/macOS/Linux.
- For large files, NEVER use `f.read()` or `f.readlines()`; iterate using `for line in f:` 
  to stream lines in O(1) memory!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import os

# Resolving path relative to this script so it runs reliably from anywhere
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_FILE = os.path.join(CURRENT_DIR, "sample_notes.txt")

# Example 1: Writing to a File ('w' mode)
with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
    f.write("Line 1: Introduction to File Handling in Python.\n")
    f.write("Line 2: Built-in context managers guarantee file closure.\n")
    f.writelines([
        "Line 3: Fast and expressive.\n",
        "Line 4: Always use encoding='utf-8'.\n"
    ])
print(f"File successfully written to: {SAMPLE_FILE}")

# Example 2: Appending to a File ('a' mode)
with open(SAMPLE_FILE, "a", encoding="utf-8") as f:
    f.write("Line 5: This line was appended at the end.\n")

# Example 3: Memory-Efficient Line-by-Line Reading (Best Practice)
print("\n--- Reading line by line via iterator ---")
with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        print(f"[{line_num}] {line.strip()}")

# Example 4: Seeking and Reading Chunks
with open(SAMPLE_FILE, "r", encoding="utf-8") as f:
    chunk = f.read(15)  # Read first 15 characters
    print(f"\nFirst 15 characters: '{chunk}'")
    print(f"Current file pointer position: {f.tell()}")
    
    # Reposition pointer back to beginning
    f.seek(0)
    print(f"After seek(0), pointer reset to: {f.tell()}")

# Example 5: Clean-up (Deleting scratch file created during test)
if os.path.exists(SAMPLE_FILE):
    os.remove(SAMPLE_FILE)
    print(f"\nCleaned up temporary demonstration file: {SAMPLE_FILE}")