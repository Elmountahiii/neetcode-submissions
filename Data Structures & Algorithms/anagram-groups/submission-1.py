class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
      anagrams : list[list[str]] = []
      groups: dict[str,list[str]]={}
      for value in strs:
        sorted_version= "".join(sorted(value))
        if sorted_version not in groups:
          groups[sorted_version] = []

      for value in strs:
        sorted_version = "".join(sorted(value))
        if sorted_version in groups:
          groups[sorted_version].append(value)

      for arrays in groups.values():
        anagrams.append(arrays)

      return anagrams

