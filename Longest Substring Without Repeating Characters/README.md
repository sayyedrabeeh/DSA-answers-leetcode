## Longest Substring Without Repeating Characters

### Question 

   Given a string s, find the length of the longest substring without duplicate characters.

 

#### Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

#### Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

#### Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

 ### Solution

   Let's go **line-by-line** and walk through **each part of the loop** for the code solving the **Longest Substring Without Repeating Characters** problem using the **sliding window** technique:

---

### 🔢   Code:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        c = 0
        m = 0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[c])
                c = c + 1
            a.add(s[i])
            m = max(m, i - c + 1)
        return m
```

---

## ✅ Line-by-Line Explanation:

### 1️⃣

```python
a = set()
```

* `a` stores characters **currently in the sliding window**.
* This helps quickly check for duplicates (since `set` has O(1) lookup).

---

### 2️⃣

```python
c = 0
```

* `c` is the **left boundary** (start index) of the sliding window.
* It will slide forward when we find a duplicate.

---

### 3️⃣

```python
m = 0
```

* `m` keeps track of the **maximum length** of substring found so far without repeating characters.

---

### 🔁 Main loop:

```python
for i in range(len(s)):
```

* `i` is the **right boundary** of the window (end index).
* We iterate through each character in the string.

---

### 4️⃣ Inner loop:

```python
while s[i] in a:
    a.remove(s[c])
    c = c + 1
```

* If `s[i]` (current character) is **already in the set**, it means we’ve found a duplicate.
* So we **shrink the window from the left** by:

  * Removing `s[c]` from the set
  * Moving `c` (left boundary) forward until `s[i]` is no longer in the window.

---

### 5️⃣ Add current character:

```python
a.add(s[i])
```

* Now we add `s[i]` to the set since the substring is guaranteed to be unique at this point.

---

### 6️⃣ Update max length:

```python
m = max(m, i - c + 1)
```

* `i - c + 1` is the **length of the current window**.
* Update `m` if this is the **longest** unique substring so far.

---

### 🔚 Return result:

```python
return m
```

* Finally, return the maximum length of substring found.

---

## 🧪 Example Trace: `s = "abcabcbb"`

Let’s step through:

* i = 0, `a = {a}`, window = "a", m = 1
* i = 1, `a = {a, b}`, window = "ab", m = 2
* i = 2, `a = {a, b, c}`, window = "abc", m = 3
* i = 3, `s[3] = a`, duplicate found:

  * remove `s[0]` = 'a', c = 1
  * add 'a' → `a = {b, c, a}`, window = "bca"
* continue similarly...

Final output: **3**

---

Perfect! Let's walk **step by step through each iteration** of your code using the example:

---

## 🔍 Input:

```python
s = "abcabcbb"
```

### Goal:

Find the **length of the longest substring** without repeating characters.

---
 
---

## 🔄 Step-by-Step Execution

| `i` | `s[i]` | `a` (set) before loop | `c` | Duplicate? | Action taken                                    | `a` (set) after loop | `m` |
| --- | ------ | --------------------- | --- | ---------- | ----------------------------------------------- | -------------------- | --- |
| 0   | 'a'    | `{}`                  | 0   | ❌ No       | Add 'a'                                         | `{a}`                | 1   |
| 1   | 'b'    | `{a}`                 | 0   | ❌ No       | Add 'b'                                         | `{a, b}`             | 2   |
| 2   | 'c'    | `{a, b}`              | 0   | ❌ No       | Add 'c'                                         | `{a, b, c}`          | 3   |
| 3   | 'a'    | `{a, b, c}`           | 0   | ✅ Yes      | Remove 'a' (`s[c]`), then c → 1 → Add 'a'       | `{a, b, c}`          | 3   |
| 4   | 'b'    | `{a, b, c}`           | 1   | ✅ Yes      | Remove 'b' (`s[c]`), then c → 2 → Add 'b'       | `{a, b, c}`          | 3   |
| 5   | 'c'    | `{a, b, c}`           | 2   | ✅ Yes      | Remove 'c' (`s[c]`), then c → 3 → Add 'c'       | `{a, b, c}`          | 3   |
| 6   | 'b'    | `{a, b, c}`           | 3   | ✅ Yes      | Remove 'a', c → 4 → Remove 'b', c → 5 → Add 'b' | `{b, c}`             | 3   |
| 7   | 'b'    | `{b, c}`              | 5   | ✅ Yes      | Remove 'c', c → 6 → Remove 'b', c → 7 → Add 'b' | `{b}`                | 3   |

---

## ✅ Final Answer:

```
m = 3
```

→ The longest substrings without repeating characters are: `"abc"`, `"bca"`, `"cab"`, all of length **3**.

---

 ### comparision 

  Let's look at **two versions** of the solution for:

> 🔹 **Longest Substring Without Repeating Characters**

We’ll compare:

1. **Brute-force approach** (No DSA, no set, no sliding window)
2. **Efficient approach** (With set + sliding window)

---

## ✅ 1. Brute Force (Without DSA, no set)

### 🔧 Code:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            current = ""
            for j in range(i, len(s)):
                if s[j] in current:
                    break
                current += s[j]
                max_len = max(max_len, len(current))
        return max_len
```

### 📊 Time Complexity:

* Outer loop runs `n` times
* Inner loop runs up to `n` times in worst case
* `in` and `+=` on strings are O(n), making this **O(n³)** in worst case
* **Space Complexity**: O(n) (due to `current` string)

---

## ⚡ 2. Optimized Sliding Window with Set (Your Version)

### ✅ Code:

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
```

### 📊 Time Complexity:

* Each character is added and removed at most once → O(n)
* **Space Complexity**: O(n) (for the set)

---

## ⚖️ Comparison Table:

| Version              | Time Complexity | Space Complexity | Speed       | Uses DSA? |
| -------------------- | --------------- | ---------------- | ----------- | --------- |
| Brute Force          | O(n³)           | O(n)             | ❌ Very slow | ❌ No      |
| Sliding Window (Set) | O(n)            | O(n)             | ✅ Fast      | ✅ Yes     |

---

### 👉 Summary:

* The **brute-force method** is simple but slow (only good for small inputs).
* The **optimized sliding window** is **far more efficient**, even for long strings.

 
 
