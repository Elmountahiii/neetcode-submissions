class Solution:
    def twoSum(self, nums: List[int], target: int) -> list[int]:
      targets: list[int]= []
      for first_index , first_number in enumerate(nums):
        for second_index, second_number in enumerate(nums):
          if first_index == second_index:
            continue
          if first_number + second_number == target:
                targets.append(first_index)
                targets.append(second_index)
                return targets

      return targets

