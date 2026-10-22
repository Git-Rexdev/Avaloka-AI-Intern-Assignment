# Avaloka Assignment: Data Structures & Systems Design

Solutions for the SE Intern assignment, written in Python 3.

## Contents

| File | Description |
| --- | --- |
| `solution.py` | All code, plus simple tests at the bottom |

## Problem 1: LRU Cache

`LRUCache(capacity)` supports `get(key)` and `put(key, value)`, both in O(1) time.

- A **hash map** gives direct access to any key's node.
- A **doubly linked list** keeps keys in order of use (most recent at the front, least recent at the back).
- Dummy head and tail nodes remove edge-case checks.

## Problem 2: Event Scheduler

- `can_attend_all(events)` sorts events by start time and returns `False` if any event starts before the previous one ends.
- `min_rooms_required(events)` sorts start and end times separately and counts the peak number of meetings running together.
- `assign_rooms(events)` (bonus) uses heaps to give each event a room name such as `Room A`, `Room B`.

Adjacent events (end time equals start time) are not treated as overlaps.

## Complexity

| Function | Time | Space |
| --- | --- | --- |
| `LRUCache.get` / `put` | O(1) | O(capacity) overall |
| `can_attend_all` | O(n log n) | O(n) |
| `min_rooms_required` | O(n log n) | O(n) |
| `assign_rooms` | O(n log n) | O(n) |

## Run

```bash
python solution.py
```

This runs the built-in tests and prints `all tests passed`.

## Example

```python
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)        # 1
cache.put(3, 3)     # evicts key 2
cache.get(2)        # -1

min_rooms_required([(9, 11), (10, 12), (10, 13)])   # 3
can_attend_all([(9, 10), (10, 11), (11, 12)])       # True
```

## Author

Manmohan Zanwar
