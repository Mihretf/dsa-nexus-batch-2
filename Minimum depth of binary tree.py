# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        left_subtree= self.minDepth(root.left)
        right_subtree= self.minDepth(root.right)

        if not root.left:
            return 1+ right_subtree
        if not root.right:
            return 1+ left_subtree

        return 1+min(left_subtree, right_subtree)
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        



# ---

# ## **Example Tree**

# Let’s use this tree:
# ```
#       1
#      / \
#     2   3
#    /
#   4
# ```
# Level-order: `[1,2,3,4]`

# - The minimum depth is **2** (path: 1 → 3).

# ---

# ## **A. Recursive Approach Trace**

# ### **Call: minDepth(1)**
# - `root` is 1 (not None, not a leaf)
# - Compute left: `minDepth(2)`
# - Compute right: `minDepth(3)`

# ---

# #### **Call: minDepth(2)**
# - `root` is 2 (not None, not a leaf)
# - Compute left: `minDepth(4)`
# - Compute right: `minDepth(None)`

# ---

# ##### **Call: minDepth(4)**
# - `root` is 4 (leaf node)
# - Return 1

# ##### **Call: minDepth(None)**
# - `root` is None
# - Return 0

# - For node 2: left = 1, right = 0
# - Only left exists, so return `1 + left = 2`

# ---

# #### **Call: minDepth(3)**
# - `root` is 3 (leaf node)
# - Return 1

# ---

# ### **Back to minDepth(1)**
# - left_subtree = 2 (from node 2)
# - right_subtree = 1 (from node 3)
# - Both children exist, so return `1 + min(2, 1) = 2`

# ---

# ## **Recursive Trace Table**

# | Node | Left Depth | Right Depth | Return Value |
# |------|------------|-------------|-------------|
# | 4    | 0          | 0           | 1           |
# | 2    | 1 (4)      | 0           | 2           |
# | 3    | 0          | 0           | 1           |
# | 1    | 2 (2)      | 1 (3)       | 2           |

# ---

