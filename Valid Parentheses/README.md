## Valid Parentheses

 ### Question 

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

     * Open brackets must be closed by the same type of brackets.
     * Open brackets must be closed in the correct order.
     * Every close bracket has a corresponding open bracket of the same type.
 

#### Example 1:
  
  Input: s = "()"
  
  Output: true
  
#### Example 2:
  
  Input: s = "()[]{}"
  
  Output: true
  
#### Example 3:
  
  Input: s = "(]"
  
  Output: false

#### Example 4:

Input: s = "([])"

Output: true

 
### Solution 

  break down your code **line by line**, analyze its **time and space complexity**, and compare it to a **non-DSA style solution**.

---

## Your code:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        bracket = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in bracket:
                b = a.pop() if a else None
                if b != bracket[i]:
                    return False
            else:
                a.append(i)
        return not a
```

---

## Explanation — Line by line:

1. `a = []`

   * Initializes an empty list `a` to be used as a **stack** to keep track of opening brackets.

2. `bracket = {')': '(', '}': '{', ']': '['}`

   * Creates a dictionary mapping each closing bracket to its corresponding opening bracket for easy matching.

3. `for i in s:`

   * Iterates over each character `i` in the input string `s`.

4. `if i in bracket:`

   * Checks if the current character `i` is a **closing bracket** (i.e., one of `')'`, `'}'`, `']'`).

5. `b = a.pop() if a else None`

   * If the stack `a` is not empty, pop the top element (which should be an opening bracket) and assign it to `b`.
   * If the stack is empty (no opening brackets to match), assign `None` to `b`.

6. `if b != bracket[i]:`

   * Compares the popped bracket `b` with the expected matching opening bracket for the current closing bracket `i`.
   * If they don't match, it means the string is invalid, so:

7. `return False`

   * Immediately return `False` indicating invalid parentheses.

8. `else:`

   * If the current character `i` is **not** a closing bracket, it must be an opening bracket.

9. `a.append(i)`

   * Push the opening bracket onto the stack `a`.

10. `return not a`

    * After processing all characters, if the stack is empty (`not a` is `True`), it means all opening brackets were properly matched and closed, so return `True`.
    * If the stack is not empty, return `False` indicating unmatched opening brackets remain.

---

## Time and Space Complexity:

* **Time Complexity:**
  O(n), where n is the length of the string `s`.
  Each character is processed once.

* **Space Complexity:**
  O(n) in the worst case (e.g., all characters are opening brackets), as the stack can hold up to n elements.

---

## Comparison with a "non-DSA" approach:

A non-DSA approach might be something like:

* **Using string replacement** repeatedly to remove matched pairs, e.g., while `"()"` or `"{}"` or `"[]"` exists in the string, remove them and check if the string becomes empty.

Example (not efficient):

```python
def isValid(s):
    while '()' in s or '{}' in s or '[]' in s:
        s = s.replace('()', '').replace('{}', '').replace('[]', '')
    return not s
```

---

### Differences:

| Aspect                   | Your Stack Solution                     | Non-DSA Replace Solution                              |
| ------------------------ | --------------------------------------- | ----------------------------------------------------- |
| **Algorithmic Approach** | Stack (classic data structure usage)    | String manipulation via replace                       |
| **Time Complexity**      | O(n)                                    | O(n²) in worst case (repeated scanning & replacement) |
| **Space Complexity**     | O(n)                                    | O(n) (strings may be recreated multiple times)        |
| **Readability**          | Clear logic using stack, typical in DSA | Intuitive but less efficient                          |
| **Scalability**          | Handles large inputs efficiently        | Slow for large inputs                                 |
| **Best for Interviews**  | Yes, commonly expected                  | No, not efficient nor typical                         |

---

### Summary:

  code uses a **stack-based DSA approach** which is optimal and efficient. The non-DSA solution using repeated replacements works but is inefficient, especially on large inputs, and generally not recommended for coding interviews or performance-critical applications.

---

 
### explanation 

Let’s go through your code **step-by-step**, using an example string to understand what happens at **every iteration**.

---

## ✅ Example:

```python
s = "({[]})"
```

---

## 🧠 Code Setup:

```python
a = []  # Stack
bracket = {')': '(', '}': '{', ']': '['}
```

This means:

* Closing → Opening mappings are:

  * `')' → '('`
  * `'}' → '{'`
  * `']' → '['`

---

## 🔄 Iteration Breakdown:

### 1. `i = '('`

* `'('` is not a closing bracket → goes to `else`.
* `a.append('(')`
* Stack: `['(']`

---

### 2. `i = '{'`

* `'{'` is not a closing bracket → goes to `else`.
* `a.append('{')`
* Stack: `['(', '{']`

---

### 3. `i = '['`

* `'['` is not a closing bracket → goes to `else`.
* `a.append('[')`
* Stack: `['(', '{', '[']`

---

### 4. `i = ']'`

* `']'` is a closing bracket → goes to `if`.
* `b = a.pop()` → `b = '['`
* `bracket[i] = '['`
* `b == bracket[i]` → ✅ match
* Stack: `['(', '{']`

---

### 5. `i = '}'`

* `'}'` is a closing bracket → goes to `if`.
* `b = a.pop()` → `b = '{'`
* `bracket[i] = '{'`
* `b == bracket[i]` → ✅ match
* Stack: `['(']`

---

### 6. `i = ')'`

* `')'` is a closing bracket → goes to `if`.
* `b = a.pop()` → `b = '('`
* `bracket[i] = '('`
* `b == bracket[i]` → ✅ match
* Stack: `[]`

---

## 🔚 End of loop

`return not a`
→ Stack is empty → `True`

---

## ✅ Final Result:

```python
Output: True
```

---

## Summary Table:

| Step | Char | Action                   | Stack            | Valid So Far? |
| ---- | ---- | ------------------------ | ---------------- | ------------- |
| 1    | `(`  | Push                     | `[`(\`]          | ✅             |
| 2    | `{`  | Push                     | \[`(`, `{`]      | ✅             |
| 3    | `[`  | Push                     | \[`(`, `{`, `[`] | ✅             |
| 4    | `]`  | Pop and compare with `[` | \[`(`, `{`]      | ✅             |
| 5    | `}`  | Pop and compare with `{` | \[`(`]           | ✅             |
| 6    | `)`  | Pop and compare with `(` | `[]`             | ✅             |

---

If you'd like, I can walk through a failing input too!
