class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

      frequents : dict[int,int] = {}
      for number in nums:
        if number not in frequents:
          frequents[number] = 1;
        else:
         frequent = frequents.get(number)
         if frequent is not None:
           frequents[number] = frequent+1;


      return sorted(frequents.keys(),key= lambda number:frequents[number],reverse=True)[:k]

