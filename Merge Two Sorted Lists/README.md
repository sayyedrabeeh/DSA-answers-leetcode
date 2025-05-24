### Merge Two Sorted Lists

#### Question 

   You are given the heads of two sorted linked lists list1 and list2.

   Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

   Return the head of the merged linked list.

 

#### Example 1:


   Input: list1 = [1,2,4], list2 = [1,3,4]
   Output: [1,1,2,3,4,4]
#### Example 2:

   Input: list1 = [], list2 = []
   Output: []
#### Example 3:

   Input: list1 = [], list2 = [0]
   Output: [0]


 
 #### Explanation 

   this **recursive solution** for merging two sorted linked lists **line by line**, and then trace it using a full example.

---

## 🔹 Code:

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

---

## 🔹 Line-by-Line Explanation:

### 1. `if not list1: return list2`

* If list1 is empty (`None`), return list2.
* This is the **base case** for recursion — when one list is exhausted, return the remaining part of the other list.

### 2. `if not list2: return list1`

* Similarly, if list2 is empty, return list1.

### 3. `if list1.val < list2.val:`

* Compare the current node values from both lists.
* If `list1.val` is smaller, it should go first in the merged list.

### 4. `list1.next = self.mergeTwoLists(list1.next, list2)`

* Move forward in `list1`, and call the function again recursively.
* Link the result of that recursive call to `list1.next`.

### 5. `return list1`

* Return `list1` as the head of the current merged part.

### 6. `else:`

* If `list2.val <= list1.val`, do the same but with `list2`.

### 7. `list2.next = self.mergeTwoLists(list1, list2.next)`

* Move forward in `list2`, keep `list1` as is.

### 8. `return list2`

* Return `list2` as the new head of this merged portion.

---

## 🔁 Walkthrough Example:

### Input:

```
list1: 1 -> 3 -> 5
list2: 2 -> 4 -> 6
```

### Step-by-step:

1. **Call**: `mergeTwoLists(1->3->5, 2->4->6)`

   * `1 < 2`, so:
   * `list1.next = mergeTwoLists(3->5, 2->4->6)`

2. **Call**: `mergeTwoLists(3->5, 2->4->6)`

   * `2 < 3`, so:
   * `list2.next = mergeTwoLists(3->5, 4->6)`

3. **Call**: `mergeTwoLists(3->5, 4->6)`

   * `3 < 4`, so:
   * `list1.next = mergeTwoLists(5, 4->6)`

4. **Call**: `mergeTwoLists(5, 4->6)`

   * `4 < 5`, so:
   * `list2.next = mergeTwoLists(5, 6)`

5. **Call**: `mergeTwoLists(5, 6)`

   * `5 < 6`, so:
   * `list1.next = mergeTwoLists(None, 6)`

6. **Call**: `mergeTwoLists(None, 6)`

   * Base case: return `6`

Now return results back up the chain:

* `list1(5).next = 6`
* `list2(4).next = 5->6`
* `list1(3).next = 4->5->6`
* `list2(2).next = 3->4->5->6`
* `list1(1).next = 2->3->4->5->6`

### ✅ Final Output:

```
1 -> 2 -> 3 -> 4 -> 5 -> 6
```

---

 