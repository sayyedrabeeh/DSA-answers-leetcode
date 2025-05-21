# 🧠 LeetCode DSA Solutions

Welcome to the **LeetCode DSA Solutions** repository!  
This project contains detailed, well-explained solutions to common **Data Structures and Algorithms (DSA)** problems on [LeetCode](https://leetcode.com/).

Each problem is organized in its own folder and includes:

- `answer.py`: Python implementation of the solution
- `README.md`: 
  - The problem statement  
  - Example inputs and outputs  
  - Brute-force and optimal approach comparisons  
  - Time and space complexity  
  - Step-by-step explanation

---

## 📁 Folder Structure

├── Two-Sum
│ ├── Two-Sum.py
│ └── README.md
├── README.md (this file)


> 📝 Follow the format `XX-Question-Name` (with padded numbers) if you’re numbering the folders in order.

---

## 📋 Questions Table

| No. | Question Name           | Difficulty | Link to Solution Folder |
|-----|-------------------------|------------|--------------------------|
| 1   | [Two Sum](./Two Sum)    | Easy       | `./Two Sum`              |
 

---

## 📌 How to Contribute

1. Fork this repository.
2. Create a new folder for each LeetCode question using this naming pattern: `XX-Question-Name`.
3. Inside the folder, add:
   - `answer.py`: Your Python solution.
   - `README.md`: Use the template below to explain your approach clearly.
4. Add an entry to the Questions Table in the main `README.md`.
5. Open a pull request.

---

## 📝 Question Folder README Template

```markdown
# 🧮 Two Sum

**LeetCode Link**: [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

---

## ❓ Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

### Example

Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]


---

## 🔍 Approaches Compared

| Approach            | Time Complexity | Space Complexity | Explanation                                |
|---------------------|------------------|------------------|--------------------------------------------|
| Brute Force         | O(n²)           | O(1)             | Check every pair of elements               |
| Hash Map (Optimal)  | O(n)            | O(n)             | Store values in a map to find complement   |

---

## ✅ Optimal Approach Explanation

### Algorithm:

- Initialize an empty dictionary `seen` to store numbers and their indices.
- Iterate through the list.
- For each element, compute its complement with respect to the target (`target - element`).
- If the complement exists in `seen`, return the pair of indices.
- Otherwise, store the current number and its index in `seen`.

### Code:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            c = target - j
            if c in seen:
                return [seen[c], i]
            seen[j] = i
```