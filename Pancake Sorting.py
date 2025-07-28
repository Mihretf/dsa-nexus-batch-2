class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res=[]
        n= len(arr)
        for size in range(n, 0, -1):
            idx = arr.index(size)
            if idx == size -1:
                continue
            if idx!=0:
                arr[:idx+1] = arr[:idx+1][::-1]
                res.append(idx+1)
            arr[:size] = arr[:size][::-1]                
            res.append(size)
        return res




# ---

# ## Initial State
# ```
# arr = [3, 2, 4, 1]
# res = []
# n = 4
# ```

# ---

# ### **First Pass (size = 4)**
# - **Find 4:** `idx = arr.index(4) = 2`
# - **Is 4 at index 3?** No (`idx != size-1`)
# - **Is 4 at the front?** No (`idx != 0`)
#     - **Flip first 3:** `arr[:3] = [3,2,4]` → `[4,2,3]`
#     - `arr = [4,2,3,1]`
#     - `res = [3]`
# - **Flip first 4:** `arr[:4] = [4,2,3,1]` → `[1,3,2,4]`
#     - `arr = [1,3,2,4]`
#     - `res = [3,4]`
# - Now, 4 is at the end.

# ---

# ### **Second Pass (size = 3)**
# - **Find 3:** `idx = arr.index(3) = 1`
# - **Is 3 at index 2?** No (`idx != size-1`)
# - **Is 3 at the front?** No (`idx != 0`)
#     - **Flip first 2:** `arr[:2] = [1,3]` → `[3,1]`
#     - `arr = [3,1,2,4]`
#     - `res = [3,4,2]`
# - **Flip first 3:** `arr[:3] = [3,1,2]` → `[2,1,3]`
#     - `arr = [2,1,3,4]`
#     - `res = [3,4,2,3]`
# - Now, 3 is at index 2.

# ---

# ### **Third Pass (size = 2)**
# - **Find 2:** `idx = arr.index(2) = 0`
# - **Is 2 at index 1?** No (`idx != size-1`)
# - **Is 2 at the front?** Yes (`idx == 0`)
#     - (Skip the first flip)
# - **Flip first 2:** `arr[:2] = [2,1]` → `[1,2]`
#     - `arr = [1,2,3,4]`
#     - `res = [3,4,2,3,2]`
# - Now, 2 is at index 1.

# ---

# ### **Fourth Pass (size = 1)**
# - **Find 1:** `idx = arr.index(1) = 0`
# - **Is 1 at index 0?** Yes (`idx == size-1`)
#     - (No flip needed)

# ---

# ## **Final State**
# - `arr = [1,2,3,4]` (sorted)
# - `res = [3, 4, 2, 3, 2]` (sequence of flips)

# ---

# ### **Summary Table**

# | Pass | size | idx | Flip(s)         | arr after flip(s) | res         |
# |------|------|-----|-----------------|-------------------|-------------|
# | 1    | 4    | 2   | 3, 4            | [1, 3, 2, 4]      | [3, 4]      |
# | 2    | 3    | 1   | 2, 3            | [2, 1, 3, 4]      | [3, 4, 2, 3]|
# | 3    | 2    | 0   | 2               | [1, 2, 3, 4]      | [3, 4, 2, 3, 2]|
# | 4    | 1    | 0   | -               | [1, 2, 3, 4]      | [3, 4, 2, 3, 2]|

# ---

