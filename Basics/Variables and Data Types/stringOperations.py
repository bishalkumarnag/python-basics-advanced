"""
================================================================================
TOPIC: String Operations & Built-in Methods
================================================================================
SHORT THEORY:
- Strings in Python are immutable sequences of Unicode characters.
- Because strings are immutable, any modification method (such as `.replace()`,
  `.upper()`, `.strip()`) returns a NEW string object.
- Indexing is 0-based for forward lookup (0, 1, 2...) and -1-based for reverse (-1, -2...).
- Slicing syntax is `string[start:stop:step]`.

SYNTAX REFERENCE:
    s[start:stop:step]      # Slice from start up to stop (exclusive)
    s[::-1]                 # Reverse a string
    s.strip(), s.rstrip()   # Remove leading/trailing whitespaces
    s.split(delimiter)      # Split string into a list of strings
    delimiter.join(list)    # Join iterable of strings into a single string
    s.replace(old, new)     # Replace occurrences of substring
    s.find(sub), s.index()  # Find substring position (-1 vs ValueError)
    s.startswith(), s.endswith() # Prefix and suffix checks

KEY TAKEAWAYS / PITFALLS:
- Attempting to modify a string character in-place (`s[0] = 'H'`) raises `TypeError`.
- String concatenation with `+` inside large loops is O(N^2); use `''.join(list)` for O(N).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Slicing & Indexing
text = "PythonProgramming"
print(f"Original: {text}")
print(f"First character: {text[0]}")          # 'P'
print(f"Last character: {text[-1]}")          # 'g'
print(f"Slice [0:6]: {text[0:6]}")            # 'Python'
print(f"Step slicing [::2]: {text[::2]}")     # Every 2nd character: 'PtoPormn'
print(f"Reversed string [::-1]: {text[::-1]}")# 'gnimmargorPnohtyP'

# Example 2: Whitespace Cleaning & Case Transformations
raw_email = "   User.Account@Domain.COM \n\t "
cleaned_email = raw_email.strip().lower()
print(f"Cleaned email: '{cleaned_email}'")

# Example 3: Splitting and Joining (Crucial for Data Processing)
csv_line = "apple,banana,orange,grape"
fruits = csv_line.split(",")
print(f"List of fruits: {fruits}")

joined_line = " -> ".join(fruits)
print(f"Re-joined with arrows: {joined_line}")

# Example 4: Substring Searching & Replacements
sentence = "The quick brown fox jumps over the lazy dog"
print(f"Contains 'fox': {'fox' in sentence}")
print(f"Index of 'fox': {sentence.find('fox')}")     # 16
print(f"Find missing word: {sentence.find('cat')}")   # -1 (safe, does not throw)
print(f"Starts with 'The': {sentence.startswith('The')}") # True

updated_sentence = sentence.replace("brown", "silver").replace("lazy", "energetic")
print(f"Updated sentence: {updated_sentence}")

# Example 5: String Validation Methods
numeric_code = "12345"
alpha_code = "Python"
mixed_code = "Python3"

print(f"numeric_code.isdigit(): {numeric_code.isdigit()}") # True
print(f"alpha_code.isalpha(): {alpha_code.isalpha()}")     # True
print(f"mixed_code.isalnum(): {mixed_code.isalnum()}")     # True
