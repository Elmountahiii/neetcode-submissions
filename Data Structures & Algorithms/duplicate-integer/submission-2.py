class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      length = len(nums)
      my_set = set()
      if (length <= 1):
        return False
      for  number in nums:
        if number in my_set:
          return True
        my_set.add(number)

      return False
