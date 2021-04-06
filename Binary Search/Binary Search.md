# Binary Search
---
## Templates
- template I:
  ```python
    def binarySearch(nums, target):
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1
  ```
  - Key Attributes:
    - Search Condition can be determined _**without**_ comparing to the element's neighbors (or use specific elements around it)
    - _**No post-processing required**_ because at each step, you are checking to see if the element has been found.
  - Distinguishing Syntax:
    - Initial Condition: `left = 0, right = length - 1`
    - Termination: `left > right`
    - Searching Left: `right = mid - 1`
    - Searching Right: `left = mid + 1`
- template II:
  ```python
    def binarySearch(nums, target):
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        # Post-processing:
        # End Condition: left == right
        if left != len(nums) and nums[left] == target:
            return left
        return -1
  ```
