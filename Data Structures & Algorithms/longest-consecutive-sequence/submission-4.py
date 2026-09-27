class Solution:


    def find_root(self, value: int, parents:dict[int,int])-> int:
      path : list[int] = [] # [3,4]
      root = value;
      while parents[root] != root:
        path.append(root)
        root = parents[root]
      for num in path: 
        parents[num] = root
      return root

  # nums=[2,20,4,10,3,4,5]
  # parents = {
  # 2:5
  # 20:20
  # 10:10
  # 3:5
  # 4:5
  # 5:5
  # }
  #
  # 1 + 1 = 2
  # 2 + 1 = 3
  #
    def union(self, first: int , second : int , parents: dict[int,int]):
      first_root = self.find_root(first,parents)  # first = 3 root 3
      second_root = self.find_root(second,parents) # second = 4 root 5

      if first_root != second_root:
        parents[first_root] = second_root

    def longestConsecutive(self, nums: list[int]) -> int:
      parents: dict[int,int] = {}
      sizes: dict[int,int] = {}
      cleaned_nums :set[int]= set(nums)

      for num in cleaned_nums:
        parents[num] = num
        sizes[num] = 0
          

      for num in cleaned_nums:
        if num + 1 in parents:
          self.union(num, num +1,parents)

      # print(parents)
      for num in cleaned_nums:
        number_root = self.find_root(num,parents)
        sizes[number_root] +=  1
      if len(sizes) > 0:
        return max(sizes.values())
      else:
        return 0
