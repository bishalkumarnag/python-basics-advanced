"""
================================================================================
TOPIC: Concurrency in Python: Threading vs Multiprocessing (The GIL Explained)
================================================================================
SHORT THEORY:
- The Global Interpreter Lock (GIL): A mutex in CPython that allows only ONE thread 
  to execute Python bytecode at a time, even on multi-core CPUs.
- When to use What?
  1. Multithreading (`threading` / `concurrent.futures.ThreadPoolExecutor`):
     - BEST FOR: I/O-bound tasks (network requests, database calls, disk I/O).
     - Threads release the GIL while waiting for network/disk responses!
     - Memory footprint is lightweight (threads share address space).
  2. Multiprocessing (`multiprocessing` / `concurrent.futures.ProcessPoolExecutor`):
     - BEST FOR: CPU-bound tasks (heavy number crunching, image processing, machine learning).
     - Bypasses the GIL by spawning independent OS processes, each with its own Python interpreter and GIL.
     - Higher memory overhead (separate memory space per process).

SYNTAX REFERENCE:
    from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(io_task, urls)

    with ProcessPoolExecutor() as executor:
        results = executor.map(cpu_task, numbers)

KEY TAKEAWAYS / PITFALLS:
- Using multithreading for CPU-heavy tasks will NOT make them run faster in standard CPython; 
  it can even be slower due to thread context-switching overhead. Use `multiprocessing` instead!
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import time
from concurrent.futures import ThreadPoolExecutor

# Example 1: Simulated I/O-Bound Task with ThreadPoolExecutor
def simulate_api_download(endpoint_id: int) -> str:
    """Simulates an I/O network call with sleep."""
    print(f"  [Thread] Requesting API endpoint #{endpoint_id}...")
    time.sleep(0.1)  # Simulates network latency (releases GIL!)
    return f"Response payload from endpoint #{endpoint_id}"


print("--- Running I/O-Bound Concurrent Tasks (ThreadPoolExecutor) ---")
endpoints = [1, 2, 3, 4, 5]

start_time = time.perf_counter()
# Executing 5 simulated 0.1s network calls across a pool of worker threads
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(simulate_api_download, endpoints))

elapsed = time.perf_counter() - start_time

print("\nResults gathered:")
for res in results:
    print(f"  {res}")
print(f"Total time elapsed: {elapsed:.2f} seconds (Sequential would take 0.50s!)")


# Example 2: Understanding the Decision Matrix
print("\n--- Concurrency Architecture Decision Matrix ---")
print("| Task Type   | Bottleneck       | Recommended Solution                |")
print("|-------------|------------------|-------------------------------------|")
print("| I/O-Bound   | Network/Disk/DB  | threading, asyncio, ThreadPool      |")
print("| CPU-Bound   | Compute/Math     | multiprocessing, ProcessPool        |")
print("| High-IOPS   | Concurrent Sockets | asyncio (Event Loop)              |")
