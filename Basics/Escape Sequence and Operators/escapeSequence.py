"""
================================================================================
TOPIC: Escape Sequences & Raw Strings in Python
================================================================================
SHORT THEORY:
- An escape sequence is a backslash `\` followed by a character that has a special
  meaning to the Python interpreter (e.g., newline, tab).
- It allows including non-printable characters or characters that would otherwise
  break string syntax (such as quotation marks).
- Prefixing a string with `r` or `R` creates a "Raw String", which ignores escape
  sequences and treats backslashes literally (essential for regex and Windows paths).

SYNTAX REFERENCE:
    \\n         # Newline (line break)
    \\t         # Horizontal tab (indentation)
    \\\\         # Literal backslash
    \\'         # Single quotation mark inside single-quoted string
    \\"         # Double quotation mark inside double-quoted string
    \\r         # Carriage return
    r"text"    # Raw string literal

KEY TAKEAWAYS / PITFALLS:
- You don't need `\\'` if the string is enclosed in double quotes `"..."`.
- Raw strings cannot end with an odd number of trailing backslashes (`r"C:\\path\\"` is invalid).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

# Example 1: Newline and Tab Formatting
formatted_text = "Item\tQuantity\tPrice\nApple\t10\t\t$2.50\nBanana\t5\t\t$1.20"
print("Table with \\t and \\n:")
print(formatted_text)

# Example 2: Quotes within Strings
dialogue1 = "She said, \"Python is elegant and readable!\""
dialogue2 = 'He replied, \'Indeed, it truly is!\''
# Pythonic alternative: alternate quote types without backslashes
dialogue3 = 'She said, "Look, no backslashes needed!"'

print(dialogue1)
print(dialogue2)
print(dialogue3)

# Example 3: Escaping Backslashes in Paths
windows_path_escaped = "C:\\Users\\Bishal\\Documents\\PythonProjects"
print(f"Escaped path: {windows_path_escaped}")

# Example 4: Raw Strings for Regex and Paths
# Raw string treats backslash literally
raw_regex = r"\d{3}-\d{2}-\d{4}"  # US SSN regex pattern
raw_path = r"C:\Users\Bishal\Documents\PythonProjects"
print(f"Raw regex: {raw_regex}")
print(f"Raw file path: {raw_path}")

# Example 5: Carriage Return (\r) Effect (Overwrites current line)
print("Downloading... 0%", end="\r")
print("Downloading... 100% Done!")