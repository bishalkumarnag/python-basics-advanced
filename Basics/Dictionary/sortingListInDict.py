"""
================================================================================
TOPIC: Sorting Lists Inside Dictionaries
================================================================================
SHORT THEORY:
- A dictionary often stores lists of numerical metrics or scores per entity.
- Common sorting goals:
  1. Sort dictionary entries based on aggregate metrics of the list (e.g., `sum()`, `len()`, `average`).
  2. Sort entries based on a specific element index in the list (e.g., final score `list[-1]`).
  3. Sort the lists contained INSIDE each dictionary key in-place.

SYNTAX REFERENCE:
    # Sort by sum of list values:
    sorted(d.items(), key=lambda item: sum(item[1]), reverse=True)

    # Sort by specific index of list:
    sorted(d.items(), key=lambda item: item[1][target_index])

KEY TAKEAWAYS / PITFALLS:
- Watch out for `IndexError` when sorting by index if lists have differing lengths.
================================================================================
"""

# ==============================================================================
# SOLVED EXAMPLES
# ==============================================================================

candidate_rounds = {
    "Aakash": [75, 80, 85, 90],
    "Bishal": [90, 85, 90, 95],
    "Chitra": [98, 67, 45, 92],
    "David":  [80, 80, 82, 85]
}

# Example 1: Sort by Total Marks (Sum) Descending
by_total = dict(sorted(candidate_rounds.items(), key=lambda item: sum(item[1]), reverse=True))
print("Ranked by Total Marks:")
for rank, (cand, scores) in enumerate(by_total.items(), start=1):
    print(f"  #{rank} {cand:<8} -> Total: {sum(scores)} {scores}")

# Example 2: Sort by Final Round Score (index -1)
by_final_round = dict(sorted(candidate_rounds.items(), key=lambda item: item[1][-1], reverse=True))
print("\nRanked by Final Round Performance:")
for cand, scores in by_final_round.items():
    print(f"  {cand:<8} -> Final Round: {scores[-1]}")

# Example 3: In-place Sorting of the Lists Inside Each Dictionary Entry
for cand in candidate_rounds:
    candidate_rounds[cand].sort()  # Sorts score list in ascending order

print(f"\nCandidate scores sorted internally: {candidate_rounds}")