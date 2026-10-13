"""
================================================================================
TOPIC: Asynchronous Programming in Python (asyncio, async/await, Event Loop)
================================================================================
SHORT THEORY:
- `asyncio` provides cooperative multitasking using an Event Loop on a SINGLE thread.
- Coroutine: A function defined with `async def`. Calling it does NOT execute the code; 
  it returns a coroutine object.
- `await`: Pauses execution of the current coroutine and yields control back to 
  the event loop until the awaited operation (e.g., I/O call) completes.
- `asyncio.gather(*coroutines)`: Runs multiple coroutines concurrently and waits 
  for all of them to finish.
- `asyncio.run(coro)`: The modern (Python 3.7+) entry point to run an async main coroutine.

SYNTAX REFERENCE:
    import asyncio

    async def fetch_data(id):
        await asyncio.sleep(1)    # Non-blocking async sleep
        return {"id": id}

    async def main():
        results = await asyncio.gather(fetch_data(1), fetch_data(2))
        return results

    asyncio.run(main())

KEY TAKEAWAYS / PITFALLS:
- Never use blocking synchronous calls (like `time.sleep()` or requests.get()) inside 
  an async coroutine. They block the ENTIRE event loop, freezing all concurrent tasks!
  Always use async-compatible equivalents (`asyncio.sleep()`, `aiohttp`, `httpx`).
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

import asyncio
import time

# Example 1: Coroutine Definition & Non-blocking Concurrency
async def fetch_weather_report(city: str, delay: float) -> str:
    print(f"  [START]: Fetching weather for {city}...")
    await asyncio.sleep(delay)  # Cooperative yield to event loop
    print(f"  [DONE]:  Weather report received for {city}!")
    return f"{city}: 24°C, Clear Skies"


async def main():
    print("--- 1. Concurrent Execution with asyncio.gather() ---")
    start = time.perf_counter()

    # Launching 3 asynchronous fetch tasks concurrently
    cities = [
        fetch_weather_report("Bengaluru", 0.1),
        fetch_weather_report("London", 0.15),
        fetch_weather_report("Tokyo", 0.08)
    ]

    reports = await asyncio.gather(*cities)

    elapsed = time.perf_counter() - start
    print("\nWeather Reports Collected:")
    for report in reports:
        print(f"  -> {report}")
    print(f"All 3 async queries completed in {elapsed:.2f}s total!")


# Example 2: Async Task Creation & Timeout Handling
async def slow_database_operation():
    await asyncio.sleep(0.5)
    return "DB_DATA"

async def demonstrate_timeout():
    print("\n--- 2. Handling Async Timeouts ---")
    try:
        # Enforcing a strict 0.2s timeout on a 0.5s task
        result = await asyncio.wait_for(slow_database_operation(), timeout=0.2)
        print("Result:", result)
    except asyncio.TimeoutError:
        print("Caught asyncio.TimeoutError: Operation exceeded deadline and was cancelled!")


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(demonstrate_timeout())
