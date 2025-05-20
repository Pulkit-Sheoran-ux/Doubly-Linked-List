# Custom Doubly Linked List Palindrome Checker

## 🔍 Problem Summary

Design a custom `DoublyLinkedList` class in Python (without using built-in list, deque, or similar collections) that stores a sequence of characters (A-Z, a-z). Implement a method to determine whether the sequence is a **custom palindrome** based on the following rules:

### Custom Palindrome Rules:
- Case-insensitive (e.g., 'A' is the same as 'a').
- Ignore all vowels: `a`, `e`, `i`, `o`, `u`.
- Ignore repeated characters (only consider their first occurrence from each end).
- Compare forward and backward sequences after filtering.

---

## 💡 Approach Used

1. **Node Class:** Represents each character node with `data`, `next`, and `prev` attributes.
2. **DoublyLinkedList Class:**
   - `insert(char)`: Appends character to the end.
   - `__str__()`: Returns the character sequence stored in the list.
   - `is_custom_palindrome()`:
     - Uses a **two-pointer approach** (`left` and `right`) to scan simultaneously from both ends.
     - Ignores:
       - Vowels
       - Repeated characters from each side (tracked using sets)
     - Compares non-repeated, non-vowel characters directly during traversal.
     - Returns `False` on first mismatch, avoiding full scan when unnecessary.

---

## 🔧 Optimizations Made

| Feature                | Properties                          |
|------------------------|-------------------------------------|
| Traversal              | One simultaneous (two-pointer) pass |
| Temporary storage      | Only two sets for repetition check  |
| Early stopping         | Yes (returns on first mismatch)     |
| Space Complexity       | O(1) extra (besides the linked list)|
| Elegance               | High                                |

## ⏱ Time & Space Complexity

| Operation              | Time Complexity | Space Complexity   |
|------------------------|-----------------|--------------------|
| `insert(char)`         | O(1)            | O(1) per char      |
| `is_custom_palindrome` | O(n)            | O(1) auxiliary     |

Where `n` is the number of characters inserted.

---

## 🧪 Sample Test Cases

### ✅ Input: Deified
**Output:** True 

### ✅ Input: DdoODd
**Output:** True 

### ✅ Input: Banana
**Output:** False 

