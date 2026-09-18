class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      length = len(nums)
      my_list = []
      if (length <= 1):
        return False
      for  number in nums:
        if number in my_list:
          return True
        my_list.append(number)

      return False
