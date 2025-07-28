class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq= [0] * 101
        for num in nums:
            freq[num]+=1
        for i in range (1, 101):
            freq[i] += freq[i-1]
        return [0 if num ==0 else freq[num-1] for num in nums]


# Let's do a detailed trace for the input:  
# **nums = [8, 1, 2, 2, 3]**

# ---

# ### 1. Frequency Count

# Start with:
# ```
# freq = [0, 0, 0, ..., 0]  # 101 zeros
# ```
# Loop through nums:
# - num = 8  → freq[8] += 1  → freq[8] = 1
# - num = 1  → freq[1] += 1  → freq[1] = 1
# - num = 2  → freq[2] += 1  → freq[2] = 1
# - num = 2  → freq[2] += 1  → freq[2] = 2
# - num = 3  → freq[3] += 1  → freq[3] = 1

# Now:
# ```
# freq[1] = 1
# freq[2] = 2
# freq[3] = 1
# freq[8] = 1
# # All other freq[i] = 0
# ```

# ---

# ### 2. Prefix Sum

# We update freq so that freq[i] = count of numbers ≤ i.

# - freq[1] = freq[1] + freq[0] = 1 + 0 = 1
# - freq[2] = freq[2] + freq[1] = 2 + 1 = 3
# - freq[3] = freq[3] + freq[2] = 1 + 3 = 4
# - freq[4] = freq[4] + freq[3] = 0 + 4 = 4
# - ...
# - freq[8] = freq[8] + freq[7] = 1 + 4 = 5

# So, after prefix sum, the relevant values are:
# ```
# freq[0] = 0
# freq[1] = 1   # 1 value ≤ 1
# freq[2] = 3   # 3 values ≤ 2
# freq[3] = 4   # 4 values ≤ 3
# freq[4] = 4   # 4 values ≤ 4
# ...
# freq[7] = 4   # 4 values ≤ 7
# freq[8] = 5   # 5 values ≤ 8
# ```

# ---

# ### 3. Build the Result

# For each num in nums, result is:
# - If num == 0: 0
# - Else: freq[num-1]

# So:
# - num = 8  → freq[7] = 4
# - num = 1  → freq[0] = 0
# - num = 2  → freq[1] = 1
# - num = 2  → freq[1] = 1
# - num = 3  → freq[2] = 3

# **Final result:**  
# `[4, 0, 1, 1, 3]`

# ---

# **Summary Table:**

# | num | freq[num-1] | result |
# |-----|-------------|--------|
# |  8  |     4       |   4    |
# |  1  |     0       |   0    |
# |  2  |     1       |   1    |
# |  2  |     1       |   1    |
# |  3  |     3       |   3    |

# ---

