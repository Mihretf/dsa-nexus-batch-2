# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left_same = self.isSameTree(p.left , q.left)
        right_same = self.isSameTree(p.right, q.right)
        return left_same and right_same
        
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        

# ---

## **Let’s Use This Example:**

# ```
# p = [1,2,3]
# q = [1,2,3]
# ```

# Both trees look like this:
# ```
#     1
#    / \
#   2   3
# ```

# ---

## **Step-by-Step Trace**

# We’ll compare the trees starting from the root and move down to the children.

# ---

# ### **Step 1: Compare Roots**
# - `p.val = 1`, `q.val = 1`
# - Both are not `None` and values are equal.
# - **Check left subtrees:** `p.left` vs `q.left`
# - **Check right subtrees:** `p.right` vs `q.right`

# ---

# ### **Step 2: Compare Left Children**
# - `p.left.val = 2`, `q.left.val = 2`
# - Both are not `None` and values are equal.
# - **Check left subtrees:** `p.left.left` vs `q.left.left` (both are `None`)
# - **Check right subtrees:** `p.left.right` vs `q.left.right` (both are `None`)

# #### **Step 2a: Compare `p.left.left` and `q.left.left`**
# - Both are `None` → return `True`

# #### **Step 2b: Compare `p.left.right` and `q.left.right`**
# - Both are `None` → return `True`

# - Since both left and right subtrees are the same, return `True` for this node.

# ---

# ### **Step 3: Compare Right Children**
# - `p.right.val = 3`, `q.right.val = 3`
# - Both are not `None` and values are equal.
# - **Check left subtrees:** `p.right.left` vs `q.right.left` (both are `None`)
# - **Check right subtrees:** `p.right.right` vs `q.right.right` (both are `None`)

# #### **Step 3a: Compare `p.right.left` and `q.right.left`**
# - Both are `None` → return `True`

# #### **Step 3b: Compare `p.right.right` and `q.right.right`**
# - Both are `None` → return `True`

# - Since both left and right subtrees are the same, return `True` for this node.

# ---

# ### **Step 4: Combine Results**
# - Both left and right subtrees of the root are the same (`True`).
# - The root values are the same.
# - **Return `True` for the whole tree.**

# ---

# ## **Summary Table**

# | Step         | p node | q node | Action/Result         |
# |--------------|--------|--------|----------------------|
# | Root         | 1      | 1      | Values equal, check children |
# | Left child   | 2      | 2      | Values equal, check children |
# | Left.left    | None   | None   | Both None → True     |
# | Left.right   | None   | None   | Both None → True     |
# | Right child  | 3      | 3      | Values equal, check children |
# | Right.left   | None   | None   | Both None → True     |
# | Right.right  | None   | None   | Both None → True     |
# | Combine      |        |        | All True → Trees are the same |

# ---

# ## **What if the Trees Are Different?**

# If at any point:
# - One node is `None` and the other isn’t → return `False`
# - The values are different → return `False`

# The function will immediately return `False` for the whole tree.

# ---

