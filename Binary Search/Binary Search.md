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

        left, right = 0, len(nums) - 1
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
        if nums[left] == target:
            return left
        return -1
  ```
  - Key Attributes:
    - Use element's right neighbor to determine if condition is met and decide whether to go left or right
    - Gurantees Search Space is _**at least 2**_ in size at each step
    - Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.
    - in `while left < right` loop, lst[mid + 1] is always valid
  - Distinguishing Syntax:
    - Initial Condition: `left = 0, right = length - 1`
    - Termination: `left == right`
    - Searching Left: `right = mid`
    - Searching Right: `left = mid + 1`
- template III:
    ```python
    def binarySearch(nums, target):
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

        # Post-processing:
        # End Condition: left + 1 == right
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1
    ```
  - Key Attributes:
    - Search Condition needs to access element's immediate left and right neighbors
    - Gurantees Search Space is _**at least 3**_ in size at each step
    - Post-processing required. Loop/Recursion ends when you have 2 elements left.
  - Distinguishing Syntax:
    - Initial Condition: `left = 0, right = length - 1`
    - Termination: `left + 1 == right`
    - Searching Left: `right = mid`
    - Searching Right: `left = mid`
