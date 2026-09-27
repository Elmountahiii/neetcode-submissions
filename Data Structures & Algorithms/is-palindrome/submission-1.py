class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i : int = 0
        j : int = (len(s) -1) 
        while i < j:
            if s[i] == " " or not s[i].isalnum():
                i += 1
                continue
            if s[j] == " " or not s[j].isalnum():
                j -= 1
                continue
            if s[i] != s[j]:
              return False
            i += 1
            j -= 1
        return True


# s="Was it a car or a cat I saw?"
# solution = Solution()

# print(solution.isPalindrome(s))