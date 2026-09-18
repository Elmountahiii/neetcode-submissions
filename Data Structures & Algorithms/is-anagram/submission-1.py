class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      dict:dict[str,int]={}
      for char in s:
        count = dict.get(char)
        if count:
          dict[char] = count+1
        else:
          dict[char]= 1
      for char in t:
        count = dict.get(char)
        if count:
           dict[char] = count-1
        else:
          dict[char] = 1
      for value in dict.values():
        if value != 0:
          return False
      return True