class Solution(object):
    def searchInsert(self, nums, target):
        left =0
        right= len(nums)-1
        while left <= right:
           mid = (left + right) // 2
           if nums[mid] == target:
            return mid
           elif nums[mid] < target:
            left = mid + 1
           else:
            right = mid - 1
        return left

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

# ## Example 1:  
# **nums = [1, 3, 5, 6], target = 5**  
# Expected Output: `2`

# | left | right | mid | nums[mid] | Compare to target | Action         |
# |------|-------|-----|-----------|-------------------|----------------|
# | 0    | 3     | 1   | 3         | 3 < 5             | left = mid+1 → 2 |
# | 2    | 3     | 2   | 5         | 5 == 5            | return 2       |

# ---

# ## Example 2:  
# **nums = [1, 3, 5, 6], target = 2**  
# Expected Output: `1`

# | left | right | mid | nums[mid] | Compare to target | Action         |
# |------|-------|-----|-----------|-------------------|----------------|
# | 0    | 3     | 1   | 3         | 3 > 2             | right = mid-1 → 0 |
# | 0    | 0     | 0   | 1         | 1 < 2             | left = mid+1 → 1 |

# Loop ends (`left` = 1, `right` = 0).  
# **Result:** Target not found, insert at index 1.

# ---

# ## Example 3:  
# **nums = [1, 3, 5, 6], target = 7**  
# Expected Output: `4`

# | left | right | mid | nums[mid] | Compare to target | Action         |
# |------|-------|-----|-----------|-------------------|----------------|
# | 0    | 3     | 1   | 3         | 3 < 7             | left = mid+1 → 2 |
# | 2    | 3     | 2   | 5         | 5 < 7             | left = mid+1 → 3 |
# | 3    | 3     | 3   | 6         | 6 < 7             | left = mid+1 → 4 |

# Loop ends (`left` = 4, `right` = 3).  
# **Result:** Target not found, insert at index 4 (end of array).



