# Custom Doubly Linked List Palindrome Checker

## Problem Summary

Design a custom `DoublyLinkedList` class in Python (without using built-in list, deque, or similar collections) that stores a sequence of characters (A-Z, a-z). Implement a method to determine whether the sequence is a **custom palindrome** based on the following rules:

### Custom Palindrome Rules:
- Case-insensitive (e.g., 'A' is the same as 'a').
- Ignore all vowels: `a`, `e`, `i`, `o`, `u`.
- Ignore repeated characters (only consider their first occurrence when scanning forward and backward).
- Compare forward and backward sequences after filtering.

---

## 💡 Approach Used

1. **Node Class:** Represents each character node with `data`, `next`, and `prev` attributes.
2. **DoublyLinkedList Class:**
   - `insert(char)`: Appends character to the list.
   - `__str__()`: Returns the character sequence stored in the list.
   - `is_custom_palindrome()`:
     - Filters characters while traversing from head to tail:
       - Ignores vowels.
       - Ignores repeated characters.
       - Converts characters to lowercase.
     - Repeats the same process in reverse (tail to head).
     - Compares the two filtered lists.

No list slicing, reverse functions, or collections are used—only custom linked list logic.

---

## ⏱ Time & Space Complexity

| Operation              | Time Complexity | Space Complexity |
|------------------------|------------------|-------------------|
| `insert(char)`         | O(1)              | O(1) per char     |
| `is_custom_palindrome` | O(n)              | O(n)              |

Where `n` is the number of nodes in the list