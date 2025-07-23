# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def isMirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            left_mirror= isMirror(left.left, right.right)
            right_mirror= isMirror(left.right, right.left)
            return left_mirror and right_mirror
        if not root:
            return True
        return isMirror(root.left, root.right)

        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
---

## **Example Input**

Let’s use this tree (from your example):

```
Input: root = [1,2,2,3,4,4,3]
```

Visualized:
```
        1
      /   \
     2     2
    / \   / \
   3  4  4   3
```

---

## **Step-by-Step Trace (Recursive Approach)**

We’ll use a helper function that compares two nodes (`left` and `right`).

### **Step 1: Start at the root**
- Compare `root.left` (2) and `root.right` (2)
- Both are not `None` and values are equal.
- Recursively check:
  - `left.left` (3) vs `right.right` (3)
  - `left.right` (4) vs `right.left` (4)

---

### **Step 2: Compare 3 and 3**
- Both are not `None` and values are equal.
- Recursively check:
  - `left.left` (None) vs `right.right` (None)
  - `left.right` (None) vs `right.left` (None)

#### **Step 2a: Compare None and None**
- Both are `None` → return `True`

#### **Step 2b: Compare None and None**
- Both are `None` → return `True`

- Both subtrees are symmetric → return `True` for this pair (3, 3)

---

### **Step 3: Compare 4 and 4**
- Both are not `None` and values are equal.
- Recursively check:
  - `left.left` (None) vs `right.right` (None)
  - `left.right` (None) vs `right.left` (None)

#### **Step 3a: Compare None and None**
- Both are `None` → return `True`

#### **Step 3b: Compare None and None**
- Both are `None` → return `True`

- Both subtrees are symmetric → return `True` for this pair (4, 4)

---

### **Step 4: Go back to Step 1**
- Both left and right subtree checks returned `True` for the first pair (2, 2).
- So, the tree is symmetric.

---

## **Summary Table**

| Step | Nodes Compared | Action/Result         |
|------|---------------|----------------------|
| 1    | 2 vs 2        | Values equal, check children |
| 2    | 3 vs 3        | Values equal, check children |
| 2a   | None vs None  | Both None → True     |
| 2b   | None vs None  | Both None → True     |
| 3    | 4 vs 4        | Values equal, check children |
| 3a   | None vs None  | Both None → True     |
| 3b   | None vs None  | Both None → True     |
| 4    | (all above)   | All True → Tree is symmetric |

---

## **What if the Tree is Not Symmetric?**

If at any point:
- One node is `None` and the other isn’t, or
- The values are different,
- The function returns `False` immediately.

---

