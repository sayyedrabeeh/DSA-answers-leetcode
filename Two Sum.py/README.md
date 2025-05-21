## Two Sum

### Question

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

#### Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#### Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
#### Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 
 
### comparison 

 
---

## ✅ Problem: Two Sum

**Given** an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

---

## 🔍 Code Explanation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Hash map to store numbers and their indices
        for i, j in enumerate(nums):  # Loop through list with index i and value j
            c = target - j  # Complement we need to find
            if c in seen:  # Check if the complement is already in the hash map
                return [seen[c], i]  # Return index of complement and current index
            seen[j] = i  # Store the number with its index
```

### 🔧 Data Structures Used:

* A **hash map (dictionary)** called `seen`, to store numbers as keys and their indices as values.

---

## ⏱️ Time and Space Complexity

### ✅ Optimized Method (Using Hash Map)

* **Time Complexity: O(n)**

  * We loop through the list of size `n` **only once**.
  * Each lookup (`c in seen`) and insertion (`seen[j] = i`) in the dictionary is **O(1)** on average.
* **Space Complexity: O(n)**

  * In the worst case, we may store all `n` elements in the dictionary.

---

## 🔁 Brute Force Method (Nested Loop)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

### 🔍 Analysis

* **Time Complexity: O(n²)**

  * For each element `i`, we check every other element `j > i`. This results in `n(n-1)/2` comparisons.
* **Space Complexity: O(1)**

  * No extra space is used.

---

## ✅ Summary Table

| Method             | Time Complexity | Space Complexity | Notes                                  |
| ------------------ | --------------- | ---------------- | -------------------------------------- |
| Brute Force        | O(n²)           | O(1)             | Simple but inefficient for large input |
| Hash Map (Optimal) | O(n)            | O(n)             | Efficient with a single pass           |

---

## 🧠 Why Hash Map Is Better in DSA Context

* The hash map method is a **classic example of a space-time tradeoff**.
* It leverages **constant-time lookup** in a dictionary to reduce the overall time complexity from quadratic to linear.
* This method is commonly asked in **coding interviews** because it demonstrates:

  * Knowledge of hash tables
  * Understanding of lookup efficiency
  * Ability to optimize brute-force approaches

---

### Explanation 


Great! Let's go **line-by-line** and walk through **each iteration** of your `twoSum` function, including what happens in the hash map (`seen`) during each step.

 

---

 

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            c = target - j 
            if c in seen:
                return [seen[c], i]
            seen[j] = i
```

---

## 🧠 Line-by-Line Explanation

### `class Solution:`

Defines a class named `Solution`. This is just a convention used in LeetCode and other platforms.

---

### `def twoSum(self, nums: List[int], target: int) -> List[int]:`

Defines a method `twoSum` that takes:

* `nums`: A list of integers.
* `target`: The target sum we want to achieve by adding two numbers from `nums`.

---

### `seen = {}`

Creates an **empty dictionary (hash map)** to store:

* Keys: Numbers from the array.
* Values: Their corresponding indices.

---

### `for i, j in enumerate(nums):`

Loops through `nums` using `enumerate`, so:

* `i` is the **index**
* `j` is the **value**

---

### `c = target - j`

Calculates the **complement**:

* `c` is the number you need so that `j + c = target`.

---

### `if c in seen:`

Checks if the **complement** `c` is already in the hash map.

* If yes: you've found two numbers that add to the target!

---

### `return [seen[c], i]`

Returns the **indices** of the two numbers:

* `seen[c]`: index of the complement.
* `i`: current index.

---

### `seen[j] = i`

Stores the current number `j` and its index `i` in the dictionary for future lookup.

---

## 🔁 Step-by-Step Iteration Example

### 🧪 Example Input:

```python
nums = [2, 7, 11, 15]
target = 9
```

### Initial state:

```python
seen = {}
```

---

### ✅ Iteration 1:

* `i = 0`, `j = 2`
* `c = 9 - 2 = 7`
* `7` is **not** in `seen`
* Store `seen[2] = 0`

➡️ `seen = {2: 0}`

---

### ✅ Iteration 2:

* `i = 1`, `j = 7`
* `c = 9 - 7 = 2`
* `2` **is** in `seen` → Found a match!
* Return `[seen[2], 1]` → `[0, 1]`

🎉 Output: `[0, 1]`

No further iterations are needed because we already found the answer.

---

## 🧠 Summary

| Step | i | j | c (`target - j`) | `seen` Before | `c in seen?` | Action             | `seen` After |
| ---- | - | - | ---------------- | ------------- | ------------ | ------------------ | ------------ |
| 1    | 0 | 2 | 7                | `{}`          | ❌ No         | Add `2: 0` to seen | `{2: 0}`     |
| 2    | 1 | 7 | 2                | `{2: 0}`      | ✅ Yes        | Return `[0, 1]`    | N/A          |

---

 
