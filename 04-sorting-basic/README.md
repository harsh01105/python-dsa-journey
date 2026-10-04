# 04 - Sorting I - Bubble, Insertion, Selection Sort

**Video chapter:** Sorting Algorithms and Divide & Conquer (Bubble Sort, Insertion Sort portions)
**Status:** In progress
**Recommended practice problems:** 2 (Easy, Medium)

## Notes
- These are the simplest sorting algorithms — easy to understand, but inefficient on large data (all O(n²) in the worst case). They're a stepping stone to Merge Sort/Quicksort (Day 5).

| Algorithm | How it works | Time (worst case) | Space |
|---|---|---|---|
| **Bubble Sort** | Repeatedly swap adjacent elements if they're in the wrong order, "bubbling" the largest to the end each pass | O(n²) | O(1) |
| **Selection Sort** | Repeatedly find the minimum of the unsorted part, swap it to the front | O(n²) | O(1) |
| **Insertion Sort** | Build the sorted list one element at a time, inserting each into its correct position | O(n²) worst, O(n) if nearly sorted | O(1) |

- All three sort **in place** (no extra array needed) — that's why space is O(1).
- **Insertion Sort is actually efficient for small or nearly-sorted lists** — that's why some real sorting libraries use it as a fallback for small sub-arrays.
- "Stable" sort = equal elements keep their original relative order. Bubble Sort and Insertion Sort are stable; Selection Sort is **not** stable by default.