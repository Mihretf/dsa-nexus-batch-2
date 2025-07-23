# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        

# ---

# ## **1. What is a Binary Tree?**

# A **binary tree** is a special kind of data structure in computer science.  
# It is made up of **nodes**. Each node can have:
# - A value (like a number or a word)
# - A **left child** (another node, or nothing)
# - A **right child** (another node, or nothing)

# **At most, each node has two children.**

# ---

# ### **Visual Example**

# Here’s a simple binary tree:

# ```
#     1
#    / \
#   2   3
# ```

# - The top node (`1`) is called the **root** (the starting point of the tree).
# - Node `1` has two children: `2` (left) and `3` (right).
# - Nodes `2` and `3` have no children, so they are called **leaves**.

# ---

# ## **2. Key Terms**

# - **Node:** A single element in the tree (like a box with a value).
# - **Root:** The very first node at the top of the tree.
# - **Child:** A node that comes from another node (left or right).
# - **Parent:** The node above a child.
# - **Leaf:** A node with no children.

# ---

# ## **3. How is a Binary Tree Represented in Code?**

# In Python, a binary tree node is often defined like this:

# ```python
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val        # The value of the node
#         self.left = left      # The left child (another TreeNode or None)
#         self.right = right    # The right child (another TreeNode or None)
# ```

# ---

# ## **4. What is the "root"?**

# - The **root** is just the very first node in the tree.
# - If you want to work with the whole tree, you start from the root.

# ---

# ## **5. What is "Inorder Traversal"?**

# Traversal means visiting all the nodes in a certain order.  
# **Inorder traversal** means:
# 1. Visit the left child (if any)
# 2. Visit the current node
# 3. Visit the right child (if any)

# For the tree above:

# ```
#     1
#    / \
#   2   3
# ```

# - Go left to `2` (visit it)
# - Go back to `1` (visit it)
# - Go right to `3` (visit it)

# **Order visited:** 2, 1, 3

# ---

# ## **6. Why Do We Use Trees?**

# - Trees are used to organize data in a way that makes searching, inserting, and deleting efficient.
# - They are used in file systems, databases, and many algorithms.

# ---

# ## **Summary Table**

# | Term   | Meaning                                      |
# |--------|----------------------------------------------|
# | Node   | An element in the tree                       |
# | Root   | The top node (starting point)                |
# | Child  | A node connected below another node          |
# | Leaf   | A node with no children                      |
# | Inorder| Visit left, then current, then right         |

# ---


# ---

# ## **1. What is the Problem Asking?**

# - You are given the **root** of a binary tree.
# - You need to return a **list of the node values** in the order of an **inorder traversal**.

# ---

# ## **2. What is Inorder Traversal?**

# **Inorder traversal** of a binary tree means:
# 1. Traverse the **left subtree** (visit all nodes on the left).
# 2. Visit the **current node** (process its value).
# 3. Traverse the **right subtree** (visit all nodes on the right).

# **Order:**  
# `left → root → right`

# ---

# ## **3. Example Tree**

# Let’s use this tree as an example:

# ```
#     1
#      \
#       2
#      /
#     3
# ```
# This is represented as `[1, null, 2, 3]`.

# ---

# ## **4. Step-by-Step Trace of Inorder Traversal**

# Let’s walk through the traversal:

# ### **Step 1: Start at the root (1)**
# - Go to the left child of 1 (which is `null`).
# - Since there’s nothing on the left, **visit 1** (add 1 to the result).

# ### **Step 2: Go to the right child of 1 (which is 2)**
# - At node 2, go to its left child (which is 3).

# ### **Step 3: At node 3**
# - Go to the left child of 3 (which is `null`).
# - Since there’s nothing on the left, **visit 3** (add 3 to the result).
# - Go to the right child of 3 (which is `null`).

# ### **Step 4: Back to node 2**
# - After finishing the left subtree (3), **visit 2** (add 2 to the result).
# - Go to the right child of 2 (which is `null`).

# ---

# ## **5. Result**

# The order in which we visited nodes:  
# **1 → 3 → 2**

# So, the output is `[1, 3, 2]`.

# ---

# ## **Summary Table for This Example**

# | Step | Current Node | Action                | Result List |
# |------|--------------|-----------------------|-------------|
# | 1    | 1            | Go left (null)        |             |
# | 2    | 1            | Visit                 | [1]         |
# | 3    | 1            | Go right (2)          | [1]         |
# | 4    | 2            | Go left (3)           | [1]         |
# | 5    | 3            | Go left (null)        | [1]         |
# | 6    | 3            | Visit                 | [1, 3]      |
# | 7    | 3            | Go right (null)       | [1, 3]      |
# | 8    | 2            | Visit                 | [1, 3, 2]   |
# | 9    | 2            | Go right (null)       | [1, 3, 2]   |

# ---

