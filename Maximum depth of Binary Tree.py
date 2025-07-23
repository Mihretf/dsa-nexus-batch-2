# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        left_subtree=self.maxDepth(root.left)
        right_subtree=self.maxDepth(root.right)
        return 1+max(left_subtree, right_subtree)
      
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        


### **What’s Happening Here?**

# - The function `maxDepth` is **calling itself** for the left and right children of the current node.
# - This is called **recursion**: a function that solves a problem by calling itself on smaller pieces of the problem.

# ---

# ### **How Does It Actually Get the Depth?**

# Let’s use a small tree as an example:

# ```
#     1
#    / \
#   2   3
#      /
#     4
# ```

# #### **Step-by-Step Trace:**

# 1. **Start at root (1):**
#    - Call `maxDepth` on `root.left` (node 2)
#    - Call `maxDepth` on `root.right` (node 3)

# 2. **At node 2:**
#    - Both left and right are `None`
#    - So, `maxDepth(None)` returns 0 for both
#    - Depth at node 2: `1 + max(0, 0) = 1`

# 3. **At node 3:**
#    - Call `maxDepth` on `root.left` (node 4)
#    - Call `maxDepth` on `root.right` (`None`)

# 4. **At node 4:**
#    - Both left and right are `None`
#    - So, `maxDepth(None)` returns 0 for both
#    - Depth at node 4: `1 + max(0, 0) = 1`

# 5. **Back at node 3:**
#    - Left subtree depth = 1 (from node 4)
#    - Right subtree depth = 0
#    - Depth at node 3: `1 + max(1, 0) = 2`

# 6. **Back at root (1):**
#    - Left subtree depth = 1 (from node 2)
#    - Right subtree depth = 2 (from node 3)
#    - Depth at root: `1 + max(1, 2) = 3`

# ---

# ### **What Function Are We Going Through?**

# - We are always going through the **same function**: `maxDepth`.
# - Each call works on a smaller part of the tree (a subtree).
# - The recursion goes all the way down to the leaves, then works its way back up, calculating the depth at each node.

# ---

# ## **Summary Table**

# | Node | Left Depth | Right Depth | Depth at Node |
# |------|------------|-------------|---------------|
# | 2    | 0          | 0           | 1             |
# | 4    | 0          | 0           | 1             |
# | 3    | 1 (4)      | 0           | 2             |
# | 1    | 1 (2)      | 2 (3)       | 3             |

# ---

# **In short:**  
# - The recursion explores all the way to the bottom of the tree.
# - Each call to `maxDepth` returns the depth of the subtree rooted at that node.
# - The `max` function chooses the deeper side at each step.

