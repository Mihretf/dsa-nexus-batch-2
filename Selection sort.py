class Solution(object):
  
    def selectionSort(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]



# ## Step-by-Step Trace

# Let's trace through the example: `arr = [4, 1, 3, 9, 7]`

# **Initial array:** `[4, 1, 3, 9, 7]`

# ### Iteration 1 (i=0):
# - **Unsorted portion:** `[4, 1, 3, 9, 7]`
# - **Find minimum:** Compare 4 with 1, 3, 9, 7
#   - 4 vs 1: 1 is smaller, min_idx = 1
#   - 1 vs 3: 1 is smaller, min_idx = 1  
#   - 1 vs 9: 1 is smaller, min_idx = 1
#   - 1 vs 7: 1 is smaller, min_idx = 1
# - **Swap:** arr[0] ↔ arr[1]
# - **Result:** `[1, 4, 3, 9, 7]`

# ### Iteration 2 (i=1):
# - **Unsorted portion:** `[4, 3, 9, 7]`
# - **Find minimum:** Compare 4 with 3, 9, 7
#   - 4 vs 3: 3 is smaller, min_idx = 2
#   - 3 vs 9: 3 is smaller, min_idx = 2
#   - 3 vs 7: 3 is smaller, min_idx = 2
# - **Swap:** arr[1] ↔ arr[2]
# - **Result:** `[1, 3, 4, 9, 7]`

# ### Iteration 3 (i=2):
# - **Unsorted portion:** `[4, 9, 7]`
# - **Find minimum:** Compare 4 with 9, 7
#   - 4 vs 9: 4 is smaller, min_idx = 2
#   - 4 vs 7: 4 is smaller, min_idx = 2
# - **Swap:** arr[2] ↔ arr[2] (no change)
# - **Result:** `[1, 3, 4, 9, 7]`

# ### Iteration 4 (i=3):
# - **Unsorted portion:** `[9, 7]`
# - **Find minimum:** Compare 9 with 7
#   - 9 vs 7: 7 is smaller, min_idx = 4
# - **Swap:** arr[3] ↔ arr[4]
# - **Result:** `[1, 3, 4, 7, 9]`

# ### Iteration 5 (i=4):
# - **Unsorted portion:** `[9]`
# - **Find minimum:** Only one element, min_idx = 4
# - **Swap:** arr[4] ↔ arr[4] (no change)
# - **Result:** `[1, 3, 4, 7, 9]`

# **Final sorted array:** `[1, 3, 4, 7, 9]`

# ## Time Complexity Analysis

# ### Best Case: O(n²)
# - Even if the array is already sorted, we still need to:
#   - Make n-1 comparisons in the first iteration
#   - Make n-2 comparisons in the second iteration
#   - And so on...
# - Total comparisons: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²)

# ### Average Case: O(n²)
# - On average, we'll need to search through roughly half of the remaining unsorted elements
# - Still results in O(n²) complexity

# ### Worst Case: O(n²)
# - When the array is sorted in descending order
# - We need to search through all remaining elements in each iteration
# - Total comparisons: (n-1) + (n-2) + ... + 1 = n(n-1)/2 = O(n²)

# ## Space Complexity: O(1)

# The algorithm uses only a constant amount of extra space:
# - Variables: `n`, `i`, `j`, `min_idx`
# - No additional data structures that grow with input size
# - Modifies the array in-place

# ## Key Characteristics

# **Advantages:**
# - Simple to understand and implement
# - Minimal memory usage (in-place sorting)
# - Performs well on small datasets
# - Number of swaps is minimal (at most n-1 swaps)

# **Disadvantages:**
# - Poor performance on large datasets due to O(n²) complexity
# - Not stable (equal elements may change relative order)
# - Not adaptive (doesn't take advantage of existing order)

