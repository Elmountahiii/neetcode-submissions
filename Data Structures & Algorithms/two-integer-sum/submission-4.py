class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      targets: list[int]= []
      indexes_dict :dict[int, int] = {}
      for index , number in enumerate(nums):
        indexes_dict[number] = index

      for index,number in enumerate(nums):
         sub = target - number
         result = indexes_dict.get(sub)
         if result is not None and result != index:
           targets.append(index)
           targets.append(result)
           return targets

      return targets