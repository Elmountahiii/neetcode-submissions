

class Solution:

    def encode(self, strs: list[str]) -> str:
      encoded = ""
      for value in strs:
        strLen= len(value)
        encoded = encoded + str(strLen) + "#"+value
      return encoded

    def decode(self, s: str) -> list[str]:
      decoded = []
      strLen = len(s)

      i = 0
      while i < strLen:
        word_len = 0

        while s[i].isdigit():
          word_len = word_len * 10  + int(s[i])
          i += 1

        if s[i] == "#":
           i += 1

        value = s[i:i + word_len]
        decoded.append(value)
        # print(value)
        i += word_len

        # for _ in range(word_len):
        #   print(f"{s[i]}",end="")
        #   i += 1
      return decoded

