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

