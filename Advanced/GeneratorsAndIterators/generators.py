"""
================================================================================
TOPIC: Generator Functions (yield), Generator Expressions, & Memory Efficiency
================================================================================
SHORT THEORY:
- A Generator is a function that returns an iterator which produces a sequence 
  of values lazily on demand.
- The `yield` keyword pauses function execution and saves its current execution state 
  (local variables, instruction pointer). When `next()` is called again, execution resumes 
  immediately after the `yield` statement.
- Why Generators?
  - Massive Memory Efficiency: Standard lists generate ALL elements in RAM at once. 
    A generator produces ONE element at a time in O(1) memory space.
  - Capable of modeling infinite sequences (e.g., real-time sensor streams, Fibonacci).
  - Pipelining: Multiple generators can be chained together without intermediate memory buffers.
- Generator Expressions: Written like list comprehensions but with parentheses `(...)`:
  `gen = (x**2 for x in range(1000000))`.

SYNTAX REFERENCE:
    def my_generator():
        yield value1
        yield value2

    gen_exp = (x * 2 for x in iterable)   # Generator expression

KEY TAKEAWAYS / PITFALLS:
- Calling a generator function `gen()` does NOT execute the body immediately; 
  it returns a generator object. Code only runs when `next()` is called or iterated over.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import sys

# Example 1: Basic Generator Function
def simple_number_stream(limit: int):
    print("  -> Generator started!")
    for i in range(1, limit + 1):
        print(f"  -> About to yield {i}")
        yield i
        print(f"  -> Resumed after yielding {i}")

gen = simple_number_stream(3)
print("Generator object instantiated:", gen)
print("First call: ", next(gen))
print("Second call:", next(gen))
print("Third call: ", next(gen))


# Example 2: Memory Benchmark: List Comprehension vs Generator Expression
list_comp = [x ** 2 for x in range(100000)]
gen_exp = (x ** 2 for x in range(100000))

print("\n--- Memory Consumption Comparison ---")
print(f"List comprehension (100,000 items in RAM): {sys.getsizeof(list_comp):,} bytes")
print(f"Generator expression (O(1) lazy pointer):   {sys.getsizeof(gen_exp):,} bytes")


# Example 3: Infinite Fibonacci Sequence Generator
def fibonacci_stream():
    """Generates an infinite stream of Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_stream()
print("\nFirst 10 Fibonacci numbers from infinite generator:")
first_10 = [next(fib) for _ in range(10)]
print(first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Example 4: Generator Pipelines (Data Processing Stream)
def read_log_lines():
    logs = [
        "2026-10-13 10:00:01 [INFO] Server started",
        "2026-10-13 10:00:05 [ERROR] Database timeout",
        "2026-10-13 10:00:10 [INFO] Client disconnected",
        "2026-10-13 10:00:15 [ERROR] Out of memory"
    ]
    for line in logs:
        yield line

def filter_errors(log_stream):
    for line in log_stream:
        if "[ERROR]" in line:
            yield line

def extract_error_message(error_stream):
    for line in error_stream:
        yield line.split("[ERROR]")[-1].strip()

# Piping generators together cleanly
pipeline = extract_error_message(filter_errors(read_log_lines()))
print("\nFiltered errors from generator pipeline:")
for err in pipeline:
    print(f"  Alert: {err}")
