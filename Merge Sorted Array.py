
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i= m-1
        j=n-1
        k= m+n -1
        while i >=0 and j>=0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j-=1
            else:
                nums1[k] = nums1[i]
                i-=1
            k-=1
        while j>=0:
            nums1[k] = nums2[j]
            j=-1
            k-=1

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
---

## **Problem Recap**

Given:
- `nums1 = [1,2,3,0,0,0]`, `m = 3`
- `nums2 = [2,5,6]`, `n = 3`

Goal: Merge `nums2` into `nums1` in-place, so that `nums1` becomes `[1,2,2,3,5,6]`.

---

## **Pointers Setup**

- `i = m - 1 = 2` (points to last real element in `nums1`)
- `j = n - 1 = 2` (points to last element in `nums2`)
- `k = m + n - 1 = 5` (points to last position in `nums1`)

---

## **Initial State**

```
nums1: [1, 2, 3, 0, 0, 0]
nums2: [2, 5, 6]
i = 2 (nums1[2] = 3)
j = 2 (nums2[2] = 6)
k = 5 (nums1[5] = 0)
```

---

## **Step-by-Step Trace**

### **Step 1**
- Compare `nums1[i]` (3) and `nums2[j]` (6)
- 3 < 6, so put 6 at `nums1[k]`
- `nums1[5] = 6`
- Decrement `j` to 1, `k` to 4

**State:**
```
nums1: [1, 2, 3, 0, 0, 6]
i = 2, j = 1, k = 4
```

---

### **Step 2**
- Compare `nums1[i]` (3) and `nums2[j]` (5)
- 3 < 5, so put 5 at `nums1[k]`
- `nums1[4] = 5`
- Decrement `j` to 0, `k` to 3

**State:**
```
nums1: [1, 2, 3, 0, 5, 6]
i = 2, j = 0, k = 3
```

---

### **Step 3**
- Compare `nums1[i]` (3) and `nums2[j]` (2)
- 3 > 2, so put 3 at `nums1[k]`
- `nums1[3] = 3`
- Decrement `i` to 1, `k` to 2

**State:**
```
nums1: [1, 2, 3, 3, 5, 6]
i = 1, j = 0, k = 2
```

---

### **Step 4**
- Compare `nums1[i]` (2) and `nums2[j]` (2)
- 2 == 2, so put 2 at `nums1[k]`
- `nums1[2] = 2`
- Decrement `j` to -1, `k` to 1

**State:**
```
nums1: [1, 2, 2, 3, 5, 6]
i = 1, j = -1, k = 1
```

---

### **Step 5**
- Now `j < 0`, so we stop the main loop.
- Any remaining elements in `nums2` would be copied, but here, all are merged.

---

## **Final State**

```
nums1: [1, 2, 2, 3, 5, 6]
```

---

## **Deep Explanation**

- **Why start from the end?**  
  If you started from the beginning, you’d overwrite elements in `nums1` that you haven’t checked yet. By starting from the end, you always write into empty space or over elements that have already been compared.

- **Why only copy from `nums2` at the end?**  
  If `nums2` has any elements left after the main loop, they are all smaller than the remaining elements in `nums1`, so you just copy them over.

- **Why is this O(m + n)?**  
  Each step moves one of the pointers (`i`, `j`, or `k`) down by 1, and you do this at most `m + n` times.

---

## **Summary Table**

| Step | i | j | k | nums1 State           | Action                |
|------|---|---|---|-----------------------|-----------------------|
| 1    | 2 | 2 | 5 | [1,2,3,0,0,6]         | Place 6 from nums2    |
| 2    | 2 | 1 | 4 | [1,2,3,0,5,6]         | Place 5 from nums2    |
| 3    | 2 | 0 | 3 | [1,2,3,3,5,6]         | Place 3 from nums1    |
| 4    | 1 | 0 | 2 | [1,2,2,3,5,6]         | Place 2 from nums2    |
| End  | 1 | -1| 1 | [1,2,2,3,5,6]         | Done                  |

---

