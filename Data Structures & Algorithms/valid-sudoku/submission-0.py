class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
      rows : dict[int,set[str]] = {}
      cols : dict[int, set[str]] = {}
      boxes : dict[int,set[str]] = {}

      for i in range(9):
        rows[i] = set()
        cols[i] = set()
        boxes[i] = set()

      for row in range(9):
        for col in range(9):
          cel = board[row][col]
          if cel == ".":
            continue

          box = (row // 3) * 3 + (col // 3)
          if (
            cel in rows[row]
            or cel in cols[col]
            or cel in boxes[box]
          ):
            return False

          rows[row].add(cel)
          cols[col].add(cel)
          boxes[box].add(cel)

      return True

