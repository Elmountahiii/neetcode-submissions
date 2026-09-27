class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
       first_index = 0
       last_index = len(numbers) - 1
       while numbers[first_index] + numbers[last_index] != target:
         if numbers[first_index] + numbers[last_index] < target:
           first_index += 1
         else:
           last_index -=1
       return [first_index+1, last_index+1]